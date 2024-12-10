import time
from pynput.keyboard import Controller, Key


class Actions:
    @staticmethod
    def perform_action():
        """Perform the required actions: press SPACE, paste clipboard content, and press ENTER twice."""
        keyboard = Controller()
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        time.sleep(0.1)

        # Simulate CTRL+V to paste clipboard content
        with keyboard.pressed(Key.ctrl):
            keyboard.press("v")
            keyboard.release("v")

        time.sleep(0.2)

        # Press ENTER twice with a delay
        for _ in range(2):
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(0.15)
