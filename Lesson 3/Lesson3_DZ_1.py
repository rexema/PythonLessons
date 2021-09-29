numbers = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять"
}
user_number = input("Введите число: ")


def num_translate(number):
    for key, val in numbers.items():

        if number == key:
            return val
        elif number == val:
            return key
        elif number.capitalize() == key.capitalize():
            return val.capitalize()
        elif number.capitalize() == key.capitalize():
            return key.capitalize()


print(num_translate(user_number))
