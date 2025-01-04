loop = 1
while loop == 1:
    try:
        tehe = input("Fraction: ")
        tehe = tehe.split("/")
        tehe = int(int(tehe[0]) / int(tehe[1]) * 100)

        if tehe <= 1:
            print("E")
        elif tehe >= 99:
            print("F")
        else:
            print(f"{tehe}%")
        loop = 0
    except (ZeroDivisionError, ValueError):
        continue  