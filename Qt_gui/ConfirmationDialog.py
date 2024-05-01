from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QMessageBox, QFileDialog
from PyQt5.QtGui import QFont

class ConfirmationDialog(QDialog):
    def __init__(self, parent, options, output_path, mode, enable_realsense_check=False, callback=None):
        super().__init__(parent)
        self.setWindowTitle("Confirm Selection")
        self.layout = QVBoxLayout()
        self.options = options
        self.output_path = output_path
        self.mode = mode
        self.enable_realsense_check = enable_realsense_check
        self.callback = callback
        self.folder_label = QLabel("No folder selected")
        self.realsense_check_label = QLabel("")  # Label for showing realsense check result
        self.init_ui()
        self.realsense_check_passed = False  # Status flag for realsense check

    def init_ui(self):
        self.resize(600, 400)
        font = QFont('Arial', 12)

        mode_label = QLabel(f"Mode: {self.mode}")
        mode_label.setFont(font)
        self.layout.addWidget(mode_label)

        label = QLabel("You have selected the following options:")
        label.setFont(font)
        self.layout.addWidget(label)

        for title, checkbox_dict in self.options.items():
            for option, is_checked in checkbox_dict.items():
                if is_checked:
                    option_label = QLabel(f"{option} : {is_checked}")
                    option_label.setFont(font)
                    self.layout.addWidget(option_label)

        path_selector = QPushButton("Choose output folder")
        path_selector.setFont(font)
        path_selector.clicked.connect(self.choose_output_folder)
        self.layout.addWidget(path_selector)
        self.folder_label.setFont(font)
        self.layout.addWidget(self.folder_label)

        if self.enable_realsense_check:
            realsense_button = QPushButton("Check RealSense Availability")
            realsense_button.setFont(font)
            realsense_button.clicked.connect(self.check_realsense)
            self.layout.addWidget(realsense_button)
            self.realsense_check_label.setFont(font)
            self.layout.addWidget(self.realsense_check_label)

        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.setFont(font)
        self.confirm_button.clicked.connect(self.on_confirm)
        self.confirm_button.setEnabled(False)  # Initially disabled
        self.layout.addWidget(self.confirm_button)

        self.setLayout(self.layout)

    def choose_output_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.output_path = folder_path
            self.folder_label.setText(f"Selected folder: {self.output_path}")
            if self.realsense_check_passed or not self.enable_realsense_check:
                self.confirm_button.setEnabled(True)

    def check_realsense(self):
        color_profiles, depth_profiles = self.callback(mode='realsense_helper')
        if color_profiles is None or not color_profiles or depth_profiles is None or not depth_profiles:
            self.realsense_check_label.setText("RealSense check failed.")
            self.confirm_button.setEnabled(False)
        else:
            self.realsense_check_label.setText("RealSense check successful.")
            self.realsense_check_passed = True
            if self.output_path:
                self.confirm_button.setEnabled(True)

    def on_confirm(self):
        if not self.output_path:
            QMessageBox.warning(self, "Selection Required", "Please select an output folder before confirming.")
        else:
            self.accept()
