import sys
import os
import io
import re
from colorama import Fore, Style, init

# Lisa `lab1` kataloog otsinguteedesse
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../lab1")))

# Colorama algatamine
init(autoreset=True)

def test_lab1_5():
    """Testib lab1_5.py väljundit."""
    saved_stdout = sys.stdout
    try:
        sys.stdout = io.StringIO()
        # Impordi ja käivita lab1_5.py
        import lab1_5
        # Loeme väljundi
        output = sys.stdout.getvalue().strip()
        pattern = r"^Minu unistuste auto on .+ aastast \d+ , mille hind on \d+\.\d+ eurot\.$"
        # Kontrollime väljundit
        if not re.match(pattern, output):
            expected_format = "Minu unistuste auto on MARK MUDEL aastast AASTA , mille hind on KOMAARV eurot."
            raise AssertionError(f"{Fore.RED}Väljund ei vasta oodatud vormingule!\n"
                                 f"Saadud: {output}\n"
                                 f"Oodatud: {expected_format}{Style.RESET_ALL}")
    finally:
        sys.stdout = saved_stdout

if __name__ == "__main__":
    try:
        test_lab1_5()
        print(f"{Fore.GREEN}Ülesanne 1.5 korras!{Style.RESET_ALL}")
    except AssertionError as e:
        print(f"{Fore.RED}Test ebaõnnestus: {e}{Style.RESET_ALL}")
