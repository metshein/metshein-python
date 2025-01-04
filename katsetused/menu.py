menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
loop = 0
summa = 0
try:
    while loop < 1: 
        toode = input("Item: ").title()
        summa+=menu[toode]

        print(f"Total: ${summa}")
except KeyError:
    exit()