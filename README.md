# NASA APOD Background
This Python script fetches a random image from NASA's Astronomy Picture of the Day (APOD) API and sets it as your desktop wallpaper. 

## Requirements
- Python 3.7+
- requests
- python-dotenv (for environment variable loading)

- (Linux only) gsettings or feh for setting wallpapers

Install the dependencies using:
```
pip install requests python-dotenv
```

## Setup
1) clone this repository 
```
git clone git@github.com:isaac-berlin/nasa_apod_background.git 
```
2) create a virtual enviornment and install the required packages
```
# install venv if you have not already
pip install virtualenv

# create a venv in the root dir of this project
python -m venv venv

# activate the venv (on windows)
.\venv\Scripts\activate

# install the requirements
pip install -r requirements.txt
```
3) Get a (Free) NASA API Key:

Go to api.nasa.gov and request a free API key.

4) Create a .env file in the same directory as the script and add:

```
NASA_API_KEY=your_api_key_here
```
If you don't provide an API key, the script will use the default "DEMO_KEY" (which has limited request quota).

### Windows
To automatically run please ```Task Scheduler``` and create a new task. You must give it a name, choose a hook (When the computer starts or Daily are reccomended), choose start a program, and choose the ```run.bat``` script in the run directory.

### Linux
Coming soon!

### Mac
Coming soon!

## Extra
This script saves the images to ~/.daily_wallpapers directory and creates it if it does not exist. Each time the script is run the contents of the daily_wallpapers folder is wiped to save space. If you wish to edit this script please refer too https://github.com/nasa/apod-api for information about Nasa's API. 