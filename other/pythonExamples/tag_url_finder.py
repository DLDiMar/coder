import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTextEdit, QVBoxLayout
import requests
from bs4 import BeautifulSoup

class HTagFinder(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 200)

        vbox = QVBoxLayout()
        self.setLayout(vbox)

        self.url_input = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.h_tags_display = QTextEdit()

        vbox.addWidget(self.url_input)
        vbox.addWidget(self.submit_button)
        vbox.addWidget(self.h_tags_display)

        self.submit_button.clicked.connect(self.find_h_tags)

    def find_h_tags(self):
        url = self.url_input.text()
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
                h_tags = soup.find_all("h1", "h2", "h3", "h4", "h5", "h6")
                h_tags_text = "\n".join([tag.text for tag in h_tags])
                self.h_tags_display.setText(h_tags_text)
            else:
                self.h_tags_display.setText("Error: Could not fetch the URL.")
        except Exception as e:
            self.h_tags_display.setText(f"Error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HTagFinder()
    window.show()
    sys.exit(app.exec_())