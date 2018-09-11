import logging
import logging.config
import othermod2


def main():
    """
    Based on http://docs.python.org/howto/logging.html#configuring-logging
    :return:
    """
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger('exampleApp')

    logger.info('Program Started')
    result = othermod2.add(7, 8)
    logger.info('Done!')


if __name__ == '__main__':
    main()
