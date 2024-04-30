from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QCheckBox, QApplication, QSizePolicy, QMessageBox, QDialog, QFileDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from functools import partial
import configparser

class Qt_gui(QWidget):
    def __init__(self, callback=None):
        super().__init__()
        self.config = configparser.ConfigParser()
        self.config.read('config.ini') 
        self.callback = callback
        self.buttons = []
        self.checkbox_options = []
        self.VerButton = None
        self.label_title = None
        self.label_description = None
        self.main_layout = None
        self.left_container = None
        self.right_container = None
        self.output_path = None
        self.initUI()

    def verify(self):
        if self.callback:

            # 處理 label_title 和 self.checkbox_options 是否合法並分配字串給字典
            # 如果合法調用 callback 函數
            # 如果不合法彈出顯示框

            dict_checkbox = {checkbox.text(): checkbox.isChecked() for checkbox in self.checkbox_options}
            dict_checkbox = {self.label_title.text() : dict_checkbox}

            #print(dict_checkbox)   
            error = self.validate_params(dict_checkbox)
            if error != 'pass':
                self.show_error_dialog(error)
            else:
                output_path = self.show_confirmation_dialog(dict_checkbox)
                if output_path:
                    self.callback(dict_checkbox, output_path)  # 在此處調用callback，只有在用戶確認後

    def show_confirmation_dialog(self, options):
        dialog = QDialog(self)
        dialog.setWindowTitle("Confirm Selection")
        layout = QVBoxLayout()

        label = QLabel("You have selected the following options:")
        layout.addWidget(label)

        for title, checkbox_dict in options.items():
            for option, is_checked in checkbox_dict.items():
                if is_checked:
                    option_label = QLabel(f"{title}: {option}")
                    layout.addWidget(option_label)

        path_selector = QPushButton("Choose output folder")
        if self.output_path:
            self.folder_label.setText(f"Selected folder: {self.output_path}")
        else:
            self.folder_label = QLabel("No folder selected")
        path_selector.clicked.connect(self.choose_output_folder)
        layout.addWidget(path_selector)
        layout.addWidget(self.folder_label)

        confirm_button = QPushButton("Confirm")
        confirm_button.clicked.connect(lambda: self.on_confirm(dialog))
        layout.addWidget(confirm_button)

        dialog.setLayout(layout)
        result = dialog.exec_()

        if result == QDialog.Accepted:
            return self.output_path
        else:
            return None

    def on_confirm(self, dialog):
        if not self.output_path:
            QMessageBox.warning(self, "Selection Required", "Please select an output folder before confirming.")
        else:
            dialog.accept()

    def choose_output_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:  # 確保用戶選擇了一個路徑
            self.output_path = folder_path  # 儲存用戶選擇的路徑
            self.folder_label.setText(f"Selected folder: {folder_path}")  # 更新標籤以顯示路徑
        else:
            self.folder_label.setText("No folder selected")  # 如果沒有選擇，顯示未選擇

    def validate_params(self, dict):
        keys = list(dict.keys())  # 将字典键转换为列表
        option_dict = dict[keys[0]]
        if keys[0] == 'Recorder':
            true_count = sum(value for value in option_dict.values() if value)
            if true_count != 1:
                return f'error{true_count}'
        if keys[0] == 'Run_system':
            true_count = sum(value for value in option_dict.values() if value)
            if true_count == 0:
                return f'error{true_count}'
        if keys[0] == 'View':
            pass
        return 'pass'

    def show_error_dialog(self, error):
        message = ''
        if error == 'error0':
            message = 'No item is selected.'
        else:
            message = 'More than one item is selected.'
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Validation Error")
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()  # 显示为模态对话框

    def initUI(self):
        # Main layout
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)
        # Left layout setup
        left_container = self.create_container(self.create_left_layout('Init', True), color="#FFA07A")
        right_container = self.create_container(self.create_right_layout(), color="#F08080")

        main_layout.addWidget(left_container, 5)
        main_layout.addWidget(right_container, 5)

        self.main_layout = main_layout
        self.left_container = left_container
        self.right_container = right_container

        # Set window properties
        self.setWindowTitle(self.config['Init']['window_title'])
        self.setGeometry(300, 300, 1500, 800)

        self.adjust_font_size()

    def create_left_layout(self, mode, is_init=False):
        """Create the left layout with labels and a checkbox."""
        left_layout = QVBoxLayout()

        upper_container = self.create_container(self.create_upper_layout(self.config[mode]['title'], self.config[mode]['description']), color="#E0FFFF")
        left_layout.addWidget(upper_container, 4)  # 4 parts of space  
        self.upper_container = upper_container
        
        if not is_init:
            lower_container = self.create_container(self.create_lower_layout(mode), color="#FFFFE0")
            left_layout.addWidget(lower_container, 6)
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

    def create_lower_layout(self, mode):
        lower_layout = QHBoxLayout()

        checkbox_row = int(self.config[mode]['checkbox_row'])
        checkbox_column = int(self.config[mode]['checkbox_column'])

        # Create layouts using a dictionary for dynamic assignment
        checkbox_layouts = {i: QVBoxLayout() for i in range(1, checkbox_column + 1)}
        button_layout = QVBoxLayout()

        for i in range(1, checkbox_row + 1):
            for j in range(1, checkbox_column + 1):
                checkbox = QCheckBox(self.config[mode][f'option{i + (j-1)* checkbox_row}'])
                self.checkbox_options.append(checkbox)
                layout = QHBoxLayout()
                layout.addWidget(checkbox)
                checkbox_layouts[j].addWidget(self.create_container(layout, color="#DCDCDC"), 1)
        
        for i in range(1, 4):
            layout = QVBoxLayout()
            if i == 2:
                Verbutton = QPushButton('Verify')
                self.VerButton = Verbutton
                Verbutton.clicked.connect(partial(self.verify))
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
        for i in range(len(self.config['Buttons']) * 2 + 1):
            if i % 2 == 1:
                button_text = self.config['Buttons'][f'button{(i // 2) + 1}']
                button_layout = self.create_button_layout(button_text)
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
        if button_text == self.config['Buttons']['button1']:
            self.update_left_layout('Recorder')
        if button_text == self.config['Buttons']['button2']:
            self.update_left_layout('Run_system')
        if button_text == self.config['Buttons']['button3']:
            self.update_left_layout('View')
        self.adjust_font_size()

    def update_left_layout(self, mode):
        # 创建新的左侧容器
        new_left_container = self.create_container(self.create_left_layout(mode), color="#FFA07A")
        
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
            "description": QFont("Arial", int(base_font_size * (2 if not self.VerButton else 1.5))),
            "buttons": QFont("Arial", int(base_font_size * 3.0)),
            "VerButton": QFont("Arial", int(base_font_size * 2.5)),
            "checkboxes": QFont("Arial", int(base_font_size * 1.8))
        }

    def adjust_font_size(self):
        fonts = self.configure_fonts()
        self.apply_font(self.label_title, fonts["title"])
        self.apply_font(self.label_description, fonts["description"])
        for button in self.buttons:
                self.apply_font(button, fonts["buttons"])
        if self.VerButton:
            self.apply_font(self.VerButton, fonts["VerButton"])
            
            for checkbox in self.checkbox_options:
                self.apply_font(checkbox, fonts["checkboxes"])


    def apply_font(self, widget, font):
        if widget is not None:
            widget.setFont(font)
        else:
            print("Warning: Attempted to set font on a widget that has not been created.")

if __name__ == "__main__":
    app = QApplication([])
    ex = Qt_gui()
    ex.show()
    app.exec_()
