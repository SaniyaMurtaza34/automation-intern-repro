
from pywinauto import Desktop
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import time


def test_notepad():

    # Launch Notepad
    Application(backend="uia").start("notepad.exe")

    window = None

    try:
        # Wait for Notepad
        time.sleep(2)

        # Find Notepad on the Windows desktop
        desktop = Desktop(backend="uia")

        windows = desktop.windows()

        for win in windows:
            print("Window found:", win.window_text())

        window = desktop.window(title_re=".*Notepad.*")
        window.wait("visible", timeout=10)

        # Display UI elements
        window.print_control_identifiers()

        # Type text
        window.set_focus()
        send_keys("Hello! This is my first Pywinauto test.")

        print("Text entered successfully!")

        # Keep Notepad open for 2 seconds
        time.sleep(2)

        # Verify that the window exists
        assert window.is_visible()

        print("TEST PASSED!")

    finally:
        # Close Notepad
        if window is not None:
            window.close()
            print("Notepad closed!")

