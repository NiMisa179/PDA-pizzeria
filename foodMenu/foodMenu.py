pizzas = [
    "Margherita", "Farm House", "Peppy Paneer", "Mexican Green Wave", "Deluxe Veggie", "Veg Extravaganza",
    "Cheese n Corn", "Fresh Veggie", "Veggie Paradise", "Special"
]

prices = [
    6.5, 6, 7.5, 7, 8, 8.5, 5, 5.5, 6.5, 9
]

print("* * * * * * Menu * * * * * *")
print("----------------------------")
for i in range(len(pizzas)):
    print(f"{i+1:<3}{pizzas[i]:<20}{prices[i]:<10}")
print("----------------------------")

ans = input("Would you like to place an order? yes/no: ")

order = []
quantity = []
check = 0

print("Place your order, Pick a number to choose a pizza and after that type the quantity of that product.")
print("If you like to stop, type -1")
print("Press 0 to modify your order")

while ans == "yes":

    num = int(input("Choose a number between 1 and " + str(len(pizzas)) + ": "))
    while num < -2 or num > len(pizzas):
        num = int(input("The number must be between 1 and " + str(len(pizzas)) + ": "))

    if num == -1:
        ans = "no"
    elif num == 0:
        for i in range(len(order)):
            print(f"{quantity[i]:<3}{pizzas[order[i]]:<20}{quantity[i] * prices[order[i]]:<10}")
        print("----------------------------")
        print(check)

        row = int(input("Which row would you like to modify? "))
        while row < 0 or row > len(order):
            row = int(input("Row must be between 1 and " + str(len(order)) + ": "))

        check -= prices[order[row-1]] * quantity[row-1]
        quant = int(input("Type the new quantity: "))
        while quant < 0:
            quant = int(input("Type the new quantity. The quantity should be >= 0 : "))
        quantity[row - 1] = quant
        check += prices[order[row-1]] * quant

        if quant == 0:
            quantity.pop(row - 1)
            order.pop(row - 1)

    else:
        quant = int(input("Type the quantity of that product: "))
        if quant > 0 and quant != 0:
            check += prices[num - 1] * quant
            if num - 1 in order:
                i = order.index(num - 1)
                quantity[i] += quant
            else:
                order.append(num - 1)
                quantity.append(quant)

    for i in range(len(order)):
        print(f"{quantity[i]:<3}{pizzas[order[i]]:<20}{quantity[i] * prices[order[i]]:<10}")
    print("----------------------------")
    print(check)

for i in range(len(order)):
    print(f"{quantity[i]:<3}{pizzas[order[i]]:<20}{quantity[i] * prices[order[i]]:<10}")
print("----------------------------")
print("Checkout: ", end="")
print(f"{check:>17}")
