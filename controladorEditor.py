#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Controlador del Editor de textos 

@author: Juan Ignacio García Bartolomé
"""

import ModeloEditor as mE

from PyQt4 import QtGui 

def openFile (widget):
    mE.openFile(widget)
    
def saveFile(widget): 
    mE.saveFile(widget)
  
def saveAsFile(widget):
    mE.saveAsFile(widget)
    
 

