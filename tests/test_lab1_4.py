import sys
import os
import io
import re
from colorama import Fore, Style, init

# Lisa `lab1` kataloog otsinguteedesse
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../lab1")))

# Colorama algatamine
init(autoreset=True)

def test_lab1_4():
    """Testib lab1_4.py väljundit."""
    saved_stdout = sys.stdout
    try:
        sys.stdout = io.StringIO()
        # Impordi ja käivita lab1_4.py
        import lab1_4
        # Loeme väljundi
        output = sys.stdout.getvalue().strip()
        pattern = r"^Minu lemmikraamat on .+ , mis on \d+ lehekülge pikk ja mille ma hindan \d+\.\d+ punktiga\.$"
        # Kontrollime väljundit
        if not re.match(pattern, output):
            expected_format = "Minu lemmikraamat on PEALKIRI AUTOR , mis on LEHEKÜLGI pikk ja mille ma hindan KOMAARV punktiga."
            raise AssertionError(f"{Fore.RED}Väljund ei vasta oodatud vormingule!\n"
                                 f"Saadud: {output}\n"
                                 f"Oodatud: {expected_format}{Style.RESET_ALL}")
    finally:
        sys.stdout = saved_stdout

if __name__ == "__main__":
    try:
        test_lab1_4()
        print(f"{Fore.GREEN}Ülesanne 1.4 korras!{Style.RESET_ALL}")
    except AssertionError as e:
        print(f"{Fore.RED}Test ebaõnnestus: {e}{Style.RESET_ALL}")
