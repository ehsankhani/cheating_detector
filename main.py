import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QListWidget, QListWidgetItem
)
from algorithms.cheating_detector import CheatingDetector
from Utils.excel_exporter import ExcelExporter
from algorithms.code_comparison_dialog import CodeComparisonDialog  # Import the new dialog class
from PyQt6.QtGui import QFont


class CheatingDetectionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cheating Detection System")
        self.setGeometry(100, 100, 800, 600)

        self.detector = None
        self.folder_path = ""  # Store the selected folder path

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout(central_widget)

        # Add buttons
        self.btn_select_folder = QPushButton("Select Folder", self)
        self.btn_select_folder.clicked.connect(self.select_folder)
        layout.addWidget(self.btn_select_folder)

        self.btn_run_detection = QPushButton("Run Detection", self)
        self.btn_run_detection.clicked.connect(self.run_detection)
        layout.addWidget(self.btn_run_detection)

        self.btn_export_excel = QPushButton("To Excel", self)
        self.btn_export_excel.clicked.connect(self.export_to_excel)
        layout.addWidget(self.btn_export_excel)

        self.btn_export_excel_students = QPushButton("Excel for students", self)
        self.btn_export_excel_students.clicked.connect(self.export_for_students)
        layout.addWidget(self.btn_export_excel_students)

        # Output box
        self.output_box = QListWidget(self)
        self.output_box.setFont(QFont("Arial", 11))
        layout.addWidget(self.output_box)

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Homework Folder")
        if folder_path:
            self.folder_path = folder_path  # Store the selected folder path
            self.output_box.addItem(f"Selected folder: {self.folder_path}")

    def run_detection(self):
        if not self.folder_path:
            self.output_box.addItem("No folder selected!")
            return

        self.detector = CheatingDetector(self.folder_path)
        report = self.detector.get_cheating_report()

        self.output_box.clear()  # Clear previous output
        for line in report:
            # Create a QListWidgetItem for each line
            item = QListWidgetItem(line)
            item.setData(Qt.ItemDataRole.UserRole, line)
            self.output_box.addItem(item)

        # Connect item clicked signal to handler
        self.output_box.itemClicked.connect(self.on_item_clicked)

    def on_item_clicked(self, item):
        # Get the message from the clicked item
        message = item.data(Qt.ItemDataRole.UserRole)

        # Extract the file names from the message
        part1 = message.split(' between ')[1].split(' and ')
        file1 = part1[0]
        file2 = part1[1].split(' with ')[0]

        # Read the content of the files using the full path
        code1 = self.get_file_content(file1)
        code2 = self.get_file_content(file2)

        # Open the comparison dialog with filenames
        dialog = CodeComparisonDialog(code1, code2, file1, file2, self)
        dialog.exec()

    def export_to_excel(self):
        if not self.detector:
            self.output_box.addItem("No detection run yet!")
            return

        excel_exporter = ExcelExporter(self.detector, self.folder_path)  # Pass the detector to the ExcelExporter
        save_path, _ = QFileDialog.getSaveFileName(self, "Save Report As", "", "Excel Files (*.xlsx)")

        if save_path:
            excel_exporter.export(save_path)
            self.output_box.addItem(f"Report saved to: {save_path}")

    def export_for_students(self):
        if not self.detector:
            self.output_box.addItem("No detection run yet!")
            return

        excel_exporter = ExcelExporter(self.detector, self.folder_path)

        try:
            save_path, _ = QFileDialog.getSaveFileName(self, "Save Student Report As", "", "Excel Files (*.xlsx)")

            if save_path:
                # Check if the file path is valid before proceeding
                if not save_path.lower().endswith('.xlsx'):
                    save_path += '.xlsx'

                excel_exporter.export_for_students(save_path)
                self.output_box.addItem(f"Student report saved to: {save_path}")
            else:
                self.output_box.addItem("Save operation canceled by the user.")
        except Exception as e:
            print(f"Error during export: {e}")
            self.output_box.addItem(f"Error during export: {e}")

    def get_file_content(self, filename):
        # Construct the full path using the selected folder path and the filename
        full_path = f"{self.folder_path}/{filename}"
        try:
            with open(full_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return f"File not found: {full_path}"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CheatingDetectionApp()
    window.show()
    sys.exit(app.exec())
