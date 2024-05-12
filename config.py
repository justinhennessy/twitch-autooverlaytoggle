import yaml
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

    def current_overlay_name(self):
        return self.overlays[self.current_index].name

def load_config():
    with open('config.yaml', 'r') as file:
        config_data = yaml.safe_load(file)

    overlays_data = config_data['overlays']
    all_off_delay = config_data['all_off_delay']

    overlays = []
    for overlay_data in overlays_data:
        overlay = ObsOverlay(overlay_data['name'], overlay_data['on_shortcut'], overlay_data['off_shortcut'], overlay_data['delay'])
        overlays.append(overlay)

    scene = ObsScene(overlays)

    return scene, all_off_delay
