# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Tue Jun 12 16:32:49 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(496, 369)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 70, 401, 241))
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
        self.line.setGeometry(QtCore.QRect(10, 50, 401, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 81, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 496, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAbout_Converter = QtGui.QAction(MainWindow)
        self.actionAbout_Converter.setObjectName(_fromUtf8("actionAbout_Converter"))
        self.menuHelp.addAction(self.actionAbout_Converter)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.hello)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.convert)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.display), QtGui.QApplication.translate("MainWindow", "Display", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Root Directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Ex: .\\convert\\deep", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Endfile Extension:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Ex: _old.htm", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Convert", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Converter.setText(QtGui.QApplication.translate("MainWindow", "About Converter", None, QtGui.QApplication.UnicodeUTF8))

    def on_Button_clicked(self, checked=None):
        if checked==None: return
        dialog = QDialog()
        dialog.ui = Ui_MyDialog()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()


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

    def hello(self):
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
            first, rest = text.split('<p class="Updated">',1)

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
                if line.find('.">') != -1:
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
                    line=line.strip('<h1>')
                    line=line.strip('<h1 class="PageHead">')
                    line=line.strip('</h1>')
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
            for line in f:
                if '<meta name="date.modified"' in line:
                    datelist=line.split('"')
                    datelist = datelist[3].split('-')

                else:
                    pass


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



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

