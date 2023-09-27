from functools import wraps


def decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"entering {fn.__name__}")
        ret = fn(*args, **kwargs)
        print(f"exiting  {fn.__name__}")
        return ret

    return wrapper


def patch_all_functions(module):
    for name in dir(module):
        value = getattr(module, name)
        # only patch callables
        if not callable(value):
            continue
        # don't patch things that were just imports
        if value.__module__ != module.__name__:
            continue
        setattr(module, name, decorator(value))
