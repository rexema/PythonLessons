import yaml
import os

pattern={'my project':
        [{'settings': [
            '__init__.py', 'dev.py', 'prod.py'],
        },
         {'mainapp': [
             '__init__.py', 'models.py', 'views.py', {'templates':[{
                 'mainapp':['base.html', 'index.html']}]
          }]},
        {"authapp":['__init__.py', 'models.py', 'views.py', {'templates': [{'authapp': ['base.html', 'index.html']}]
         }
                    ]
         }
    ]
}
with open('config.yaml', 'w') as f:
    f.write(yaml.dump(pattern))
    f.close()

with open('config.yaml')as y_file:
    pattern=yaml.safe_load(y_file)

def copy_folder(data):
    for folder, data_tmps in data.items():
        if  not os.path.exists(folder):
            os.mkdir(folder)
        os.chdir(folder)
        for data_tmp in data_tmps:
            if isinstance(data_tmp, dict):
                copy_folder(data_tmp)
            else:
                if not os.path.exists(data_tmp):
                    if "."in data_tmp:
                        with open(data_tmp, 'w') as f:
                            f.write('')
        else:
            os.chdir('../')
copy_folder(pattern)
