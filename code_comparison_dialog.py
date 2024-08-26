from PyQt6.QtWidgets import QDialog, QTextEdit, QVBoxLayout, QLabel
from PyQt6.QtGui import QFont


class CodeComparisonDialog(QDialog):
    def __init__(self, code1, code2, filename1, filename2, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Code Comparison")
        self.setGeometry(100, 100, 1000, 600)

        # Layouts
        layout = QVBoxLayout(self)

        # Filenames Labels
        label1 = QLabel(filename1)
        label1.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        layout.addWidget(label1)

        code1_text = QTextEdit()
        code1_text.setPlainText(code1)
        code1_text.setFont(QFont("Courier", 10))
        code1_text.setReadOnly(True)
        layout.addWidget(code1_text)

        label2 = QLabel(filename2)
        label2.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        layout.addWidget(label2)

        code2_text = QTextEdit()
        code2_text.setPlainText(code2)
        code2_text.setFont(QFont("Courier", 10))
        code2_text.setReadOnly(True)
        layout.addWidget(code2_text)

        # Set layout for the dialog
        self.setLayout(layout)
