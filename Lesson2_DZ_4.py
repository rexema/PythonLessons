list1 = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
my_string = " ".join(list1)
name1 = my_string.split()[1]
name2 = my_string.split()[4].capitalize()
name3 = my_string.split()[8].capitalize()
name4 = my_string.split()[10].capitalize()

print(f'Привет,  {name1}! , Привет, {name2}!, Привет, {name3}!, Привет, {name4}!')
