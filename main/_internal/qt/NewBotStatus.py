# Form implementation generated from reading ui file 'NewBotStatus.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgNewBotStatus(object):
    def setupUi(self, dlgNewBotStatus):
        dlgNewBotStatus.setObjectName("dlgNewBotStatus")
        dlgNewBotStatus.resize(320, 150)
        dlgNewBotStatus.setMinimumSize(QtCore.QSize(320, 150))
        dlgNewBotStatus.setMaximumSize(QtCore.QSize(320, 150))
        self.btnBox = QtWidgets.QDialogButtonBox(parent=dlgNewBotStatus)
        self.btnBox.setGeometry(QtCore.QRect(10, 110, 301, 32))
        self.btnBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.btnBox.setObjectName("btnBox")
        self.leNewBotStatus = QtWidgets.QLineEdit(parent=dlgNewBotStatus)
        self.leNewBotStatus.setGeometry(QtCore.QRect(20, 75, 280, 20))
        self.leNewBotStatus.setObjectName("leNewBotStatus")
        self.lblNewBotStatus1 = QtWidgets.QLabel(parent=dlgNewBotStatus)
        self.lblNewBotStatus1.setGeometry(QtCore.QRect(20, 30, 281, 16))
        self.lblNewBotStatus1.setObjectName("lblNewBotStatus1")
        self.lblNewBotStatus2 = QtWidgets.QLabel(parent=dlgNewBotStatus)
        self.lblNewBotStatus2.setGeometry(QtCore.QRect(20, 42, 271, 20))
        self.lblNewBotStatus2.setObjectName("lblNewBotStatus2")

        self.retranslateUi(dlgNewBotStatus)
        self.btnBox.accepted.connect(dlgNewBotStatus.accept) # type: ignore
        self.btnBox.rejected.connect(dlgNewBotStatus.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(dlgNewBotStatus)

    def retranslateUi(self, dlgNewBotStatus):
        _translate = QtCore.QCoreApplication.translate
        dlgNewBotStatus.setWindowTitle(_translate("dlgNewBotStatus", "New Bot Status"))
        self.lblNewBotStatus1.setText(_translate("dlgNewBotStatus", "Please provide a new bot status for the bot to cycle"))
        self.lblNewBotStatus2.setText(_translate("dlgNewBotStatus", "through."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgNewBotStatus = QtWidgets.QDialog()
    ui = Ui_dlgNewBotStatus()
    ui.setupUi(dlgNewBotStatus)
    dlgNewBotStatus.show()
    sys.exit(app.exec())
