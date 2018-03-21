#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Vista del editor de textos

@author: Juan Ignacio García Bartolomé
"""

import sys
from PyQt4 import QtGui
import controladorEditor as ctrl

class Editor(QtGui.QWidget):
    
    def __init__(self):
        super(Editor,self).__init__()
        
           
        # Declaramos los elementos que va a tener la ventana:
        
        labelCarpeta=QtGui.QLabel("Carpeta:",self)                   
        self.carpetaEdit=QtGui.QLineEdit()
        
        self.selectButton=QtGui.QPushButton("Seleccionar",None)
        self.selectButton.setShortcut('Ctrl+O')
        self.selectButton.clicked.connect(self.openFile)
        
        labelArchivos=QtGui.QLabel("Archivos",self)
        self.listWidgetArchivos = QtGui.QListWidget()
        
        labelEditor=QtGui.QLabel("Editor",self)
        self.cuadroEditor=QtGui.QTextEdit()
        
        self.saveButton=QtGui.QPushButton("Guardar")
        self.saveButton.setShortcut('Ctrl+S')
        self.saveButton.clicked.connect(self.saveFile)
        
        self.saveAsButton=QtGui.QPushButton("Guardar como")
        self.saveAsButton.clicked.connect(self.saveAsFile) 
        
        
        
        # De manera similar dichos controles deberan de llevar unas
        # determinadas propiedades en la ventana para organizarlos
        # por lo tanto debemos de organizarlos mediante un grid 
        # Declaramos el grid y la unidad de espaciado entre elementos
        
        grid = QtGui.QGridLayout()
        grid.setSpacing(20)

        # Añadimos el texto de carpeta el cuadro de texto y el boton de 
        # seleccionar 
            
        grid.addWidget(labelCarpeta,1,1,1,1)
        grid.addWidget(self.carpetaEdit,1,2,1,22)
        grid.addWidget(self.selectButton,1,24,1,4)
        
        
        grid.addWidget(labelArchivos,3,1,1,4)
        grid.addWidget(labelEditor,3,7,1,4)
        
        grid.addWidget(self.listWidgetArchivos,4,1,9,6)
        grid.addWidget(self.cuadroEditor,4,7,9,20)

        grid.addWidget(self.saveButton,15,1,1,3)
        grid.addWidget(self.saveAsButton,15,4,1,5)
        
        
        # Debemos declarar un mainLayout, que hará la función de mascara
        # distribuyendo los distintos elementos dentro de la ventana

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(grid)
        #mainLayout.addLayout(self.buttomsLayout)        
        
        # Elegimos el layout que hemos definido previamente
        
        self.setLayout(mainLayout)
        
        # Definimos las propiedades de la ventana, tendremos una ventana 
        # con icono personalizado de 800x600 llamada Editor. 
        # Esta además estará alineada en el centro de la pantalla         

        self.setWindowIcon(QtGui.QIcon('editor.png'))      
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle(u"Editor")
        self.show()
    
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())     

    def openFile(self):
        ctrl.openFile(self)
        
    def saveFile(self):
        ctrl.saveFile(self)
        
    def saveAsFile(self):
        ctrl.saveAsFile(self)
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ed = Editor()
    sys.exit(app.exec_())