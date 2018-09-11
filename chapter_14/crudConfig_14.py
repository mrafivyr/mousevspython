import configparser
import os
from chapter_14.createConfig_14 import createconfig


def crudConfig(path):
    """
    Create, read, update, delete config
    :param path:
    :return:
    """
    if not os.path.exists(path):
        createconfig(path)

    config = configparser.ConfigParser()
    config.read(path)

    # read some value from the config
    font = config.get('Settings', 'font')
    font_size = config.get('Settings', 'font_size')
    print('font is %(font)s and font size is %(font_size)s.' % ({'font': font, 'font_size': font_size}))

    # change a value in the config
    config.set('Settings', 'font_size', '12')

    # delete a value from the config
    config.remove_option('Settings', 'font_style')

    # write changes back to the config file
    with open(path, 'w') as config_file:
        config.write(config_file)


if __name__ == '__main__':
    path_file = 'Settings.ini'
    crudConfig(path_file)
