from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
import configparser
from gui import Qt_gui
from subprocess_run import PythonScriptExecutor

def get_command_line(options_dict):
    if 'Recorder' in options_dict:
        # 生成由命令行标志组成的列表
        args = [f'--{key}' for key, value in options_dict['Recorder'].items() if value]
        return 'realsense_recorder.py', args
    return None, []

def my_callback_function(options_dict, path):
    print(f'Callback function has been called!', options_dict, path)
    script_name, args = get_command_line(options_dict)
    if script_name:
        args += ['--output_folder', path]
        stdout, stderr = run_script(script_name, args)
        print("STDOUT:", stdout)
        print("STDERR:", stderr)
    else:
        print("Error: No valid script or arguments found.")

def run_script(script_name, args):
    executor = PythonScriptExecutor()  # 确保executor在这个作用域中有效
    stdout, stderr = executor.run_script(script_name, args)
    return stdout, stderr

if __name__ == "__main__":
    app = QApplication([])
    executor = PythonScriptExecutor()
    ex = Qt_gui(callback=my_callback_function)
    ex.show()
    app.exec_()

# Run ['python', 'realsense_recorder.py', '--record_imgs', '--output_folder', 'E:\\O3d_gui\\Qt_gui\\imgs']
# Run ['python', 'realsense_recorder.py', '--record_imgs', '--output_folder', 'E:/O3d_gui/Qt_gui/imgs']