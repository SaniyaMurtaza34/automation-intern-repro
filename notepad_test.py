
from pywinauto.application import Application

# Launch Windows Notepad
app = Application(backend="uia").start("notepad.exe")

# Connect to the Notepad window
window = app.window(title_re=".*Notepad.*")

# Wait until the window is visible
window.wait("visible", timeout=10)

# Enter text into Notepad
window.type_keys("Hello from Pywinauto!", with_spaces=True)

# Verify that the window is visible
assert window.is_visible()

print("Notepad automation test passed!")
