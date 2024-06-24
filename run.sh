#!/bin/bash

# Ensure the virtual environment is activated
source ~/my_work/ram/god_env/bin/activate

# Ensure the directories exist
mkdir -p uploads processed static/css static/js

# Run the FastAPI application with Uvicorn
uvicorn main:app &

# Wait for a few seconds to ensure the server is up
sleep 3

# Open the application in the default web browser
xdg-open http://127.0.0.1:8000/ || open http://127.0.0.1:8000/ || start http://127.0.0.1:8000/

# Keep the script running to keep the server alive
wait
