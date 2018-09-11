import logging


logging.basicConfig(filename='sample.log', level=logging.INFO)
log = logging.getLogger('ex')

try:
    raise RuntimeError
except RuntimeError:
    log.error('Error!')
    log.exception('Error!')
    log.debug('Error!')
    # logging.error('Error!')
