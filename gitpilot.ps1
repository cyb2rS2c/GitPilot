curl -o GitPilot-main.zip https://github.com/cyb2rS2c/GitPilot/archive/refs/heads/main.zip
Expand-Archive -Force  .\GitPilot-main.zip
cd GitPilot-main/GitPilot-main
python -m venv myvenv
./myvenv/Scripts/Activate.ps1
pip install -r requirements.txt
python GitPilot.py
