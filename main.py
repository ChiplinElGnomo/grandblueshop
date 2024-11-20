import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QStackedWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from funciones import *  # Solo importamos la función de login

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Grand Blue")
        self.setFixedSize(600, 700)
        self.setObjectName("ventana_principal")
        
        # Fondo de la ventana
        background_label = QLabel(self)
        pixmap = QPixmap('fondoapp2.png')
        background_label.setPixmap(pixmap)
        background_label.setScaledContents(True)
        background_label.setGeometry(0, 0, self.width(), self.height())

        # Crear el stacked_widget
        self.stacked_widget = QStackedWidget(self)

        # Crear la vista principal (ya está creada en el constructor)
        self.vista_principal = QWidget(self)

        # Layout de la vista principal
        layout_principal = QVBoxLayout(self.vista_principal)

        # Código para el cartel
        self.carteltienda = QLabel(self)
        pixmap2 = QPixmap('grand_blue.png')
        self.carteltienda.setPixmap(pixmap2)
        self.carteltienda.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.carteltienda.setFixedSize(400, 200)
        self.carteltienda.setScaledContents(True)

        # Layout para el cartel
        layout_cartel = QVBoxLayout()
        layout_cartel.addWidget(self.carteltienda)
        layout_cartel.setAlignment(Qt.AlignTop | Qt.AlignHCenter)  # Alineación del cartel en la parte superior central

        # Código para los botones
        self.botonempleados = QPushButton("Zona Empleados", self)
        self.botonclientes = QPushButton("Zona Clientes", self)
        self.botonclientes.setObjectName("botonclientes")
        self.botonempleados.setObjectName("botonempleados")
        self.botonclientes.setFixedSize(160, 50)
        self.botonempleados.setFixedSize(160, 50)
        self.botonempleados.clicked.connect(self.mostrar_login)

        # Layout para los botones
        layout_botones = QVBoxLayout()
        layout_botones.addWidget(self.botonempleados)
        layout_botones.addWidget(self.botonclientes)
        layout_botones.setAlignment(Qt.AlignCenter)  # Centrar los botones
        layout_botones.setContentsMargins(50, 50, 50, 130)
        layout_botones.setSpacing(50)

        # Añadir el layout del cartel y espaciado entre el cartel y los botones
        layout_principal.addLayout(layout_cartel)
        layout_principal.addSpacing(20)  # Controla la distancia entre el cartel y los botones

        # Añadir el layout de los botones al layout principal
        layout_principal.addLayout(layout_botones)
        layout_principal.setContentsMargins(70, 200, 50, 0)  # Márgenes de la ventana

        # Añadir la vista principal al stacked_widget
        self.stacked_widget.addWidget(self.vista_principal)

        # Crear la vista de login
        self.login = QWidget(self)
        crear_login(self.login)  # Llamamos a la función que crea la vista de login
        self.stacked_widget.addWidget(self.login)  # Agregamos la vista de login al stacked_widget

        # Añadir el stacked_widget al layout principal
        layout_principal_general = QVBoxLayout(self)
        layout_principal_general.addWidget(self.stacked_widget)
        self.setLayout(layout_principal_general)  # Asignamos el layout principal

        aplicar_stylesheet(self, 'estilos.css')

    def mostrar_login(self):
        # Cambiar al login
        self.stacked_widget.setCurrentWidget(self.login)

# Ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())







