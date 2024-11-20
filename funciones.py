from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QStackedWidget, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QFile, QTextStream
from funciones import *

def login():
     

     print("Funciono")







        



def aplicar_stylesheet(widget, filename):      
    """Aplica los estilos CSS desde un archivo."""
    file = QFile(filename)
    if file.open(QFile.ReadOnly | QFile.Text):
        stylesheet = QTextStream(file).readAll()  

        
        widget.setStyleSheet(stylesheet)  

        file.close()








def crear_login(self):
    # Crear el widget de login
    self.login = QWidget(self)  # Asegúrate de crear el widget

    layout_login = QVBoxLayout()  # Renombrado a layout_login

    # Fondo y cartel en login
    self.carteltienda_login = QLabel(self)  # Renombrado a carteltienda_login
    pixmap2 = QPixmap('grand_blue.png')
    self.carteltienda_login.setPixmap(pixmap2)
    self.carteltienda_login.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
    self.carteltienda_login.setFixedSize(400, 200)
    self.carteltienda_login.setScaledContents(True)

    layout_cartel_login = QVBoxLayout()
    layout_cartel_login.addWidget(self.carteltienda_login)
    layout_cartel_login.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

    # Campos de usuario y contraseña
    self.usuario_input = QLineEdit(self)
    self.usuario_input.setPlaceholderText("Usuario")
    self.contraseña_input = QLineEdit(self)
    self.contraseña_input.setPlaceholderText("Contraseña")
    self.contraseña_input.setEchoMode(QLineEdit.Password)

    # Botón de login
    self.boton_login = QPushButton("Iniciar sesión", self)

    # Añadir widgets al layout de login
    layout_login.addLayout(layout_cartel_login)
    layout_login.addWidget(self.usuario_input)
    layout_login.addWidget(self.contraseña_input)
    layout_login.addWidget(self.boton_login)
    layout_login.setAlignment(Qt.AlignCenter)

    self.login.setLayout(layout_login)  # Aquí se configura el layout para 'login'




def mostrar_login(self):
        self.stacked_widget.setCurrentIndex(1)