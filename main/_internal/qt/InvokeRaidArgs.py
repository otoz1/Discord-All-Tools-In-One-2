# Form implementation generated from reading ui file 'InvokeRaidArgs.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgInvokeRaidArgs(object):
    def setupUi(self, dlgInvokeRaidArgs):
        dlgInvokeRaidArgs.setObjectName("dlgInvokeRaidArgs")
        dlgInvokeRaidArgs.resize(320, 400)
        dlgInvokeRaidArgs.setMinimumSize(QtCore.QSize(320, 400))
        dlgInvokeRaidArgs.setMaximumSize(QtCore.QSize(320, 400))
        self.btnBox = QtWidgets.QDialogButtonBox(parent=dlgInvokeRaidArgs)
        self.btnBox.setGeometry(QtCore.QRect(10, 350, 301, 32))
        self.btnBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.btnBox.setObjectName("btnBox")
        self.lblRoleName = QtWidgets.QLabel(parent=dlgInvokeRaidArgs)
        self.lblRoleName.setGeometry(QtCore.QRect(20, 30, 281, 16))
        self.lblRoleName.setObjectName("lblRoleName")
        self.lblNickname = QtWidgets.QLabel(parent=dlgInvokeRaidArgs)
        self.lblNickname.setGeometry(QtCore.QRect(20, 95, 271, 16))
        self.lblNickname.setObjectName("lblNickname")
        self.leNickname = QtWidgets.QLineEdit(parent=dlgInvokeRaidArgs)
        self.leNickname.setGeometry(QtCore.QRect(20, 115, 281, 20))
        self.leNickname.setObjectName("leNickname")
        self.leRoleName = QtWidgets.QLineEdit(parent=dlgInvokeRaidArgs)
        self.leRoleName.setGeometry(QtCore.QRect(20, 50, 281, 20))
        self.leRoleName.setObjectName("leRoleName")
        self.lblAmount = QtWidgets.QLabel(parent=dlgInvokeRaidArgs)
        self.lblAmount.setGeometry(QtCore.QRect(20, 160, 281, 16))
        self.lblAmount.setObjectName("lblAmount")
        self.sbAmount = QtWidgets.QSpinBox(parent=dlgInvokeRaidArgs)
        self.sbAmount.setGeometry(QtCore.QRect(20, 180, 281, 22))
        self.sbAmount.setMinimum(1)
        self.sbAmount.setMaximum(100)
        self.sbAmount.setObjectName("sbAmount")
        self.lblChannelName = QtWidgets.QLabel(parent=dlgInvokeRaidArgs)
        self.lblChannelName.setGeometry(QtCore.QRect(20, 225, 281, 16))
        self.lblChannelName.setObjectName("lblChannelName")
        self.leChannelName = QtWidgets.QLineEdit(parent=dlgInvokeRaidArgs)
        self.leChannelName.setGeometry(QtCore.QRect(20, 245, 281, 20))
        self.leChannelName.setObjectName("leChannelName")
        self.lblMessage = QtWidgets.QLabel(parent=dlgInvokeRaidArgs)
        self.lblMessage.setGeometry(QtCore.QRect(20, 285, 281, 16))
        self.lblMessage.setObjectName("lblMessage")
        self.leMessage = QtWidgets.QLineEdit(parent=dlgInvokeRaidArgs)
        self.leMessage.setGeometry(QtCore.QRect(20, 305, 281, 20))
        self.leMessage.setObjectName("leMessage")

        self.retranslateUi(dlgInvokeRaidArgs)
        self.btnBox.accepted.connect(dlgInvokeRaidArgs.accept) # type: ignore
        self.btnBox.rejected.connect(dlgInvokeRaidArgs.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(dlgInvokeRaidArgs)
        dlgInvokeRaidArgs.setTabOrder(self.leRoleName, self.leNickname)
        dlgInvokeRaidArgs.setTabOrder(self.leNickname, self.sbAmount)
        dlgInvokeRaidArgs.setTabOrder(self.sbAmount, self.leChannelName)
        dlgInvokeRaidArgs.setTabOrder(self.leChannelName, self.leMessage)

    def retranslateUi(self, dlgInvokeRaidArgs):
        _translate = QtCore.QCoreApplication.translate
        dlgInvokeRaidArgs.setWindowTitle(_translate("dlgInvokeRaidArgs", "Raid Args"))
        self.lblRoleName.setText(_translate("dlgInvokeRaidArgs", "Enter a name for the new raided role"))
        self.lblNickname.setText(_translate("dlgInvokeRaidArgs", "Enter the nickname to nickname all members"))
        self.lblAmount.setText(_translate("dlgInvokeRaidArgs", "Enter the number of channels to create"))
        self.lblChannelName.setText(_translate("dlgInvokeRaidArgs", "Enter a name for the channels"))
        self.lblMessage.setText(_translate("dlgInvokeRaidArgs", "Enter the message to spam to all channels"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgInvokeRaidArgs = QtWidgets.QDialog()
    ui = Ui_dlgInvokeRaidArgs()
    ui.setupUi(dlgInvokeRaidArgs)
    dlgInvokeRaidArgs.show()
    sys.exit(app.exec())
