# Form implementation generated from reading ui file 'InvokeCPurge.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgInvokeCPurge(object):
    def setupUi(self, dlgInvokeCPurge):
        dlgInvokeCPurge.setObjectName("dlgInvokeCPurge")
        dlgInvokeCPurge.resize(320, 150)
        dlgInvokeCPurge.setMinimumSize(QtCore.QSize(320, 150))
        dlgInvokeCPurge.setMaximumSize(QtCore.QSize(320, 150))
        self.btnBox = QtWidgets.QDialogButtonBox(parent=dlgInvokeCPurge)
        self.btnBox.setGeometry(QtCore.QRect(10, 110, 301, 32))
        self.btnBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.btnBox.setObjectName("btnBox")
        self.lblComf = QtWidgets.QLabel(parent=dlgInvokeCPurge)
        self.lblComf.setGeometry(QtCore.QRect(20, 30, 281, 16))
        self.lblComf.setObjectName("lblComf")
        self.lblComf2 = QtWidgets.QLabel(parent=dlgInvokeCPurge)
        self.lblComf2.setGeometry(QtCore.QRect(20, 45, 281, 16))
        self.lblComf2.setObjectName("lblComf2")

        self.retranslateUi(dlgInvokeCPurge)
        self.btnBox.accepted.connect(dlgInvokeCPurge.accept) # type: ignore
        self.btnBox.rejected.connect(dlgInvokeCPurge.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(dlgInvokeCPurge)

    def retranslateUi(self, dlgInvokeCPurge):
        _translate = QtCore.QCoreApplication.translate
        dlgInvokeCPurge.setWindowTitle(_translate("dlgInvokeCPurge", "Confirm CPurge"))
        self.lblComf.setText(_translate("dlgInvokeCPurge", "Are you sure you want Horus to delete"))
        self.lblComf2.setText(_translate("dlgInvokeCPurge", "every channel in the given server?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgInvokeCPurge = QtWidgets.QDialog()
    ui = Ui_dlgInvokeCPurge()
    ui.setupUi(dlgInvokeCPurge)
    dlgInvokeCPurge.show()
    sys.exit(app.exec())
