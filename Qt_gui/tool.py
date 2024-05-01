def parse_resolution(selected_resolution):
    # 假设 selected_resolution 的格式是 "1920x1080 at 30 FPS"
    parts = selected_resolution.split(' at ')  # 分割出 "1920x1080" 和 "30 FPS"
    resolution_part = parts[0]  # "1920x1080"
    fps_part = parts[1]  # "30 FPS"
    
    # 提取分辨率的宽度和高度
    width, height = resolution_part.split('x')
    width = int(width)  # 转换为整数
    height = int(height)  # 转换为整数
    
    # 提取帧率
    fps = int(fps_part.split(' ')[0])  # 分割 "30 FPS" 并转换第一部分为整数
    
    return width, height, fps