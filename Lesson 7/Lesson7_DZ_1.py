import os


def make_dirs(x):
    new_dir_path = os.path.join("my project", x)
    for x in new_dir_path:
        if not os.path.exists(new_dir_path):
            os.makedirs(new_dir_path)


make_dirs("settings")
make_dirs("authapp")
make_dirs("adminapp")
make_dirs("authapp")
