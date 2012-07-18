# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Thu Jun 14 11:39:33 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4 import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    
extension = "_old.htm"
root = ".\convert\deep"

class EmittingStream(QtCore.QObject):

    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

def createDWT(self):
    import re
    import codecs


    parsing =False
    aList = []
    TheList = []
    headerlist = [] 
    fileObj = codecs.open('./default.htm', 'r', "utf-8")
    for line in fileObj:
        if line.find('<!DOCTYPE html') != -1:
            line
            parsing = True
        if line.find('"DocTitle" -->') != -1:
            parsing = False
            headerlist.append(line)

        
        if parsing:
            instruct = re.split(r"\s|," , line)
            aList.append(' '.join(instruct))
        else:
            pass
    for x in aList:
        f = x.strip()
        TheList.append(f)


    header1 = (' '.join(aList))
    header2 = (''.join(headerlist))

    header = (header1 + header2)
    header = header.strip()

    t = "\n"

    outfile = codecs.open('headerTest.txt', 'wb', "utf-8")
    for x in TheList:
        outfile.writelines(x + '\r\n')
        outfile.writelines(t)

    outfile.writelines(header2)
    outfile.close()


    outfile1 = codecs.open('step1Test.txt', 'wb', "utf-8")
    step1 = ['\t<!-- #EndEditable -->', '\t<meta http-equiv="content-type" content="text/html" />', '\t<meta http-equiv="Content-Style-Type" content="text/css" />', '\t<link rel="schema.DC" href="http://purl.org/dc/elements/1.1/" />', '\t<link rel="schema.DCTERMS" href="http://purl.org/dc/terms/" />', '\t<!-- #BeginEditable "RequiredMetas" -->']
    for x in step1:
        outfile1.writelines(x + '\r\n')

    outfile1.close()
    fileObj.close()
    #================================================================
    parsing =False
    aList = []
    TheList = []
    headerlist = [] 
    fileObj = codecs.open('./default.htm', 'r', "utf-8")
    for line in fileObj:
        if line.find('<!-- #BeginEditable "OptionalMetas" -->') != -1:
            line
            parsing = True
        if line.find('<!-- #BeginEditable "PageBranding" -->') != -1:
            parsing = False
            headerlist.append(line)

        
        if parsing:
            instruct = re.split(r"\s|," , line)
            aList.append(' '.join(instruct))
        else:
            pass
    for x in aList:
        f = x.strip()
        TheList.append(f)


    header1 = (' '.join(aList))
    header2 = (''.join(headerlist))

    header = (header1 + header2)
    header = header.strip()

    outfile = codecs.open('step2Test.txt', 'wb', "utf-8")
    outfile.writelines('\t<!-- #EndEditable -->\r\n')
    for x in TheList:
        outfile.writelines("\t" + x + '\r\n')
    outfile.writelines('\t\t\t\t<!-- #BeginEditable "PageBranding" -->')
    outfile.close()
    fileObj.close()

    #================================================================
    parsing =False
    aList = []
    TheList = []
    headerlist = [] 
    fileObj = codecs.open('./default.htm', 'r', "utf-8")
    for line in fileObj:
        if line.find('<div id="PageInfo">') != -1:
            line
            parsing = True
        if line.find('</html>') != -1:
            parsing = False
            headerlist.append(line)

        
        if parsing:
            instruct = re.split(r"\s|," , line)
            aList.append(' '.join(instruct))
        else:
            pass
    for x in aList:
        f = re.sub('    ', "\t", x)
        g = re.sub('^ ', "\t", f)
        TheList.append(g)


    header1 = (' '.join(aList))
    header2 = (''.join(headerlist))

    header = (header1 + header2)
    header = header.strip()

    outfile = codecs.open('footerTest.txt', 'wb', "utf-8")
    outfile.writelines('\t\t\t<!-- #EndEditable -->\r\n')
    for x in aList:
        outfile.writelines(x + '\r\n')
    outfile.close()
    fileObj.close()

        
class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(484, 356)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 401, 241))
        font = QtGui.QFont()
        font.setItalic(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.display = QtGui.QWidget()
        self.display.setObjectName(_fromUtf8("display"))
        self.gridLayoutWidget = QtGui.QWidget(self.display)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 371, 171))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textBrowser = QtGui.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setFrameShadow(QtGui.QFrame.Sunken)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.tabWidget.addTab(self.display, _fromUtf8(""))
        self.settings = QtGui.QWidget()
        self.settings.setObjectName(_fromUtf8("settings"))
        self.label = QtGui.QLabel(self.settings)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 16))
        font = QtGui.QFont()
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.settings)
        self.lineEdit.setGeometry(QtCore.QRect(110, 10, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self.settings)
        self.label_2.setGeometry(QtCore.QRect(240, 10, 141, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(8)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.settings)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 101, 16))
        font = QtGui.QFont()
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(self.settings)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 40, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_4 = QtGui.QLabel(self.settings)
        self.label_4.setGeometry(QtCore.QRect(240, 40, 141, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Rounded MT Bold"))
        font.setPointSize(8)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_2 = QtGui.QPushButton(self.settings)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 180, 75, 23))
        font = QtGui.QFont()
        font.setItalic(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tabWidget.addTab(self.settings, _fromUtf8(""))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 10, 401, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 484, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAbout_Converter = QtGui.QAction(MainWindow)
        self.actionAbout_Converter.setObjectName(_fromUtf8("actionAbout_Converter"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionClear_Display = QtGui.QAction(MainWindow)
        self.actionClear_Display.setObjectName(_fromUtf8("actionClear_Display"))
        self.actionConvert = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Free MP3 Converter-256.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConvert.setIcon(icon)
        self.actionConvert.setObjectName(_fromUtf8("actionConvert"))
        self.actionCreate_DWT = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/Write-Document-48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreate_DWT.setIcon(icon1)
        self.actionCreate_DWT.setObjectName(_fromUtf8("actionCreate_DWT"))
        self.menu_File.addAction(self.actionClose)
        self.menu_File.addAction(self.actionClear_Display)
        self.menuHelp.addAction(self.actionAbout_Converter)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionConvert)
        self.toolBar.addAction(self.actionCreate_DWT)
        
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionConvert, QtCore.SIGNAL(_fromUtf8("triggered()")), self.convert)
        QtCore.QObject.connect(self.actionCreate_DWT, QtCore.SIGNAL(_fromUtf8("triggered()")), self.selectFile)
        QtCore.QObject.connect(self.actionAbout_Converter, QtCore.SIGNAL(_fromUtf8("triggered()")), self.textBrowser.show)
        QtCore.QObject.connect(self.actionClear_Display, QtCore.SIGNAL(_fromUtf8("triggered()")), self.textBrowser.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Template Converter", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:normal; color:#ff0000;\">Set up your DWT by choosing the correct file and hit the convert button to do a mass conversion of all the pages inside your root.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:normal; color:#ff0000;\">-----------------------------------------------------------------------------------------</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.display), QtGui.QApplication.translate("MainWindow", "Display", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Root Directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Ex: .\\convert\\deep", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Endfile Extension:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Ex: _old.htm", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Converter.setText(QtGui.QApplication.translate("MainWindow", "About Converter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear_Display.setText(QtGui.QApplication.translate("MainWindow", "Clear Display", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConvert.setText(QtGui.QApplication.translate("MainWindow", "Convert", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConvert.setToolTip(QtGui.QApplication.translate("MainWindow", "Convert files", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreate_DWT.setText(QtGui.QApplication.translate("MainWindow", "Create DWT", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreate_DWT.setToolTip(QtGui.QApplication.translate("MainWindow", "Create DWT", None, QtGui.QApplication.UnicodeUTF8))


    
    
    def selectFile(self):
        DWTfilename=QtGui.QFileDialog.getOpenFileName()
        createDWT(self)
        print("The neccessary template files have been created")
        #fname = open(filename)
        #data = fname.read()
        #self.textEdit.setText(data)
        #fname.close()
        
    

    def __init__(self, parent=None, **kwargs):
        # ...

        # Install the custom output stream
        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)

    def __del__(self):
        # Restore sys.stdout
        sys.stdout = sys.__stdout__

    def normalOutputWritten(self, text):
        """Append text to the QtextBrowser."""
        # Maybe QtextBrowser.append() works as well, but this is how I do it:
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()

    def convert(self):
        global extension
        global root
        root = self.lineEdit.text()
        root = root.strip()
        if root == "":
            root = ".\convert\deep"
        else:
            pass
        extension = self.lineEdit_2.text()
        extension = extension.strip()
        if not extension:
            extension = "_old.htm"
        else:
            pass
        return extension, root

    def convert(self):
        import sys
        import os
        import fileinput
        import re
        import codecs
        from itertools import dropwhile


            
        #Enter local root web directory
        



        filenames = []


        path = os.path.join(root, "convert")

        filenames = []
        for path, subdirs, files in os.walk(root):
            for name in files:
                filenames.append(os.path.join(path, name))


        print ("These pages are being converted: ")
        for x in filenames:
            print (x)

        for x in filenames:
            namefile2 = []
            namefile = x
            namefile2 = namefile
            namefile = (namefile)
            endfile = 'convert/done/temporary.htm'
            print ("Converting:")
            print (namefile)
            f = open(namefile)
            for line in f:
                line=line.lower()
                outfile = open('extract.htm', 'a')
                outfile.writelines(line)
            else:
                pass

            outfile.close()
            f.close()



            #Removes all <td valign="top"> from file
            inp = open(namefile, 'r')
            goodf = open("goodRanges.htm",'w+')
            lines = inp.readlines()
            for line in lines:
                if line.find('<td valign="top">') != -1:
                    pass
                else:
                    goodf.write(line)
               
            goodf.close()
            inp.close()

            #Copies everything below <td rowspan="2" width="1"></td> and places into file
            f = open('goodRanges.htm')
            f1 = open('final.htm', 'a')
            doIHaveToCopyTheLine=False
            for line in f.readlines():
              if '<td rowspan="2"' in line:
                doIHaveToCopyTheLine=True
              if doIHaveToCopyTheLine:
                f1.write(line)
            f1.close()
            f.close()
            os.remove('goodRanges.htm')

            #Searches <td rowspan="2" and replaces with nothing
            def replaceAll(file,searchExp,replaceExp):
                for line in fileinput.input(file, inplace=1):
                    if searchExp in line:
                        line = line.replace(searchExp,replaceExp)
                    sys.stdout.write(line)

            replaceAll("final.htm",'<td rowspan="2"></td>',"")
            replaceAll("final.htm",'<td rowspan="2" width="1"></td>',"")
            replaceAll("final.htm",'<td rowspan="2" width="2"></td>',"")
            replaceAll("final.htm",'<td rowspan="2" width="3"></td>',"")
            replaceAll("final.htm",'<td rowspan="2" width="1"></td>\n\t<td>',"")


            # first, read everything from the old file
            text = open("final.htm", 'rt').read()

            # split it at the first empty line ("\n\n")
            first, rest = text.split('<p class="Updated"',1)

            # make a new file and write the rest
            open("final2.htm", 'wt').write(first)
            os.remove('final.htm')
            replaceAll("final2.htm",'  ',' ')
            replaceAll("final2.htm",'ï¿½s','\'s')
            replaceAll("final2.htm",'ï¿½','-')
            
            


            parsing =False
            aList = []
            descriplist = [] 
            fileObj = open('extract.htm', 'r')
            for line in fileObj:
                if line.find('<meta name="description"') != -1:
                    line
                    parsing = True
                if line.find('.">') != -1 or line.find('">') != -1 or line.find('. ">') != -1:
                    parsing = False
                    descriplist.append(line)
             
                if parsing:
                    instruct = re.split(r"\s|," , line)
                    aList.append(' '.join(instruct))
                else:
                    pass

            descrip1 = (' '.join(aList))
            descrip2 = (''.join(descriplist[0]))

            description = (descrip1 + descrip2)
            description = description.strip()
            outfile = codecs.open('meta.htm', 'w', 'utf-8')
            outfile.writelines("\t")
            outfile.writelines(description)
            fileObj.close()
            outfile.close()


            outfile.close()

            f = open('extract.htm')
            for line in f:
                if '<meta name="date"' in line:
                    line=line.strip()
                    outfile = codecs.open('meta.htm', 'a', 'utf-8')
                    outfile.writelines("\n")
                    outfile.writelines(line)
                else:
                    pass

            outfile.close()

            f = open('extract.htm')
            for line in f:
                if '<meta name="date.modified"' in line:
                    line=line.strip()
                    outfile = codecs.open('meta.htm', 'a', 'utf-8')
                    outfile.writelines("\n")
                    outfile.writelines(line)

                else:
                    pass
                   

            outfile.close()

            f = open(namefile)
            for line in f:
                if '<title>' in line:
                    line=line.strip()
                    outfile = open('meta2.htm', 'w')
                    outfile.writelines(line)
                    outfile.writelines("\n")
                else:
                    pass

            outfile.close()


            f = open(namefile)
            for line in f:
                if '<p class="PageBranding">' in line:
                    line=line.strip()
                    outfile = open('meta2.htm', 'a')
                    outfile.writelines(line)
                else:
                    pass

            outfile.close()


            f = open(namefile)
            for line in f:
                if '<h1' in line:
                    line=line.strip()
                    line=re.sub('</h1>', '', line)
                    line=re.sub('<h1>', '', line)
                    line=re.sub('<h1 class="PageHead">', '', line)
                    outfile = open('meta2.htm', 'a')
                    outfile.writelines("\n")
                    outfile.writelines(line)
                    outfile.writelines("\n")
                else:
                    pass

            outfile.close()
            f.close()


            import fileinput
            import sys



            #mylist = []
            for line in open('meta.htm','r').readlines():
                var = line.split()
                del var[0]
                del var[0]
                #del mylist[:]
                var = ' '.join(var)
                stripped = open("stripped.htm",'a+')
                stripped.write(var)
                stripped.write("\n")
                
            stripped.close()







            def replaceAll(file,searchExp,replaceExp):
                for line in fileinput.input(file, inplace=1):
                    if searchExp in line:
                        line = line.replace(searchExp,replaceExp)
                    sys.stdout.write(line)

            replaceAll("stripped.htm",'">','" />')


            mylist = open("stripped.htm").readlines()
            
            try:
                mylist[2]
            except IndexError:
                mylist.append(mylist[1])  
            pilot = '<meta name="description" '+mylist[0]
            pilot2 = '<meta name="DC.date.created" scheme="ISO8601" ' + mylist[1]
            pilot3 = '<meta name="DC.date.modified" scheme="ISO8601" ' + mylist[2]


            stripped = open("stripped.htm",'w')
            stripped.write(pilot)
            stripped.write("\t")
            stripped.write(pilot2)
            stripped.write("\t")
            stripped.write(pilot3)
            stripped.write("\n")
                
            stripped.close()


            # append file2 data to file1 data
            meta2list = []


            fin = open("header.htm", 'r')
            data2 = fin.read()
            fin.close()
            fout = open(endfile, "w")
            fout.write(data2)


            meta2list = open("meta2.htm").readlines()
            fout.write("\n")
            fout.write("\t")
            fout.write(meta2list[0])




            fin = codecs.open("step1.txt", 'r', 'utf-8')
            data2 = fin.read()
            fin.close()
            fout = codecs.open(endfile, "a", 'utf-8')
            fout.write(data2)
            


            fin = open("stripped.htm", "r")
            data2 = fin.read()
            fin.close()
            fout = open(endfile, "a")
            fout.write("\n")
            fout.write(data2)



            fin = open("step2.htm", "r")
            data2 = fin.read()
            fin.close()
            fout = codecs.open(endfile, "a", 'utf-8')
            fout.write(data2)

            metalist2 = []
            metalist2 = open("meta2.htm").readlines()
            fout.write("\t\t\t\t")
            if len(metalist2) >1:
                fout.write(metalist2[1])
            else:
                pass
            fout.write('\t\t\t\t<!-- #EndEditable -->\n')
            fout.write('\t\t\t\t<h1><!-- #BeginEditable "PageTitle" -->')
            fout.write(metalist2[2])
            fout.write('\t\t\t\t<!-- #EndEditable --></h1>\n')
            fout.write('\t\t\t\t<!-- #BeginEditable "MainContent" -->')




            fin = open("final2.htm", "r")
            data2 = fin.read()
            fin.close()
            fout = open(endfile, "a")
            fout.write(data2)    


            fin = open("footer.htm", "r")
            data2 = fin.read()
            fin.close()
            fout = codecs.open(endfile, "a", 'utf-8')
            fout.write(data2)

            fout.close()
            metalist2 = []
            metalist2 = open("meta2.htm").readlines()
            pagebranding = '\t\t\t\t' + metalist2[1] + '</p><!-- #EndEditable -->'


            f = open(namefile)
            datelist = []
            datelist=mylist[2].split('"')
            
            datelist = datelist[1].split('-')
            print(datelist)
            

            if datelist[1] == '01':
                month = ("January")
            elif datelist[1] == '02':
                month = ("February")
            elif datelist[1] == '03':
                month = ("March")
            elif datelist[1] == '04':
                month = ("April")
            elif datelist[1] == '05':
                month = ("May")
            elif datelist[1] == '06':
                month = ("June")
            elif datelist[1] == '07':
                month = ("July")
            elif datelist[1] == '08':
                month = ("August")
            elif datelist[1] == '09':
                month = ("September")
            elif datelist[1] == '10':
                month = ("October")
            elif datelist[1] == '11':
                month = ("November")
            elif datelist[1] == '12':
                month = ("December")
            else:
                month = ("January")

            year = datelist[0]
            day = datelist[2]
            date = month + ' ' + day + ',' + ' ' + year
            f.close()

            replaceAll(endfile,'Month DD, YYYY',date)
            replaceAll(endfile,'<meta name="DRRR.date.nextreview" scheme="ISO8601" content="1900-MM-DD" />','<meta name="DRRR.date.nextreview" scheme="ISO8601" content="2012-11-30" />')
            replaceAll(endfile,'<meta name="DRRR.reviewfor" content="Reason for review needed if next review date used." />','<meta name="DRRR.reviewfor" content="Check for updates every 6 months." />')
            replaceAll(endfile,'<blockquote>','<div class="Indent">')
            replaceAll(endfile,'</blockquote>','</div>')
            replaceAll(endfile,'border="0"','')
            replaceAll(endfile,'<ul type="square">','<ul>')
            replaceAll(endfile,' align="left"','')
            replaceAll(endfile,'’','\'')
            replaceAll(endfile,'-','-')
            replaceAll(endfile,'–','-')
            replaceAll(endfile,'ï»¿ ','')
            replaceAll(endfile,'<meta http-equiv="content-type" content="text/html" />','<meta http-equiv="content-type" content="text/html; charset=utf-8" />')
            replaceAll(endfile,'<td valign="bottom">','')
            
            import shutil
            #cleanup
            os.remove('meta.htm')
            os.remove('meta2.htm')
            os.remove('final2.htm')
            os.remove('stripped.htm')
            os.remove('extract.htm')


            filelist = []
            filelist = os.path.splitext(namefile)
            os.rename(namefile, filelist[0]+extension)

            os.rename(endfile, namefile2)

            #========================================================
        #removes </td>\n','</tr>\n','<tr>\n at end of all files
        remove = ['</td>\n','</tr>\n','<tr>\n']
        for x in remove:
            
            file = open(namefile2, 'r')
            dalist = []
            countlist = []
            count = 0
            for line in file:
                
                dalist.append(line)
                count += 1
                countlist.append(count)


            darev = []
            countrev = []
            darev = dalist[::-1]
            countrev = countlist[::-1]
            darev = [x.strip(' ') for x in darev]


            def search(b):
             try:
              k=darev.index(x)
              return k+1

             except ValueError:
                return 0
            linenumber = (search(500))

            if linenumber != 0:
                origlinenum = countrev[linenumber]

                file.close()
                origlist = (countrev[linenumber])
                def mangle(fn):
                    fo = open(fn, 'r')
                    contents = fo.readlines()
                    fo.close()
                    contents[origlinenum] = contents[origlinenum].replace(dalist[origlist], '')
                    fo = open(fn, 'w')
                    fo.writelines(contents)
                    fo.close()
                mangle(namefile2)

                
            else:
                pass

        #================================================
    




#import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

