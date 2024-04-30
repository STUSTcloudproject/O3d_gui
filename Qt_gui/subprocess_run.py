import subprocess

class PythonScriptExecutor:
    def __init__(self, interpreter='python'):
        """
        初始化 PythonScriptExecutor 實例。
        
        Args:
        interpreter (str): 用於執行 Python 腳本的解釋器。
        """
        self.interpreter = interpreter

    def run_script(self, script_path, args=[]):
        """
        執行指定的 Python 腳本與參數，並捕獲其輸出與錯誤。
        
        Args:
        script_path (str): 要執行的腳本的路徑。
        args (list): 傳遞給腳本的命令行參數列表。
        
        Returns:
        tuple: 包含腳本的 stdout 和 stderr 的元組。
        """
        try:
            # 構造完整命令
            command = [self.interpreter, script_path] + args
            # 執行命令並捕獲輸出
            print(f'Run {command}')
            result = subprocess.run(command, capture_output=True, input='y\n', text=True, check=True)
            return result.stdout, result.stderr
        except subprocess.CalledProcessError as e:
            return e.stdout, e.stderr
        except subprocess.TimeoutExpired as e:
            return e.stdout, e.stderr
        except Exception as e:
            return "", str(e)

# 示例使用
if __name__ == "__main__":
    # 创建 PythonScriptExecutor 实例
    executor = PythonScriptExecutor()

    # 设置脚本路径
    script_path = 'realsense_recorder.py'

    # 定义要传递给脚本的命令行参数
    args = ['--record_imgs', '--output_folder', 'E:/O3d_gui/Qt_gui/imgs']

    # 调用 run_script 方法执行脚本
    stdout, stderr = executor.run_script(script_path, args)

    # 打印执行结果
    if stderr:
        print("脚本执行错误，错误信息如下：")
        print(stderr)
    else:
        print("脚本执行成功，输出如下：")
        print(stdout)
