# -*- coding: utf-8 -*-
import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog

ABSOLUT_PATH = os.path.dirname(os.path.realpath(__file__))
interface_path = os.path.join(ABSOLUT_PATH, 'interface')
functions_path = os.path.join(ABSOLUT_PATH, 'functions')
database_path = os.path.join(ABSOLUT_PATH, 'database')

from interface.gui_main import Ui_MainWindow

from functions.loginPage import loginPage
from functions.page_cadastro import setarCadastro
from functions.page_consultar import consultarCadastro
from icon.icon import icon
from database.bd import bd

class FrontEnd(QMainWindow, QDialog):
    def __init__(self):
        super(FrontEnd, self).__init__()

    #GUI - interface
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.showMaximized()

        self.icon = icon()
        self.bd = bd()

    #Funções -- INICIO - LOGIN 
        self.loginPage = loginPage(self, self.icon)
    
    ## Cadastrar
        self.setarCadastro = setarCadastro(self, self.bd)

    ## Consultar  
        self.consultarCadastro = consultarCadastro(self, self.bd)

## FECHAR PROGRAMA
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Encerrar', 'Você realmente deseja sair?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()        
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    gui = FrontEnd()
    gui.show() 
    sys.exit(app.exec_())
        

