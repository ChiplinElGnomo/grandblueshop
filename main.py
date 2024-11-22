import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QStackedWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from funciones import *  

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        #! ===========================>Ventana principal<=========================== !# 
        self.setWindowTitle("Grand Blue")
        self.setFixedSize(600, 700)
        self.setObjectName("ventana_principal")
        
        
        #* Aqui se crea un label para la imagen de fondo usando pixmap y se configura para que se adapte a la ventana principal
        background_label = QLabel(self)
        pixmap = QPixmap('fondoapp2.png')
        background_label.setPixmap(pixmap)
        background_label.setScaledContents(True)
        background_label.setGeometry(0, 0, self.width(), self.height())

        
        #! ===========================>Vista inicial<=========================== !#
        # Crear la vista principal (ya está creada en el constructor)
        self.vista_principal = QWidget(self)
        layout_principal = QVBoxLayout(self.vista_principal) #* Layout que contiene a su vez los layouts de los botones y el cartel
        self.login = QWidget(self)
        crear_login(self.login) 
        

        #* Codigo para el cartel de grand blue
        self.carteltienda = QLabel(self)
        pixmap2 = QPixmap('grand_blue.png')
        self.carteltienda.setPixmap(pixmap2)
        self.carteltienda.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.carteltienda.setFixedSize(400, 200)
        self.carteltienda.setScaledContents(True)
        layout_cartel = QVBoxLayout()
        layout_cartel.addWidget(self.carteltienda)
        layout_cartel.setAlignment(Qt.AlignTop | Qt.AlignHCenter)  # Alineación del cartel en la parte superior central
        layout_principal.addLayout(layout_cartel)
        layout_principal.addSpacing(20)

        #* Código para los botones
        self.botonempleados = QPushButton("Zona Empleados", self)
        self.botonclientes = QPushButton("Zona Clientes", self)
        self.botonclientes.setObjectName("botonclientes")
        self.botonempleados.setObjectName("botonempleados")
        self.botonclientes.setFixedSize(160, 50)
        self.botonempleados.setFixedSize(160, 50)
        self.botonempleados.clicked.connect(lambda: mostrar_login(self))  #* Funcion que se llama al clicar para que vista cambie a otra (login)
        layout_botones = QVBoxLayout()
        layout_botones.addWidget(self.botonempleados)
        layout_botones.addWidget(self.botonclientes)
        layout_botones.setAlignment(Qt.AlignCenter)  # Centrar los botones
        layout_botones.setSpacing(20)
        layout_principal.addLayout(layout_botones) #* Aqui se añade el layout de los botones al layout principal para unirlo con el del cartel
        layout_principal.setContentsMargins(70, 200, 50, 0)  # Márgenes de la ventana


         
        
        

        #! ===========================>StackedWidget<=========================== !#
        self.stacked_widget = QStackedWidget(self)    #* Aqui se crea el StackedWidget
        self.stacked_widget.addWidget(self.vista_principal) #* Aqui se añade la vista_principal creada al inicio como widget, que es igual a toda la ventana inicial, el cartel y los botones.
        self.stacked_widget.addWidget(self.login) #* Se añade la vista de login al stackedwidget despues de crearse.
        

        # Añadir el stacked_widget al layout principal
        layout_principal_general = QVBoxLayout(self)
        layout_principal_general.addWidget(self.stacked_widget)
        self.setLayout(layout_principal_general)  

        #* Aqui se crea la vista de login como widget, se llama a la funcion que la crea con sus layouts y widgets y se añade al stacked
        

        #* Aqui se llama a la funcion que aplica los estilos de css a los respectivos widgets
        aplicar_stylesheet(self, 'estilos.css')


    

# Ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())







