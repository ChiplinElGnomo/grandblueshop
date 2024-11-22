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








def crear_login(self):          #* Funcion que crea la vista del login, con sus layouts, botones y demás
    # Crear el widget de login
    self.login = QWidget(self)  
    layout_login = QVBoxLayout()  

    # Fondo y cartel en login
    self.carteltienda_login = QLabel(self)  
    pixmap2 = QPixmap('grand_blue.png')
    self.carteltienda_login.setPixmap(pixmap2)
    self.carteltienda_login.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
    self.carteltienda_login.setFixedSize(400, 200)
    self.carteltienda_login.setScaledContents(True)
    layout_cartel_login = QVBoxLayout()
    layout_cartel_login.addWidget(self.carteltienda_login)
    layout_cartel_login.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
    layout_cartel_login.setContentsMargins(29, 0, 0, 0)

    # Campos de usuario y contraseña
    self.usuario_input = QLineEdit(self)
    self.usuario_input.setPlaceholderText("Usuario")
    self.contraseña_input = QLineEdit(self)
    self.contraseña_input.setPlaceholderText("Contraseña")
    self.contraseña_input.setEchoMode(QLineEdit.Password)
    self.usuario_input.setFixedSize(160, 50)
    self.contraseña_input.setFixedSize(160, 50)
    self.boton_login = QPushButton("Iniciar sesión", self)
    self.boton_login.clicked.connect(login)
    self.boton_login.setFixedSize(160, 50)
    self.usuario_input.setObjectName("cuadrousuario")
    self.contraseña_input.setObjectName("cuadrocontra")
    self.boton_login.setObjectName("botonlogin")
    layout_botones_login = QVBoxLayout()
    layout_botones_login.addWidget(self.usuario_input)
    layout_botones_login.addWidget(self.contraseña_input)
    layout_botones_login.addWidget(self.boton_login)
    layout_botones_login.setSpacing(20)
    layout_botones_login.setContentsMargins(150, 0, 0, 100)
    layout_login.addLayout(layout_cartel_login)
    layout_login.addLayout(layout_botones_login)
    layout_login.addWidget(self.boton_login)
    layout_login.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
    layout_login.setSpacing(50)
    layout_login.setContentsMargins(70, 200, 70, 0)
    

    self.login.setLayout(layout_login)  # Aquí se configura el layout para 'login'




def mostrar_login(self): #* Esta funcion solamente cambia la pagina de la vista actual a la de login
        # Cambiar al login
        self.stacked_widget.setCurrentWidget(self.login)


