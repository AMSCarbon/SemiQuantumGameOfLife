from time import perf_counter
from functools import wraps
from typing import Dict, List
from statistics import median

benchmark_dict: Dict[str, List[float]] = {}


def record_duration(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        if func.__name__ in benchmark_dict:
            benchmark_dict[key(func)].append(end-start)
        else:
            benchmark_dict[key(func)] = [end-start]
        return result
    return wrap

# some classes have functions with the same name. Append the class name to avoid collision.
# The NoClass variant is just normal non-class specific methods.
# I coooouuullddd use the __code__.co_code or inspect.getsource to be super sure.
# But it's probably over kill for this.
def key(func):
    return func.__qualname__ if func.__name__ != func.__qualname__ else f"NoClass.{func.__name__}"


def print_benchmarking():
    for key in benchmark_dict.keys():
        formatted_val = "{0:.6f}".format(median(benchmark_dict[key]))
        print(f"{key}: {formatted_val}")