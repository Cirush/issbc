# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 19:26:16 2018

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
        """Se inicializa el nombre del archivo"""
        self.filename = ""
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

        """ Creamos un editor de texto """
        self.textLayout = QtGui.QTextEdit(w)
        
        """Hacemos el widget central"""
        self.setCentralWidget(self.textLayout)
        
        """
        Definimos las propiedades de nuestra MainWindow.
            -Nombre
            -Tamanio minimo
            -Tamanio por defecto, que sera el recomendado
        """
        self.setWindowTitle("Editor de texto")
        self.setMinimumSize(480,320)
        self.resize(self.sizeHint()) 

        self.show()
        
  
    def createActions(self):
        """
        Se crea por cada accion que se quiera un QtGui.QAction
        """
        self.newAct = QtGui.QAction("&Nuevo", self,
                shortcut="Ctrl+N",
                statusTip="Crea un nuevo archivo", triggered=self.newFile)
        self.openAct = QtGui.QAction("&Abrir...", self,
                shortcut="Ctrl+O",
                statusTip="Abre un archivo existente", triggered=self.open)
        self.saveAct = QtGui.QAction("&Guardar", self,
                shortcut="Ctrl+S",
                statusTip="Guarda el documento en el disco", triggered=self.save)   
        self.saveasAct = QtGui.QAction("&Guardar como", self,
                shortcut="Ctrl+A",
                statusTip="Guarda el documento en el disco", triggered=self.saveAs) 
        self.exitAct = QtGui.QAction("&Salir", self, shortcut="Ctrl+Q",
                statusTip="Salir de la aplicacion", triggered=self.close)  
        self.changeFont = QtGui.QAction("&Fuente", self, shortcut="Crtl+F", statusTip="Cambiar el tipo de letra",triggered=self.font)
        self.list = QtGui.QAction("&Listar", self, shortcut="Crtl+L", statusTip="Crear una lista", triggered=self.lista)
    
    
    def createToolBar(self):
        """
        Creacion de la barra de herramientas con las acciones declaradas en createActions
        """
        self.toolbar = self.addToolBar('Herramientas')
        self.toolbar.addAction(self.newAct)
        self.toolbar.addAction(self.openAct)
        self.toolbar.addAction(self.saveAct)
        self.toolbar.addAction(self.saveasAct)
        self.formatbar = self.addToolBar('Formato')
        self.formatbar.addAction(self.changeFont)
        self.formatbar.addAction(self.list)
  
     

 
    def createMenus(self):
        '''
        Función para crear menús
        '''
        self.fileMenu = self.menuBar().addMenu("&Archivo")#Crea un menú
        self.toolsMenu = self.menuBar().addMenu("&Herramientas")#Crea un menú
        self.helpMenu = self.menuBar().addMenu("&Ayuda")#Crea un menú
        self.fileMenu.addAction(self.newAct)#Añade una acción al menú
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.saveasAct)
        self.fileMenu.addAction(self.exitAct)
        self.toolsMenu.addAction(self.changeFont)
        self.toolsMenu.addAction(self.list)
        

        
    def newFile(self):
        self.filename = ""
        self.textLayout.clear()
        self.statusBar().showMessage("Documento creado")

        
    def open(self):
        """Metodo sobrecargado"""
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Abrir Documento')
        f = open(filename, 'r')
        filedata = f.read()
        self.textLayout.setText(filedata)
        f.close()
        self.statusBar().showMessage("Documento abierto")

        
    def save(self):
        
        """Si el nombre aún no ha sido puesto se abre un dialogo para elegir
        el nombre del archivo"""
        
        if self.filename == "":
            self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Guardar Documento')    
        f = open(self.filename, 'w')
        filedata = self.textLayout.toHtml()
        f.write(filedata)
        f.close()
        self.statusBar().showMessage("Documento guardado")

    def saveAs(self):
        self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Guardar Documento')
        f = open(self.filename, 'w')
        filedata = self.textLayout.toHtml()
        f.write(filedata)
        f.close()
        self.statusBar().showMessage("Documento guardado")
    
    def font(self):
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.textLayout.setFont(font)
            
    def lista(self):
        cursor = self.textLayout.textCursor()
        cursor.insertList(QtGui.QTextListFormat.ListDisc)
        

def main():
    
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
