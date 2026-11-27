
from pywinauto import Application
import time


def test_launch_notepad():

    # Launch Notepad
    app = Application(backend="uia").start("notepad.exe")

    # Allow Windows time to open Notepad
    time.sleep(5)

    # Get the top-level application window
    window = app.top_window()

    # Wait for the window to become visible
    window.wait("visible", timeout=20)

    # Display the window title
    print("Window title:", window.window_text())

    # Display available UI elements
    window.print_control_identifiers()

    # Verify that Notepad is visible
    assert window.is_visible()

    print("Notepad launched successfully!")

    # Close Notepad
    app.kill()
