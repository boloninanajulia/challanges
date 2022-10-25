from datetime import datetime
from typing import Any
from functools import wraps


def run_and_calculate_speed__decorator(func) -> (Any, dict):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()

        speed = end - start
        return result, {'input': (args, kwargs), 'speed': speed.microseconds}

    return wrapper


def print_launch_result(speed_items):
    avg_speed = sum(speed_items) / len(speed_items)
    max_speed = max(speed_items)
    min_speed = min(speed_items)
    print(f'AVG speed: {avg_speed}, Max speed: {max_speed}, Min speed: {min_speed} (microseconds)')


def run_testing_func_by_args_iterator__decorator(func):
    @wraps(func)
    def _func(*args, args_iterator, args_iterator_kwargs=None, **kwargs):
        print(f'\nRun {func.__name__.replace("_", " ")}, parameters: {args_iterator_kwargs}')
        speed_items = []
        for i in args_iterator(**(args_iterator_kwargs or {})):
            launch_info = func(*args, *i, **kwargs)
            speed_items.append(launch_info['speed'])

        print_launch_result(speed_items)

    return _func
