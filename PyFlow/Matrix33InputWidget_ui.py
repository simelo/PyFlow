# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:/GIT/nodes/PyFlow/Matrix33InputWidget_ui.ui'
#
# Created: Sun Feb 04 18:32:04 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(221, 72)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.dsbm22 = QtGui.QDoubleSpinBox(Form)
        self.dsbm22.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dsbm22.setSingleStep(0.1)
        self.dsbm22.setObjectName("dsbm22")
        self.gridLayout.addWidget(self.dsbm22, 1, 1, 1, 1)
        self.dsbm21 = QtGui.QDoubleSpinBox(Form)
        self.dsbm21.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dsbm21.setSingleStep(0.1)
        self.dsbm21.setObjectName("dsbm21")
        self.gridLayout.addWidget(self.dsbm21, 1, 0, 1, 1)
        self.dsbm31 = QtGui.QDoubleSpinBox(Form)
        self.dsbm31.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dsbm31.setSingleStep(0.1)
        self.dsbm31.setObjectName("dsbm31")
        self.gridLayout.addWidget(self.dsbm31, 2, 0, 1, 1)
        self.dsbm23 = QtGui.QDoubleSpinBox(Form)
        self.dsbm23.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dsbm23.setSingleStep(0.1)
        self.dsbm23.setObjectName("dsbm23")
        self.gridLayout.addWidget(self.dsbm23, 1, 2, 1, 1)
        self.dsbm32 = QtGui.QDoubleSpinBox(Form)
        self.dsbm32.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dsbm32.setSingleStep(0.1)
        self.dsbm32.setObjectName("dsbm32")
        self.gridLayout.addWidget(self.dsbm32, 2, 1, 1, 1)
        self.dsbm33 = QtGui.QDoubleSpinBox(Form)
        self.dsbm33.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dsbm33.setSingleStep(0.1)
        self.dsbm33.setObjectName("dsbm33")
        self.gridLayout.addWidget(self.dsbm33, 2, 2, 1, 1)
        self.dsbm12 = QtGui.QDoubleSpinBox(Form)
        self.dsbm12.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dsbm12.setSingleStep(0.1)
        self.dsbm12.setObjectName("dsbm12")
        self.gridLayout.addWidget(self.dsbm12, 0, 1, 1, 1)
        self.dsbm11 = QtGui.QDoubleSpinBox(Form)
        self.dsbm11.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dsbm11.setSingleStep(0.1)
        self.dsbm11.setObjectName("dsbm11")
        self.gridLayout.addWidget(self.dsbm11, 0, 0, 1, 1)
        self.dsbm13 = QtGui.QDoubleSpinBox(Form)
        self.dsbm13.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dsbm13.setSingleStep(0.1)
        self.dsbm13.setObjectName("dsbm13")
        self.gridLayout.addWidget(self.dsbm13, 0, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pbReset = QtGui.QPushButton(Form)
        self.pbReset.setMaximumSize(QtCore.QSize(25, 25))
        self.pbReset.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/resources/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbReset.setIcon(icon)
        self.pbReset.setObjectName("pbReset")
        self.verticalLayout.addWidget(self.pbReset)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))

import nodes_res_rc
