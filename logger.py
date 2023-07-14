import logging as LOGGER

# create logger
logger = LOGGER.getLogger('EXCEL')
logger.setLevel(LOGGER.DEBUG)

# create console handler and set level to debug
ch = LOGGER.StreamHandler()
ch.setLevel(LOGGER.DEBUG)

# create formatter
formatter = LOGGER.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')