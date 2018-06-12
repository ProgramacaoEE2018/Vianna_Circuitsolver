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


      
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calc_tax_button.clicked.connect(self.CalculateTax)
        #inicia a interface
    
        

class Req:
    def serie(R1,R2):
        return R1+R2
    def paralelo(R1,R2):
        return (R1*R2)/(R1+R2)
    
    #calculo de resistência em série e em paralelo
        
    

if checkBox.isChecked() == True:
       ResAux=int(textEdit.toPlainText().split(','))
       R[1,1]=Req.serie(ResAux[0],ResAux[1])
       
if checkBox_12.isChecked() == True:
    ResAux=int(textEdit.toPlainText().split(','))
    R[1,1]=Req.paralelo(ResAux[0],ResAux[1])
else:
    if not textEdit.toPlainText():
        R[1,1]=int(textEdit.toPlainText())
      
if checkBox_2.isChecked() == True:
       ResAux=int(textEdit_2.toPlainText().split(','))
       R[2,2]=Req.serie(ResAux[0],ResAux[1])
       
if checkBox_11.isChecked() == True:
    ResAux=int(textEdit_2.toPlainText().split(','))
    R[2,2]=Req.paralelo(ResAux[0],ResAux[1])
else:
    if not textEdit_2.toPlainText():
        R[2,2]=int(textEdit_2.toPlainText())
           
if checkBox_3.isChecked() == True:
       ResAux=int(textEdit_3.toPlainText().split(','))
       R[3,3]=Req.serie(ResAux[0],ResAux[1])
       
if checkBox_13.isChecked() == True:
    ResAux=int(textEdit_3.toPlainText().split(','))
    R[3,3]=Req.paralelo(ResAux[0],ResAux[1])
else:
    if not textEdit_3.toPlainText():
        R[3,3]=int(textEdit_3.toPlainText())
           
if checkBox_4.isChecked() == True:
       ResAux=int(textEdit_4.toPlainText().split(','))
       R[4,4]=Req.serie(ResAux[0],ResAux[1])
   
if checkBox_14.isChecked() == True:
    ResAux=int(textEdit_4.toPlainText().split(','))
    R[4,4]=Req.paralelo(ResAux[0],ResAux[1])
else:
    if not textEdit_4.toPlainText():
        R[4,4]=int(textEdit_4.toPlainText())
if checkBox_5.isChecked() == True:
       ResAux=int(textEdit_5.toPlainText().split(','))
       R[5,5]=Req.serie(ResAux[0],ResAux[1])
   
if checkBox_10.isChecked() == True:
    ResAux=int(textEdit_5.toPlainText().split(','))
    R[5,5]=Req.paralelo(ResAux[0],ResAux[1])
else:
    if not textEdit_5.toPlainText():
        R[5,5]=int(textEdit_5.toPlainText())
if checkBox_6.isChecked() == True:
       ResAux=int(textEdit_6.toPlainText().split(','))
       R[1,2]=Req.serie(ResAux[0],ResAux[1])
   
if checkBox_9.isChecked() == True:
    ResAux=int(textEdit_6.toPlainText().split(','))
    R[1,2]=Req.paralelo(ResAux[0],ResAux[1])
else:
    if not textEdit_6.toPlainText():
        R[1,2]=int(textEdit_6.toPlainText())
if checkBox_8.isChecked() == True:
       ResAux=int(textEdit_7.toPlainText().split(','))
       R[2,3]=Req.serie(ResAux[0],ResAux[1])
   
if checkBox_15.isChecked() == True:
    ResAux=int(textEdit_7.toPlainText().split(','))
    R[2,3]=Req.paralelo(ResAux[0],ResAux[1])
else:
    if not textEdit_7.toPlainText():
        R[2,3]=int(textEdit_7.toPlainText())
if checkBox_19.isChecked() == True:
       ResAux=int(textEdit_8.toPlainText().split(','))
       R[3,4]=Req.serie(ResAux[0],ResAux[1])
   
if checkBox_16.isChecked() == True:
    ResAux=int(textEdit_8.toPlainText().split(','))
    R[3,4]=Req.paralelo(ResAux[0],ResAux[1])
else:
    if not textEdit_8.toPlainText():
        R[3,4]=int(textEdit_8.toPlainText())
if checkBox_7.isChecked() == True:
       ResAux=int(textEdit_9.toPlainText().split(','))
       R[4,5]=Req.serie(ResAux[0],ResAux[1])
   
if checkBox_18.isChecked() == True:
    ResAux=int(textEdit_9.toPlainText().split(','))
    R[4,5]=Req.paralelo(ResAux[0],ResAux[1])
else:
    if not textEdit_9.toPlainText():
        R[4,5]=int(textEdit_9.toPlainText())
        
        #essa sessão confere se há ou não resistores em série ou em paralelo e define o valor de Req


if not textEdit_10.toPlainText():
           F[0]=int(textEdit_10.toPlainText())           
if not textEdit_16.toPlainText():
           F[1]=int(textEdit_16.toPlainText())
if not textEdit_14.toPlainText():
           F[2]=int(textEdit_14.toPlainText())
if not textEdit_15.toPlainText():
           F[3]=int(textEdit_15.toPlainText())
if not textEdit_18.toPlainText():
           F[4]=int(textEdit_18.toPlainText())
           
           #essa sessão define o valor das fontes
           
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
M[3,4]=R[4,5]
M[4,3]=R[4,5]

#essa sessão cria a matriz de resistência


correntes=np.linalg.solve(M, F)     

#essa sessão resolve o sistema linear das resistências
 
results_window.setText(",".join(correntes))

#printa as resistências no textbox
          
      
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
