import logger as l
# from logger import log
import sys

print(sys.stdout.mode)


logger = l.NefxLoggerBuilder().use_file().build()

logger.log('hao')
logger.info('hao')
logger.warn('hao')
logger.error('hao')


# logger.log('hao')
# logger.info('hao')
# logger.warn('hao')
# logger.error('hao')
# log('hao!')

# import requests


# response = requests.get('https://app.apifox.com/project/5473101/test')
# response.encoding = response.apparent_encoding


# print(response.text)