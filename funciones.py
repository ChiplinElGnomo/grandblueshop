from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QStackedWidget, QLineEdit, QMessageBox, QShortcut
from PyQt5.QtGui import QPixmap, QKeySequence
from PyQt5.QtCore import Qt, QFile, QTextStream, QDir, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import sys
import os


jukebox = QMediaPlayer()
 
music_playing = False


def aplicar_stylesheet(widget, filename):
    """Aplica los estilos CSS desde un archivo ubicado en la carpeta 'recursos'."""
    
    # Ruta absoluta al archivo CSS dentro de la carpeta 'recursos'
    archivo_css = os.path.join(os.getcwd(), 'recursos', filename)  # Obtén la ruta correcta
    
    # Verificar que el archivo existe antes de intentar abrirlo
    if not os.path.exists(archivo_css):
        print(f"Error: El archivo CSS no se encuentra en la ruta: {archivo_css}")
        return  # Salir si no se encuentra el archivo

    # Abre y lee el archivo CSS
    file = QFile(archivo_css)
    if file.open(QFile.ReadOnly | QFile.Text):
        stylesheet = QTextStream(file).readAll()

        # Aplica el CSS al widget
        widget.setStyleSheet(stylesheet)
        file.close()
    




def crear_login(self):          #* Funcion que crea la vista del login, con sus layouts, botones y demás
    # Crear el widget de login
    self.login = QWidget(self)  
    layout_login = QVBoxLayout()  
    

    
    self.carteltienda_login = QLabel(self)  
    pixmap2 = QPixmap('recursos/grand_blue.png')
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
    self.boton_login.setFixedSize(160, 50)
    self.boton_login.setDefault(True)
    shortcut_enter = QShortcut(QKeySequence("Return"), self)
    shortcut_enter.activated.connect(self.boton_login.click)
    self.usuario_input.setObjectName("cuadrousuario")
    self.contraseña_input.setObjectName("cuadrocontra")
    self.boton_login.setObjectName("botonlogin")
    self.boton_login.clicked.connect(lambda: comprobarlogin(self))
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



def comprobarlogin(self):

    global jukebox, music_playing 
    musica = os.path.join(os.getcwd(), "recursos", "musicaloli.mp3")
    usuario = self.usuario_input.text()
    contra = self.contraseña_input.text()
    self.usuario_input.clear()
    self.contraseña_input.clear()
    

    if usuario == "admin" and contra == "admin":
          
        QMessageBox.information(self, "Correcto", "Bienvenido administrador")


    elif usuario == "Kohei" and contra == "Nanaka":
         if not music_playing:
            QMessageBox.information(self, "Easter egg", "Has desbloqueado el easter egg de Kohei, felicidades")
            jukebox.setMedia(QMediaContent(QUrl.fromLocalFile(musica)))
            jukebox.play()
            
            music_playing = True

             
        


    else:
        QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")
        
    

def handle_media_status(status):
    global jukebox, music_playing
    # Verifica si la música ha terminado de reproducirse
    if status == QMediaPlayer.StoppedState and music_playing:
        jukebox.play()  