import logging


def add(x, y):
    """
    add method with logging
    :param x:
    :param y:
    :return:
    """
    logging.info('added %s and %s to get %s' %(x, y, x+y))
    return x+y
