import logging
import othermod2


def main():
    """
    The main entry point of the application
    :return:
    """
    logger = logging.getLogger('exampleApp')
    logger.setLevel(logging.INFO)

    # create the logging file handler
    fh = logging.FileHandler('new_snake.log')

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)

    logger.info('Program Started')
    result = othermod2.add(7, 8)
    logger.info('Done!')


if __name__ == '__main__':
    main()
