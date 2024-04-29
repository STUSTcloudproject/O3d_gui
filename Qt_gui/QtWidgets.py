from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QApplication, QSizePolicy

class ExampleGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Main layout
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # Left layout setup
        left_layout = self.create_left_layout()
        main_layout.addLayout(left_layout, 5)

        # Set window properties
        self.setWindowTitle('GUI Example')
        self.setGeometry(300, 300, 1500, 800)

    def create_left_layout(self):
        """Create the left layout with labels and a checkbox."""
        left_layout = QVBoxLayout()

        # Top part with labels
        top_labels_layout = QVBoxLayout()
        label_title = QLabel('Open3d GUI')
        label_description = QLabel('Description goes here.')
        label_description.setWordWrap(True)
        
        # Add labels to the top layout
        top_labels_layout.addWidget(label_title)
        top_labels_layout.addWidget(label_description)

        # Bottom part with checkbox
        bottom_checkbox_layout = QVBoxLayout()
        checkbox = QCheckBox('Option 1')
        
        # Add checkbox to the bottom layout
        bottom_checkbox_layout.addWidget(checkbox)

        # Container for top labels layout
        top_container = QWidget()
        top_container.setLayout(top_labels_layout)
        top_container.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        # Container for bottom checkboxes layout
        bottom_container = QWidget()
        bottom_container.setLayout(bottom_checkbox_layout)
        bottom_container.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        # Add containers to the left layout with stretch factors
        left_layout.addWidget(top_container, 4)  # 4 parts of space
        left_layout.addWidget(bottom_container, 6)  # 6 parts of space

        return left_layout

# Application creation and main loop
if __name__ == "__main__":
    app = QApplication([])
    ex = ExampleGUI()
    ex.show()
    app.exec_()
