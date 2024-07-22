# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMessageBox
from unidecode import unidecode

class setarCadastro():
    def __init__(self, main_window, bd):
        self.main_window = main_window
        self.gui = main_window.gui

        self.bd = bd

        self.start_system()

    def start_system(self):
        try:
            self.tab_order()
            self.gui.btn_enviar.clicked.connect(self.cadastrar_padrao)
            self.gui.btn_limpar.clicked.connect(self.limpar_cadastro)
        except Exception as e:
            print(f'Ocorreu uma exceção: {e}')

    def tab_order(self):
        self.main_window.setTabOrder(self.gui.ln_cd, self.gui.ln_marca)
        self.main_window.setTabOrder(self.gui.ln_marca, self.gui.ln_tipo)
        self.main_window.setTabOrder(self.gui.ln_tipo, self.gui.ln_cat)
        self.main_window.setTabOrder(self.gui.ln_cat, self.gui.ln_preco)
        self.main_window.setTabOrder(self.gui.ln_preco, self.gui.ln_custo)
        self.main_window.setTabOrder(self.gui.ln_custo, self.gui.ln_obs)
        self.main_window.setTabOrder(self.gui.ln_obs, self.gui.btn_enviar)
        self.main_window.setTabOrder(self.gui.btn_enviar, self.gui.btn_limpar)

    def ler_informacoes(self):
        try:
            ln_cd = self.gui.ln_cd.text()
            if ln_cd:
                ln_cd = unidecode(ln_cd)
            ln_marca = self.gui.ln_marca.text()
            if ln_marca:
                ln_marca = unidecode(ln_marca)
            ln_tipo = self.gui.ln_tipo.text()
            if ln_tipo:
                ln_tipo = unidecode(ln_tipo)
            ln_cat = self.gui.ln_cat.text()
            if ln_cat:
                ln_cat = unidecode(ln_cat)
            ln_preco = self.gui.ln_preco.text()
            if ln_preco:
                ln_preco = ln_preco.replace(',', '.')
                ln_preco = float(ln_preco)
            ln_custo = self.gui.ln_custo.text()
            if ln_custo:
                ln_custo = ln_custo.replace(',', '.')
                ln_custo = float(ln_custo)
            ln_obs = self.gui.ln_obs.text()
            if ln_obs:
                ln_obs = unidecode(ln_obs)
               
            infos = [ln_cd, ln_marca, ln_tipo, ln_cat, ln_preco, ln_custo]

            todos_preenchidos = all(info != "" and info is not None for info in infos)

            if todos_preenchidos:
                dictCadastro = {'cd': ln_cd,
                                'marca': ln_marca,
                                'tipo': ln_tipo,
                                'cat': ln_cat,
                                'preco_un': ln_preco,
                                'custo': ln_custo,
                                'obs': ln_obs                            
                }     

                return dictCadastro
            else:
                QMessageBox.warning(None, 'Dados Inválidos', 'Um ou mais dados em brancos, preencha todas informações para realizar o cadastro!')
                return
        except Exception as e:
            print(f'Ocorreu uma exceção: {e}')
           
    def limpar_cadastro(self):
        try:
            self.gui.ln_cd.clear()
            self.gui.ln_marca.clear()
            self.gui.ln_tipo.clear()
            self.gui.ln_cat.clear()
            self.gui.ln_preco.clear()
            self.gui.ln_custo.clear()
            self.gui.ln_obs.clear()
        except Exception as e:
            print(f'Ocorreu uma exceção: {e}')

    def cadastrar_padrao(self):
        try:
            dictCadastro = self.ler_informacoes()
            if dictCadastro:
                resultado = self.bd.query_cadastrar(dictCadastro)
                if resultado in 'sucesso':
                    QMessageBox.information(None, 'Confirmação', 'Cadastro inserido com sucesso!')    
                    self.limpar_cadastro()     
                else:
                    QMessageBox.information(None, 'Erro', 'Erro ao concluir a solicitação, tente novamente!') 
                    return   
        except Exception as e:
            print(f'Ocorreu uma exceção: {e}')




    