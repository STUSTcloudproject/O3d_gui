from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

btn1 = QPushButton("Button 1")
btn1.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
btn2 = QPushButton("Button 2")
btn2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

layout.addWidget(btn1)
layout.addWidget(btn2)

layout.setStretchFactor(btn1, 2)  # 设置第一个按钮的拉伸因子为 2
layout.setStretchFactor(btn2, 1)  # 设置第二个按钮的拉伸因子为 1

window.setLayout(layout)
window.show()
app.exec_()
