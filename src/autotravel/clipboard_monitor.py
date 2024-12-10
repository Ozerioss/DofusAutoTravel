import pyperclip
from autotravel.window_manager import WindowManager
from autotravel.actions import Actions
import time


class ClipboardMonitor:
    def __init__(self, suffix, gui_log=None):
        self.suffix = suffix
        self.last_content = ""
        self.gui_log = gui_log
        self.running = False

    def log_message(self, message):
        """Log a message to the GUI or print it."""
        if self.gui_log:
            self.gui_log(message)
        print(message)

    def monitor(self):
        """Monitor clipboard and perform actions for matching clipboard content."""
        self.running = True
        self.log_message("Monitoring clipboard for /travel commands ...")
        try:
            while self.running:
                current_content = pyperclip.paste()
                if current_content.startswith("/travel"):
                    self.log_message(f"Detected '/travel' command: {current_content}")
                    window = WindowManager.find_window_by_title_suffix(self.suffix)
                    if window:
                        if WindowManager.activate_window(window):
                            self.log_message(f"Switched to window: '{window.title}'.")
                            Actions.perform_action()
                            self.log_message(f"Traveling to {current_content}")
                        else:
                            self.log_message(f"Failed to activate window: '{window.title}'.")
                    else:
                        self.log_message(f"No window found ending with '{self.suffix}'.")

                    pyperclip.copy("")  # empty clipboard
                    self.log_message("Clipboard cleared after processing.")
                # reduce CPU usage, can probably wait even longer tbh
                time.sleep(0.5)
        except KeyboardInterrupt:
            self.log_message("Clipboard monitoring stopped.")

    def stop(self):
        """Stop the clipboard monitoring loop."""
        self.running = False
