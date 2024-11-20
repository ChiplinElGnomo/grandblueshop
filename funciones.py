from PyQt5.QtWidgets import QLineEdit, QPushButton, QFormLayout, QWidget 
from PyQt5.QtCore import QFile, QTextStream


def show_login(widget):
    # Ocultar los botones antes de mostrar el login
    widget.botoncliente.hide()
    widget.botonempleado.hide()

    # Crear un layout para el formulario de login
    login_layout = QFormLayout()

    # Crear widgets para el login
    username_input = QLineEdit()
    password_input = QLineEdit()
    password_input.setEchoMode(QLineEdit.Password)

    # Agregar los widgets al layout de login
    login_layout.addRow('Usuario:', username_input)
    login_layout.addRow('Contraseña:', password_input)

    # Botón de iniciar sesión
    login_button = QPushButton('Iniciar Sesión')
    login_layout.addRow('', login_button)

    # Crear un widget contenedor para el formulario de login
    login_widget = QWidget(widget)
    login_widget.setLayout(login_layout)

    # Establecer un tamaño fijo para el widget contenedor
    login_widget.setFixedSize(300, 200)  # Ajusta el tamaño según lo necesites

    # Centrar el widget contenedor en la ventana
    window_width = widget.width()  # Ancho de la ventana principal
    window_height = widget.height()  # Alto de la ventana principal
    login_widget_width = login_widget.width()  # Ancho del widget de login
    login_widget_height = login_widget.height()  # Alto del widget de login

    # Calcular las coordenadas para centrar el widget
    x_pos = (window_width - login_widget_width) // 2
    y_pos = (window_height - login_widget_height) // 2

    # Mover el widget al centro de la ventana
    login_widget.move(x_pos, y_pos)

    # Añadir el widget contenedor con el layout de login a la ventana principal
    widget.layout().addWidget(login_widget)

    # Mostrar el formulario de login
    login_widget.show()



def clear_layout(widget):
        
        
        # Elimina el layout actual si existe
        if widget.layout() is not None:
            old_layout = widget.layout()
            while old_layout.count():
                item = old_layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
            old_layout.deleteLater()


