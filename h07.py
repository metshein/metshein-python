# Ülesanne 7.2

# Sorteeri temperatuurid nimekirjas kasvavas järjekorras

jtemp = ["jaanuar",-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3]
temps = []

print(f"Mõõdetav kuu: {jtemp[0]}")
print(f"Viimane mõõtmise tulemus: {jtemp[-1]} kraadi")


maks = -100
mini = 100
summa = 0
kokku = 0
kordused = 0

for t in range(1,len(jtemp)):
    temps.append(jtemp[t])
    print(jtemp[t], end=" ")    #prindib kõik tempid
    if jtemp[t]>maks:           #max temp kontroll
        maks = jtemp[t]
    if jtemp[t]<mini:           #min temp kontroll
        mini = jtemp[t]
    summa+=jtemp[t]
    kokku+=1
    if jtemp[t] == -20:
        kordused+=1

jtemp.pop(5)        #kustutab
jtemp.insert(5,44)  #lisab
temps.sort()

print()
print(f"Maksimum temp on: {maks}")
print(f"Miinimum temp on: {mini}")
print(f"Keskmine temp on: {summa/kokku:0.2f}")
print(f"Temp -20 esineb: {kordused} korda")
print(jtemp)









