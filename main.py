import subprocess
import os

def start_streamlit():
    command = [
        "streamlit", "run", "streamlit_app/app.py", 
        "--server.port", os.getenv("PORT", "8000"), 
        "--server.headless", "true"
    ]
    subprocess.run(command)

if __name__ == "__main__":
    start_streamlit()
