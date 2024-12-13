import logging




auth_logger = logging.getLogger('auth_logger')
auth_handler = logging.FileHandler('logs/auth.log', encoding='utf-8')
auth_handler.setLevel(logging.INFO)
auth_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
auth_handler.setFormatter(auth_formatter)
auth_logger.addHandler(auth_handler)
auth_logger.setLevel(logging.INFO)


transaction_logger = logging.getLogger('transaction_logger')
transaction_handler = logging.FileHandler('logs/app.log', encoding='utf-8')
transaction_handler.setLevel(logging.INFO)
transaction_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
transaction_handler.setFormatter(transaction_formatter)
transaction_logger.addHandler(transaction_handler)
transaction_logger.setLevel(logging.INFO)
