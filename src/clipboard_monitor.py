import pyperclip
from window_manager import WindowManager
from actions import Actions
import time


class ClipboardMonitor:

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

                        window = WindowManager.find_window_by_title_suffix(suffix)
                        if window:
                            if WindowManager.activate_window(window):
                                print(f"Switched to window: '{window.title}'.")
                                Actions.perform_action()
                            else:
                                print(f"Failed to activate window: '{window.title}'.")
                        else:
                            print(f"No window found ending with '{suffix}'.")

                    last_content = current_content

                # reduce CPU usage, can probably wait even longer tbh
                time.sleep(0.5)
        except KeyboardInterrupt:
            print("Clipboard monitoring stopped.")
