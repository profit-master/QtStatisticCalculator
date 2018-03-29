# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instrumentView.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(605, 418)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vBoxLeft = QtWidgets.QVBoxLayout()
        self.vBoxLeft.setContentsMargins(-1, -1, 10, -1)
        self.vBoxLeft.setObjectName("vBoxLeft")
        self.labelWatchLists = QtWidgets.QLabel(Dialog)
        self.labelWatchLists.setObjectName("labelWatchLists")
        self.vBoxLeft.addWidget(self.labelWatchLists)
        self.comboWatch = QtWidgets.QComboBox(Dialog)
        self.comboWatch.setObjectName("comboWatch")
        self.vBoxLeft.addWidget(self.comboWatch)
        self.listWatch = QtWidgets.QListView(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWatch.sizePolicy().hasHeightForWidth())
        self.listWatch.setSizePolicy(sizePolicy)
        self.listWatch.setObjectName("listWatch")
        self.vBoxLeft.addWidget(self.listWatch)
        self.hBoxButtons = QtWidgets.QHBoxLayout()
        self.hBoxButtons.setObjectName("hBoxButtons")
        self.btnNew = QtWidgets.QPushButton(Dialog)
        self.btnNew.setObjectName("btnNew")
        self.hBoxButtons.addWidget(self.btnNew)
        self.btnDelete = QtWidgets.QPushButton(Dialog)
        self.btnDelete.setObjectName("btnDelete")
        self.hBoxButtons.addWidget(self.btnDelete)
        self.vBoxLeft.addLayout(self.hBoxButtons)
        self.horizontalLayout.addLayout(self.vBoxLeft)
        self.vLine = QtWidgets.QFrame(Dialog)
        self.vLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.vLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vLine.setObjectName("vLine")
        self.horizontalLayout.addWidget(self.vLine)
        self.vBoxRight = QtWidgets.QVBoxLayout()
        self.vBoxRight.setContentsMargins(10, -1, -1, -1)
        self.vBoxRight.setObjectName("vBoxRight")
        self.labelAvaliableInstruments = QtWidgets.QLabel(Dialog)
        self.labelAvaliableInstruments.setObjectName("labelAvaliableInstruments")
        self.vBoxRight.addWidget(self.labelAvaliableInstruments)
        self.hBoxSearch = QtWidgets.QHBoxLayout()
        self.hBoxSearch.setContentsMargins(-1, 5, -1, 5)
        self.hBoxSearch.setObjectName("hBoxSearch")
        self.formSearch = QtWidgets.QFormLayout()
        self.formSearch.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.formSearch.setContentsMargins(-1, -1, 20, -1)
        self.formSearch.setHorizontalSpacing(20)
        self.formSearch.setObjectName("formSearch")
        self.labelName = QtWidgets.QLabel(Dialog)
        self.labelName.setObjectName("labelName")
        self.formSearch.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelName)
        self.labelDescription = QtWidgets.QLabel(Dialog)
        self.labelDescription.setObjectName("labelDescription")
        self.formSearch.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelDescription)
        self.lineName = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineName.sizePolicy().hasHeightForWidth())
        self.lineName.setSizePolicy(sizePolicy)
        self.lineName.setObjectName("lineName")
        self.formSearch.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lineName)
        self.lineDescription = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineDescription.sizePolicy().hasHeightForWidth())
        self.lineDescription.setSizePolicy(sizePolicy)
        self.lineDescription.setObjectName("lineDescription")
        self.formSearch.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineDescription)
        self.hBoxSearch.addLayout(self.formSearch)
        self.btnSearch = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSearch.sizePolicy().hasHeightForWidth())
        self.btnSearch.setSizePolicy(sizePolicy)
        self.btnSearch.setObjectName("btnSearch")
        self.hBoxSearch.addWidget(self.btnSearch, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.vBoxRight.addLayout(self.hBoxSearch)
        self.hBoxChecked = QtWidgets.QHBoxLayout()
        self.hBoxChecked.setObjectName("hBoxChecked")
        self.vBoxListButtons = QtWidgets.QVBoxLayout()
        self.vBoxListButtons.setObjectName("vBoxListButtons")
        self.btnSelectAll = QtWidgets.QPushButton(Dialog)
        self.btnSelectAll.setObjectName("btnSelectAll")
        self.vBoxListButtons.addWidget(self.btnSelectAll)
        self.btnDeselectAll = QtWidgets.QPushButton(Dialog)
        self.btnDeselectAll.setObjectName("btnDeselectAll")
        self.vBoxListButtons.addWidget(self.btnDeselectAll)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vBoxListButtons.addItem(spacerItem)
        self.btnInsert = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnInsert.sizePolicy().hasHeightForWidth())
        self.btnInsert.setSizePolicy(sizePolicy)
        self.btnInsert.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btnInsert.setObjectName("btnInsert")
        self.vBoxListButtons.addWidget(self.btnInsert)
        self.btnRemove = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRemove.sizePolicy().hasHeightForWidth())
        self.btnRemove.setSizePolicy(sizePolicy)
        self.btnRemove.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btnRemove.setObjectName("btnRemove")
        self.vBoxListButtons.addWidget(self.btnRemove)
        self.hBoxChecked.addLayout(self.vBoxListButtons)
        self.listChecked = QtWidgets.QListView(Dialog)
        self.listChecked.setObjectName("listChecked")
        self.hBoxChecked.addWidget(self.listChecked)
        self.vBoxRight.addLayout(self.hBoxChecked)
        self.vBoxRight.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.vBoxRight)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.hLine = QtWidgets.QFrame(Dialog)
        self.hLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.hLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hLine.setObjectName("hLine")
        self.verticalLayout.addWidget(self.hLine)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 10, 0, 5)
        self.gridLayout.setHorizontalSpacing(80)
        self.gridLayout.setObjectName("gridLayout")
        self.btnOK = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOK.sizePolicy().hasHeightForWidth())
        self.btnOK.setSizePolicy(sizePolicy)
        self.btnOK.setObjectName("btnOK")
        self.gridLayout.addWidget(self.btnOK, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.btnCancel = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCancel.sizePolicy().hasHeightForWidth())
        self.btnCancel.setSizePolicy(sizePolicy)
        self.btnCancel.setObjectName("btnCancel")
        self.gridLayout.addWidget(self.btnCancel, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelWatchLists.setText(_translate("Dialog", "Watch lists: "))
        self.btnNew.setText(_translate("Dialog", "New"))
        self.btnDelete.setText(_translate("Dialog", "Delete"))
        self.labelAvaliableInstruments.setText(_translate("Dialog", "Available master instruments"))
        self.labelName.setText(_translate("Dialog", "Name"))
        self.labelDescription.setText(_translate("Dialog", "Description"))
        self.btnSearch.setText(_translate("Dialog", "Search"))
        self.btnSelectAll.setText(_translate("Dialog", "Select All"))
        self.btnDeselectAll.setText(_translate("Dialog", "Deselect All"))
        self.btnInsert.setText(_translate("Dialog", "<"))
        self.btnRemove.setText(_translate("Dialog", ">"))
        self.btnOK.setText(_translate("Dialog", "OK"))
        self.btnCancel.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

