import subprocess
import sys

def install_requirements():
    """Paigaldab requirements.txt failis olevad sõltuvused."""
    try:
        print("Paigaldan vajalikud Python'i paketid...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Kõik sõltuvused paigaldatud!")
    except subprocess.CalledProcessError as e:
        print(f"Sõltuvuste paigaldamine ebaõnnestus: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_requirements()
