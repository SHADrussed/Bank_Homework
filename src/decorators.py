from functools import wraps
from typing import Callable, Optional, Any, TypeVar

# Define a type variable for the return type of the decorated function
F = TypeVar("F", bound=Callable[..., Any])


def log(filename: Optional[str] = None) -> Callable[[F], F]:
    """
    Decorator to log function calls and their results or errors.

    Args:
        filename (Optional[str]): The name of the file to log to. If None, logs to stdout.

    Returns:
        Callable[[F], F]: The decorated function.
    """

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
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

        return wrapper  # type: ignore

    return decorator
