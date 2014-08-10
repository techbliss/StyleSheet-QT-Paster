

from PyQt4 import QtCore, QtGui
from ui_stylesheeteditor import Ui_StyleSheetEditor

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_StyleSheetEditor(object):
    def setupUi(self, StyleSheetEditor):
        self.ui = Ui_StyleSheetEditor()
        StyleSheetEditor.setObjectName(_fromUtf8("StyleSheetEditor"))
        StyleSheetEditor.resize(445, 289)
        self.gridlayout = QtGui.QGridLayout(StyleSheetEditor)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        spacerItem = QtGui.QSpacerItem(321, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.saveButton = QtGui.QPushButton(StyleSheetEditor)
        self.saveButton.setEnabled(True)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.hboxlayout.addWidget(self.saveButton)
        self.applyButton = QtGui.QPushButton(StyleSheetEditor)
        self.applyButton.setEnabled(True)
        self.applyButton.setObjectName(_fromUtf8("applyButton"))
        self.hboxlayout.addWidget(self.applyButton)
        self.gridlayout.addLayout(self.hboxlayout, 2, 0, 1, 5)
        spacerItem1 = QtGui.QSpacerItem(32, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(32, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem2, 0, 4, 1, 1)
        self.styleTextEdit = QtGui.QTextEdit(StyleSheetEditor)
        self.styleTextEdit.setObjectName(_fromUtf8("styleTextEdit"))
        self.gridlayout.addWidget(self.styleTextEdit, 1, 0, 1, 5)
        spacerItem3 = QtGui.QSpacerItem(10, 16, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem3, 0, 2, 1, 1)
        self.label_8 = QtGui.QLabel(StyleSheetEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridlayout.addWidget(self.label_8, 0, 1, 1, 1)

        self.retranslateUi(StyleSheetEditor)
        QtCore.QMetaObject.connectSlotsByName(StyleSheetEditor)

    def retranslateUi(self, StyleSheetEditor):
        StyleSheetEditor.setWindowTitle(_translate("StyleSheetEditor", "StyleSheet Paster", None))
        self.saveButton.setText(_translate("StyleSheetEditor", "&Save", None))
        self.applyButton.setText(_translate("StyleSheetEditor", "&Apply", None))
        self.label_8.setText(_translate("StyleSheetEditor", "By Zadow", None))
        self.applyButton.clicked.connect(self.apply)
        self.saveButton.clicked.connect(self.save)

    def apply(self):
         QtGui.qApp.setStyleSheet(ui.styleTextEdit.toPlainText())

    def save(self):
        fileName = QtGui.QFileDialog.getSaveFileName()
        if fileName:
            self.saveStyleSheet(fileName)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication.instance()
    if not app:
        app = QtGui.QApplication([])
    StyleSheetEditor = QtGui.QWidget()
    ui = Ui_StyleSheetEditor()
    ui.setupUi(StyleSheetEditor)
    StyleSheetEditor.show()
    app.exec_()

