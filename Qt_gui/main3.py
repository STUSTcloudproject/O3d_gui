from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox, QSizePolicy
from PyQt5.QtCore import Qt

class ExampleGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.num_buttons = 3
        self.checkbox_row = 5
        self.checkbox_column = 2 
        self.buttons = []
        self.checkbox_options = []
        self.initUI()
    
    def initUI(self):
        # Main layout
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # Left layout setup
        left_layout = self.create_left_layout()
        main_layout.addLayout(left_layout, 5)

        # Right layout setup
          # To store button references for dynamic font resizing
        right_layout = self.create_right_layout()
        main_layout.addLayout(right_layout, 5)

        # Set window properties
        self.setWindowTitle('GUI Example')
        self.setGeometry(300, 300, 1500, 800)

    def create_left_layout(self):
        """Create the left layout with labels and a checkbox."""
        left_layout = QVBoxLayout()

        # Top part with labels
        top_labels_layout = self.create_top_labels_layout()
        left_layout.addLayout(top_labels_layout, 4)
        
        # Bottom part with checkbox
        bottom_checkbox_layout = self.create_bottom_checkbox_layout()
        left_layout.addLayout(bottom_checkbox_layout, 6)

        return left_layout

    def create_top_labels_layout(self):
        """Create the top part layout with labels."""
        top_labels_layout = QVBoxLayout()
        self.label_title = QLabel('Open3d GUI')
        self.label_title.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.label_description = QLabel('This is an example of using the Open3d GUI, a versatile tool designed to simplify the visualization, analysis, and processing of 3D data. With Open3d GUI, users can effortlessly interact with 3D models and point clouds, enjoying features such as real-time rendering, easy manipulation of objects through rotation, zooming, and panning.')
        self.label_description.setWordWrap(True)  # Enable word wrap
        self.label_description.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        top_labels_layout.addWidget(self.label_title, alignment=Qt.AlignCenter)
        top_labels_layout.addWidget(self.label_description, alignment=Qt.AlignCenter)
        return top_labels_layout

    def create_bottom_checkbox_layout(self):
        """Create the bottom part layout with a checkbox."""
        bottom_checkbox_layout = QHBoxLayout()
        
        checkbox1_layout = QVBoxLayout()
        checkbox2_layout = QVBoxLayout()
        bottom_layout = QVBoxLayout()
        
        bottom_checkbox_layout.addLayout(checkbox1_layout, 1)
        bottom_checkbox_layout.addLayout(checkbox2_layout, 1)
        bottom_checkbox_layout.addLayout(bottom_layout, 1)

        for i in range(1, self.checkbox_row + 1):
            checkbox1 = QCheckBox(f'Option {i}')
            checkbox2 = QCheckBox(f'Option {i + self.checkbox_row}')

            self.checkbox_options.append(checkbox1)
            self.checkbox_options.append(checkbox2)

            checkbox1_layout.addWidget(checkbox1, alignment=Qt.AlignCenter)
            checkbox2_layout.addWidget(checkbox2, alignment=Qt.AlignCenter)

        return bottom_checkbox_layout

    def create_right_layout(self):
        """Create the right layout with three buttons."""
        right_layout = QVBoxLayout()

        # Add buttons with spacing
        right_layout.addStretch(1)
        for i in range(1, self.num_buttons + 1):
            button_layout, button = self.create_button_layout(f'Button {i}')
            self.buttons.append(button)  # Store the button for later font resizing
            right_layout.addLayout(button_layout, 2)
            right_layout.addStretch(1)

        return right_layout

    def create_button_layout(self, button_text):
        """Helper function to create a button and its layout."""
        button = QPushButton(button_text)
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        
        button_layout = QHBoxLayout()
        button_layout.addStretch(2)
        button_layout.addWidget(button, 6)
        button_layout.addStretch(2)
        
        return button_layout, button

    def resizeEvent(self, event):
        """Resize the font size of labels and buttons based on the window size."""
        self.update_fonts()
        super().resizeEvent(event)

    def update_fonts(self):
        """Update font size based on window width, number of buttons, and text length."""
        width = self.width()
        font_size = max(width // 50, 8)  # Simple calculation for font size
        
        # Apply the calculated font size to labels and buttons
        #self.label_title.setStyleSheet(f"font-size: {font_size + 28}px;")
        self.label_description.setStyleSheet(f"font-size: {font_size - 4}px;")
        #self.checkbox_option1.setStyleSheet(f"font-size: {font_size}px;")
        for button in self.buttons:
            button.setStyleSheet(f"font-size: {font_size}px;")

# Application creation and main loop
if __name__ == "__main__":
    app = QApplication([])
    ex = ExampleGUI()
    ex.show()
    app.exec_()
