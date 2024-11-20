from PyQt5.QtWidgets import QLineEdit, QPushButton, QFormLayout, QWidget 
from PyQt5.QtCore import QFile, QTextStream


def login():
     

     print("Funciono")







        



def aplicar_stylesheet(widget, filename):      
    """Aplica los estilos CSS desde un archivo."""
    file = QFile(filename)
    if file.open(QFile.ReadOnly | QFile.Text):
        stylesheet = QTextStream(file).readAll()  

        
        widget.setStyleSheet(stylesheet)  

        file.close()