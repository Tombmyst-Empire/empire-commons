from functools import wraps


def returns_on_falsy_first_parameter(func):
    """
    Decorator that makes the function returns if the first provided argument of it evaluates to False.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args and not args[0]:
            return args[0]

        if not args and kwargs:
            first_key: str = list(kwargs.keys())[0]
            if not kwargs[first_key]:
                return kwargs[first_key]

        return func(*args, **kwargs)

    return wrapper
