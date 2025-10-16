import os
import subprocess
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from pathlib import Path
import uuid

app = FastAPI()

UPLOAD_FOLDER = Path("uploads")
CONVERT_FOLDER = Path("converted")
UPLOAD_FOLDER.mkdir(exist_ok=True)
CONVERT_FOLDER.mkdir(exist_ok=True)

templates = Jinja2Templates(directory="templates")
app.mount("/converted", StaticFiles(directory="converted"), name="converted")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/convert")
async def convert(file: UploadFile = File(...)):
    if not file.filename.endswith(".mov"):
        return {"error": "Only .mov files allowed"}

    # Save uploaded .mov
    input_path = UPLOAD_FOLDER / f"{uuid.uuid4()}_{file.filename}"
    with open(input_path, "wb") as f:
        f.write(await file.read())

    # Output path
    output_filename = input_path.stem + ".mp4"
    output_path = CONVERT_FOLDER / output_filename

    # Convert using ffmpeg
    try:
        subprocess.run([
            "ffmpeg",
            "-i", str(input_path),
            "-c:v", "libx264",
            "-c:a", "aac",
            "-y",
            str(output_path)
        ], check=True)
    except subprocess.CalledProcessError as e:
        return {"error": f"Conversion failed: {e}"}

    return {"download_url": f"/converted/{output_filename}"}
