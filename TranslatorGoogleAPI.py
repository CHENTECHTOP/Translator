from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from googletrans import Translator
from translator import Ui_Form
import requests
import sys


class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        if not self.check_internet_connection():
            self.show_no_internet_message()

        self.translator = Translator()
        self.ui.pushButton.clicked.connect(self.translate_text)

    def check_internet_connection(self):
        try:
            requests.get("https://www.google.com", timeout=3)
            return True
        except requests.ConnectionError:
            return False

    def show_no_internet_message(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Помилка")
        msg.setText("У вас немає підключення до Інтернету :(")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(self.close_app)
        msg.exec_()

    def close_app(self):
        sys.exit()  # Закриваємо програму повністю

    def translate_text(self):
        text = self.ui.textEdit.toPlainText()
        src_lang = self.ui.vibormovi1.currentText().lower()
        dest_lang = self.ui.vibormovi1_2.currentText().lower()

        lang_map = {"українська": "uk", "англійська": "en"}
        src_code = lang_map.get(src_lang, "auto")
        dest_code = lang_map.get(dest_lang, "uk")

        try:
            translated = self.translator.translate(text, src=src_code, dest=dest_code)
            self.ui.textBrowser_2.setPlainText(translated.text)
        except Exception as e:
            self.ui.textBrowser_2.setPlainText(f"Помилка перекладу: {e}")


if __name__ == "__main__":
    app = QApplication([])
    window = TranslatorApp()
    window.show()
    app.exec_()



