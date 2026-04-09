from datetime import datetime

def log_exceptions(log_file="Practicum/Practicum_18/errors.log"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                with open(log_file, "a", encoding="utf-8") as f:
                    f.write(f"{datetime.now()} - {type(e).__name__}: {str(e)}\n")
                raise
        return wrapper
    return decorator

@log_exceptions("Practicum/Practicum_18/errors.log")
def divide(a, b):
    return a / b

try:
    print(divide(10, 0))
except:
    print("error")