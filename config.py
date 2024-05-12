import yaml
from obs_overlay import ObsOverlay
from obs_scene import ObsScene

def load_config(file_path):
    with open(file_path, 'r') as file:
        config_data = yaml.safe_load(file)

    overlays = []
    for overlay_data in config_data['overlays']:
        overlay = ObsOverlay(
            overlay_data['name'],
            overlay_data['on_shortcut'],
            overlay_data['off_shortcut'],
            overlay_data.get('delay', 10)
        )
        overlays.append(overlay)

    scene = ObsScene(overlays)
    all_off_delay = config_data.get('all_off_delay', 60)

    return scene, all_off_delay
