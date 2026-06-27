import sys
from pathlib import Path

from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QFileDialog, QMessageBox
)

from converter import convert, ConverterError

FILE_FILTER = "Data files (*.json *.xml *.yml *.yaml)"


class ConvertThread(QThread):
    succeeded = pyqtSignal(str)
    failed = pyqtSignal(str)

    def __init__(self, src: Path, dst: Path):
        super().__init__()
        self.src = src
        self.dst = dst

    def run(self):
        try:
            convert(self.src, self.dst)
            self.succeeded.emit(f"Done: '{self.src}' → '{self.dst}'")
        except ConverterError as e:
            self.failed.emit(str(e))


class ConverterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Format Converter")
        self.setMinimumWidth(520)
        self._thread = None

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

        self.convert_btn.setEnabled(False)
        self.status.setText("Converting…")

        self._thread = ConvertThread(Path(src), Path(dst))
        self._thread.succeeded.connect(self._on_success)
        self._thread.failed.connect(self._on_error)
        self._thread.start()

    def _on_success(self, message: str):
        self.status.setText(message)
        self.convert_btn.setEnabled(True)

    def _on_error(self, message: str):
        self.status.setText(f"Error: {message}")
        QMessageBox.critical(self, "Conversion Error", message)
        self.convert_btn.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ConverterWindow()
    window.show()
    sys.exit(app.exec())
