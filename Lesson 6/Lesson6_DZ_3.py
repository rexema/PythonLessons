from itertools import zip_longest

with open("users.txt", 'r', encoding='utf-8') as f:
    content = f.read()
    clean_content = content.replace('\n', " ")
    names = content.splitlines()

with open("hobby.txt", 'r', encoding='utf-8') as f:
    content = f.read()
    clean_content = content.replace('\n', " ")
    hobbies = content.splitlines()

new_dict = {name: hobby for name, hobby in zip_longest(names, hobbies)}
if len(hobbies) > len(names):
    exit(1)
print(new_dict)
