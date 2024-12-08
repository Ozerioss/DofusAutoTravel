from pynput.keyboard import Controller
from clipboard_monitor import ClipboardMonitor

keyboard = Controller()

if __name__ == "__main__":
    # Replace '- Release' with the desired suffix
    target_suffix = "- Release"
    ClipboardMonitor.clipboard_monitor(target_suffix)
