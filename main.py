import sys
from PyQt6 import QtCore
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QTextEdit, QListWidget, QLabel
)
from PyQt6.QtCore import Qt

from cheating_detector import CheatingDetector
from excel_exporter import ExcelExporter  # Import the new ExcelExporter module


class CheatingDetectionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cheating Detection System")
        self.setGeometry(100, 100, 800, 600)

        self.detector = None

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

        # Output box
        self.output_box = QListWidget(self)
        layout.addWidget(self.output_box)

        self.folder_path = "\\"

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Homework Folder")
        if folder_path:
            self.folder_path = folder_path
            self.output_box.addItem(f"Selected folder: {self.folder_path}")

    def run_detection(self):
        if not self.folder_path:
            self.output_box.addItem("No folder selected!")
            return

        self.detector = CheatingDetector(self.folder_path)
        report = self.detector.get_cheating_report()

        self.output_box.clear()  # Clear previous output
        for line in report:
            self.output_box.addItem(line)

    def export_to_excel(self):
        if not self.detector:
            self.output_box.addItem("No detection run yet!")
            return

        excel_exporter = ExcelExporter(self.detector)  # Pass the detector to the ExcelExporter
        save_path, _ = QFileDialog.getSaveFileName(self, "Save Report As", "", "Excel Files (*.xlsx)")

        if save_path:
            excel_exporter.export(save_path)
            self.output_box.addItem(f"Report saved to: {save_path}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CheatingDetectionApp()
    window.show()
    sys.exit(app.exec())
