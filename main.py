import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from funciones import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Grand Blue")
        self.setFixedSize(600, 700)
        self.setObjectName("ventana_principal")
        background_label = QLabel(self)
        pixmap = QPixmap('fondoapp2.png')
        background_label.setPixmap(pixmap)
        background_label.setScaledContents(True)  # Ajustar imagen al tamaño de la ventana
        background_label.setGeometry(0, 0, self.width(), self.height())
        layout_principal = QVBoxLayout()

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
        self.aplicar_stylesheet('estilos.css')

        # Layout para los botones
        layout_botones = QVBoxLayout()
        layout_botones.addWidget(self.botonempleados)
        layout_botones.addWidget(self.botonclientes)
        layout_botones.setAlignment(Qt.AlignCenter)  # Centrar los botones
        layout_botones.setContentsMargins(50, 50, 50, 130)
        layout_botones.setSpacing(20)

        # Añadir el layout del cartel y espaciado entre el cartel y los botones
        layout_principal.addLayout(layout_cartel)
        layout_principal.addSpacing(20)  # Controla la distancia entre el cartel y los botones

        # Añadir el layout de los botones al layout principal
        layout_principal.addLayout(layout_botones)
        layout_principal.setContentsMargins(70, 200, 50, 0)  # Márgenes de la ventana
        self.setLayout(layout_principal)

    def aplicar_stylesheet(self, filename):      
        """Aplica los estilos CSS desde un archivo."""
        file = QFile(filename)
        if file.open(QFile.ReadOnly | QFile.Text):
            stylesheet = QTextStream(file)
            self.setStyleSheet(stylesheet.readAll())  # Aplica los estilos
            file.close()

# Ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



