# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QToolTip
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
import base64
import re

class loginPage():
    def __init__(self, main_window, icon):
        super().__init__()
        self.main_window = main_window
        self.gui = main_window.gui

        self.icon = icon
        
        self.start_system()

    def start_system(self):
        try:
            #definir menu
            self.botoes_iniciais()
            #navegação oculta
            self.gui.gridGroupBox_navegacao.setVisible(False)
            self.gui.gridGroupBox_logo.setVisible(False)
            self.icon_password()
            self.infos_login()

        except Exception as e:
            print(f'Ocorreu uma exceção: {e}')

    def botoes_iniciais(self):
        try:
            #PAGINAS 
            self.gui.btn_home.clicked.connect(lambda: self.gui.stackedWidget.setCurrentWidget(self.gui.page_inicial))
            self.gui.btn_cadastrar.clicked.connect(lambda: self.gui.stackedWidget.setCurrentWidget(self.gui.page_cadastro))
            self.gui.btn_consulta.clicked.connect(lambda: self.gui.stackedWidget.setCurrentWidget(self.gui.page_consulta))         

            self.gui.btn_autenticar.clicked.connect(self.validar_login)
            self.gui.ln_senhaLogin.returnPressed.connect(self.validar_login)

        except Exception as e:
            print(f'Ocorreu uma exceção: {e}')
    
    def decode_b64(self, img_data):
        img_bytes = base64.b64decode(img_data)
        return img_bytes
    
    def logoAutenticacao(self):
        try:
            logo = self.icon.logo()
            logo = self.decode_b64(logo)

            label_logo = self.gui.logo
            pixmap = QPixmap()  # Substitua pelo caminho correto da logo
            pixmap.loadFromData(logo)
            pixmap = pixmap.scaled(380, 180, Qt.KeepAspectRatio)
            label_logo.setPixmap(pixmap)
            self.gui.gridGroupBox_logo.setVisible(True)            
        except Exception as e:
            print(f'Ocorreu uma exceção: {e}')

    #icon botao --> exibir e ocultar senha
    def icon_password(self):
        try:
            password_icon = self.icon.password_icon()
            password_icon = self.decode_b64(password_icon)
            temp_image = QPixmap()
            temp_image.loadFromData(password_icon)
            icon = QIcon(temp_image)

            pass_button = [self.gui.show_password_button]     

            for button in pass_button:
                button.setIcon(icon)
                button.setIconSize(icon.actualSize(button.size()))  # Define o tamanho do ícone com base no tamanho do botão
                button.setFixedSize(icon.actualSize(button.size()))  # Define o tamanho fixo do botão com base no tamanho do ícone

                button.setStyleSheet(
                "QPushButton {"
                "   border-radius: 5px;" 
                "   background-color: #ffffff;" 
                "}"
                "QPushButton:hover {"
                "   background-color: #ecf0f1;"  
                "}"
                "QPushButton:pressed {"
                "   background-color: #bdc3c7;" 
                "}"
                )

                button.setToolTip('Mostrar senha')

                # Conecta o sinal de passagem do mouse para mostrar a dica de ferramenta
                button.enterEvent = lambda event: QToolTip.showText(button.mapToGlobal(event.pos()), button.toolTip())
        except Exception as e:
            print(f'Ocorreu uma exceção: {e}')

    #seta configuracoes de senha
    def infos_login(self):
        try:
            ##senha
            self.gui.ln_senhaLogin.setEchoMode(QLineEdit.Password)
            self.gui.ln_usuarioLogin.setPlaceholderText("Digite seu e-mail")
            self.gui.ln_senhaLogin.setPlaceholderText("Digite sua senha")
            self.gui.show_password_button.pressed.connect(self.mostrar_senhaLogin)
            self.gui.show_password_button.released.connect(self.ocultar_senhaLogin)
        except Exception as e:
            print(f'Ocorreu uma exceção: {e}')
       
    def mostrar_senhaLogin(self):
        try:
        # Quando o botão é pressionado, alterar o modo de exibição da senha para normal
            self.gui.ln_senhaLogin.setEchoMode(QLineEdit.Normal)
        except Exception as e:
            print(f'Ocorreu uma exceção: {e}')

    def ocultar_senhaLogin(self):
        try:
            # Quando o botão é solto, voltar o modo de exibição da senha para oculto
            self.gui.ln_senhaLogin.setEchoMode(QLineEdit.Password)
        except Exception as e:
            print(f'Ocorreu uma exceção: {e}')
    
    def is_valid_email(self, email):
        # Expressão regular para validar o formato básico de um e-mail
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(regex, email) is not None

    def validar_login(self):
        try:
            usuario = self.gui.ln_usuarioLogin.text()
            senha = self.gui.ln_senhaLogin.text()

            email_valido = self.is_valid_email(usuario)
            if not email_valido:
                QMessageBox.warning(None, 'Alerta', 'Digite um e-mail válido!')
                return

            if usuario and senha:
                self.gui.gridGroupBox_login.setVisible(False)
                self.gui.gridGroupBox_navegacao.setVisible(True)
                self.logoAutenticacao()
                self.gui.ln_senhaLogin.clear()
            else:
                QMessageBox.warning(None, 'Senha Inválida', 'A senha fornecida é inválida. Por favor, tente novamente.')     
                return   
        except Exception as e:
            print(f'Ocorreu uma exceção: {e}')


