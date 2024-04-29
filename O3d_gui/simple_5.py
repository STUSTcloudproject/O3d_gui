import open3d.visualization.gui as gui

def main():
    app = gui.Application.instance
    app.initialize()

    # Create a window
    window = app.create_window("Preferred Size Example", 640, 480)
    
    # Create a button
    button = gui.Button("Click Me")

    # Create a callback to calculate and print the preferred size
    def on_window_draw(window):
        layout_context = window.theme
        size = button.calc_preferred_size(layout_context, gui.Widget.Constraints())
        print(f"Preferred size of the button: {size.width} x {size.height}")
    
    # Set the callback to be called whenever the window needs to be redrawn
    window.set_on_draw(on_window_draw)

    # Add the button to the window
    window.add_child(button)
    
    # Run the application
    app.run()

if __name__ == "__main__":
    main()
