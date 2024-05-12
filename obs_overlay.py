import sys
import pyautogui
import time

class ObsOverlay:
    def __init__(self, name: str, on_shortcut: list, off_shortcut: list, delay: int = 10):
        self.name = name
        self.on_shortcut = on_shortcut
        self.off_shortcut = off_shortcut
        self.delay = delay

    def _trigger_hotkey(self, shortcut):
        original_stdout = sys.stdout
        sys.stdout = open('/dev/null', 'w')
        pyautogui.hotkey(*shortcut, _pause=False)
        sys.stdout = original_stdout  # Restore stdout
        time.sleep(0.1)  # Introduce a short delay after each key press

    def on(self):
        self._trigger_hotkey(self.on_shortcut)
        # Implement your logic for turning on the overlay
        print(f"{self.name} overlay turned on")

    def off(self):
        self._trigger_hotkey(self.off_shortcut)
        # Implement your logic for turning off the overlay
        print(f"{self.name} overlay turned off")

    def set_delay(self, delay: int):
        self.delay = delay