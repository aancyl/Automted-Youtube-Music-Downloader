# YouTube Music Downloader using Videoder and PyAutoGUI

This is a Python automation script that uses `pyautogui` to control the Videoder desktop application and download audio from YouTube. The script simulates mouse and keyboard actions to open a browser, search for a video, copy its URL, and trigger a download in Videoder.

> ⚠️ This script is resolution and screen-layout dependent. You **must** adjust the click coordinates to match your screen using tools such as [mPos](https://sourceforge.net/projects/mpos/).

---

## Features

- Automates YouTube audio downloads using the Videoder desktop application
- Simulates keyboard and mouse input to navigate both the browser and Videoder
- Requires minimal manual interaction once configured
- Works with desktop Windows environment

---

## Prerequisites

- **Windows OS**
- **Videoder Desktop Application**  
  [Download from official site](https://www.videoder.com/)

- **Python 3.7 or later**
- Required Python libraries:
  - `pyautogui`
  - `time` (standard library)

Install dependencies via pip:

```
pip install pyautogui
```
