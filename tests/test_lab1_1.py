import io
import sys
import re
import os
from colorama import Fore, Style, init

# Colorama algatamine
init(autoreset=True)

def test_lab1_1():
    """Testib lab1_1.py väljundit."""
    saved_stdout = sys.stdout
    try:
        sys.stdout = io.StringIO()

        # Käivita lab1_1.py
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../lab1")))
        import lab1_1

        # Loeme väljundi
        output = sys.stdout.getvalue().strip()
        pattern = r"^[A-Za-z]+ , \d+ aastat vana ja keskmine hinne on \d+\.\d+$"

        # Kontrollime väljundit
        if not re.match(pattern, output):
            expected_format = "NIMI , VANUS aastat vana ja keskmine hinne on KOMAARV"
            raise AssertionError(f"{Fore.RED}Väljund ei vasta oodatud vormingule!\n"
                                 f"Saadud: {output}\n"
                                 f"Oodatud: {expected_format}{Style.RESET_ALL}")
    finally:
        sys.stdout = saved_stdout

if __name__ == "__main__":
    try:
        test_lab1_1()
        # Kui kõik testid õnnestusid, näidatakse ainult roheline teade
        print(f"{Fore.GREEN}Ülesanne 1.1 korras!{Style.RESET_ALL}")
    except AssertionError as e:
        # Kui test ebaõnnestub, prinditakse veateade
        print(f"{Fore.RED}Test ebaõnnestus: {e}{Style.RESET_ALL}")
