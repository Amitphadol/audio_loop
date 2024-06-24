# Audio Looper Application

This project is a simple audio processing application built using FastAPI. It allows users to upload an audio file, process it by looping the audio a specified number of times, and download the processed file.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [Directory Structure](#directory-structure)
- [Endpoints](#endpoints)
- [HTML Template](#html-template)
- [Scripts](#scripts)

## Features

- Upload audio files.
- Process audio files by looping them a specified number of times.
- Download the processed audio files.
- Web-based interface to interact with the application.

## Requirements

- Python 3.8+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Pydub](https://pydub.com/)
- [FFmpeg](https://ffmpeg.org/)

## Setup

### 1. Clone the Repository

```bash
git git clone https://github.com/Amitphadol/audio_loop.git
cd audio-loop
```

### 2. Create a Virtual Environment

Create a virtual environment to manage dependencies:

```bash
python -m venv env_name
```

Replace `env_name` with your desired environment name.

### 3. Activate the Virtual Environment

Activate the virtual environment:

- **On macOS/Linux:**
  ```bash
  source env_name/bin/activate
  ```

### 4. Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```
## Running the Application

### Using the Provided Shell Script

The `run.sh` script simplifies the process of running the application:

```bash
./run.sh
```

### Manually

To run the application manually, follow these steps:

1. Run the FastAPI application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

2. Open the application in your web browser:
   ```bash
   xdg-open http://127.0.0.1:8000/ || open http://127.0.0.1:8000/ || start http://127.0.0.1:8000/
   ```

## Directory Structure

- `main.py`: Contains the FastAPI application code.
- `static/`: Directory for static files like CSS and JavaScript.
- `templates/`: Directory for HTML templates.
- `uploads/`: Directory where uploaded audio files are saved.
- `processed/`: Directory where processed audio files are saved.
- `run.sh`: Script to run the application.

## Endpoints

- **`GET /`**: Serves the index page with forms for uploading and processing audio files.
- **`POST /process/`**: Processes an uploaded audio file by looping it a specified number of times and provides a link to download the processed file.
- **`GET /download/{filename}`**: Provides the processed file for download.

## HTML Template

A simple HTML form is used for uploading and processing audio files. It provides two sections: one for uploading and one for processing the audio file. The HTML template can be found in the `index.html` file:
## Scripts

### `run.sh`

The `run.sh` script sets up and runs the application. It ensures the required directories are present, runs the FastAPI application using Uvicorn, and opens the application in the default web browser. It also keeps the script running to keep the server alive:

Make sure the script has executable permissions:

```bash
chmod +x run.sh
```

## Notes

- Customize the `index.html` file as needed for your application.
- Ensure FFmpeg is correctly installed and accessible to avoid issues with audio processing.
