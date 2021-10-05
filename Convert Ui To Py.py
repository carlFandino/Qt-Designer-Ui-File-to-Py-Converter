
import time
import os
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(460, 246)
        Form.setStyleSheet("background-color: rgb(0, 95, 95);")
        self.UiFileText = QtWidgets.QLabel(Form)
        self.UiFileText.setGeometry(QtCore.QRect(30, 50, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.UiFileText.setFont(font)
        self.UiFileText.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border-radius:10px;\n"
"border: 1px solid rgba(255,255,255,100%)")
        self.UiFileText.setObjectName("UiFileText")
        self.TextPath = QtWidgets.QLabel(Form)
        self.TextPath.setGeometry(QtCore.QRect(106, 50, 261, 21))
        self.TextPath.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border: 1px solid rgba(255,255,255,100%)\n"
"")
        self.TextPath.setText("")
        self.TextPath.setObjectName("TextPath")
        self.SelectButton = QtWidgets.QPushButton(Form)
        self.SelectButton.setGeometry(QtCore.QRect(370, 49, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.SelectButton.setFont(font)
        self.SelectButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SelectButton.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"border: 1px solid rgba(255,255,255,100%)")
        self.SelectButton.setCheckable(False)
        self.SelectButton.setChecked(False)
        self.SelectButton.setObjectName("SelectButton")
        self.ConvertButton = QtWidgets.QPushButton(Form)
        self.ConvertButton.setGeometry(QtCore.QRect(120, 180, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ConvertButton.setFont(font)
        self.ConvertButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ConvertButton.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.4 rgba(0, 0, 104, 105), stop:0.9 rgba(255, 255, 0, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"border: 1px solid rgba(0,0,0,100%)\n"
"")
        self.ConvertButton.setCheckable(False)
        self.ConvertButton.setChecked(False)
        self.ConvertButton.setObjectName("ConvertButton")
        self.Title = QtWidgets.QLabel(Form)
        self.Title.setGeometry(QtCore.QRect(160, 20, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(14)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color: rgb(0, 255, 0);")
        self.Title.setObjectName("Title")
        self.FileNameText = QtWidgets.QLabel(Form)
        self.FileNameText.setGeometry(QtCore.QRect(10, 90, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.FileNameText.setFont(font)
        self.FileNameText.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border-radius:10px;\n"
"border: 1px solid rgba(255,255,255,100%)")
        self.FileNameText.setObjectName("FileNameText")
        self.FileName = QtWidgets.QLineEdit(Form)
        self.FileName.setGeometry(QtCore.QRect(106, 90, 261, 20))
        self.FileName.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border: 1px solid rgba(255,255,255,100%)\n"
"")
        self.FileName.setObjectName("FileName")
        self.OutputText = QtWidgets.QLabel(Form)
        self.OutputText.setGeometry(QtCore.QRect(0, 130, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.OutputText.setFont(font)
        self.OutputText.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border-radius:10px;\n"
"border: 1px solid rgba(255,255,255,100%)")
        self.OutputText.setObjectName("OutputText")
        self.OutputDir = QtWidgets.QLineEdit(Form)
        self.OutputDir.setGeometry(QtCore.QRect(106, 130, 261, 20))
        self.OutputDir.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border: 1px solid rgba(255,255,255,100%)\n"
"")
        self.OutputDir.setReadOnly(True)
        self.OutputDir.setObjectName("OutputDir")
        self.OutputDirButton = QtWidgets.QPushButton(Form)
        self.OutputDirButton.setGeometry(QtCore.QRect(370, 130, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.OutputDirButton.setFont(font)
        self.OutputDirButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.OutputDirButton.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"border: 1px solid rgba(255,255,255,100%)")
        self.OutputDirButton.setCheckable(False)
        self.OutputDirButton.setChecked(False)
        self.OutputDirButton.setObjectName("OutputDirButton")
        self.OutputTextResetter = QtWidgets.QPushButton(Form)
        self.OutputTextResetter.setGeometry(QtCore.QRect(320, 130, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.OutputTextResetter.setFont(font)
        self.OutputTextResetter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.OutputTextResetter.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"border: 1px solid rgba(255,255,255,100%)")
        self.OutputTextResetter.setCheckable(False)
        self.OutputTextResetter.setChecked(False)
        self.OutputTextResetter.setObjectName("OutputTextResetter")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ui to Py Converter"))
        self.UiFileText.setText(_translate("Form", "Ui File:"))
        self.SelectButton.setText(_translate("Form", "Select Ui File type"))
        self.ConvertButton.setText(_translate("Form", "Convert To Py"))
        self.Title.setText(_translate("Form", "Convert Ui to Py"))
        self.FileNameText.setText(_translate("Form", "File Name :"))
        self.OutputText.setText(_translate("Form", "Output Directory :"))
        self.OutputDirButton.setText(_translate("Form", "Select Output Dir"))
        self.OutputTextResetter.setText(_translate("Form", "Reset"))

        self.changes()
    def changes(self):
        self.SelectButton.clicked.connect(self.openFileName)
        self.ConvertButton.clicked.connect(self.ConvertNow_)
        self.OutputDirButton.clicked.connect(self.getOutputDir)
        self.OutputTextResetter.clicked.connect(self.ResetOutputText)
    def openFileName(self):
 
        self.a = QtWidgets.QFileDialog.getOpenFileName(None,"Open Ui File Type",f"C:/Users/{os.getlogin()}/Desktop","Convert Ui To Py (*.ui)\nAll Files(*)","")
        self.theFile = f"{self.a[0]}".split("/")
        
        

        self.fileOnlyNoDir = ""
        self.fileOnlyWithDir = self.a[0]
        self.filesdir = ""
        
        for i in self.theFile:
                if ".ui" in i:
                        self.fileOnlyNoDir = i
                        break
        self.filesdir = os.path.dirname(self.fileOnlyWithDir)
        
        self.TextPath.setText(self.a[0])
    def ResetOutputText(self):
        self.OutputDir.setText("")
    def getOutputDir(self):
        self.b = QtWidgets.QFileDialog.getExistingDirectory()
        self.OutputDir.setText(self.b)
    
    def ConvertNow_(self):
        self.TextPathval = self.TextPath.text()

        self.FileNameVal = self.FileName.text()
        self.FileNameVal2 = self.TextPath.text()
        file = self.FileNameVal2
        file = file.replace(".ui","")
        outputDir = self.OutputDir.text()
        outputText = self.OutputDir.text()

        fileOnlyNoDir = f"{self.fileOnlyNoDir}"
        fileOnlyWithDir = f"{self.fileOnlyWithDir}"


        fileOnlyNoDir = fileOnlyNoDir.replace(".ui","")
        fileOnlyWithDir = fileOnlyWithDir.replace(".ui","")

        

        
        if self.TextPathval == "":
                b = QtWidgets.QMessageBox()
                b.setText("cannot convert the specified file: There's no selected file.")
                b.setIcon(QtWidgets.QMessageBox.Critical)
                b.setWindowTitle("UltraWares")
                b.exec_()
        
        elif self.TextPathval != "" and self.FileNameVal == "":
                if self.TextPathval[::-1][0] == "i" and self.TextPathval[::-1][1] == "u":
                    b = QtWidgets.QMessageBox()
                    b.setText("""No file name detected, Do you want to set the filename as default name?""")
                    b.setIcon(QtWidgets.QMessageBox.Question)
                    b.setWindowTitle("UltraWares")
                    b.setStandardButtons(b.Yes|b.No)
                    def yesorno(response):
                        if response.text() == "&Yes":
                           
                            
                            b.setCursor(QtCore.Qt.CursorShape.WaitCursor)

                            def successOrNot(a,dir):
                                #Success
                                if a == 0:
                                        b = QtWidgets.QMessageBox()
                                        b.setText(f"File converted successfully.\nFile located in: {dir}")
                                        b.setWindowTitle("Converted.")
                                        b.setIcon(b.Information)
                                        
                                        b.exec_()
                                #Error
                                elif a == 1:
                                        b = QtWidgets.QMessageBox()
                                        b.setText("File not converted.")
                                        b.setWindowTitle("Convertion Failed.")
                                        b.setIcon(b.Critical)
                                        b.exec_()
                            
                            if outputText == "":
                                
                                os.chdir(f"{self.filesdir}")
                                o = os.system(f"pyuic5 -x {self.fileOnlyNoDir} -o C:/Users/{os.getlogin()}/Desktop/{fileOnlyNoDir}.py")
                                successOrNot(o,f"C:/Users/{os.getlogin()}/Desktop/")
                               
                            else:
                                print(self.fileOnlyNoDir)
                                os.chdir(f"{self.filesdir}")
                                o = os.system(f"cd {self.filesdir}\npyuic5 -x {self.fileOnlyNoDir} -o {str(outputDir)}/{fileOnlyNoDir}.py")
                                successOrNot(o,outputDir)
                                

                            
                            

                        elif response.text() == "&No":
                            print("cancelled")
                    b.buttonClicked.connect(yesorno)
                    b.exec_()

                else:


                        a = QtWidgets.QMessageBox()
                        a.setText("The file type is not acceptable : must be ui file.")
                        a.setWindowTitle("Type Error")
                        a.setIcon(a.Critical)
                        a.exec_()

        elif self.TextPathval != "" and self.FileNameVal != "":
                if self.TextPathval[::-1][0] == "i" and self.TextPathval[::-1][1] == "u":
                    b = QtWidgets.QMessageBox()
                    b.setText("""Are you sure you want to convert?""")
                    b.setIcon(QtWidgets.QMessageBox.Question)
                    b.setWindowTitle("UltraWares")
                    b.setStandardButtons(b.Yes|b.No)
                    def yesorno(response):          
                            if response.text() == "&Yes":    

                                    b.setCursor(QtCore.Qt.CursorShape.WaitCursor)
                                    def successOrNot(a,dir):
                                        #Success
                                        if a == 0:
                                            b = QtWidgets.QMessageBox()
                                            b.setText(f"File converted successfully.\nFile located in: {dir}")
                                            b.setWindowTitle("Converted.")
                                            b.setIcon(b.Information)
                                        
                                            b.exec_()
                                        #Error
                                        elif a == 1:
                                            b = QtWidgets.QMessageBox()
                                            b.setText("File not converted.")
                                            b.setWindowTitle("Convertion Failed.")
                                            b.setIcon(b.Critical)
                                            b.exec_()
                            
                                    if outputText == "":
                                        o = os.system(f"pyuic5 -x {self.TextPathval} -o C:/Users/{os.getlogin()}/Desktop/{self.FileNameVal}.py")
                                        successOrNot(o,f"C:/Users/{os.getlogin()}/Desktop")
                                    else:
                                        o = os.system(f"pyuic5 -x {self.TextPathval} -o {str(outputDir)}/{self.FileNameVal}.py")
                                        successOrNot(o,outputDir)
                            else:
                                print("cancelled")
                    b.buttonClicked.connect(yesorno)
                    b.exec_()
                else:
                        a = QtWidgets.QMessageBox()
                        a.setText("The file type is not acceptable : must be ui file.")
                        a.setWindowTitle("Type Error")
                        a.setIcon(a.Critical)
                        a.exec_()
                #os.system(f"pyuic5 -x {self.TextPathval} -o {self.FileNameVal}.py")
          

    
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
