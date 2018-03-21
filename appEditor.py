#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Editor de textos creado mediante la arquitectura MVC (Modelo-Vista-Controlador)

@author: Juan Ignacio García Bartolomé
"""
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
import vistaEditor as vts

app = QtGui.QApplication(sys.argv) #Crea una aplicación
form = vts.Editor()   #Crea una insytancia del formulario
sys.exit(app.exec_())   #Se inicia la aplicación y se espera eventos
