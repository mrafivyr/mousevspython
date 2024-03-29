import configparser


def createconfig(path):
    """
    Create a config file
    :param path:
    :return:
    """
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set('Settings', 'font', 'Courier')
    config.set('Settings', 'font_size', '10')
    config.set('Settings', 'font_style', 'Normal')
    config.set('Settings', 'font_info', 'You are using %(font)s at %(font_size)s pt')

    with open(path, 'w') as config_file:
        config.write(config_file)


if __name__ == '__main__':
    path_file = 'settings.ini'
    createconfig(path_file)
