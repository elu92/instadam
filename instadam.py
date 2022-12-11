# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 14:13:35 2022

@author: uwakw
"""

from windows import Window
from PyQt5 import QtWidgets
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(500, 300, 800, 600)
    window.show()
    sys.exit(app.exec_())

