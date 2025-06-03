from nicegui import ui, app
from functools import wraps


def protected_route(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user_id' not in app.storage.user:
            ui.navigate.to('/')
            return
        return func(*args, **kwargs)
    return wrapper


def public_route(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user_id' in app.storage.user:
            ui.navigate.to('/accounts')  # Redirige les utilisateurs déjà connectés
            return
        return func(*args, **kwargs)
    return wrapper
