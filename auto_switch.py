import pyautogui
import time
import sys

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

class ObsScene:
    def __init__(self, overlays: list):
        self.overlays = overlays
        self.current_index = 0

    def next(self):
        next_index = (self.current_index + 1) % len(self.overlays)
        return self.overlays[next_index].name

    def switch_to_next(self):
        self.overlays[self.current_index].off()
        self.current_index = (self.current_index + 1) % len(self.overlays)
        self.overlays[self.current_index].on()

    def current_overlay_name(self):
        return self.overlays[self.current_index].name

# Example usage:
overlay1 = ObsOverlay("SideCam", ["f1"], ["f2"], delay=10)
overlay2 = ObsOverlay("Guitar Zoom", ["f3"], ["f4"], delay=5)

scene = ObsScene([overlay1, overlay2])

while True:
    scene.switch_to_next()
    remaining_time = scene.overlays[scene.current_index].delay
    next_overlay_name = scene.next()  # Retrieve the name of the next overlay
    while remaining_time > 0:
        print(f"Next change to {next_overlay_name} in {remaining_time} seconds", end='\r')
        time.sleep(1)
        remaining_time -= 1
