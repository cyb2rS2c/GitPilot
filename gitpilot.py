import os
import sys
import re
import platform
import subprocess
import zipfile
import requests
from io import BytesIO
from urllib.request import urlopen
from colorama import init, Fore, Style
from pyfiglet import Figlet
import readchar
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Initialize color output for all platforms
init(autoreset=True)

# CONFIGURATION
USERNAME = "cyb2rS2c"
TITLE = "GitPilot"
DESCRIPTION = "Your autopilot for GitHub repositories - clone, install, and run with a single command.\nDesigned and built by **[@cyb2rS2c](https://github.com/cyb2rS2c)**"

# ────────────────────────────────────────────────────────────────
# Utility Functions
# ────────────────────────────────────────────────────────────────

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_header():
    """Displays a styled header using ASCII art."""
    clear_screen()
    fig = Figlet(font="slant")
    print(Fore.RED + fig.renderText(TITLE))
    print(Fore.YELLOW + DESCRIPTION + "\n" + Style.RESET_ALL)


def get_system():
    """Returns the current operating system name."""
    return "Windows" if platform.system().lower().startswith("win") else "Linux"


# ────────────────────────────────────────────────────────────────
# GitHub Data Handling
# ────────────────────────────────────────────────────────────────

def detect_supported_systems(readme_text: str):
    text = re.sub(r'\s+', ' ', readme_text.lower())
    git_found = bool(re.search(r"(sudo\s+)?git\s+clone", text))
    curl_found = bool(re.search(r"curl\s+-", text))

    if git_found and curl_found:
        return ["Windows", "Linux"]
    elif git_found:
        return ["Linux"]
    elif curl_found:
        return ["Windows"]
    return ["Windows", "Linux"]


def fetch_user_repositories(username: str):
    api_url = f"https://api.github.com/users/{username}/repos"
    repos, page = [], 1

    print(Fore.MAGENTA + f"Fetching repositories for {username} ...\n")
    while True:
        response = requests.get(api_url, params={"page": page, "per_page": 100})
        if response.status_code != 200:
            sys.exit(Fore.RED + f"Error: Failed to retrieve repository list (HTTP {response.status_code})")

        data = response.json()
        if not data:
            break

        repos.extend(data)
        page += 1

    repo_info = []
    for repo in repos:
        name, supported_systems = repo["name"], ["Windows", "Linux"]

        # Try detecting OS support from README
        for branch in ["main", "master", "develop"]:
            readme_url = f"https://raw.githubusercontent.com/{username}/{name}/{branch}/README.md"
            try:
                resp = requests.get(readme_url)
                if resp.status_code == 200:
                    supported_systems = detect_supported_systems(resp.text)
                    break
            except Exception:
                continue

        repo_info.append((name, supported_systems))

    return repo_info


# ────────────────────────────────────────────────────────────────
# Interactive Menu System
# ────────────────────────────────────────────────────────────────

def interactive_menu(repos, system):
    index = 0
    compatible_repos = [r for r in repos if system in r[1] or len(r[1]) == 2]

    if not compatible_repos:
        sys.exit(Fore.RED + "No compatible repositories found for this system.\n")

    while True:
        print_header()
        print(Fore.GREEN + f"Detected System: {system}\n" + Style.RESET_ALL)
        print("Use UP/DOWN to navigate, [Enter] to select, or 'q' to quit.\n")

        for i, (name, systems) in enumerate(compatible_repos):
            label = f"{name} ({'/'.join(systems)})"
            pointer = Fore.RED + "* " + Fore.MAGENTA if i == index else "  "
            print(pointer + label + Style.RESET_ALL)

        key = readchar.readkey()

        if key == readchar.key.UP:
            index = (index - 1) % len(compatible_repos)
        elif key == readchar.key.DOWN:
            index = (index + 1) % len(compatible_repos)
        elif key == readchar.key.ENTER:
            return compatible_repos[index][0]
        elif key.lower() == 'q':
            clear_screen()
            sys.exit(0)


# ────────────────────────────────────────────────────────────────
# Cloning / Downloading
# ────────────────────────────────────────────────────────────────

def clone_or_download(repo_url: str):
    repo_name = repo_url.rstrip("/").split("/")[-1].replace(".git", "")

    try:
        subprocess.run(["git", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        subprocess.run(["git", "clone", repo_url], check=True)
        os.chdir(repo_name)
    except Exception:
        print(Fore.YELLOW + "Git not found or cloning failed — switching to ZIP download..." + Style.RESET_ALL)
        if repo_url.endswith(".git"):
            repo_url = repo_url[:-4]

        for branch in ["main", "master"]:
            try:
                zip_url = f"{repo_url}/archive/refs/heads/{branch}.zip"
                with urlopen(zip_url) as resp:
                    with zipfile.ZipFile(BytesIO(resp.read())) as zf:
                        zf.extractall(".")
                extracted = [d for d in os.listdir(".") if os.path.isdir(d)]
                if extracted:
                    os.chdir(max(extracted, key=os.path.getmtime))
                return
            except Exception:
                continue

        sys.exit(Fore.RED + "Failed to download repository ZIP.")


# ────────────────────────────────────────────────────────────────
# Dependency Installation
# ────────────────────────────────────────────────────────────────

def install_dependencies():
    for root, _, files in os.walk("."):
        for f in files:
            if f.lower() == "requirements.txt":
                req_path = os.path.join(root, f)
                print(Fore.CYAN + f"Installing dependencies from {req_path}" + Style.RESET_ALL)
                try:
                    subprocess.run([sys.executable, "-m", "pip", "install", "-r", req_path], check=True)
                except subprocess.CalledProcessError:
                    print(Fore.RED + f"Failed to install dependencies from {req_path}\n")


# ────────────────────────────────────────────────────────────────
# File Detection & Execution
# ────────────────────────────────────────────────────────────────

def find_runnable_files(system):
    runnable = []
    for root, _, files in os.walk("."):
        for f in files:
            path = os.path.join(root, f)
            if system == "Windows" and f.endswith((".py", ".ps1", ".bat")):
                runnable.append(path)
            elif system == "Linux" and f.endswith((".py", ".sh")):
                runnable.append(path)
    return runnable


def run_selected_repo(repo_name):
    repo_url = f"https://github.com/{USERNAME}/{repo_name}.git"
    system = get_system()

    print(Fore.GREEN + f"\nSelected repository: {repo_name}\n" + Style.RESET_ALL)

    try:
        clone_or_download(repo_url)
    except Exception as e:
        sys.exit(Fore.RED + f"Download/Clone failed: {e}")

    install_dependencies()
    runnable_files = find_runnable_files(system)

    if not runnable_files:
        print(Fore.RED + "No runnable scripts found. Check the README.md for usage details.\n")
        return

    if len(runnable_files) > 1:
        print(Fore.YELLOW + "Multiple runnable files found:\n")
        for i, f in enumerate(runnable_files, start=1):
            print(f"{i}. {f}")
        choice = input("\nEnter the number of the file to execute: ").strip()
        try:
            selected = runnable_files[int(choice) - 1]
        except Exception:
            sys.exit(Fore.RED + "Invalid selection.\n")
    else:
        selected = runnable_files[0]

    print(Fore.GREEN + f"\nExecuting: {selected}\n" + Style.RESET_ALL)
    try:
        if selected.endswith(".py"):
            subprocess.run([sys.executable, selected], check=True)
        elif selected.endswith(".ps1"):
            subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", selected], check=True)
        elif selected.endswith(".sh"):
            subprocess.run(["bash", selected], check=True)
    except subprocess.CalledProcessError:
        print(Fore.RED + f"Error executing {selected}. Check README for guidance.\n")


# ────────────────────────────────────────────────────────────────
# Main Execution Entry
# ────────────────────────────────────────────────────────────────

def main():
    system = get_system()
    repos = fetch_user_repositories(USERNAME)
    selected_repo = interactive_menu(repos, system)
    run_selected_repo(selected_repo)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\nOperation cancelled by user.\n" + Style.RESET_ALL)
        sys.exit(0)
