# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import Qt, QAbstractTableModel
from unidecode import unidecode

class consultarCadastro():
    def __init__(self, main_window, bd):
        self.main_window = main_window
        self.gui = main_window.gui

        self.bd = bd
        self.start_system()
    
    def start_system(self):
        try:
            #button consulta
            self.gui.ln_cons_cd.returnPressed.connect(self.consultar_padrao)
            self.gui.ln_cons_marca.returnPressed.connect(self.consultar_padrao)
            self.gui.ln_cons_tipo.returnPressed.connect(self.consultar_padrao)
            self.gui.ln_cons_categoria.returnPressed.connect(self.consultar_padrao)
            self.gui.btn_cons_procurar.clicked.connect(self.consultar_padrao)
           
        except Exception as e:
            print(f'Ocorreu uma exceção: {e}')

    def ler_informacoes(self):
        try:
            ln_cons_cd = self.gui.ln_cons_cd.text()
            if ln_cons_cd:
                ln_cons_cd = unidecode(ln_cons_cd)
            ln_cons_marca = self.gui.ln_cons_marca.text()
            if ln_cons_marca:
                ln_cons_marca = unidecode(ln_cons_marca)
            ln_cons_tipo = self.gui.ln_cons_tipo.text()
            if ln_cons_tipo:
                ln_cons_tipo = unidecode(ln_cons_tipo)
            ln_cons_categoria = self.gui.ln_cons_categoria.text()
            if ln_cons_categoria:
                ln_cons_categoria = unidecode(ln_cons_categoria)            

            variaveis = {'cd': ln_cons_cd,
            'marca': ln_cons_marca,
            'tipo': ln_cons_tipo,
            'cat': ln_cons_categoria       
            }
            for key, value in variaveis.items():
                variaveis[key] = f"%{value}%"

            consulta = {}
            for key, valor in variaveis.items():
                if valor not in ['', 'None', None]:
                    consulta[key] = valor
            return consulta
        except Exception as e:
            print(f'Ocorreu uma exceção: {e}')

    def consultar_padrao(self):
        try:
            consulta = self.ler_informacoes()
            dfconsulta = self.bd.query_consulta(**consulta)
           
            self.model = PandasModel(dfconsulta)
            self.gui.tableView_consulta.setModel(self.model)
            self.gui.tableView_consulta.setSelectionMode(QAbstractItemView.SingleSelection)
            self.gui.tableView_consulta.resizeColumnsToContents()
    
        except Exception as e:
            print(f'Ocorreu uma exceção: {e}')  
    
class PandasModel(QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """
    def __init__(self, data, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None
        