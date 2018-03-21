#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Modelo del Editor de textos

@author: Juan Ignacio García Bartolomé
"""

from PyQt4 import QtGui 


def openFile(widget):
    
        filename = QtGui.QFileDialog.getOpenFileName(widget, 'Abrir Documento')
        f = open(filename, 'r')
        filedata = f.read()
        widget.textLayout.setText(filedata)
        f.close()
        widget.statusBar().showMessage("Documento abierto")


    
def saveFile(widget): 
    
        if widget.filename == "":
            widget.filename = QtGui.QFileDialog.getSaveFileName(widget, 'Guardar Documento')    
        f = open(widget.filename, 'w')
        filedata = widget.textLayout.toHtml()
        f.write(filedata)
        f.close()
        widget.statusBar().showMessage("Documento guardado")

def saveAsFile(widget):

        widget.filename = QtGui.QFileDialog.getSaveFileName(widget, 'Guardar Documento')
        f = open(widget.filename, 'w')
        filedata = widget.textLayout.toHtml()
        f.write(filedata)
        f.close()
        widget.statusBar().showMessage("Documento guardado")
