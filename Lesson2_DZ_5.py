prices = [32.48, 46.51, 97.2, 52.15, 85, 20.09, 35.4, 75.5, 15.4, 64, 150, 212.56, 46, 74.8]
new_prices = []

for number in prices:
    if isinstance(number, int):
        zero = str("00 коп")
        new_prices.append(str(number) + " " + "руб" + " " + zero)

    elif isinstance(number, float):
        number = str(number)
        new_number = number.split(".")
        if len(new_number[1]) < 2:
            new_prices.append(str(new_number[0]) + " " + "руб" + " " + str(new_number[1]) + "0" + " " + "коп")
        else:
            new_prices.append(str(new_number[0]) + " " + "руб" + " " + str(new_number[1]) + " " + "коп")


message = ",".join(new_prices)
print(message)








