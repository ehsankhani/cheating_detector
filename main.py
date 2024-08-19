import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QWidget, QTextEdit
import traceback


class CheatingDetectionGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Cheating Detection Tool')
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.select_folder_button = QPushButton('Select Homework Folder', self)
        self.select_folder_button.clicked.connect(self.load_homework_folder)

        self.result_display = QTextEdit(self)
        self.result_display.setReadOnly(True)

        self.layout.addWidget(self.select_folder_button)
        self.layout.addWidget(self.result_display)

    def load_homework_folder(self):
        directory = QFileDialog.getExistingDirectory(self, 'Select Directory')
        if directory:
            try:
                from cheating_detector import CheatingDetector
                detector = CheatingDetector(directory)
                report = detector.get_cheating_report()
                self.result_display.setPlainText('\n'.join(report))
            except Exception as e:
                error_message = f"An error occurred: {str(e)}\n{traceback.format_exc()}"
                self.result_display.setPlainText(error_message)


def main():
    app = QApplication(sys.argv)
    window = CheatingDetectionGUI()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
