import glob
import subprocess
from colorama import Fore, Style, init

# Colorama algatamine
init(autoreset=True)

# Leia kõik testifailid
test_files = glob.glob("./tests/test_lab1_*.py")

# Käivita testid ja kuva tulemused
for test in test_files:
    print(f"{Fore.YELLOW}Käivitame {test}...{Style.RESET_ALL}")
    result = subprocess.run(["python", test])
    print(f"{'-' * 50}")
