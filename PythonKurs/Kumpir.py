# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Kumpir.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#pycui5 -x Kumpir.ui -o Kumpir.py
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(483, 377)
        self.cmb_kumpir_tipi = QtWidgets.QComboBox(Form)
        self.cmb_kumpir_tipi.setGeometry(QtCore.QRect(260, 50, 161, 22))
        self.cmb_kumpir_tipi.setObjectName("cmb_kumpir_tipi")
        self.cmb_kumpir_tipi.addItem("")
        self.cmb_kumpir_tipi.addItem("")
        self.cmb_kumpir_tipi.addItem("")
        self.cmb_kumpir_tipi.addItem("")
        self.cmb_kumpir_tipi.setItemText(3, "")
        self.cmb_malzeme1 = QtWidgets.QComboBox(Form)
        self.cmb_malzeme1.setGeometry(QtCore.QRect(260, 110, 161, 22))
        self.cmb_malzeme1.setObjectName("cmb_malzeme1")
        self.cmb_malzeme1.addItem("")
        self.cmb_malzeme1.addItem("")
        self.cmb_malzeme1.addItem("")
        self.cmb_malzeme1.addItem("")
        self.cmb_malzeme1.addItem("")
        self.cmb_malzeme2 = QtWidgets.QComboBox(Form)
        self.cmb_malzeme2.setGeometry(QtCore.QRect(260, 150, 161, 22))
        self.cmb_malzeme2.setObjectName("cmb_malzeme2")
        self.cmb_malzeme2.addItem("")
        self.cmb_malzeme2.addItem("")
        self.cmb_malzeme2.addItem("")
        self.cmb_malzeme2.addItem("")
        self.cmb_malzeme2.addItem("")
        self.cmb_cikolata = QtWidgets.QComboBox(Form)
        self.cmb_cikolata.setGeometry(QtCore.QRect(260, 210, 161, 22))
        self.cmb_cikolata.setObjectName("cmb_cikolata")
        self.cmb_cikolata.addItem("")
        self.cmb_cikolata.addItem("")
        self.cmb_susleme = QtWidgets.QComboBox(Form)
        self.cmb_susleme.setGeometry(QtCore.QRect(260, 250, 161, 22))
        self.cmb_susleme.setObjectName("cmb_susleme")
        self.cmb_susleme.addItem("")
        self.cmb_susleme.addItem("")
        self.cmb_susleme.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 50, 121, 16))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 110, 121, 16))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 150, 121, 16))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 210, 121, 16))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(80, 250, 121, 16))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btn_Hesapla = QtWidgets.QPushButton(Form)
        self.btn_Hesapla.setGeometry(QtCore.QRect(170, 290, 131, 31))
        self.btn_Hesapla.setObjectName("btn_Hesapla")
        self.edt_sonuc = QtWidgets.QLineEdit(Form)
        self.edt_sonuc.setGeometry(QtCore.QRect(20, 330, 441, 20))
        self.edt_sonuc.setObjectName("edt_sonuc")
        
        self.cmb_kumpir_tipi.currentIndexChanged.connect(self.kumpir_tipi_secim)
        self.btn_Hesapla.clicked.connect(self.hesaplama)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.cmb_kumpir_tipi.setItemText(0, _translate("Form", "Sade Kumpir:Tereyağ+Kaşar"))
        self.cmb_kumpir_tipi.setItemText(1, _translate("Form", "Çift Kaşarlı Kumpir"))
        self.cmb_kumpir_tipi.setItemText(2, _translate("Form", "Karışık Kumpir"))
        self.cmb_malzeme1.setItemText(0, _translate("Form", "Mantar"))
        self.cmb_malzeme1.setItemText(1, _translate("Form", "Siyah Zeytin"))
        self.cmb_malzeme1.setItemText(2, _translate("Form", "Ketçap"))
        self.cmb_malzeme1.setItemText(3, _translate("Form", "Mayonez"))
        self.cmb_malzeme1.setItemText(4, _translate("Form", "Salam"))
        self.cmb_malzeme2.setItemText(0, _translate("Form", "Mantar"))
        self.cmb_malzeme2.setItemText(1, _translate("Form", "Yeşil Zeytin"))
        self.cmb_malzeme2.setItemText(2, _translate("Form", "Ketçap"))
        self.cmb_malzeme2.setItemText(3, _translate("Form", "Mayonez"))
        self.cmb_malzeme2.setItemText(4, _translate("Form", "Salam"))
        self.cmb_cikolata.setItemText(0, _translate("Form", "Beyaz Çikolata"))
        self.cmb_cikolata.setItemText(1, _translate("Form", "Bitter"))
        self.cmb_susleme.setItemText(0, _translate("Form", "Kivi"))
        self.cmb_susleme.setItemText(1, _translate("Form", "Hindistan Cevizi"))
        self.cmb_susleme.setItemText(2, _translate("Form", "Damla çikolata"))
        self.label.setText(_translate("Form", "Kumpir Tipi Seçin"))
        self.label_2.setText(_translate("Form", "Malzeme 1"))
        self.label_3.setText(_translate("Form", "Malzeme 2"))
        self.label_4.setText(_translate("Form", "Çikolata"))
        self.label_5.setText(_translate("Form", "Süsleme"))
        self.btn_Hesapla.setText(_translate("Form", "Hesapla"))
        
        self.cmb_kumpir_tipi.currentIndexChanged.connect(self.kumpir_tipi_secim)
        self.btn_Hesapla.clicked.connect(self.hesaplama)       
        
        
        
        
    def kumpir_tipi_secim(self):
        secilen_index=self.cmb_kumpir_tipi.currentIndex()
        if(secilen_index<2):
             self.cmb_malzeme1.setEnabled(False)
             self.cmb_malzeme2.setEnabled(False)
             self.cmb_cikolata.setEnabled(False)
             self.cmb_susleme.setEnabled(False)
        else:
             self.cmb_malzeme1.setEnabled(True)
             self.cmb_malzeme2.setEnabled(True)
             self.cmb_cikolata.setEnabled(True)
             self.cmb_susleme.setEnabled(True)
             
             
    def hesaplama(self):
        str_sonuc=""
        secilen_index=self.cmb_kumpir_tipi.currentIndex()
        if(secilen_index<2):
            str_sonuc=self.cmb_kumpir_tipi.currentText()
        else:
            str_sonuc=self.cmb_malzeme1.currentText() + " " + \
            self.cmb_malzeme2.currentText() + " " + \
            self.cmb_cikolata.currentText() + " " + \
            self.cmb_susleme.currentText() + " " + \
            self.cmb_kumpir_tipi.currentText()
            
        self.edt_sonuc.setText(str_sonuc)
           
      


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
