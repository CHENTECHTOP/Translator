# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Translator.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(971, 653)
        Form.setStyleSheet("")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-310, -280, 1831, 1061))
        self.widget.setStyleSheet("background-color: white;\n"
"")
        self.widget.setObjectName("widget")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setGeometry(QtCore.QRect(330, 280, 381, 91))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setGeometry(QtCore.QRect(370, 410, 841, 211))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_3 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_3.setGeometry(QtCore.QRect(720, 630, 21, 51))
        self.textEdit_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_2.setGeometry(QtCore.QRect(370, 690, 841, 221))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textEdit_4 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_4.setGeometry(QtCore.QRect(880, 630, 21, 51))
        self.textEdit_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(770, 640, 75, 23))
        self.pushButton.setStyleSheet("Fusion")
        self.pushButton.setObjectName("pushButton")
        self.vibormovi1 = QtWidgets.QComboBox(self.widget)
        self.vibormovi1.setGeometry(QtCore.QRect(370, 370, 111, 31))
        self.vibormovi1.setObjectName("vibormovi1")
        self.vibormovi1.addItem("")
        self.vibormovi1.addItem("")
        self.vibormovi1_2 = QtWidgets.QComboBox(self.widget)
        self.vibormovi1_2.setGeometry(QtCore.QRect(370, 650, 111, 31))
        self.vibormovi1_2.setObjectName("vibormovi1_2")
        self.vibormovi1_2.addItem("")
        self.vibormovi1_2.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Vladichhok Перекладач"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt;\">Перекладач</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">↓</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">↓</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Перекласти"))
        self.vibormovi1.setItemText(0, _translate("Form", "Українська"))
        self.vibormovi1.setItemText(1, _translate("Form", "Англійська"))
        self.vibormovi1_2.setItemText(0, _translate("Form", "Англійська"))
        self.vibormovi1_2.setItemText(1, _translate("Form", "Українська"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
