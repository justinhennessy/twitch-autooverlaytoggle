from config import load_config
import time

scene, all_off_delay = load_config()

while True:
    current_overlay = scene.overlays[scene.current_index]
    current_overlay.on()

    # Countdown for the current overlay
    print(f"Turning on {current_overlay.name} for {current_overlay.delay} seconds...")
    remaining_time = current_overlay.delay
    while remaining_time > 0:
        print(f"Next change: All overlays will turn off in {remaining_time} seconds", end='\r')
        time.sleep(1)
        remaining_time -= 1

    # Countdown for the period when all overlays are off
    print(f"Turning off all overlays for {all_off_delay} seconds...")
    remaining_time = all_off_delay

    # Turn off all overlays
    for overlay in scene.overlays:
        overlay.off()

    next_overlay_name = scene.next()
    while remaining_time > 0:
        print(f"Next change: {next_overlay_name} will turn on in {remaining_time} seconds", end='\r')
        time.sleep(1)
        remaining_time -= 1

    # Move to the next overlay
    scene.current_index = (scene.current_index + 1) % len(scene.overlays)
