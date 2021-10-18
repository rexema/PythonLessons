import os
import shutil

src = r"C:\Users\ASosnina\PycharmProjects\pythonProject\my project\mainapp\templates"
dst = r"C:\Users\ASosnina\PycharmProjects\pythonProject\my project\templates"


def copytree(src, dst):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        #print(f's=', s, f'd=', d)
        shutil.copytree(s, d)



copytree(src, dst)
