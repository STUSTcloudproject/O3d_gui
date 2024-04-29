import open3d.visualization.gui as gui

def main():
    app = gui.Application.instance
    app.initialize()

    window = app.create_window("Open3D GUI Layout Example", 800, 600)

    em = window.theme.font_size
    spacing = int(round(0.5 * em))  # Based on font size
    
    # 主水平布局，將視窗分成左右兩側
    main_layout = gui.Horiz()

    # 左側的垂直布局
    left_layout = gui.Vert()
    left_upper = gui.Vert()  # 左上區塊
    left_lower = gui.Vert()  # 左下區塊

    # 右側的垂直布局
    right_layout = gui.Vert()

    # 添加左上的大標籤和小標籤
    title_label = gui.Label("Open3d GUI")
    intro_label = gui.Label("This is an example of using the Open3d GUI.")
    
    # 左上區塊添加標籤和彈性空間
    left_upper.add_child(title_label)
    left_upper.add_child(intro_label)
    left_upper.add_stretch()

    # 左下區塊的選項
    for i in range(1, 6):
        left_lower.add_child(gui.Checkbox(f"option{i}"))
    left_lower.add_stretch()  # Adds more space at the bottom
    
    # 右側區塊的按鈕
    for i in range(1, 4):
        right_layout.add_fixed(spacing)
        right_layout.add_child(gui.Button(f"Button {i}"))
        right_layout.add_fixed(spacing)  # Space between buttons
    right_layout.add_stretch()

    # 將左上和左下區塊加入左側布局
    left_layout.add_child(left_upper)
    left_layout.add_stretch()  # Less space for upper
    left_layout.add_child(left_lower)
    left_layout.add_stretch()  # More space for lower

    # 將左右布局加入主布局
    main_layout.add_child(left_layout)
    main_layout.add_stretch()  # Left side
    main_layout.add_child(right_layout)
    main_layout.add_stretch()  # Right side

    # 將主布局加入窗口
    window.add_child(main_layout)
    
    # 運行應用
    app.run()

if __name__ == "__main__":
    main()
