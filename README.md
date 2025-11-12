# GitPilot

> **Your autopilot for GitHub repositories - clone, install, and run with a single command.**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-green?logo=linux)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Version](https://img.shields.io/badge/Version-3.0-orange)

---

## 🧠 Overview

**GitPilot** is a cross-platform, intelligent command-line tool that automates the entire process of exploring and running GitHub repositories.

It’s an interactive assistant that:
- 🔍 Lists all **public repositories** of a given GitHub user  
- 🧩 Detects supported operating systems (**Windows** / **Linux**) based on README contents  
- ⚙️ **Clones** or **downloads** repositories automatically  
- 📦 Installs dependencies from `requirements.txt`  
- 🚀 Detects and executes runnable files (`.py`, `.sh`, `.ps1`, `.bat`)  

> Designed and built by **[@cyb2rS2c](https://github.com/cyb2rS2c)**  
> Version: **3.0**

---

## 🖥️ Features

| Feature | Description |
|----------|--------------|
| 🔗 Repo Fetcher | Lists all public GitHub repositories for a specified username |
| 🧠 OS Detection | Analyzes README content to infer Windows/Linux compatibility |
| ⚙️ Smart Cloning | Uses `git clone` or ZIP fallback automatically |
| 📦 Auto Installer | Installs dependencies from all detected `requirements.txt` |
| 🚀 Runner | Automatically locates and executes runnable project files |
| 🧭 Interactive UI | Navigate repositories via an arrow-key menu |
| 💡 Cross-Platform | Works seamlessly on both Windows and Linux |

---

## ⚙️ Installation

### Prerequisites
- 🐍 Python **3.8+**
- `pip` package manager  
- Optional: `git` (for faster cloning)

### Clone this Repository
1. Clone this repository: (windows)
```bash
curl -o GitPilot-main.zip https://github.com/cyb2rS2c/GitPilot/archive/refs/heads/main.zip
Expand-Archive -Force  .\GitPilot-main.zip
cd GitPilot-main/GitPilot-main
```
2. Install dependencies in venv using cmd (Recommended):
```bash
python -m venv myvenv
./myvenv/Scripts/activate.bat
pip install -r requirements.txt
```
1. Clone this repository: (Linux):
```bash
git clone https://github.com/cyb2rS2c/GitPilot.git
cd GitPilot
```
2. Install dependencies in venv using Terminal (Recommended):
```bash
python -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
```
### 🚀 Usage
Run the main script directly:
```bash
python gitpilot.py
```
### Advanced Installer (Skip the steps above)
#### For Windows:
Run the .bat file via CMD or using GUI:
```bash
curl https://raw.githubusercontent.com/cyb2rS2c/GitPilot/refs/heads/main/gitpilot.bat -o gitpilot.bat&&gitpilot.bat
```
#### For Linux:
Run the .sh file using Terminal:
```bash
wget https://raw.githubusercontent.com/cyb2rS2c/GitPilot/refs/heads/main/gitpilot.sh;sudo chmod +x gitpilot.sh;./gitpilot.sh
```
## Interactive Flow

1. The tool detects your OS (Windows/Linux).
2. Lists all your public repositories on GitHub.
3. You navigate with ↑/↓ and press Enter to select one.
4. GitPilot clones (or downloads) the repository.
5. It installs dependencies automatically.
6. Finally, it runs any runnable files found in the repo.

## Screenshots
<img width="1051" height="515" alt="bild" src="https://github.com/user-attachments/assets/0699716e-115e-438f-b2ef-d879fc763289" />
<img width="751" height="454" alt="Screenshot_2025-11-12_13-35-33" src="https://github.com/user-attachments/assets/0ce64ef8-4a0c-41c2-8560-be783b7b25b8" />

## 📝 Author

cyb2rS2c - [GitHub Profile](https://github.com/cyb2rS2c)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

The software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

