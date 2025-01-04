cart = {}

while True:
    try:
        toode = input("Item: ").upper()
        if toode == "":
            break
        elif toode not in cart:
            cart[toode] = 1
        else:
            cart[toode] += 1
    except EOFError:
        break

for i in cart:
    print(f"{i}: {cart[i]}")
