import sys
from string import digits

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QPushButton, QWidget, QTextEdit, QLineEdit, QLabel
)
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtCore import Qt

from requests_vat.requests_vat import validate_address
from parse_vat_re.parser_vat import VATCleaner
from parser_char.holder_parser_char import HolderNameCleaner

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VAT Validator & Holder Name Cleaner")
        self.setGeometry(400, 150, 150, 780)
        self.setMinimumSize(820, 600)


        self.vat_input = QLineEdit()
        self.vat_button = QPushButton("Validate Address")
        self.holder_name_input = QLineEdit()
        self.holder_name_button = QPushButton("Validate Holder Name")
        self.clear_button = QPushButton("Clear")
        self.output = QTextEdit()
        self.output.setReadOnly(True)

        self.vat_input.setObjectName("vat_input")
        self.vat_button.setObjectName("vat_button")
        self.holder_name_input.setObjectName("holder_name_input")
        self.holder_name_button.setObjectName("holder_name_button")
        self.clear_button.setObjectName("clear_button")
        self.output.setObjectName("output")



        self._apply_background("background.jpg")

        self.setStyleSheet("""
                    QMainWindow {
                        background-color: transparent;
                    }

                    QWidget#central_widget {
                        background: transparent;
                    }

                    QWidget#card {
                        background: rgba(255, 240, 245, 0.82);
                        border-radius: 24px;
                        border: 1.5px solid rgba(255, 100, 140, 0.25);
                    }

                    QLabel#title_label {
                        color: #c0003a;
                        font-family: 'Trebuchet MS', sans-serif;
                        font-size: 22px;
                        font-weight: 700;
                        letter-spacing: 1px;
                        padding: 0px 0px 6px 2px;
                        min-height: 34px;
                        max-height: 34px;
                    }

                    QLabel#vat_label, QLabel#holder_label, QLabel#output_label {
                        color: #d4005a;
                        font-family: 'Trebuchet MS', sans-serif;
                        font-size: 10px;
                        font-weight: 700;
                        letter-spacing: 2.5px;
                        padding: 0px 0px 2px 2px;
                        min-height: 16px;
                        max-height: 16px;
                    }

                    #vat_input {
                        background: rgba(255, 255, 255, 0.72);
                        border: 1.5px solid rgba(220, 60, 100, 0.35);
                        border-radius: 10px;
                        padding: 0px 12px;
                        font-family: 'Trebuchet MS', sans-serif;
                        font-size: 13px;
                        color: #3a0015;
                        min-height: 36px;
                        max-height: 36px;
                        selection-background-color: #ff3366;
                    }
                    #vat_input:focus {
                        border: 1.5px solid #ff2060;
                        background: rgba(255, 255, 255, 0.92);
                    }

                    #vat_button {
                        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                            stop:0 #ff5590, stop:0.5 #ff1a55, stop:1 #c4003c);
                        border: none;
                        border-radius: 10px;
                        padding: 0px 16px;
                        font-family: 'Trebuchet MS', sans-serif;
                        font-size: 13px;
                        font-weight: 600;
                        color: white;
                        letter-spacing: 0.4px;
                        min-height: 36px;
                        max-height: 36px;
                        min-width: 150px;
                        max-width: 150px;
                    }
                    #vat_button:hover {
                        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                            stop:0 #ff77aa, stop:0.5 #ff3d72, stop:1 #e6004a);
                    }
                    #vat_button:pressed {
                        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                            stop:0 #aa002e, stop:1 #880024);
                    }

                    #holder_name_input {
                        background: rgba(255, 255, 255, 0.72);
                        border: 1.5px solid rgba(220, 60, 100, 0.35);
                        border-radius: 10px;
                        padding: 0px 12px;
                        font-family: 'Trebuchet MS', sans-serif;
                        font-size: 13px;
                        color: #3a0015;
                        min-height: 36px;
                        max-height: 36px;
                        selection-background-color: #ff3366;
                    }
                    #holder_name_input:focus {
                        border: 1.5px solid #ff2060;
                        background: rgba(255, 255, 255, 0.92);
                    }

                    #holder_name_button {
                        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                            stop:0 #ff5590, stop:0.5 #ff1a55, stop:1 #c4003c);
                        border: none;
                        border-radius: 10px;
                        padding: 0px 16px;
                        font-family: 'Trebuchet MS', sans-serif;
                        font-size: 13px;
                        font-weight: 600;
                        color: white;
                        letter-spacing: 0.4px;
                        min-height: 36px;
                        max-height: 36px;
                        min-width: 150px;
                        max-width: 150px;
                    }
                    #holder_name_button:hover {
                        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                            stop:0 #ff77aa, stop:0.5 #ff3d72, stop:1 #e6004a);
                    }
                    #holder_name_button:pressed {
                        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                            stop:0 #aa002e, stop:1 #880024);
                    }

                    #clear_button {
                        background: rgba(255, 255, 255, 0.55);
                        border: 1.5px solid rgba(220, 60, 100, 0.4);
                        border-radius: 10px;
                        padding: 0px 14px;
                        font-family: 'Trebuchet MS', sans-serif;
                        font-size: 13px;
                        font-weight: 600;
                        color: #c0003a;
                        letter-spacing: 0.4px;
                        min-height: 32px;
                        max-height: 32px;
                        min-width: 90px;
                        max-width: 90px;
                    }
                    #clear_button:hover {
                        background: rgba(255, 50, 100, 0.12);
                        border: 1.5px solid rgba(220, 40, 80, 0.65);
                        color: #8c0028;
                    }
                    #clear_button:pressed {
                        background: rgba(255, 50, 100, 0.22);
                    }

                    #output {
                        background: rgba(255, 255, 255, 0.78);
                        border: 1.5px solid rgba(220, 60, 100, 0.25);
                        border-radius: 14px;
                        padding: 14px;
                        font-family: 'Consolas', 'Courier New', monospace;
                        font-size: 13px;
                        color: #3a0015;
                        min-height: 280px;
                        max-height: 280px;
                        selection-background-color: #ff3366;
                    }

                    QScrollBar:vertical {
                        background: rgba(255, 200, 215, 0.3);
                        width: 7px;
                        border-radius: 4px;
                        margin: 0;
                    }
                    QScrollBar::handle:vertical {
                        background: rgba(220, 60, 100, 0.5);
                        border-radius: 4px;
                        min-height: 20px;
                    }
                    QScrollBar::add-line:vertical,
                    QScrollBar::sub-line:vertical {
                        height: 0;
                    }
                """)

        self.build_ui()


    def _apply_background(self, image_path):
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            palette = self.palette()
            scaled = pixmap.scaled(
                self.size(),
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )
            palette.setBrush(QPalette.Window, QBrush(scaled))
            self.setPalette(palette)

    def build_ui(self):
        central = QWidget()
        central.setObjectName("central_widget")
        self.setCentralWidget(central)

        outer = QVBoxLayout(central)
        outer.setContentsMargins(36, 36, 36, 36)

        card = QWidget()
        card.setObjectName("card")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(32, 24, 32, 24)
        card_layout.setSpacing(8)

        title = QLabel("VAT Validator & Holder Name Cleaner")
        title.setObjectName("title_label")
        card_layout.addWidget(title)

        card_layout.addSpacing(4)

        vat_label = QLabel("VAT CODE")
        vat_label.setObjectName("vat_label")
        card_layout.addWidget(vat_label)

        vat_row = QHBoxLayout()
        vat_row.setSpacing(10)
        self.vat_input.setPlaceholderText("Paste your VAT Code here..")
        vat_row.addWidget(self.vat_input)
        vat_row.addWidget(self.vat_button)
        card_layout.addLayout(vat_row)

        card_layout.addSpacing(10)

        holder_label = QLabel("BANK HOLDER NAME")
        holder_label.setObjectName("holder_label")
        card_layout.addWidget(holder_label)

        holder_row = QHBoxLayout()
        holder_row.setSpacing(10)
        self.holder_name_input.setPlaceholderText("Paste your Holder Name here..")
        holder_row.addWidget(self.holder_name_input)
        holder_row.addWidget(self.holder_name_button)
        card_layout.addLayout(holder_row)

        card_layout.addSpacing(12)

        output_label = QLabel("OUTPUT")
        output_label.setObjectName("output_label")
        card_layout.addWidget(output_label)

        output_and_clear = QVBoxLayout()
        output_and_clear.setSpacing(6)
        output_and_clear.addWidget(self.output)

        clear_row = QHBoxLayout()
        clear_row.addStretch()
        clear_row.addWidget(self.clear_button)
        output_and_clear.addLayout(clear_row)

        card_layout.addLayout(output_and_clear)

        outer.addWidget(card)

        self.vat_button.clicked.connect(self.click_vat)
        self.holder_name_button.clicked.connect(self.click_holder_name)
        self.clear_button.clicked.connect(self.erase)


    def erase(self):
        self.vat_input.clear()
        self.holder_name_input.clear()
        self.output.clear()


    def click_holder_name(self):
        text = self.holder_name_input.text().strip()

        if not text:
            self.output.setText("Please enter a holder name...")
            return

        try:
            holder_name_parser = HolderNameCleaner()
            clean = holder_name_parser.clean_all(text)
            self.output.setText(str(clean))
        except Exception as e:
            self.output.setText(f"Unexpected error: {str(e)}")




    def click_vat(self):
        text = self.vat_input.text().strip().upper()
        if not text:
            self.output.setText("Please enter a VAT Code...")
            return
        try:
            parser = VATCleaner()
            cleaned = text
            cleaned = parser.extra_whitespace(cleaned)
            cleaned = parser.special_chars(cleaned)
            cleaned = parser.leading(cleaned)
            cleaned = parser.dash(cleaned)
            cleaned = parser.comma(cleaned)
            result = validate_address(cleaned)
            self.output.setText(result)
        except Exception as e:
            self.output.setText(f"Something went wrong: {e}")
































