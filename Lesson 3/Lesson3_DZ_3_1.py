"""В данном задании использовала шаблон от преподавателя."""


def thesaurus_adv(*names_surnames):
    new_dict = {}
    for name_surname in names_surnames:
        name, surname = name_surname.split()
        new_dict.setdefault(surname[0], {})
        new_dict[surname[0]].setdefault(name[0], [])
        new_dict[surname[0]][name[0]].append(name_surname)
    return new_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
