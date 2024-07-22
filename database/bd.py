# -*- coding: utf-8 -*-
import os
import sqlite3
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
ABSOLUT_PATH = os.path.join(script_dir, '..')
database_path = os.path.join(ABSOLUT_PATH, 'database')

#PAGINA PARA CONTROLE DO BANCO DE DADOS
class bd():
    def __init__(self):
        print('Sistema Python PowerUp')
        self.diretorio = os.path.join(database_path, 'database.db')

    def query_cadastrar(self, dictCadastro):
        try:
            conn = sqlite3.connect(self.diretorio)
            c = conn.cursor()

            # Inserir dados na tabela
            c.execute('''
                INSERT INTO produtos (cd, marca, tipo, cat, preco_un, custo, obs)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (dictCadastro['cd'], dictCadastro['marca'], dictCadastro['tipo'], dictCadastro['cat'], dictCadastro['preco_un'], dictCadastro['custo'], dictCadastro['obs']))

            conn.commit()
            return 'sucesso'
        except Exception as e:
            print(f'Ocorreu uma exceção: {e}')
            return None
        finally:
            if conn:
                conn.close()

    ## CONSULTA
    def query_consulta(self, **kwargs):
        try:
            conn = sqlite3.connect(self.diretorio)
            c = conn.cursor()

            sql = "SELECT cd, marca, tipo, cat, preco_un, custo, obs FROM produtos"
            if kwargs:
                conditions = []
                for key, value in kwargs.items():
                    conditions.append(f"{key} LIKE ?")
                sql += " WHERE " + " AND ".join(conditions)

            c.execute(sql, tuple(kwargs.values()))
            resultados = c.fetchall()
            
            if resultados:
                df = pd.DataFrame(resultados, columns=['Código', 'Marca', 'Tipo', 'Categoria', 'Preço Unitário', 'Custo do Produto', 'OBS'])
            else:
                df = pd.DataFrame(columns=['Código', 'Marca', 'Tipo', 'Categoria', 'Preço Unitário', 'Custo do Produto', 'OBS'])
            return df
        except Exception as e:
            print(f'Ocorreu uma exceção: {e}')
            return None
        finally:
            if conn:
                conn.close()

   