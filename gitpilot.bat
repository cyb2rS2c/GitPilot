@echo off
curl -L -o GitPilot-main.zip https://github.com/cyb2rS2c/GitPilot/archive/refs/heads/main.zip
powershell -Command "Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned"
powershell -Command "Expand-Archive -Force .\GitPilot-main.zip"
cd GitPilot-main\GitPilot-main
python -m venv myvenv
call myvenv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
cmd /k "myvenv\Scripts\python.exe -i -c ""exec(open('gitpilot.py').read())"""
