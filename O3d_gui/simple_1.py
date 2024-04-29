import open3d.visualization.gui as gui

def main():
    # 初始化應用和窗口
    app = gui.Application.instance
    app.initialize()
    
    # 創建一個窗口
    window = app.create_window("Simple GUI Example", 400, 150)
    
    # 創建水平布局
    layout = gui.Horiz()
    
    # 創建標籤
    label = gui.Label("Please click on the button")
    
    # 創建按鈕 1
    btn_press = gui.Button("Press me")
    def on_press():
        label.text = "pressed"
    btn_press.set_on_clicked(on_press)
    
    # 創建按鈕 2
    btn_clear = gui.Button("clear")
    def on_clear():
        label.text = "Please click on the button"
    btn_clear.set_on_clicked(on_clear)
    
    # 將元件加入布局
    layout.add_child(btn_press)
    layout.add_child(btn_clear)
    layout.add_child(label)
    
    # 將布局加入窗口
    window.add_child(layout)
    
    # 運行應用
    app.run()

# 確保當此腳本作為主程式運行時才執行 main 函數
if __name__ == "__main__":
    main()
