from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
import configparser
from gui import Qt_gui

def my_callback_function():
    print("Callback function has been called!")

if __name__ == "__main__":
    app = QApplication([])
    ex = Qt_gui(callback=my_callback_function)
    ex.show()
    app.exec_()