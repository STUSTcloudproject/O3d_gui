from PyQt5.QtWidgets import QMessageBox

class ErrorDialog(QMessageBox):
    def __init__(self, parent, error_code):
        super().__init__(parent)
        self.setWindowTitle("Validation Error")
        self.setIcon(QMessageBox.Warning)
        self.setStandardButtons(QMessageBox.Ok)
        self.set_error_message(error_code)
        self.exec_()  # 顯示為模態對話框

    def set_error_message(self, error_code):
        if error_code == 'error0':
            message = 'No item is selected.'
        else:
            message = 'More than one item is selected.'
        self.setText(message)
