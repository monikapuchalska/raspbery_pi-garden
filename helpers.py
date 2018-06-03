import logging

from functools import wraps

logging.basicConfig(
    level=logging.DEBUG,
    # format='%(real_func_name) - %(message)',
)
# logging.info(statement, extra={'real_func_name': func.__name__})


def garden_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # logging.info("%s - args: %s, kwargs: %s", func.__name__, str(*args), str(**kwargs))
        try:
            result = func(*args, **kwargs)
            logging.info("%s - result: %s", func.__name__, result)
        except Exception as e:
            logging.exception(repr(e))
            raise
        return result
    return wrapper
