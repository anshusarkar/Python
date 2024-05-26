from pynput import mouse
import time

def get_mouse_position():
    # Function to get the current mouse position
    with mouse.Controller() as controller:
        while True:
            x, y = controller.position
            print(f"X: {x}, Y: {y}")
            time.sleep(1)

# Run the function to print the mouse position every second
get_mouse_position()
