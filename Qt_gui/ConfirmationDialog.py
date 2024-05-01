from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QMessageBox, QFileDialog

class ConfirmationDialog(QDialog):
    def __init__(self, parent, options, output_path):
        super().__init__(parent)
        self.setWindowTitle("Confirm Selection")
        self.layout = QVBoxLayout()
        self.options = options
        self.output_path = output_path
        self.folder_label = QLabel("No folder selected")
        self.init_ui()

    def init_ui(self):
        label = QLabel("You have selected the following options:")
        self.layout.addWidget(label)

        for title, checkbox_dict in self.options.items():
            for option, is_checked in checkbox_dict.items():
                if is_checked:
                    option_label = QLabel(f"{title}: {option}")
                    self.layout.addWidget(option_label)

        path_selector = QPushButton("Choose output folder")
        path_selector.clicked.connect(self.choose_output_folder)
        self.layout.addWidget(path_selector)
        self.layout.addWidget(self.folder_label)

        confirm_button = QPushButton("Confirm")
        confirm_button.clicked.connect(self.on_confirm)
        self.layout.addWidget(confirm_button)

        self.setLayout(self.layout)

    def choose_output_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.output_path = folder_path
            self.folder_label.setText(f"Selected folder: {self.output_path}")
        else:
            self.folder_label.setText("No folder selected")

    def on_confirm(self):
        if not self.output_path:
            QMessageBox.warning(self, "Selection Required", "Please select an output folder before confirming.")
        else:
            self.accept()
