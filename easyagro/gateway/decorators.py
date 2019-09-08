from functools import wraps

from easyagro.gateway.extensions import db


def transational():
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                result = fn(*args, **kwargs)
                db.session.commit()
                return result
            except:
                db.session.rollback()
                raise
        return wrapper
    return decorator
