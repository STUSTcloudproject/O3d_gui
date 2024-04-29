from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFrame

class ExampleGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Main layout
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # Create left layout with different background
        left_layout = QVBoxLayout()
        left_frame = QFrame()  # 使用 QFrame 作为容器
        left_frame.setLayout(left_layout)
        left_frame.setStyleSheet("background-color: lightblue;")  # 设置浅蓝色背景
        main_layout.addWidget(left_frame, 5)

        # Create right layout with different background
        right_layout = QVBoxLayout()
        right_frame = QFrame()  # 使用 QFrame 作为容器
        right_frame.setLayout(right_layout)
        right_frame.setStyleSheet("background-color: lightgreen;")  # 设置浅绿色背景
        main_layout.addWidget(right_frame, 5)

        # Set window properties
        self.setWindowTitle('GUI Example')
        self.setGeometry(300, 300, 1500, 800)

# Application creation and main loop
if __name__ == "__main__":
    app = QApplication([])
    ex = ExampleGUI()
    ex.show()
    app.exec_()
