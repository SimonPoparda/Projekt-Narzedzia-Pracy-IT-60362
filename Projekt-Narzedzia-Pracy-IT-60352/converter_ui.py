import sys
from pathlib import Path

from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QFileDialog, QMessageBox
)

from converter import convert, ConverterError

FILE_FILTER = "Data files (*.json *.xml *.yml *.yaml)"


class ConverterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Format Converter")
        self.setMinimumWidth(520)

        layout = QVBoxLayout(self)

        layout.addLayout(self._file_row("Input:", "input.json / .xml / .yml", self._browse_input))
        layout.addLayout(self._file_row("Output:", "output.json / .xml / .yml", self._browse_output))

        self.convert_btn = QPushButton("Convert")
        self.convert_btn.clicked.connect(self._convert)
        layout.addWidget(self.convert_btn)

        self.status = QLabel("")
        layout.addWidget(self.status)

    def _file_row(self, label: str, placeholder: str, browse_fn) -> QHBoxLayout:
        row = QHBoxLayout()
        field = QLineEdit()
        field.setPlaceholderText(placeholder)
        btn = QPushButton("Browse…")
        btn.clicked.connect(browse_fn)
        row.addWidget(QLabel(label))
        row.addWidget(field)
        row.addWidget(btn)
        if label == "Input:":
            self.input_field = field
        else:
            self.output_field = field
        return row

    def _browse_input(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select input file", "", FILE_FILTER)
        if path:
            self.input_field.setText(path)

    def _browse_output(self):
        path, _ = QFileDialog.getSaveFileName(self, "Select output file", "", FILE_FILTER)
        if path:
            self.output_field.setText(path)

    def _convert(self):
        src = self.input_field.text().strip()
        dst = self.output_field.text().strip()
        if not src or not dst:
            self.status.setText("Please select both input and output files.")
            return
        try:
            convert(Path(src), Path(dst))
            self.status.setText(f"Done: '{src}' → '{dst}'")
        except ConverterError as e:
            self.status.setText(f"Error: {e}")
            QMessageBox.critical(self, "Conversion Error", str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ConverterWindow()
    window.show()
    sys.exit(app.exec())
