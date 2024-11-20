import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QGridLayout, QSizePolicy,QLabel
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

        

        # Crear los botónes
        self.botonempleados = QPushButton("Zona Empleados", self)
        self.botonclientes = QPushButton("Zona Clientes", self)
        self.botonclientes.setObjectName("botonclientes")
        self.botonempleados.setObjectName("botonempleados")
        self.botonclientes.setFixedSize(160, 50)
        self.botonempleados.setFixedSize(160, 50)
        self.aplicar_stylesheet('estilos.css')


        #Cartel Grand Blue
        self.carteltienda = QLabel(self)
        pixmap2 = QPixmap('grand_blue.png')
        self.carteltienda.setPixmap(pixmap2)
        self.carteltienda.setAlignment(Qt.AlignTop)
        self.carteltienda.setFixedSize(400, 200)
        self.carteltienda.setScaledContents(True)



        # Layout vertical menu
        layout = QVBoxLayout()
        layout.addWidget(self.botonempleados)
        layout.addWidget(self.botonclientes)
        layout.addWidget(self.carteltienda)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(220,320,220,220)
        self.setLayout(layout)

        
        
        
        
        
        

        



          
        
        

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
