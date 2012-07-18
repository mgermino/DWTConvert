################################################################################
#Monthly Rollover System                                                       #
#Written by Ryan Hanson 2012                                                   #
#                                                                              #
################################################################################

#Python Imports
import sys

#PyQt4 Imports
from PyQt4 import QtCore, QtGui, QtSql #@UnusedImport

#UI Imports
from main import Ui_MainWindow
from popup import Ui_Dialog

#Variables
dbhost = "192.168.1.39"
dbname = "material"
dbuser = "fab"
dbpswd = "doylefab"

#This Runs First
class launch(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        #Prepare the first window 
        self.main = Ui_MainWindow()
        self.main.setupUi(self)

        #Set the icon and select the first tab
        self.setWindowIcon(QtGui.QIcon("icons/main.png"))
        self.setWindowTitle("Material Tracking")
        self.main.tabs.setCurrentIndex(0)

        #Make db accessible to the whole app - I am not sure this is the best way to do this?
        global db
        db = QtSql.QSqlDatabase.addDatabase("QMYSQL");

        #Host name and Database
        db.setHostName(dbhost)
        db.setDatabaseName(dbname)
        db.setUserName(dbuser)
        db.setPassword(dbpswd)
        ok = db.open()

        #ok is true if the database can be connected to
        if ok:
            self.materialQuery = QtSql.QSqlQuery(db)
            materialdata = "select id, material, d1, d2, d3 from material_tbl"
            if self.materialQuery.exec_(materialdata):
                self.materialchange(1)

                #Set the range for the slider so all records can be navigated to.
                self.main.horizontalSlider.setRange(1, self.materialQuery.size())

                self.main.modelMaterial = QtSql.QSqlTableModel()
                self.main.modelMaterial.setTable("inventory_view")
                self.main.modelMaterial.select()
                self.main.tableMaterial.setModel(self.main.modelMaterial)

                #Is there a better way to set columns?
                self.main.tableMaterial.setColumnWidth(0, 50)
                self.main.tableMaterial.setColumnWidth(1, 200)
                self.main.tableMaterial.setColumnWidth(2, 75)
                self.main.tableMaterial.setColumnWidth(3, 100)
                self.main.tableMaterial.setColumnWidth(4, 100)
                self.main.tableMaterial.setColumnWidth(5, 100)

#########CONNECTIONS###############################################################################
            self.main.horizontalSlider.valueChanged.connect(self.materialchange)            
            self.main.tableMaterial.doubleClicked.connect(self.dblclickMaterial)            
            self.main.lineSearch.textChanged.connect(self.filterMaterial)          
            self.main.buttonReceive.clicked.connect(self.received)
            self.main.buttonUsed.clicked.connect(self.used)

#########END IF THE CONNECTION FAILS###############################################################
        else:
            self.dberror()

    def materialchange(self, index):
        if db.isOpen():
            #Seek to the next record and load the proper data
            self.materialQuery.seek(index-1)
            mat = self.materialQuery.value(0).toString()
            self.main.lineId.setText(mat)
            self.main.lineMaterial.setText(self.materialQuery.value(1).toString())
            self.main.lined1.setText(self.materialQuery.value(2).toString())
            self.main.lined2.setText(self.materialQuery.value(3).toString())
            self.main.lined3.setText(self.materialQuery.value(4).toString())

            self.main.modelreceived = QtSql.QSqlTableModel()
            self.main.modelreceived.setTable("received_tbl")
            self.main.modelreceived.setFilter('mat_id = {0}'.format(mat))
            self.main.modelreceived.select()
            self.main.tablereceived.setModel(self.main.modelreceived)

            #Is there a better way to set columns?
            self.main.tablereceived.setColumnWidth(0, 50)
            self.main.tablereceived.setColumnWidth(1, 50)
            self.main.tablereceived.setColumnWidth(2, 75)
            self.main.tablereceived.setColumnWidth(3, 125)
            self.main.tablereceived.setColumnWidth(4, 125)

            self.main.modelused = QtSql.QSqlTableModel()
            self.main.modelused.setTable("used_tbl")
            self.main.modelused.setFilter('mat_id = {0}'.format(mat))
            self.main.modelused.select()
            self.main.tableused.setModel(self.main.modelused)

            #Is there a better way to set columns?
            self.main.tableused.setColumnWidth(0, 50)
            self.main.tableused.setColumnWidth(1, 50)
            self.main.tableused.setColumnWidth(2, 75)
            self.main.tableused.setColumnWidth(3, 125)
            self.main.tableused.setColumnWidth(4, 125)
        else:
            self.dberror()

    def dblclickMaterial(self, index):
        row = index.row()
        kid = self.main.modelMaterial.data(self.main.modelMaterial.index(row, 0)).toString()
        i=0
        self.materialQuery.seek(i)

        #This is probably a relatively slow way to find the right record. Any suggestions?
        while self.materialQuery.value(0).toString() <> kid:
            i+=1
            self.materialQuery.seek(i)

        self.materialchange(i+1)
        self.main.tabs.setCurrentIndex(1)
        self.main.horizontalSlider.setSliderPosition(i+1)

    def filterMaterial(self):
        r=0
        R=self.main.modelMaterial.rowCount()
        c=0
        C=self.main.modelMaterial.columnCount()
        s=0
        search = str(self.main.lineSearch.text())
        #Loop though all columns on all rows and hide rows where none of the columns match the search term.
        while r < R:
            while c<C:
                if search.lower() not in str(self.main.modelMaterial.data(self.main.modelMaterial.index(r, c)).toString()).lower():
                    s += 1
                c += 1
            if s==C:
                self.main.tableMaterial.setRowHidden(r, True)
            else:
                self.main.tableMaterial.setRowHidden(r, False)
            c=0
            r +=1
            s=0

    def received(self):
        def accept():
            mat = self.main.lineId.text()
            qty = self.popup.dialog.lineQty.text()
            notes = self.popup.dialog.lineNotes.text()
            insertQuery = QtSql.QSqlQuery(db)
            #There are two tables used to track material, one that records details about each load we receive and the other that keeps a running total of what we should have on hand.
            insertdata = "INSERT INTO `material`.`received_tbl` (`id`, `mat_id`, `quantity`, `date`, `note`) VALUES (NULL, {0}, {1}, CURRENT_TIMESTAMP, '{2}');".format(mat, qty, notes)
            if insertQuery.exec_(insertdata):
                inventoryQuery=QtSql.QSqlQuery(db)
                inventorydata = "Update inventory_tbl set quantity = (quantity + {0}) where mat_id = {1}".format(qty, mat)
                if inventoryQuery.exec_(inventorydata):
                    print("{0} Received.".format(qty))
                    self.main.modelMaterial.select()
                    if self.main.lineSearch <> "":
                        self.filterMaterial()
                else:
                    print(inventoryQuery.lastError().text()) 
                    QtGui.QMessageBox.about(self, "Fail...", 'There was a problem and this operation did not complete...')                   
            else:
                print(insertQuery.lastError().text())
                QtGui.QMessageBox.about(self, "Fail...", 'There was a problem and this operation did not complete...')

        self.popup = QtGui.QDialog()
        self.popup.show()
        self.popup.dialog = Ui_Dialog()
        self.popup.dialog.setupUi(self.popup)
        self.popup.setWindowTitle("Received")
        self.popup.setWindowIcon(QtGui.QIcon("icons/main.png"))

        self.popup.dialog.buttonBox.accepted.connect(accept)

    #Almost exactly the same as received but it updates the used table and subtracts from the total.
    def used(self):
        def accept():
            mat = self.main.lineId.text()
            qty = self.popup.dialog.lineQty.text()
            notes = self.popup.dialog.lineNotes.text()
            insertQuery = QtSql.QSqlQuery(db)
            insertdata = "INSERT INTO `material`.`used_tbl` (`id`, `mat_id`, `quantity`, `date`, `note`) VALUES (NULL, {0}, {1}, CURRENT_TIMESTAMP, '{2}');".format(mat, qty, notes)
            if insertQuery.exec_(insertdata):
                inventoryQuery=QtSql.QSqlQuery(db)
                inventorydata = "Update inventory_tbl set quantity = (quantity - {0}) where mat_id = {1}".format(qty, mat)
                if inventoryQuery.exec_(inventorydata):
                    print("{0} Used.".format(qty))
                    self.main.modelMaterial.select()
                    if self.main.lineSearch <> "":
                        self.filterMaterial()
                else:
                    print(inventoryQuery.lastError().text())
                    QtGui.QMessageBox.about(self, "Fail...", 'There was a problem and this operation did not complete...')
            else:
                print(insertQuery.lastError().text())
                QtGui.QMessageBox.about(self, "Fail...", 'There was a problem and this operation did not complete...')

        self.popup = QtGui.QDialog()
        self.popup.show()
        self.popup.dialog = Ui_Dialog()
        self.popup.dialog.setupUi(self.popup)
        self.popup.setWindowTitle("Used")
        self.popup.setWindowIcon(QtGui.QIcon("icons/main.png"))

        self.popup.dialog.buttonBox.accepted.connect(accept)

    #Called when the database encounters a connection problem.
    def dberror(self):
        print(db.lastError().text())
        QtGui.QMessageBox.about(self, "Fail...", 'Could not connect...')
        sys.exit()

    #This is in place to unload material query.
    def closeEvent(self, event):
        print("Unloading Material Query...")
        self.materialQuery.finish()
        print("Have a nice day!")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = launch()
    myapp.show()
    sys.exit(app.exec_())
