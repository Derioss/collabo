#!/user/bin/env python3
import yaml

def load_config(project_root):
    with open(f'{project_root}/conf/main.yaml') as ymlfile:
        conf = yaml.load(ymlfile, Loader=yaml.FullLoader)