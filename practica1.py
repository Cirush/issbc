# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 19:26:16 2018

@author: Juan Ignacio García Bartolomé
"""
############################################################################
#
#  Pequeño programa de prueba con todo lo visto en el tutorial.
#
############################################################################
from PyQt4 import QtCore, QtGui

"""
Clase que sera nuestra ventana principal.
"""
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
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

        """
        Definimos las propiedades de nuestra MainWindow.
            -Nombre
            -Tamanio minimo
            -Tamanio por defecto, que sera el recomendado
        """
        self.setWindowTitle("Practica 1")
        self.setMinimumSize(480,320)
        self.resize(self.sizeHint()) 


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
        #rv=Review(parent=self).exec_()
        #rv.show()
        
    def open(self):
        self.statusBar().showMessage("Documento abierto")
        
    def save(self):
        self.statusBar().showMessage("Documento guardado")



if __name__ == '__main__':
 
    import sys
 
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
