from .utils import run_testing_func_by_args_iterator__decorator, run_and_calculate_speed__decorator


@run_testing_func_by_args_iterator__decorator
def stress_testing(func_under_test, right_func, *args, **kwargs) -> dict:
    right_answer = right_func(*args, **kwargs)
    answer, launch_info = run_and_calculate_speed__decorator(func_under_test)(*args, **kwargs)
    assert right_answer == answer, \
        f'Wrong answer: {answer}, Right answer: {right_answer}, Input: {(args, kwargs)}'
    return launch_info


@run_testing_func_by_args_iterator__decorator
def speed_testing(func_under_test, *args, **kwargs) -> dict:
    _, launch_info = run_and_calculate_speed__decorator(func_under_test)(*args, **kwargs)
    return launch_info
