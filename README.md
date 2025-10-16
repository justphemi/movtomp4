MOV to MP4 Converter (FastAPI + HTML Frontend)

A lightweight web app that allows you to upload a .mov file and convert it to .mp4 directly from your browser.
Built with FastAPI, MoviePy, and a simple HTML frontend.

🧰 Requirements

Before running locally, make sure you have:

Python 3.9+

pip (or pip3)

ffmpeg installed on your system
On macOS:

brew install ffmpeg

📦 1. Clone the project
git clone https://github.com/justphemi/movtomp4.git
cd movmp4

🧪 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

📚 3. Install dependencies
pip install -r requirements.txt


If you get a PEP 668 warning about a managed environment, use:

python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt

⚙️ 4. Run the backend server
uvicorn main:app --reload


Once started, the FastAPI server will run on:

👉 http://127.0.0.1:8000

🖥️ 5. Run the frontend (HTML)

You can open index.html directly in your browser or serve it with a simple local server:

python3 -m http.server 3000


Then visit:
👉 http://localhost:3000

🧩 6. How it works

Upload a .mov file from your browser.

The file is sent to the FastAPI backend (/upload endpoint).

MoviePy uses FFmpeg to convert it to .mp4.

Once complete, your browser automatically downloads the converted file.