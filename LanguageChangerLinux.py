import subprocess
import time

def set_keyboard_layout(layout: str):
    """Set the keyboard layout using setxkbmap."""
    subprocess.run(["setxkbmap", layout])

if __name__ == "__main__":
    # Array of XKB layouts corresponding to the languages
    layouts = [
        "de",  # German
        "pt",  # Portuguese
        "nl",  # Dutch
        "se",  # Swedish
        "ru",  # Russian
        "cn",  # Chinese
        "jp",  # Japanese
        "kr",  # Korean
        "ara", # Arabic
        "in",  # Hindi
        "pl"   # Polish
    ]

    # Loop through each layout, set the layout, and wait for 20 seconds
    for layout in layouts:
        print(f"Setting keyboard layout to: {layout}")
        set_keyboard_layout(layout)
        time.sleep(20)
