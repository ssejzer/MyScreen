import tkinter as tk
from PIL import Image, ImageTk
import mss
import sys

def update_screen(monitor_id):
    with mss.mss() as sct:
        # Capture the screen of the specific monitor
        screen_capture = sct.grab(sct.monitors[monitor_id])

    # Keep the original size, if changed
    if not hasattr(screen_label, 'x') or hasattr(screen_label, 'y') or (screen_label.x != screen_capture.width) or (screen_label.y != screen_capture.height):
        screen_label.x = screen_capture.width
        screen_label.y = screen_capture.height
        root.minsize(screen_label.x, screen_label.y)
        root.maxsize(screen_label.x, screen_label.y)
        root.geometry( str(screen_label.x) + "x" + str(screen_label.y) + "+0+" + str(screen_label.y))

    # Convert the screen capture to a PIL Image
    img = Image.frombytes("RGB", (screen_capture.width, screen_capture.height), screen_capture.rgb)

    # Convert the image to a format Tkinter can display, and keep a reference to avoid garbage collection
    screen_label.image = ImageTk.PhotoImage(img)

    # Update the label to display the captured image
    screen_label.config(image=screen_label.image)

    # Repeat this function
    root.after(250, lambda: update_screen(monitor_id))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        monitor_id = int(sys.argv[1])
    elif len(sys.argv) < 2:
        monitor_id = 0
    else:
        print("Usage: python myscreen.py <monitorID>")
        print("")
        print("monitorID: 0 all screens")
        print("           1 first screen")
        print("           2 second screen")
        print("           n Nth screen")
        print("")
        sys.exit(1)

    # Create the main window
    root = tk.Tk()
    root.title(f"MyScreen")

    # Make the window full-screen
    #root.state('iconic')  # Start the window minimized

    # Create a label to hold the screen capture
    screen_label = tk.Label(root)
    screen_label.pack(fill="both", expand=True)

    # Start the screen capture update loop for the specified monitor
    update_screen(monitor_id)

    # Run the Tkinter event loop
    root.mainloop()
