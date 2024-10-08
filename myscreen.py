import tkinter as tk
from PIL import Image, ImageTk
import mss
import sys

def update_screen(monitor_id):
    with mss.mss() as sct:
        # Capture the screen of the specific monitor
        monitor = sct.monitors[monitor_id]  # Get the specific monitor based on monitor_id
        screen_capture = sct.grab(monitor)

        # Convert the screen capture to a PIL Image
        img = Image.frombytes("RGB", (screen_capture.width, screen_capture.height), screen_capture.rgb)

        # Convert the image to a format Tkinter can display
        screen_image = ImageTk.PhotoImage(img)

        # Update the label to display the captured image
        screen_label.config(image=screen_image)
        screen_label.image = screen_image  # Keep a reference to avoid garbage collection

        # Repeat this function after a short delay (e.g., 200 milliseconds)
        root.after(200, lambda: update_screen(monitor_id))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python myscreen.py <monitorID>")
        sys.exit(1)

    monitor_id = int(sys.argv[1])

    # Create the main window
    root = tk.Tk()
    root.title(f"MyScreen")

    # Make the window full-screen
    #root.attributes('-fullscreen', True)
    root.state('iconic')  # Start the window minimized

    # Create a label to hold the screen capture
    screen_label = tk.Label(root)
    screen_label.pack(fill="both", expand=True)

    # Start the screen capture update loop for the specified monitor
    update_screen(monitor_id)

    # Run the Tkinter event loop
    root.mainloop()
