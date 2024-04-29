from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class ExampleGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)
        
        self.label_title = QLabel('Open3d GUI', self)
        self.label_description = QLabel('This is an example of using the Open3d GUI.', self)

        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.label_title)
        self.layout.addWidget(self.label_description)

        self.update_labels_font()

    def resizeEvent(self, event):
        self.update_labels_font()
        super().resizeEvent(event)

    def update_labels_font(self):
        width = self.width()
        font_size_title = max(width // 50, 10)  # Ensure a minimum font size of 10
        font_size_description = max(width // 60, 8)  # Ensure a minimum font size of 8

        self.label_title.setStyleSheet(f"font-size: {font_size_title}px;")
        self.label_description.setStyleSheet(f"font-size: {font_size_description}px;")

if __name__ == "__main__":
    app = QApplication([])
    ex = ExampleGUI()
    ex.show()
    app.exec_()
