# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 19:26:16 2018

@author: Juan Ignacio García Bartolomé
"""
############################################################################
#
#  Desarrollo de una aplicación básica
#
############################################################################
from PyQt4 import QtCore, QtGui
import sys

"""
Clase que sera nuestra ventana principal.
"""
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
    
    def initUI(self):
        """
        Creamos el esqueleto de nuestra aplicacion. 
            -Menu
            -Barra de herramientas
            -Barra de estado
        Estos metodos estan definidos mas abajo
        """
        self.createActions()
        self.createMenus()
        self.createToolBar()

        self.statusBar().showMessage("Barra de estado")

        """Creamos un widget Central"""
        w = QtGui.QWidget()
        """ Creamos dos botones """
        okButton = QtGui.QPushButton("Enviar",w)
        cancelButton = QtGui.QPushButton("Cancelar",w)
        """ Creamos un editor de texto """
        textLayout = QtGui.QTextEdit(w)
        
        """Establecemos los conenedores vertical y horizontal para el widget cental"""
        hbox = QtGui.QHBoxLayout() #Se establece un contenedor horizontal de controles
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        
        

        vbox = QtGui.QVBoxLayout()#Se establece un contenedor vertical de controles
        vbox.addWidget(textLayout)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        QtGui.QTextEdit()
        """Aniadimos nuestro contenedor vertical al widget"""
        w.setLayout(vbox)  
        """Hacemos el widget central"""
        self.setCentralWidget(w)
        
        """
        Definimos las propiedades de nuestra MainWindow.
            -Nombre
            -Tamanio minimo
            -Tamanio por defecto, que sera el recomendado
        """
        self.setWindowTitle("Aplicacion Basica")
        self.setMinimumSize(480,320)
        self.resize(self.sizeHint()) 

        self.show()
        
  
    def createActions(self):
        """
        Se crea por cada accion que se quiera un QtGui.QAction
        """
        self.newAct = QtGui.QAction("&Nuevo", self,
                shortcut=QtGui.QKeySequence.New,
                statusTip="Crea un nuevo archivo", triggered=self.newFile)
        self.openAct = QtGui.QAction("&Abrir...", self,
                shortcut=QtGui.QKeySequence.Open,
                statusTip="Abre un archivo existente", triggered=self.open)
        self.exitAct = QtGui.QAction("&Salir", self, shortcut="Ctrl+Q",
                statusTip="Salir de la aplicacion", triggered=self.close)    
        #self.exitAct.setIcon(QtGui.QIcon('exit.jpg') )
        self.saveAct = QtGui.QAction("&Guardar", self,
                shortcut=QtGui.QKeySequence.Save,
                statusTip="Guarda el documento en el disco", triggered=self.save)
    
    
    def createToolBar(self):
        """
        Creacion de la barra de herramientas con las acciones declaradas en createActions
        """
        self.toolbar = self.addToolBar('Herramientas')
        self.toolbar.addAction(self.newAct)
        self.toolbar.addAction(self.openAct)
        self.toolbar.addAction(self.saveAct)
        self.toolbar.addAction(self.exitAct)

  
     

 
    def createMenus(self):
        '''
        Función para crear menús
        '''
        self.fileMenu = self.menuBar().addMenu("&Archivo")#Crea un menú
        self.fileMenu.addAction(self.newAct)#Añade una acción al menú
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.exitAct)
        self.fileMenu.addAction(self.saveAct)
        
    def newFile(self):
        self.statusBar().showMessage("Documento creado")

        
    def open(self):
        """Metodo sobrecargado"""
        self.statusBar().showMessage("Documento abierto")
        
    def save(self):
        self.statusBar().showMessage("Documento guardado")

def main():
    
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
