import re

Email = re.compile(r'([a-z0-9_.]+)@([a-z0-9]+\.[a-z]+)')


def email_parse(email):
    found_info = Email.findall(email)
    if found_info:
        username = list(found_info[0])[0]
        domain = list(found_info[0])[1]

        email_info = {"username": username, "domain": domain}

    else:
        raise ValueError(f'wrong email: {email}')

    print(email_info)


email_parse('rexema@gmail.com')
