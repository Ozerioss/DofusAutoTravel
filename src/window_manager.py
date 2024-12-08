import pyautogui
from pynput.keyboard import Controller, Key
import win32gui


class WindowManager:

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

        keyboard = Controller()
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
