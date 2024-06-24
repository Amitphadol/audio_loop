from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydub import AudioSegment
import os

app = FastAPI()

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ensure upload and processed directories exist
os.makedirs("uploads", exist_ok=True)
os.makedirs("processed", exist_ok=True)

@app.get("/")
async def read_index():
    return FileResponse("templates/index.html")

# @app.post("/upload/")
# async def create_upload_file(file: UploadFile = File(...)):
#     file_location = f"uploads/{file.filename}"
#     with open(file_location, "wb+") as file_object:
#         file_object.write(file.file.read())
#     return {"info": f"file saved at {file_location}"}

@app.post("/process/", response_class=HTMLResponse)
async def process_audio(file: UploadFile = File(...), loops: int = Form(1)):
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())

    audio = AudioSegment.from_file(file_location)
    looped_audio = audio * loops

    output_file = f"processed/{file.filename}"
    looped_audio.export(output_file, format="mp3")

    return f"""
    <html>
        <head>
            <title>Audio Looper</title>
            <link rel="stylesheet" type="text/css" href="/static/css/styles.css">
            <link rel="icon" href="/static/favicon.png" type="image/png">
        </head>
        <body>
            <div class="container">
                <h1>Processing Complete</h1>
                <a href="/download/{file.filename}" class="button">Download Processed File</a>
            </div>
        </body>
    </html>
    """

@app.get("/download/{filename}", response_class=FileResponse)
async def download_file(filename: str):
    file_path = f"processed/{filename}"
    return file_path
