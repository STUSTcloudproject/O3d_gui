import open3d.visualization.gui as gui

def main():
    app = gui.Application.instance
    app.initialize()

    window = app.create_window("Open3D GUI Layout Example", 800, 600)

    # 右侧的主垂直布局，用于容纳三个子水平布局
    right_layout = gui.Vert()

    # 创建三个子水平布局，每个布局中有一个居中的按钮
    for i in range(1, 4):
        horiz_layout = gui.Horiz()
        horiz_layout.add_stretch()  # 在按钮前添加弹性空间
        button = gui.Button(f"Button {i}")
        horiz_layout.add_child(button)  # 添加按钮
        horiz_layout.add_stretch()  # 在按钮后添加弹性空间
        right_layout.add_child(horiz_layout)  # 将此水平布局添加到右侧的垂直布局中

    window.add_child(right_layout)  # 将右侧布局添加到窗口中
    app.run()

if __name__ == "__main__":
    main()
