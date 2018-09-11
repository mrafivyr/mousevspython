import logging
import othermod


def main():
    """
    The main entry point of the application
    :return:
    """
    logging.basicConfig(filename='mysnake.log', level=logging.INFO)
    logging.info('Program started')
    result = othermod.add(7, 8)
    logging.info('Done!')


if __name__ == '__main__':
    main()
