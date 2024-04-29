from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QCheckBox, QApplication, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from functools import partial

class ExampleGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.num_buttons = 3
        self.checkbox_row = 5
        self.checkbox_column = 2
        self.buttons = []
        self.checkbox_options = []
        self.VerButton = None
        self.label_title = None
        self.label_description = None
        self.main_layout = None
        self.left_container = None
        self.right_container = None
        self.initUI()
    
    def initUI(self):
        # Main layout
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        title = 'Open3d GUI'
        description = 'This is an example of using the Open3d GUI, a versatile tool designed to simplify the visualization, analysis, and processing of 3D data. With Open3d GUI, users can effortlessly interact with 3D models and point clouds, enjoying features such as real-time rendering, easy manipulation of objects through rotation, zooming, and panning.'

        # Left layout setup
        left_container = self.create_container(self.create_left_layout(title, description, self.checkbox_column, self.checkbox_row), color="#FFA07A")
        right_container = self.create_container(self.create_right_layout(), color="#F08080")

        main_layout.addWidget(left_container, 5)
        main_layout.addWidget(right_container, 5)

        self.main_layout = main_layout
        self.left_container = left_container
        self.right_container = right_container

        # Set window properties
        self.setWindowTitle('O3d GUI')
        self.setGeometry(300, 300, 1500, 800)

        self.adjust_font_size()

    def create_left_layout(self, title, description, checkbox_column, checkbox_row):
        """Create the left layout with labels and a checkbox."""
        left_layout = QVBoxLayout()

        upper_container = self.create_container(self.create_upper_layout(title, description), color="#E0FFFF")
        lower_container = self.create_container(self.create_lower_layout(checkbox_column, checkbox_row), color="#FFFFE0")

        left_layout.addWidget(upper_container, 4)  # 4 parts of space
        left_layout.addWidget(lower_container, 6)

        self.upper_container = upper_container
        self.lower_container = lower_container

        return left_layout

    def create_upper_layout(self, title, description):
        upper_layout = QVBoxLayout()

        label_title_layout = QVBoxLayout()
        label_title = QLabel(title)
        label_title_layout.addWidget(label_title, alignment=Qt.AlignCenter)
        label_title_container = self.create_container(label_title_layout, color="#90EE90")

        description_layout = QVBoxLayout()
        label_description = QLabel(description)
        label_description.setWordWrap(True)
        description_layout.addWidget(label_description, alignment=Qt.AlignCenter)
        description_container = self.create_container(description_layout, color="#AFEEEE")
        
        upper_layout.addWidget(label_title_container, 4)
        upper_layout.addWidget(description_container, 6)

        self.label_title = label_title
        self.label_description = label_description

        return upper_layout

    def create_lower_layout(self, checkbox_column, checkbox_row):
        lower_layout = QHBoxLayout()

        # Create layouts using a dictionary for dynamic assignment
        checkbox_layouts = {i: QVBoxLayout() for i in range(1, checkbox_column + 1)}
        button_layout = QVBoxLayout()

        for i in range(1, checkbox_row + 1):
            for j in range(1, checkbox_column + 1):
                checkbox = QCheckBox(f'Option {i + (j-1)* checkbox_row}')
                self.checkbox_options.append(checkbox)
                layout = QHBoxLayout()
                layout.addWidget(checkbox)
                checkbox_layouts[j].addWidget(self.create_container(layout, color="#DCDCDC"), 1)
        
        for i in range(1, 4):
            layout = QVBoxLayout()
            if i == 2:
                Verbutton = QPushButton('Verify')
                self.VerButton = Verbutton
                Verbutton.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
                layout.addWidget(Verbutton)
            button_layout.addWidget(self.create_container(layout, color="#FFD700" if i == 2 else "#A4C639"), 1)

        # Add checkbox layouts to the lower layout
        for layout in checkbox_layouts.values():
            lower_layout.addWidget(self.create_container(layout), 1)
        lower_layout.addWidget(self.create_container(button_layout), 1)

        return lower_layout

    def create_right_layout(self):
        right_layout = QVBoxLayout()
        # Adding spacer widgets and button containers dynamically
        for i in range(self.num_buttons * 2 + 1):
            if i % 2 == 1:
                button_layout = self.create_button_layout(f'Button {i//2 + 1}')
                button_container = self.create_container(button_layout, color="lightblue")
                right_layout.addWidget(button_container, 2)
            else:
                right_layout.addWidget(self.create_container(QVBoxLayout(), color="gray"), 1)

        return right_layout

    def create_button_layout(self, text):
        button_layout = QHBoxLayout()
        button = QPushButton(text)
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.buttons.append(button)
        button_layout.addStretch(1)
        button_layout.addWidget(button, 3)
        button_layout.addStretch(1)

        button.clicked.connect(partial(self.button_clicked, text))

        return button_layout

    def button_clicked(self, button_text):
        self.checkbox_options = []
        if button_text == "Button 1":
            self.update_left_layout(button_text, f'This is {button_text}', 2, 1)
        if button_text == "Button 2":
            self.update_left_layout(button_text, f'This is {button_text}', 2, 2)
        if button_text == "Button 3":
            self.update_left_layout(button_text, f'This is {button_text}', 2, 3)
        self.adjust_font_size()

    def update_left_layout(self, title, description, checkbox_column, checkbox_row):
        # 创建新的左侧容器
        new_left_container = self.create_container(self.create_left_layout(title, description, checkbox_column, checkbox_row), color="#FFA07A")
        
        # 替换旧的左侧容器，保持布局比例
        index = self.main_layout.indexOf(self.left_container)
        self.main_layout.insertWidget(index, new_left_container, 5)  # 在原位置插入新容器，设置比例为5

        # 安全地移除旧容器
        if self.left_container:
            self.left_container.setParent(None)
            self.left_container.deleteLater()  # 请求Qt删除旧容器对象

        # 更新引用到新的容器
        self.left_container = new_left_container

        # 刷新主布局，确保更新反映到UI
        self.main_layout.update()

    def create_container(self, layout, color=None):
        #color=None
        container = QWidget()
        container.setLayout(layout)
        container.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        if color:
            container.setStyleSheet(f"background-color: {color};")
        return container

    def resizeEvent(self, event):
        self.adjust_font_size()

    def configure_fonts(self):
        base_font_size = max(8, min(self.width(), self.height()) // 100)
        return {
            "title": QFont("Arial", int(base_font_size * 4)),
            "description": QFont("Arial", int(base_font_size * 1.0)),
            "buttons": QFont("Arial", int(base_font_size * 3.0)),
            "VerButton": QFont("Arial", int(base_font_size * 2.5)),
            "checkboxes": QFont("Arial", int(base_font_size * 1.8))
        }

    def adjust_font_size(self):
        fonts = self.configure_fonts()
        self.apply_font(self.label_title, fonts["title"])
        self.apply_font(self.label_description, fonts["description"])
        self.apply_font(self.VerButton, fonts["VerButton"])
        for button in self.buttons:
            self.apply_font(button, fonts["buttons"])
        for checkbox in self.checkbox_options:
            self.apply_font(checkbox, fonts["checkboxes"])


    def apply_font(self, widget, font):
        if widget is not None:
            widget.setFont(font)
        else:
            print("Warning: Attempted to set font on a widget that has not been created.")

if __name__ == "__main__":
    app = QApplication([])
    ex = ExampleGUI()
    ex.show()
    app.exec_()
