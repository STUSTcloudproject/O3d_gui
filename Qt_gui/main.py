import pythoncom
import win32api
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
import configparser
from gui import Qt_gui
from subprocess_run import PythonScriptExecutor
from realsense_helper import get_profiles

def my_callback_function(mode, options_dict=None, path=None , width=640, height=480, fps=30):
    print(f'Callback function has been called!')
    if mode == 'run_script':
        script_name, args = get_command_line(options_dict)
        if script_name == 'realsense_recorder.py':
            args += ['--output_folder', path, '--width', str(width), '--height', str(height), '--fps', str(fps)]
            stdout, stderr = run_script(script_name, args)
            #print("STDOUT:", stdout)
            if stderr:
                ex.show_error('error_callback', stderr)
            #print("STDERR:", stderr)
        elif script_name == 'vis_gui.py':
            print("Run vis_gui.py")
            stdout, stderr = run_script(script_name, [])
        else:
            print("Error: No valid script or arguments found.")
    elif mode == 'realsense_helper' :
        try:
            color_profiles, depth_profiles = get_profiles()
        except Exception as e:
            print(f"An error occurred: {e}")
            return None, None
        #print(f'Color profiles: {color_profiles}')
        #print(f'Depth profiles: {depth_profiles}')
        return color_profiles, depth_profiles

def get_command_line(options_dict):
    print(f'Options dict: {options_dict}')
    if config['Mode']['mode1'] in options_dict:
        # 生成由命令行标志组成的列表
        args = [f'--{key}' for key, value in options_dict['Recorder Mode'].items() if value]
        return 'realsense_recorder.py', args
    elif config['Mode']['mode2'] in options_dict:
        return None, []
    elif config['Mode']['mode3'] in options_dict:
        return 'vis_gui.py', []
    return None, []

def run_script(script_name, args):
    print(f'Run {script_name} {args}')
    executor = PythonScriptExecutor()  # 确保executor在这个作用域中有效
    stdout, stderr = executor.run_script(script_name, args)
    return stdout, stderr

if __name__ == "__main__":
    try:
        config = configparser.ConfigParser()
        config.read('config.ini') 
        pythoncom.CoInitializeEx(pythoncom.COINIT_APARTMENTTHREADED)
        app = QApplication([])
        executor = PythonScriptExecutor()
        ex = Qt_gui(config=config, callback=my_callback_function)
        ex.show()
        app.exec_()
    finally:
        pythoncom.CoUninitialize()

# Run ['python', 'realsense_recorder.py', '--record_imgs', '--output_folder', 'E:\\O3d_gui\\Qt_gui\\imgs']
# Run ['python', 'realsense_recorder.py', '--record_imgs', '--output_folder', 'E:/O3d_gui/Qt_gui/imgs']