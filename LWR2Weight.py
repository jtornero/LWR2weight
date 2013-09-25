#!/usr/bin/env python

from PyQt4 import QtCore, QtGui, QtSql
import sys
import os
import math


class MainDialog(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)

        if not os.path.exists('./data/LWR.data'):
            message = QtGui.QMessageBox(None)
            message.setText(self.tr("""<center><b>There is a problem with the LWR database file</b><br>
				Please check that the file LWR.data is in the
				./data subdirectory</center>"""))
            btn1 = message.addButton(self.tr("Ok"), QtGui.QMessageBox.YesRole)
            message.exec_()
            sys.exit()

        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('./data/LWR.data')
        self.db.open()

        self.menu = QtGui.QMenuBar(self)
        self.about = self.menu.addMenu(self.tr("&About"))
        self.licenseAction = self.about.addAction(self.tr("License"))
        self.creditsAction = self.about.addAction(self.tr("Credits"))
        self.exitAction = self.about.addAction(self.tr("Exit"))
        self.layout = QtGui.QGridLayout(self)

        self.LWRTreeView = QtGui.QTreeWidget(self)
        self.LWRTreeView.setColumnCount(2)
        self.LWRTreeView.setHeaderLabels(
            [self.tr("Family/Species/Origin"), self.tr("Measure")])
        self.LWRTreeView.header().setStretchLastSection(True)

        self.LFDTableView = QtGui.QTableWidget(self)
        self.LFDTableView.setColumnCount(2)
        self.LFDTableView.setSortingEnabled(False)
        self.LFDTableView.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.LFDTableView.setHorizontalHeaderLabels(
            [self.tr("Length\nClass"), self.tr("Number")])
        self.LFDTableView.horizontalHeader().setStretchLastSection(True)
        self.LFDTableView.verticalHeader().hide()

        self.labelSelHeader = QtGui.QLabel(
            self.tr("<center><b>Length-Weight Relationship</b></center>"))
        self.labelLWRHeader = QtGui.QLabel(
            self.tr("<center><b>Parameters</b></center>"))
        self.labelLFDHeader = QtGui.QLabel(
            self.tr("<center><b>Lenght Frecuency<br>Distribution</b></center>"))

        self.selectionGroup = QtGui.QButtonGroup(self)
        self.optionFamilyTree = QtGui.QRadioButton(self.tr("Select by Family"))
        self.optionSpeciesTree = QtGui.QRadioButton(
            self.tr("Select by Species"))
        self.optionFamilyTree.setChecked(True)

        self.selectionGroup.addButton(self.optionFamilyTree)
        self.selectionGroup.addButton(self.optionSpeciesTree)

        self.labelNumberInd = QtGui.QLabel(self.tr("Number of Samples"))
        self.textNumberInd = QtGui.QLineEdit()
        self.textNumberInd.setReadOnly(True)

        self.labelMinLength = QtGui.QLabel(self.tr("Minimum length (cm)"))
        self.textMinLength = QtGui.QLineEdit()
        self.textMinLength.setReadOnly(True)

        self.labelMaxLength = QtGui.QLabel(self.tr("Maximum Length (cm)"))
        self.textMaxLength = QtGui.QLineEdit()
        self.textMaxLength.setReadOnly(True)

        self.labelCoefA = QtGui.QLabel(self.tr("Slope (a)"))
        self.textCoefA = QtGui.QLineEdit()
        self.textCoefA.setReadOnly(True)

        self.labelCoefB = QtGui.QLabel(self.tr("Intercept (b)"))
        self.textCoefB = QtGui.QLineEdit()
        self.textCoefB.setReadOnly(True)

        self.labelCoefR2 = QtGui.QLabel(
            self.tr("Coefficient of determination (r<sup>2</sup>)"))
        self.textCoefR2 = QtGui.QLineEdit()
        self.textCoefR2.setReadOnly(True)

        self.labelTotalWeight = QtGui.QLabel(self.tr("<b>Total weight</b>"))
        self.labelTotalWeight.setSizePolicy(
            QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding))
        self.textTotalWeight = QtGui.QLineEdit()
        self.textTotalWeight.setReadOnly(True)
        self.textTotalWeight.setSizePolicy(
            QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding))

        self.buttonIntroLFD = QtGui.QPushButton(self.tr("Set LFD"))
        self.buttonCalculateWeight = QtGui.QPushButton(
            self.tr("Calculate weight"))

        self.layout.setColumnMinimumWidth(0, 350)

        self.layout.addWidget(self.labelSelHeader, 0, 0, 1, 2)

        self.layout.addWidget(self.optionFamilyTree, 1, 0, 1, 1)
        self.layout.addWidget(self.optionSpeciesTree, 1, 1, 1, 1)

        self.layout.addWidget(self.labelLWRHeader, 21, 0, 1, 2)
        self.layout.addWidget(self.labelLFDHeader, 0, 2, 2, 2)

        self.layout.addWidget(self.LWRTreeView, 2, 0, 18, 2)
        self.layout.addWidget(self.LFDTableView, 2, 2, 29, 2)

        self.layout.addWidget(self.labelMinLength, 22, 0, 1, 2)
        self.layout.addWidget(self.textMinLength, 23, 0, 1, 2)

        self.layout.addWidget(self.labelMaxLength, 24, 0, 1, 2)
        self.layout.addWidget(self.textMaxLength, 25, 0, 1, 2)

        self.layout.addWidget(self.labelNumberInd, 26, 0, 1, 2)
        self.layout.addWidget(self.textNumberInd, 27, 0, 1, 2)

        self.layout.addWidget(self.labelCoefA, 28, 0, 1, 2)
        self.layout.addWidget(self.textCoefA, 29, 0, 1, 2)

        self.layout.addWidget(self.labelCoefB, 30, 0, 1, 2)
        self.layout.addWidget(self.textCoefB, 31, 0, 1, 2)

        self.layout.addWidget(self.labelCoefR2, 32, 0, 1, 2)
        self.layout.addWidget(self.textCoefR2, 33, 0, 1, 2)

        self.layout.addWidget(self.labelTotalWeight, 31, 2, 1, 1)
        self.layout.addWidget(self.textTotalWeight, 31, 3, 1, 1)

        self.layout.addWidget(self.buttonIntroLFD, 32, 2, 1, 2)
        self.layout.addWidget(self.buttonCalculateWeight, 33, 2, 1, 2)

        self.LWRTreeView.header().setResizeMode(3)
        self.LWRTreeView.itemSelectionChanged.connect(
            self.displayLWRParameters)
        self.buttonIntroLFD.clicked.connect(self.introLFD)
        self.selectionGroup.buttonClicked.connect(self.loadLWR)
        self.buttonCalculateWeight.clicked.connect(self.calculateWeight)
        self.exitAction.triggered.connect(self.close)

        self.loadLWR()

    def loadLWR(self):

        self.LWRTreeView.clear()

        if self.selectionGroup.checkedButton() == self.optionFamilyTree:
            searchingBySpecies = False
        else:
            searchingBySpecies = True

        self.queryFamilies = QtSql.QSqlQuery(
            'Select distinct family from LWR order by family')
        self.queryFamilies.exec_()

        while self.queryFamilies.next():

            if not searchingBySpecies:
                familyText = self.queryFamilies.value(0).toString()
                whereClauseText = ("where family='%s'" % familyText)
                newFamilyItem = QtGui.QTreeWidgetItem(self.LWRTreeView)
                newFamilyItem.setText(0, familyText)

            else:
                whereClauseText = ''

            self.querySpecies = QtSql.QSqlQuery(("""Select distinct
				      species from LWR %s
				      order by species""" % whereClauseText))
            self.querySpecies.exec_()

            while self.querySpecies.next():

                speciesText = self.querySpecies.value(0).toString()

                if not searchingBySpecies:

                    treeRoot = newFamilyItem
                    whereClauseText2 = whereClauseText = (
                                                """where family='%s' and
				      species='%s' and
				      LWR.dimref=DIMS.dimsid and
				      LWR.biblioref=BIBLIO.biblioid""" % (familyText, speciesText))

                else:
                    treeRoot = self.LWRTreeView
                    whereClauseText2 = whereClauseText = (
                                                """where species='%s' and
				      LWR.dimref=DIMS.dimsid and
				      LWR.biblioref=BIBLIO.biblioid""" % speciesText)

                newSpeciesItem = QtGui.QTreeWidgetItem(treeRoot)
                newSpeciesItem.setText(0, speciesText)

                self.queryRegions = QtSql.QSqlQuery((
                                              """Select distinct
				      species,region,dimfull,minlength,maxlength,n,a,b,r2,authors,title
				      from LWR,DIMS,BIBLIO
				      %s order by species"""
                                              % (whereClauseText2)
                ))

                self.queryRegions.exec_()

                while self.queryRegions.next():

                    newRegionsItem = QtGui.QTreeWidgetItem(newSpeciesItem)
                    newRegionsItem.setText(
                        0, self.queryRegions.value(1).toString())
                    newRegionsItem.setText(
                        1, self.queryRegions.value(2).toString())
                    newRegionsItem.setText(
                        3, self.queryRegions.value(3).toString())
                    newRegionsItem.setText(
                        4, self.queryRegions.value(4).toString())
                    newRegionsItem.setText(
                        5, self.queryRegions.value(5).toString())
                    newRegionsItem.setText(
                        6, self.queryRegions.value(6).toString())
                    newRegionsItem.setText(
                        7, self.queryRegions.value(7).toString())
                    newRegionsItem.setText(
                        8, self.queryRegions.value(8).toString())
                    newRegionsItem.setText(
                        9, self.queryRegions.value(9).toString())
                    newRegionsItem.setText(
                        10, self.queryRegions.value(10).toString())

            if searchingBySpecies:
                break

    def displayLWRParameters(self):
        if self.LWRTreeView.currentItem().childCount() == 0:

            self.textMinLength.setText(self.LWRTreeView.currentItem().text(3))
            self.textMaxLength.setText(self.LWRTreeView.currentItem().text(4))
            self.textNumberInd.setText(self.LWRTreeView.currentItem().text(5))
            self.textCoefA.setText(self.LWRTreeView.currentItem().text(6))
            self.textCoefB.setText(self.LWRTreeView.currentItem().text(7))
            self.textCoefR2.setText(self.LWRTreeView.currentItem().text(8))

    def introLFD(self):
        parameters = ParametersLFD(self)
        if parameters.exec_():
            self.finalLFD = parameters.dialogLFD.sampling
            numberOfRows = len(self.finalLFD)

            self.LFDTableView.setRowCount(numberOfRows + 1)
            total = 0
            for lengthClass in enumerate(self.finalLFD):
                self.LFDTableView.setItem(
                    lengthClass[0], 0, QtGui.QTableWidgetItem("%s" % lengthClass[1][0]))
                self.LFDTableView.setItem(
                    lengthClass[0], 1, QtGui.QTableWidgetItem("%i" % lengthClass[1][2]))
                total += lengthClass[1][2]
            self.LFDTableView.setItem(
                numberOfRows, 0, QtGui.QTableWidgetItem("%s" % self.tr("TOTAL")))
            self.LFDTableView.setItem(
                numberOfRows, 1, QtGui.QTableWidgetItem("%i" % total))

    def calculateWeight(self):

        message = QtGui.QMessageBox(None)
        if self.LWRTreeView.currentItem().childCount() != 0:
            message.setText(
                self.tr("<center>You must select a Length-Weight Relationship in order to compute the Length Frecuency Distribution Weight</center>"))
            btn1 = message.addButton(self.tr("Ok"), QtGui.QMessageBox.YesRole)
            message.exec_()
            return

        elif self.LFDTableView.rowCount() == 0:
            message.setText(
                self.tr("<center>You must provide a Length Frecuency Distribution in order to compute its weight</center>"))
            btn1 = message.addButton(self.tr("Ok"), QtGui.QMessageBox.YesRole)
            message.exec_()
            return

        elif self.finalLFD[0][0] < math.floor(float(self.textMinLength.text())):
            message.setText(
                self.tr("<center>The initial length class is smaller than the minimum length of the Length-Weight Relationship. The computed weight could be innaccurate due to extrapolation</center>"))
            btn1 = message.addButton(
                self.tr("Ignore"), QtGui.QMessageBox.YesRole)
            btn2 = message.addButton(
                self.tr("Set LFD"), QtGui.QMessageBox.NoRole)
            btn3 = message.addButton(
                self.tr("Cancel"), QtGui.QMessageBox.NoRole)
            message.exec_()
            if message.clickedButton() == btn1:
                pass
            elif message.clickedButton() == btn2:
                self.introLFD()
                return
            else:
                return

        elif math.ceil(self.finalLFD[-1][0]) > math.ceil(float(self.textMaxLength.text())):
            message.setText(
                self.tr("<center>The final length class is greater than the maximum length of the Length-Weight Relationship. The computed weight could be innaccurate due to extrapolation</center>"))
            btn1 = message.addButton(
                self.tr("Ignore"), QtGui.QMessageBox.YesRole)
            btn2 = message.addButton(
                self.tr("Set LFD"), QtGui.QMessageBox.NoRole)
            btn3 = message.addButton(
                self.tr("Cancel"), QtGui.QMessageBox.NoRole)
            message.exec_()
            if message.clickedButton() == btn1:
                pass
            elif message.clickedButton() == btn2:
                self.introLFD()
                return
            else:
                return

        regrParamA = self.textCoefA.text().toDouble()[0]
        regrParamB = self.textCoefB.text().toDouble()[0]
        weightForLFD = 0.0
        for lclass in self.finalLFD:
            weightForClass = ((lclass[1] ** regrParamB) * regrParamA)
            weightForLFD += (weightForClass * lclass[2])
        self.textTotalWeight.setText("%.3f Kg" % (weightForLFD / 1000.0))


class ParametersLFD(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)

        self.validateCm = QtCore.QRegExp('^(([0-9]{0,3})?)$')
        self.validateHalfCm = QtCore.QRegExp(
            '^(([0-9]{0,3})?(\.[0,5]{0,1})?)$')

        self.layout = QtGui.QGridLayout(self)

        self.optionClassInterval = QtGui.QButtonGroup(self)
	
	self.labelOptionsInterval = QtGui.QLabel(self.tr("Length Class Interval"))
        self.optionCm = QtGui.QRadioButton(self.tr("1 cm"))
        self.optionHalfCm = QtGui.QRadioButton(self.tr("0.5 cm"))
        self.optionCm.setChecked(True)

        self.optionClassInterval.addButton(self.optionCm)
        self.optionClassInterval.addButton(self.optionHalfCm)

        self.labelBeginClass = QtGui.QLabel(
            self.tr("Beginning length class (cm)"))
        self.labelEndClass = QtGui.QLabel(self.tr("Final length class (cm)"))
        self.textBeginClass = QtGui.QLineEdit(self)
        self.textEndClass = QtGui.QLineEdit(self)
        self.buttonIntroLFD = QtGui.QPushButton(self.tr("Proceed"))

        # self.buttonIntroLFD.setAutoDefault(False)
	self.layout.addWidget(self.labelOptionsInterval, 0, 0, 1, 1)
        self.layout.addWidget(self.optionCm, 0, 1, 1, 1)
        self.layout.addWidget(self.optionHalfCm, 0, 2, 1, 1)

        self.layout.addWidget(self.labelBeginClass, 2, 0, 1, 1)

        self.layout.addWidget(self.labelEndClass, 3, 0, 1, 1)

        self.layout.addWidget(self.textBeginClass, 2, 1, 1, 2)

        self.layout.addWidget(self.textEndClass, 3, 1, 1, 2)

        self.layout.addWidget(self.buttonIntroLFD, 4, 0, 1, 3)

        # self.textBeginClass.setFocus()

        self.setUnitsValidator()

        self.optionClassInterval.buttonClicked.connect(self.setUnitsValidator)
        self.optionClassInterval.buttonClicked.connect(
            self.textBeginClass.setFocus)
        self.textBeginClass.returnPressed.connect(self.textEndClass.setFocus)
        # self.textEndClass.returnPressed.connect(self.validateLengthClasses)
        self.textEndClass.returnPressed.connect(self.buttonIntroLFD.setFocus)
        self.buttonIntroLFD.clicked.connect(self.proceedToLFD)

        self.show()

    def setUnitsValidator(self):

        if self.optionClassInterval.checkedButton() == self.optionCm:
            self.textBeginClass.setValidator(
                QtGui.QRegExpValidator(self.validateCm, self))
            self.textEndClass.setValidator(
                QtGui.QRegExpValidator(self.validateCm, self))

        else:
            self.textBeginClass.setValidator(
                QtGui.QRegExpValidator(self.validateHalfCm, self))
            self.textEndClass.setValidator(
                QtGui.QRegExpValidator(self.validateHalfCm, self))

    def validateLengthClasses(self):

        if self.textBeginClass.text().toDouble() > self.textEndClass.text().toDouble():
            QtGui.QMessageBox.information(None, self.tr("Accept"),
                                          self.tr("Initial length class is greater than final length class"))
        else:
            self.buttonIntroLFD.setFocus()
        return

    def proceedToLFD(self):
        if (self.textBeginClass.text().isEmpty() or self.textEndClass.text().isEmpty()):
            return
        elif self.textBeginClass.text().toDouble() > self.textEndClass.text().toDouble():
            QtGui.QMessageBox.information(None, self.tr("Accept"),
                                          self.tr("Initial length class is greater than final length class"))
            return
        else:
            initial = self.textBeginClass.text().toDouble()[0]
            final = self.textEndClass.text().toDouble()[0]
            intervalCm = self.optionCm.isChecked()
            self.dialogLFD = LFDDialog(initial, final, intervalCm, self)
            if self.dialogLFD.exec_():
                self.finalLFD = self.dialogLFD.sampling
            self.done(1)


class LFDDialog(QtGui.QDialog):

    def nextChild(self):
        self.focusNextChild()

    def previousChild(self):
        self.focuspreviousChildusChild()

    def __init__(self, initialLengthClass, finalLengthClass, intervalCm=True, parent=None):

        QtGui.QDialog.__init__(self, parent)
        if intervalCm:
            lengthClassInterval = 10
        else:
            lengthClassInterval = 5

        self.setWindowTitle(self.tr("Length Frecuency Distribution"))
        self.labelNumber = QtGui.QLabel(
            self.tr("<center><b>Number</b></center>"))
        self.labelLengthClass = QtGui.QLabel(
            self.tr("<center><b>Length<br>class</b></center>"))

        self.group = QtGui.QGridLayout(self)
        self.group.addWidget(self.labelLengthClass, 0, 0, 1, 1)
        self.group.addWidget(self.labelNumber, 0, 1, 1, 1)
        self.rule = QtCore.QRegExp('^-\d{0,3}\.[05]$|\d{0,3}$')
        self.val = QtGui.QRegExpValidator(self)
        self.val.setRegExp(self.rule)
        self.initialLengthClass = int(initialLengthClass * 10)
        self.finalLengthClass = int(
            (finalLengthClass * 10 + lengthClassInterval))
        self.startPosition = 1
        self.widtgetsLength = []
        column = 0
        for i in range(self.initialLengthClass, self.finalLengthClass, lengthClassInterval):
            self.length = i / 10.0
            self.meanClassLength = (i + (lengthClassInterval / 2.0)) / 10.0
            
            if intervalCm:
                self.labelClass = QtGui.QLabel(
                    self.tr("<center><b>%i</b></center>" % int(self.length)), self)
            else:
                self.labelClass = QtGui.QLabel(
                    self.tr("<center><b>%.1f</b></center>" % self.length), self)
            self.textNumber = customLineEdit(self)
            self.textNumber.setValidator(self.val)
            self.textNumber.retorno.connect(self.nextChild)
            self.textNumber.ctrlRetorno.connect(self.previousChild)
            self.startPosition += 1
            self.group.addWidget(self.labelClass, self.startPosition, column)
            self.group.addWidget(
                self.textNumber, self.startPosition, column + 1)
            self.setOfWidgets = (
                self.length, self.meanClassLength, self.textNumber)
            self.widtgetsLength.append(self.setOfWidgets)
            if self.startPosition == 20:
                self.startPosition = 1
                column += 2

        self.save = QtGui.QPushButton(QtCore.QString(self.tr("Save")), self)
        self.cancel = QtGui.QPushButton(
            QtCore.QString(self.tr("Cancel")), self)
        self.cleanUp = QtGui.QPushButton(
            QtCore.QString(self.tr("Cleanup")), self)
        self.group.addWidget(self.save, self.startPosition + 1, column + 1)
        self.group.addWidget(self.cancel, self.startPosition + 2, column + 1)
        self.group.addWidget(self.cleanUp, self.startPosition + 3, column + 1)
        self.save.clicked.connect(self.saveData)
        self.cleanUp.clicked.connect(self.cleanUpForm)
        self.cancel.clicked.connect(self.exit)
        self.show()

    def exit(self):
        self.close()

    def saveData(self):
        self.sampling = []
        for setOf in self.widtgetsLength:

            lengthNumero = setOf[0], setOf[1], setOf[2].text().toInt()[0]
            self.sampling.append(lengthNumero)

        self.done(1)

    def cleanUpForm(self):
        for setOf in self.widtgetsLength:
            setOf[1].clear()
        self.widtgetsLength[0][1].setFocus()


class customLineEdit(QtGui.QLineEdit):

    retorno = QtCore.pyqtSignal()
    ctrlRetorno = QtCore.pyqtSignal()

    def __init__(self, parent, passFocus=None):

        QtGui.QLineEdit.__init__(self, parent)
        self.parent = parent

        if (passFocus != None):
            self.setFocusOn(passFocus)

    def setFocusOn(widget):

        self.returnPressed.connect(widget.setFocus())

    def keyPressEvent(self, event):

        if ((event.key() == QtCore.Qt.Key_Return and event.modifiers() == QtCore.Qt.ControlModifier)
                or (event.key() == QtCore.Qt.Key_Enter and event.modifiers() == (QtCore.Qt.ControlModifier | QtCore.Qt.KeypadModifier))):
            event.accept()
            self.ctrlRetorno.emit()
            # self.parent.done(1)
        elif (event.key() == QtCore.Qt.Key_Return or (event.key() == QtCore.Qt.Key_Enter)):
            event.accept()
            self.retorno.emit()
        else:
            event.ignore()
            QtGui.QLineEdit.keyPressEvent(self, event)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    # Internationalization
    appTranslator = QtCore.QTranslator()
    appTranslator.load('./LWR2Weight.qm')
    app.installTranslator(appTranslator)
    wid = MainDialog()
    wid.show()
    sys.exit(app.exec_())
