from __future__ import division
import sys
import numpy as np
from PyQt5 import QtCore, QtWidgets, uic

qtCreatorFile = "circuitsolver.ui" # nome interface grafica

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

R = np.empty([6,6])
R.fill(0)   
F = np.empty([5])
F.fill(0)

M = np.empty([5,5])
M.fill(0)  #define as matrizez

class Req:
    def serie(R1,R2):
        return R1+R2
    def paralelo(R1,R2):
        return (R1*R2)/(R1+R2)
      
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.results)
        
    def serie(R1,R2):
        return R1+R2
    def paralelo(R1,R2):
        return (R1*R2)/(R1+R2)

    #calculo de resistência em série e em paralelo
    def results (self):
        
        if self.checkBox.isChecked()==True:
            ResAux = [int(x) for x in self.textEdit.toPlainText().split(',')]
            R[1,1]=self.serie(ResAux[0],ResAux[1])
        else:
            
            if self.checkBox_12.isChecked() == True:
                ResAux=int(self.textEdit.toPlainText().split(','))
                R[1,1]=Req.paralelo(ResAux[0],ResAux[1])
            else:
                R[1,1]=int(self.textEdit.toPlainText())
        if self.checkBox.isChecked()==True:
               ResAux=int(self.textEdit.toPlainText().split(','))
               R[1,1]=Req.serie(ResAux[0],ResAux[1])
               
        if self.checkBox_12.isChecked() == True:
            ResAux=int(self.textEdit.toPlainText().split(','))
            R[1,1]=Req.paralelo(ResAux[0],ResAux[1])
        else:
            R[1,1]=int(self.textEdit.toPlainText())
              
        if self.checkBox_2.isChecked() == True:
               ResAux=int(self.textEdit_2.toPlainText().split(','))
               R[2,2]=Req.serie(ResAux[0],ResAux[1])
               
        if self.checkBox_11.isChecked() == True:
            ResAux=int(self.textEdit_2.toPlainText().split(','))
            R[2,2]=Req.paralelo(ResAux[0],ResAux[1])
        else:
            R[2,2]=int(self.textEdit_2.toPlainText())
                   
        if self.checkBox_3.isChecked() == True:
               ResAux=int(self.textEdit_3.toPlainText().split(','))
               R[3,3]=Req.serie(ResAux[0],ResAux[1])
               
        if self.checkBox_13.isChecked() == True:
            ResAux=int(self.textEdit_3.toPlainText().split(','))
            R[3,3]=Req.paralelo(ResAux[0],ResAux[1])
        else:
            R[3,3]=int(self.textEdit_3.toPlainText())
                   
        if self.checkBox_4.isChecked() == True:
               ResAux=int(self.textEdit_4.toPlainText().split(','))
               R[4,4]=Req.serie(ResAux[0],ResAux[1])
           
        if self.checkBox_14.isChecked() == True:
            ResAux=int(self.textEdit_4.toPlainText().split(','))
            R[4,4]=Req.paralelo(ResAux[0],ResAux[1])
        else:
            R[4,4]=int(self.textEdit_4.toPlainText())
        if self.checkBox_5.isChecked() == True:
               ResAux=int(self.textEdit_5.toPlainText().split(','))
               R[5,5]=Req.serie(ResAux[0],ResAux[1])
           
        if self.checkBox_10.isChecked() == True:
            ResAux=int(self.textEdit_5.toPlainText().split(','))
            R[5,5]=Req.paralelo(ResAux[0],ResAux[1])
        else:
            R[5,5]=int(self.textEdit_5.toPlainText())
        if self.checkBox_6.isChecked() == True:
               ResAux=int(self.textEdit_6.toPlainText().split(','))
               R[1,2]=Req.serie(ResAux[0],ResAux[1])
           
        if self.checkBox_9.isChecked() == True:
            ResAux=int(self.textEdit_6.toPlainText().split(','))
            R[1,2]=Req.paralelo(ResAux[0],ResAux[1])
        else:
            R[1,2]=int(self.textEdit_6.toPlainText())
        if self.checkBox_8.isChecked() == True:
               ResAux=int(self.textEdit_7.toPlainText().split(','))
               R[2,3]=Req.serie(ResAux[0],ResAux[1])
           
        if self.checkBox_15.isChecked() == True:
            ResAux=int(self.textEdit_7.toPlainText().split(','))
            R[2,3]=Req.paralelo(ResAux[0],ResAux[1])
        else:
            R[2,3]=int(self.textEdit_7.toPlainText())
        if self.checkBox_19.isChecked() == True:
               ResAux=int(self.textEdit_8.toPlainText().split(','))
               R[3,4]=Req.serie(ResAux[0],ResAux[1])
           
        if self.checkBox_16.isChecked() == True:
            ResAux=int(self.textEdit_8.toPlainText().split(','))
            R[3,4]=Req.paralelo(ResAux[0],ResAux[1])
        else:
            R[3,4]=int(self.textEdit_8.toPlainText())
        if self.checkBox_7.isChecked() == True:
               ResAux=int(self.textEdit_9.toPlainText().split(','))
               R[4,5]=Req.serie(ResAux[0],ResAux[1])
           
        if self.checkBox_18.isChecked() == True:
            ResAux=int(self.textEdit_9.toPlainText().split(','))
            R[4,5]=Req.paralelo(ResAux[0],ResAux[1])
        else:
            R[4,5]=int(self.textEdit_9.toPlainText())    
        #seta os valores de resistÊncia
        
            F[0]=int(self.textEdit_10.toPlainText())           
        
            F[1]=int(self.textEdit_16.toPlainText())
        
            F[2]=int(self.textEdit_14.toPlainText())
        
            F[3]=int(self.textEdit_15.toPlainText())
        
            F[4]=int(self.textEdit_18.toPlainText())
                   #cria o vetor fonte
                   
        M[0,0]=R[1,1]
        M[1,1]=R[2,2]
        M[2,2]=R[3,3]
        M[3,3]=R[4,4]
        M[4,4]=R[5,5]
        M[0,1]=R[1,2]
        M[1,0]=R[1,2]
        M[1,2]=R[2,3]
        M[2,1]=R[2,3]
        M[2,3]=R[3,4]
 
       M[3,2]=R[3,4]
        M[3,4]=R[4,5] #cria a matriz
        M[4,3]=R[4,5] 
        correntes=np.linalg.solve(M,F)
        self.textEdit_19.setText(','.join([str(i) for i in correntes]))
        #resolve o sistema linear


        

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
