import subprocess

# Caminho para o seu arquivo app.py do Streamlit
app_path = "streamlit_app/app.py"

# Comando para iniciar o Streamlit
command = ["streamlit", "run", app_path, "--server.port", "8000", "--server.headless", "true"]

# Iniciar o Streamlit
subprocess.Popen(command).wait()
