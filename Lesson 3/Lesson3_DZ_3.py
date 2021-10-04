"""В данном задании использовала шаблон от преподавателя."""


def thesaurus(*names):
    new_dict = dict()
    for name in names:
        new_dict.setdefault(name[0], [])
        new_dict[name[0]].append(name)
    return new_dict


print(thesaurus("Ильдар", "Ангелина", "Иван", "Мария", "Петр", "Илья", "Михаил", "Алла", "Светлана", "Анфиса", "Марфа"))
