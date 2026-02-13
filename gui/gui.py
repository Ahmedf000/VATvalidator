from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QTextEdit, QLineEdit, QLabel
from PyQt5.QtWidgets.QMainWindow import centralWidget

from requests_vat.requests_vat import validate_address

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VAT Validator & Holder Name Cleaner")
        self.setGeometry(700, 500, 800, 500)
        self.vat_input = QLineEdit()
        self.vat_button = QPushButton("Validate Address")
        self.holder_name_input = QLineEdit()
        self.holder_name_button = QPushButton("Validate Holder Name")
        self.clear_button = QPushButton("Clear")
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.build_ui()



    def build_ui(self):
        central = centralWidget(self)
        self.setCentralWidget(central)

        vbox = QVBoxLayout()

        vat_code = QLabel("VAT Code:  ")
        vbox.addWidget(vat_code)
        vbox.addWidget(self.vat_input)
        self.vat_input.setPlaceholderText("Paste your VAT Code here..")

        holder_name = QLabel("Bank holder name:  ")
        vbox.addWidget(holder_name)
        vbox.addwidget(self.holder_name_input)
        self.holder_name_input.setPlaceholderText("Paste your Holder Name here..")

        self.vat_input.setObjectName("vat_input")
        self.vat_button.setObjectName("vat_button")
        self.holder_name_input.setObjectName("holder_name_input")
        self.holder_name_button.setObjectName("holder_name_button")
        self.clear_button.setObjectName("clear_button")
        self.output.setObjectName("output")

        self.setStyleSheet("""
        QWidget {
            background-image: url(:/images/your_background.png);
            background-repeat: no-repeat;
            background-position: center;
            background-color: transparent;
            font-family: "Segoe UI", sans-serif;
            color: #333;
        }

        #vat_input, #holder_name_input {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #ff9a9e, stop:1 #f77062);
            border: none;
            border-radius: 12px;
            padding: 8px 10px;
            font-size: 14px;
            color: white;
        }

        #vat_button, #holder_name_button, #clear_button {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #ff4fa1, stop:1 #ff1c6c);
            border: none;
            border-radius: 12px;
            padding: 10px 18px;
            font-size: 14px;
            color: white;
        }

        #vat_button:hover, #holder_name_button:hover, #clear_button:hover {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #ff1c6c, stop:1 #e60050);
        }

        #output {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 14px;
            padding: 12px;
            font-size: 13px;
            color: #333;
        }
        """)

        central.setLayout(vbox)


    def erase(self):
        pass


    def click(self):
        pass