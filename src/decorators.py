from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            message = f"{func.__name__}"
            try:
                result = func(*args, **kwargs)
                message += " ok"
            except Exception as e:
                message += f" error {e}. Inputs: {args, kwargs}"
                result = None
            if filename is None:
                print(message)
            else:
                with open(filename, "a") as file:
                    file.write(message + "\n")
            return result

        return wrapper

    return decorator
