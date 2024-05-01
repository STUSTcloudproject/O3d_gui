# -*- coding: utf-8 -*-

block_cipher = None

added_files = [
    ('ConfirmationDialog.py', '.'),  # 副程式 1 的檔案路徑
    ('ErrorDialog.py', '.'),  # 副程式 2 的檔案路徑
    ('gui.py', '.'),  # 副程式 3 的檔案路徑
    ('realsense_helper.py', '.'),  # 副程式 4 的檔案路徑
    ('realsense_recorder.py', '.'), 
    ('subprocess_run.py', '.'),
    ('tool.py', '.'),
    ('vis_gui.py', '.'),
    ('config.ini', '.'),
]

a = Analysis(['main.py'],  # 主程式的檔案名稱
             pathex=[],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='my_program',  # 可執行檔案的名稱
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True)  # 添加逗號並設置 onefile=True
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='my_program')  # 打包後的資料夾名稱
