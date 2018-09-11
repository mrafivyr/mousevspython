import configparser
import os
from chapter_14.configparser_functions_14 import create_config


def interpolationdemo(path):
    if not os.path.exists(path):
        create_config(path)

    config = configparser.ConfigParser()
    config.read(path)

    print(config.get('Settings', 'font_info'))
    print(config.get('Settings', 'font_info', vars={'font': 'Arial', 'font_size': '17'}))


if __name__ == '__main__':
    path_file = 'settingss.ini'
    interpolationdemo(path_file)
