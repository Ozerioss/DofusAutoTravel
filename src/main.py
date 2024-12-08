import pyautogui
import pyperclip
import time
from pynput.keyboard import Controller, Key
import win32gui

keyboard = Controller()


def find_window_by_title_suffix(suffix):
    """Find a window by its title suffix using PyAutoGUI."""
    all_windows = pyautogui.getAllWindows()
    for window in all_windows:
        if window.title.strip().endswith(suffix):
            print(f"Found target window. {window.title}")
            return window
    return None


def activate_window(window):
    """
    Bring the specified window to the foreground using an Alt key press trick.

    See https://stackoverflow.com/a/73921057 for why we are doing the Alt key workaround

    :param window: A pyautogui.Window object.
    :return: True if successful, False otherwise.
    """
    if not window:
        print("Invalid window object.")
        return False

    hwnd = window._hWnd  # Extract the raw window handle
    try:
        keyboard.press(Key.alt)
        win32gui.SetForegroundWindow(hwnd)
        return True
    except Exception as e:
        print(f"Failed to activate window: {e}")
        return False
    finally:
        keyboard.release(Key.alt)


def perform_action():
    """Perform the required actions: press SPACE, paste clipboard content, and press ENTER twice."""
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    time.sleep(0.1)

    # Simulate CTRL+V to paste clipboard content
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')

    time.sleep(0.2)

    for _ in range(2):
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.1)


def clipboard_monitor(suffix):
    """Monitor clipboard and perform actions for matching clipboard content."""
    last_content = pyperclip.paste()

    print("Monitoring clipboard... Press Ctrl+C to stop.")
    try:
        while True:
            current_content = pyperclip.paste()

            # Check if the content has changed
            if current_content != last_content:
                if current_content.startswith("/travel"):
                    print(f"Detected '/travel' command: {current_content}")

                    window = find_window_by_title_suffix(suffix)
                    if window:
                        if activate_window(window):
                            print(f"Switched to window: '{window.title}'.")
                            perform_action()
                        else:
                            print(f"Failed to activate window: '{window.title}'.")
                    else:
                        print(f"No window found ending with '{suffix}'.")

                last_content = current_content

            # reduce CPU usage, can probably wait even longer tbh
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Clipboard monitoring stopped.")


if __name__ == "__main__":
    # Replace '- Release' with the desired suffix
    target_suffix = "- Release"
    clipboard_monitor(target_suffix)
