# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.edt_mesaj = QtWidgets.QLineEdit(Dialog)
        self.edt_mesaj.setGeometry(QtCore.QRect(40, 50, 113, 20))
        self.edt_mesaj.setObjectName("edt_mesaj")
        self.btn_merhaba_yaz = QtWidgets.QPushButton(Dialog)
        self.btn_merhaba_yaz.setGeometry(QtCore.QRect(220, 50, 75, 23))
        self.btn_merhaba_yaz.setObjectName("btn_merhaba_yaz")

        self.btn_merhaba_yaz.clicked.connect(self.btn_merhaba_yaz_clicked)
         
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Merhaba"))
        self.btn_merhaba_yaz.setText(_translate("Dialog", "Merhaba Yaz"))
        
    def btn_merhaba_yaz_clicked(self):
        self.edt_mesaj.setText("Merhaba QT")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
