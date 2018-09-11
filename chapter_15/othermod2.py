import logging


module_logger = logging.getLogger('exampleApp.othermod2')

def add(x, y):
    """
    :param x:
    :param y:
    :return:
    """
    logger = logging.getLogger('exampleApp.othermod2.add')
    logger.info('added %s and %s to get %s' %(x, y, x+y))

    return x+y
