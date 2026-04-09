import time
import functools


class TimeLimitExceeded(Exception):
    pass


class CallLimitExceeded(Exception):
    pass


def limit(max_time=5, max_calls=3, period=10):
    def decorator(function):
        calls = []
        
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            calls[:] = [t for t in calls if current_time - t < period]
            
            if len(calls) >= max_calls:
                raise CallLimitExceeded(f"Превышен лимит вызовов: {max_calls} за {period}с")
            
            calls.append(current_time)
            start = time.time()
            result = function(*args, **kwargs)
            elapsed = time.time() - start
            
            if elapsed > max_time:
                raise TimeLimitExceeded(f"Превышено время выполнения: {elapsed:.2f}с > {max_time}с")
            
            return result
        return wrapper
    return decorator


@limit(max_time=2, max_calls=2, period=5)
def slow_function(n):
    time.sleep(n)
    return n * 2


try:
    print(slow_function(1))
    print(slow_function(1))
    print(slow_function(1))
except Exception:
    print("error")