#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Editor de textos creado mediante la arquitectura MVC (Modelo-Vista-Controlador)

@author: Juan Ignacio Garc�a Bartolom�
"""
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
import vistaEditor as vts

app = QtGui.QApplication(sys.argv) #Crea una aplicaci�n
form = vts.Editor()   #Crea una insytancia del formulario
sys.exit(app.exec_())   #Se inicia la aplicaci�n y se espera eventos
