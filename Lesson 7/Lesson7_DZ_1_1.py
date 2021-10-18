
import os

new_folder={'my project': ['settings', 'mainapp', 'adminapp', 'authapp']}

for root,folders in new_folder.items():
    if os.path.exists(root):
        print("папка уже существует")
    else:
        for folder in folders:
            folder_path=os.path.join(root,folder)
            os.makedirs(folder_path)

