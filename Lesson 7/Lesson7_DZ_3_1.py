import os
import shutil
my_dir='DZ3'
if not os.path.exists(my_dir):
    os.mkdir(my_dir)

s_folder=r'my project'
new_folder=[]

for r,d,f in os.walk(s_folder):
    for file in f:
        if file.endswith('.html'):
            new_folder.append(os.path.join(r,file))

    for path in new_folder:
        new_f=os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
        if not os.path.exists(new_f):
            os.mkdir(new_f)
        save_path=os.path.join(new_f, os.path.basename(path))
        shutil.copy(path, save_path)

