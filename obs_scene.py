class ObsScene:
    def __init__(self, overlays: list):
        self.overlays = overlays
        self.current_index = 0

    def next(self):
        next_index = (self.current_index + 1) % len(self.overlays)
        return self.overlays[next_index].name

    def current_overlay_name(self):
        return self.overlays[self.current_index].name