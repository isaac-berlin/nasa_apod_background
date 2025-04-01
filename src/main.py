import os
import platform
import requests
from pathlib import Path
from datetime import datetime
import ctypes
import subprocess
import dotenv

# === CONFIGURATION ===
dotenv.load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
APOD_URL = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}&count=1" # fetch a random image from APOD

# === CONSTANTS ===
SAVE_DIR = Path.home() / ".daily_wallpapers" # directory to save the wallpaper
SAVE_DIR.mkdir(exist_ok=True) # create the directory if it doesn't exist
IMAGE_PATH = SAVE_DIR / "apod.jpg" # path to save the image

# === FUNCTIONS ===
def clear_old_images(): # remove all images in the SAVE_DIR directory
    for file in SAVE_DIR.iterdir():
        if file.is_file():
            file.unlink()

def download_apod_image():
    try:
        response = requests.get(APOD_URL) # connect to NASA API
        data = response.json()[0] # get the response
        image_url = data["url"] # get the image URL
        img_data = requests.get(image_url).content # download the image
    except Exception as e:
        raise Exception(f"Failed to fetch image: {e}")
    
    if not image_url.lower().endswith(('.jpg', '.jpeg')):
        raise Exception("Image is not a JPEG file.")

    with open(IMAGE_PATH, "wb") as f:
        f.write(img_data)

def set_wallpaper(path: Path):
    system = platform.system()

    if system == "Windows": # Windows
        ctypes.windll.user32.SystemParametersInfoW(20, 0, str(path), 3)

    elif system == "Darwin":  # macOS
        SCRIPT = f'''
        tell application "System Events"
            set picture of every desktop to "{path}"
        end tell
        '''
        subprocess.run(["osascript", "-e", SCRIPT])

    elif system == "Linux": # Linux
        try:
            subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", f"file://{path}"])
        except Exception as e:
            print("Failed with gsettings:", e)
            subprocess.run(["feh", "--bg-scale", str(path)])
    else:
        raise Exception(f"Unsupported OS: {system}")

if __name__ == "__main__":
    try:
        clear_old_images()
        download_apod_image()
        set_wallpaper(IMAGE_PATH)
    except Exception as e:
        print(f"Error: {e}")
