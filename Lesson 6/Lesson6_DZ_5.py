import sys
from itertools import zip_longest

users, hobby, out=sys.argv[1:]

with open(out, 'w', encoding='utf-8') as f:
    with open(users,  encoding='utf-8') as users:
        with open(hobby, encoding='utf-8') as hobby:
            num_lines_users=sum(1 for line in users)
            num_line_hobby=sum(1 for line in hobby)

            if num_lines_users<num_line_hobby:
                exit(1)
            users.seek(0)
            hobby.seek(0)
            for line_user, line_user_hobby in zip_longest(users, hobby):
                f.write(f'{line_user.strip()}:' f'{line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby}\n')
