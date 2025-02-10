import logging


logging.basicConfig(
    level=logging.DEBUG,
    filename='main.log',
    filemode='w',
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
)

logging.debug('123')
logging.info('Сообщение отправлено')
logging.warning('Большая нагрузка')
logging.error('Бот не смог отправить сообщение')
logging.critical('Все упало. Зовите админа!!!')
