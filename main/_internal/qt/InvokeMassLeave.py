# Form implementation generated from reading ui file 'InvokeMassLeave.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgInvokeMassLeave(object):
    def setupUi(self, dlgInvokeMassLeave):
        dlgInvokeMassLeave.setObjectName("dlgInvokeMassLeave")
        dlgInvokeMassLeave.resize(320, 150)
        dlgInvokeMassLeave.setMinimumSize(QtCore.QSize(320, 150))
        dlgInvokeMassLeave.setMaximumSize(QtCore.QSize(320, 150))
        self.btnBox = QtWidgets.QDialogButtonBox(parent=dlgInvokeMassLeave)
        self.btnBox.setGeometry(QtCore.QRect(10, 110, 301, 32))
        self.btnBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.btnBox.setObjectName("btnBox")
        self.lblComf = QtWidgets.QLabel(parent=dlgInvokeMassLeave)
        self.lblComf.setGeometry(QtCore.QRect(20, 30, 281, 16))
        self.lblComf.setObjectName("lblComf")
        self.lblComf2 = QtWidgets.QLabel(parent=dlgInvokeMassLeave)
        self.lblComf2.setGeometry(QtCore.QRect(20, 45, 281, 16))
        self.lblComf2.setObjectName("lblComf2")

        self.retranslateUi(dlgInvokeMassLeave)
        self.btnBox.accepted.connect(dlgInvokeMassLeave.accept) # type: ignore
        self.btnBox.rejected.connect(dlgInvokeMassLeave.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(dlgInvokeMassLeave)

    def retranslateUi(self, dlgInvokeMassLeave):
        _translate = QtCore.QCoreApplication.translate
        dlgInvokeMassLeave.setWindowTitle(_translate("dlgInvokeMassLeave", "Leave Every Server"))
        self.lblComf.setText(_translate("dlgInvokeMassLeave", "Are you sure you want Horus to leave"))
        self.lblComf2.setText(_translate("dlgInvokeMassLeave", "every server it is in?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgInvokeMassLeave = QtWidgets.QDialog()
    ui = Ui_dlgInvokeMassLeave()
    ui.setupUi(dlgInvokeMassLeave)
    dlgInvokeMassLeave.show()
    sys.exit(app.exec())
