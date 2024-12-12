from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QListWidget, QVBoxLayout, QWidget
from googletrans import Translator
import speech_recognition as sr
from translator import Ui_Form
import requests
import sys

class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.voice_input_button = QPushButton(self)
        self.voice_input_button.setIcon(QIcon("microphone.png"))
        self.voice_input_button.setIconSize(QSize(35, 35))
        self.voice_input_button.setFixedSize(50, 50)
        self.voice_input_button.setStyleSheet("""
            QPushButton {
                border: none;
                border-radius: 20px;
                background-color: #87CEEB;
            }
            QPushButton:hover {
                background-color: #4682B4;
            }
            QPushButton:pressed {
                background-color: #1E90FF;
            }
        """)
        self.voice_input_button.move(self.width() - 70, self.height() - 70)
        self.voice_input_button.clicked.connect(self.voice_input)

        self.ui.vibormovi1.addItems(["Німецька", "Французька", "Італійська", "Польська"])
        self.ui.vibormovi1_2.addItems(["Німецька", "Французька", "Італійська", "Польська"])

        # Контейнер для історії та кнопки "Очистити історію"
        self.history_container = QWidget(self)
        self.history_container.setGeometry(20, 40, 400, 200)  # Розміщуємо під кнопкою "Історія"

        # Список для історії
        self.history_list = QListWidget(self.history_container)
        self.history_list.setGeometry(10, 10, 380, 150)

        # Кнопка "Очистити історію"
        self.clear_history_button = QPushButton("Очистити історію", self.history_container)
        self.clear_history_button.setGeometry(250, 170, 130, 30)
        self.clear_history_button.clicked.connect(self.clear_history)

        # Кнопка для відкриття/закриття історії
        self.toggle_history_button = QPushButton("Історія", self)
        self.toggle_history_button.setGeometry(self.width() - 120, 10, 100, 30)
        self.toggle_history_button.clicked.connect(self.toggle_history)

        # Історія прихована за замовчуванням
        self.history_container.setVisible(False)

        self.setStyleSheet("""
            QWidget {
                background-image: url("background.jpg");
                background-repeat: no-repeat;
                background-position: center;
                background-size: cover;
            }
        """)

        self.ui.textEdit.setStyleSheet("""
            QTextEdit {
                border: 2px solid gray;
                border-radius: 10px;
                padding: 5px;
                font-size: 18px;  /* Відновлено розмір шрифта */
                font-family: Arial, sans-serif;  /* Встановлено шрифт */
            }
        """)

        self.ui.textBrowser_2.setStyleSheet("""
            QTextBrowser {
                border: 2px solid gray;
                border-radius: 10px;
                padding: 5px;
                background-color: white;
                font-size: 18px;  /* Відновлено розмір шрифта */
                font-family: Arial, sans-serif;  /* Встановлено шрифт */
            }
        """)

        self.ui.vibormovi1.setStyleSheet("""
            QComboBox {
                border: 2px solid gray;
                border-radius: 10px;
                padding: 5px;
                background: rgba(255, 255, 255, 180);
                background-image: url("background.jpg");
                background-repeat: no-repeat;
                background-position: center;
            }
            QComboBox::drop-down {
                border: 0px;
            }
        """)
        self.ui.vibormovi1_2.setStyleSheet("""
            QComboBox {
                border: 2px solid gray;
                border-radius: 10px;
                padding: 5px;
                background: rgba(255, 255, 255, 180);
                background-image: url("background.jpg");
                background-repeat: no-repeat;
                background-position: center;
            }
            QComboBox::drop-down {
                border: 0px;
            }
        """)

        self.ui.pushButton.setStyleSheet("""
            QPushButton {
                border: 2px solid gray;
                border-radius: 15px;
                padding: 5px;
                background-color: #87CEEB;
                color: black;
                font-size: 11px;
            }
            QPushButton:hover {
                background-color: #4682B4;
            }
            QPushButton:pressed {
                background-color: #1E90FF;
            }
        """)

        if not self.check_internet_connection():
            self.show_no_internet_message()

        self.translator = Translator()
        self.ui.pushButton.clicked.connect(self.translate_text)
        self.setFixedSize(971, 653)

    def voice_input(self):
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                self.ui.textBrowser_2.setPlainText("Слухаю...")
                QApplication.processEvents()  # Оновлення інтерфейсу під час прослуховування

                audio = recognizer.listen(source)

                text = recognizer.recognize_google(audio, language="uk-UA")

                self.ui.textBrowser_2.clear()
                self.ui.textEdit.setPlainText(text)  # Вставляємо розпізнаний текст
        except sr.UnknownValueError:
            self.ui.textBrowser_2.setPlainText("Не вдалося розпізнати голос.")
        except sr.RequestError as e:
            self.ui.textBrowser_2.setPlainText(f"Помилка з'єднання з сервером: {e}")
        except Exception as e:
            self.ui.textBrowser_2.setPlainText(f"Невідома помилка: {e}")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.voice_input_button.move(self.width() - 63, self.height() - 60)
        self.toggle_history_button.move(self.width() - 120, 10)  # Зміщуємо кнопку "Історія"
        self.history_container.move(self.width() - 410, 50)

    def check_internet_connection(self):
        try:
            requests.get("https://www.google.com", timeout=3)
            return True
        except requests.ConnectionError:
            return False

    def add_to_history(self, text, translated_text):
        # Додаємо слово і переклад в історію
        self.history_list.addItem(f"{text} - {translated_text}")

    def clear_history(self):
        self.history_list.clear()

    def toggle_history(self):
        current_visibility = self.history_container.isVisible()
        self.history_container.setVisible(not current_visibility)

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

        lang_map = {"українська": "uk", "англійська": "en", "німецька": "de", "французька": "fr", "італійська": "it", "польська": "pl"}
        src_code = lang_map.get(src_lang, "auto")
        dest_code = lang_map.get(dest_lang, "uk")

        try:
            translated = self.translator.translate(text, src=src_code, dest=dest_code)
            translated_text = translated.text
            self.ui.textBrowser_2.setPlainText(translated_text)

            # Додаємо введене слово і переклад в історію
            self.add_to_history(text, translated_text)

        except Exception as e:
            self.ui.textBrowser_2.setPlainText(f"Помилка перекладу: {e}")


if __name__ == "__main__":
    app = QApplication([])
    window = TranslatorApp()
    window.show()
    app.exec_()
