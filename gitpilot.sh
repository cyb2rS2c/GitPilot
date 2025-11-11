curl -L -o GitPilot-main.zip https://github.com/cyb2rS2c/GitPilot/archive/refs/heads/main.zip
unzip -o GitPilot-main.zip
cd GitPilot-main
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
python3 gitpilot.py
