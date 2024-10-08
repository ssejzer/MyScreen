# MyScreen v1.00

This Python application captures and displays the real-time content of a specific monitor. You can specify the monitor to capture by passing a `monitorID` argument, and the application will display the live screen of that monitor in a minimized window using Tkinter.

## Features

- Capture and display real-time screen content from any connected monitor.
- Start the application window minimized to the taskbar.
- Supports multi-monitor setups by passing the desired monitor ID.

## Requirements

- Python **3.6** or higher
- External libraries:
  - **MSS**: for screen capturing
  - **Pillow (PIL)**: for image handling and display

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ssejzer/MyScreen.git
   cd MyScreen
   ```

2. **Install dependencies:**

   You can install the required libraries using `pip`:

   ```bash
   pip install mss pillow
   ```

3. **Verify Python version:**

   Ensure you are running Python 3.6 or higher:

   ```bash
   python --version
   ```

## Usage

1. **Run the script with the desired monitor ID:**

   The monitor ID starts from `1` (primary monitor) and increases for additional monitors. For example, to capture the first monitor:

   ```bash
   python myscreen.py 1
   ```

2. **Exit full-screen mode:**
   - The application window starts minimized. You can maximize or restore the window to see the screen capture.
   - Press `Esc` to exit full-screen mode if you change the window state to full-screen.

## Example

To capture and display the second monitor, run:

```bash
python myscreen.py 2
```

## TODO

- [ ] use the first monitor by default if not specified
- [ ] don't refresh the size if not needed
- [ ] be able to switch screen on-the-fly
- [ ] option to show only one app or a fraction of the screen

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [MSS](https://pypi.org/project/mss/): A fast and cross-platform multiple screenshots module.
- [Pillow](https://python-pillow.org/): Python Imaging Library (PIL) fork.



