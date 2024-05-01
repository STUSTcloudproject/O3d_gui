from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QMessageBox, QLineEdit, QComboBox
from PyQt5.QtGui import QFont
import os

class ConfirmationDialog(QDialog):
    """Dialog to confirm settings and check RealSense device configurations."""

    def __init__(self, parent, options, mode, enable_realsense_check=False, callback=None):
        super().__init__(parent)
        self.setWindowTitle("Confirm Selection")
        self.layout = QVBoxLayout()
        self.options = options
        self.mode = mode
        self.enable_realsense_check = enable_realsense_check
        self.callback = callback
        self.output_path = ""
        self.selected_resolution = ""
        self.init_ui()

    def init_ui(self):
        """Initializes the user interface components."""
        font = QFont('Arial', 12)
        self.add_label(f"Mode: {self.mode}", font)
        self.add_label("You have selected the following options:", font)

        for title, checkbox_dict in self.options.items():
            for option, is_checked in checkbox_dict.items():
                self.add_label(f"{option} : {is_checked}", font)

        self.setup_path_input(font)
        self.setup_realsense_check(font)
        self.setup_confirm_button(font)
        self.setLayout(self.layout)

    def add_label(self, text, font):
        """Adds a label to the layout."""
        label = QLabel(text)
        label.setFont(font)
        self.layout.addWidget(label)

    def setup_path_input(self, font):
        """Sets up the path input field and confirm path button."""
        self.folder_input = QLineEdit()
        self.folder_input.setPlaceholderText("Enter folder path here")
        self.folder_input.setFont(font)
        self.layout.addWidget(self.folder_input)

        self.folder_label = QLabel("No folder selected")
        self.folder_label.setFont(font)
        self.layout.addWidget(self.folder_label)

        path_confirm_button = QPushButton("Confirm Folder Path", clicked=self.confirm_output_folder)
        path_confirm_button.setFont(font)
        self.layout.addWidget(path_confirm_button)

    def setup_realsense_check(self, font):
        """Sets up the RealSense check button and profile dropdown if enabled."""
        if self.enable_realsense_check:
            realsense_button = QPushButton("Check RealSense Availability", clicked=self.check_realsense)
            realsense_button.setFont(font)
            self.layout.addWidget(realsense_button)

            self.realsense_check_label = QLabel("")
            self.realsense_check_label.setFont(font)
            self.layout.addWidget(self.realsense_check_label)

            self.profile_combo = QComboBox()
            self.profile_combo.setFont(font)
            self.layout.addWidget(self.profile_combo)

    def setup_confirm_button(self, font):
        """Sets up the confirm button."""
        self.confirm_button = QPushButton("Confirm", clicked=self.on_confirm)
        self.confirm_button.setFont(font)
        self.confirm_button.setEnabled(False)
        self.layout.addWidget(self.confirm_button)

    def confirm_output_folder(self):
        """Validates the manually entered output folder path."""
        folder_path = self.folder_input.text()
        if os.path.isdir(folder_path):
            self.output_path = folder_path
            self.folder_label.setText(f"Selected folder: {self.output_path}")
            
            if self.enable_realsense_check:
                self.confirm_button.setEnabled(self.profile_combo.currentIndex() != -1)
            else:
                self.confirm_button.setEnabled(True)
        else:
            QMessageBox.warning(self, "Path Invalid", "The specified folder path is not valid. Please enter a correct path.")
            self.folder_label.setText("No folder selected")
            self.confirm_button.setEnabled(False)

    def check_realsense(self):
        """Checks RealSense configurations and updates the profile dropdown."""
        color_profiles, depth_profiles = self.callback(mode='realsense_helper')
        if not color_profiles or not depth_profiles:
            self.realsense_check_label.setText("RealSense check failed.")
            self.profile_combo.clear()
            self.confirm_button.setEnabled(False)
        else:
            self.update_profile_combobox(color_profiles, depth_profiles)

    def update_profile_combobox(self, color_profiles, depth_profiles):
        """Updates the profile combobox with matching profiles."""
        matched_profiles = [
            profile for profile in depth_profiles
            if any(profile[:3] == cp[:3] for cp in color_profiles)
        ]
        if matched_profiles:
            self.profile_combo.clear()
            for profile in matched_profiles:
                display_text = f"{profile[0]}x{profile[1]} at {profile[2]} FPS"
                self.profile_combo.addItem(display_text)
            self.realsense_check_label.setText("RealSense check successful.")
            self.confirm_button.setEnabled(True if self.output_path else False)
        else:
            self.realsense_check_label.setText("No matching profiles found.")
            self.profile_combo.clear()
            self.confirm_button.setEnabled(False)

    def on_confirm(self):
        """Handles the confirm button click to close the dialog."""
        if not self.output_path:
            QMessageBox.warning(self, "Selection Required", "Please select or confirm a valid output folder before confirming.")
        else:
            self.selected_resolution = self.profile_combo.currentText() if self.enable_realsense_check else ""
            self.accept()
