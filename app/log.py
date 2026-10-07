import logging
from functools import wraps

logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y/%m/%d - %I:%M:%S %p',
    encoding='utf-8',
)

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            logging.info(f'Function {func.__name__} | params: {args, kwargs} | output: {result}')
            return result
        except Exception as e:
            logging.exception(f'Function {func.__name__} | params: {args, kwargs} | error: {e}')
            raise
    return wrapper