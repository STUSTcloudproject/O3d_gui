import open3d.visualization.gui as gui

def main():
    app = gui.Application.instance
    app.initialize()

    # 创建一个窗口，标题为"Centered Button Layout"，大小为800x600像素
    window = app.create_window("Centered Button Layout", 800, 600)

    # 主垂直布局，用于管理按钮的垂直居中
    main_layout = gui.Horiz()

    # 在按钮前添加弹性空间，以推动按钮到中心
    main_layout.add_stretch()

    # 水平布局，用于管理按钮的水平居中
    Vert_layout = gui.Vert()
    Vert_layout.add_stretch()  # 按钮前的弹性空间，用于水平居中
    button = gui.Button("Button1")  # 我们想要居中的按钮
    Vert_layout.add_child(button)
    Vert_layout.add_stretch()  # 按钮后的弹性空间，保持水平居中
    button = gui.Button("Button2")  # 我们想要居中的按钮
    Vert_layout.add_child(button)
    Vert_layout.add_stretch()  # 按钮后的弹性空间，保持水平居中
    button = gui.Button("Button3")  # 我们想要居中的按钮
    Vert_layout.add_child(button)
    Vert_layout.add_stretch()  # 按钮后的弹性空间，保持水平居中

    # 将水平居中的布局添加到主垂直布局中
    main_layout.add_child(Vert_layout)

    # 在按钮后再添加弹性空间，保持垂直居中
    main_layout.add_stretch()
    windows1_layout = gui.Horiz()
    #windows1_layout.add_stretch()
    windows1_layout.add_child(main_layout)
    
    # 将主布局添加到窗口中
    window.add_child(windows1_layout)
    
    # 运行应用
    app.run()

if __name__ == "__main__":
    main()
