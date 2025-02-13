import os
from datetime import date

print(f"Tere {os.getlogin()}")
print(f"Sinu rada {os.getcwd()}")

kataloogidearv = 10
kustuta = 12
kp = str(date.today())

try:
    os.mkdir(kp)
    print(f"{kp} kataloog loodud")
    for i in range(1,kataloogidearv+1):
        kaust = kp+"/"+str(i)
        os.makedirs(kaust)
except:
    print("Kataloog juba olemas")


# Kustutab kausta
if os.path.exists(kp+"/"+str(kustuta)):
    os.rmdir(kp+"/"+str(kustuta))
    print(f"{kustuta} kataloog kustutatud")
else:
    print(f"{kustuta} kataloogi ei leitud")

# kuva kataloogi sisu
dir_list = os.listdir(kp)
print("Kataloogi sisu: ")
for i in dir_list:
    print(i)