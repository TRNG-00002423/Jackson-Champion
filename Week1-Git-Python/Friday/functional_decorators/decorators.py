import time
from functools import wraps

def timer(func):
    """Decorator that measures and prints execution time.

    Output format: "⏱️ {func_name} completed in {seconds:.4f}s"
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        seconds = end - start

        print(f"⏱️ {func.__name__} completed in {seconds:.4f}s")

        return result

    return wrapper

#Test
@timer
def slow_operation():
    time.sleep(0.5)
    return "done"

result = slow_operation()
# Should print: ⏱️ slow_operation completed in 0.50XXs
assert result == "done"
assert slow_operation.__name__ == "slow_operation"  # @wraps preserves metadata


def retry(max_attempts=3, delay=0.5, exceptions=(Exception,)):
    """Parameterized decorator that retries on failure.

    Args:
        max_attempts: Maximum number of tries
        delay: Seconds between retries
        exceptions: Tuple of exception types to catch

    Prints progress: "⚠️ Attempt {n}/{max}: {error}. Retrying in {delay}s..."
    On final failure: "💥 {func_name} failed after {max} attempts"
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"Attempt {attempt} failed: {e}. Retrying...")
                    time.sleep(delay)
        return wrapper
    return decorator

attempt_count = 0

@retry(max_attempts=3, delay=0.1)
def flaky_function():
    global attempt_count
    attempt_count += 1
    if attempt_count < 3:
        raise ConnectionError("Server unavailable")
    return "success"

result = flaky_function()
assert result == "success"



def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        arg_parts = [str(arg) for arg in args]
        kwarg_parts = [f"{key}={value}" for key, value in kwargs.items()]

        all_args = ", ".join(arg_parts + kwarg_parts)

        print(f"📞 Calling {func.__name__}({all_args})")

        result = func(*args, **kwargs)

        print(f"✅ {func.__name__} → {result}")

        return result

    return wrapper

@timer
@log_calls
@retry(max_attempts=2, delay=0.1)
def process_data(data):
    """Process data with timing, logging, and retry."""
    if not data:
        raise ValueError("Empty data")
    return [x * 2 for x in data]

result = process_data([1, 2, 3])