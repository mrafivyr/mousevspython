import configparser
import os


def create_config(path):
    """
    Create a config file
    :param path:
    :return:
    """
    config = configparser.ConfigParser()
    config.add_section('Settings')
    config.set('Settings', 'font', 'Courier')
    config.set('Settings', 'font_size', '10')
    config.set('Settings', 'font_style', 'Normal')
    config.set('Settings', 'font_info', 'You are using %(font)s at %(font_size)s pt')

    write_config(config, path)


def write_config(config, path):
    with open(path, 'w') as config_file:
        config.write(config_file)


def get_config(path):
    """
    Returns the config object
    :param path:
    :return:
    """
    if not os.path.exists(path):
        create_config(path)

    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_setting(path, section, setting):
    """
    Print out a setting
    :param path:
    :param section:
    :param setting:
    :return:
    """
    config = get_config(path)
    value = config.get(section, setting)
    msg = "{section} {setting} is {value}".format(section=section, setting=setting, value=value)

    print(msg)
    return value


def update_setting(path, section, setting, value):
    """
    Update a setting
    :param path:
    :param section:
    :param setting:
    :param value:
    :return:
    """
    config = get_config(path)
    config.set(section, setting, value)

    write_config(config, path)


def delete_setting(path, section, setting):
    """
    Delete a setting
    :param path:
    :param section:
    :param setting:
    :return:
    """
    config = get_config(path)
    config.remove_option(section, setting)

    write_config(config, path)


if __name__ == '__main__':
    path_file = 'settings.ini'

    font = get_setting(path_file, 'Settings', 'font')
    font_size = get_setting(path_file, 'Settings', 'font_size')

    update_setting(path_file, 'Settings', 'font_size', '15')

    delete_setting(path_file, 'Settings', 'font_style')
