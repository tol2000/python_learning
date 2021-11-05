from datetime import datetime
from functools import wraps


def trace_explorer(max_level_to_display=-1):
    """
    For tracing
    :param max_level_to_display: -1 - print all calls
                                  0 - print only top level calls
                                      (for fast tracing, with only summary execution params)
    :return:
    """

    def trace_explorer_internal(func):

        delimiters_count = 30
        indent_str = "|   "
        min_level = 0
        func.level = min_level
        func.max_level = min_level
        func.calls = 0

        @wraps(func)
        def wrapper(*args, **kwargs):

            if func.level == min_level:
                func.time = datetime.now()
                print(delimiters_count * "-", f'Tracing {func.__name__}...')

            f_args = ', '.join([str(x) for x in args])

            func.calls += 1

            # print function enter
            if max_level_to_display == -1 or func.level <= max_level_to_display:
                print(f'{func.level * indent_str}[{func.level}]--> {func.__name__}({f_args})')

            # set max nested level watermark
            if func.level > func.max_level:
                func.max_level = func.level

            # increase calls count
            func.level += 1
            # Call the function
            res = func(*args, **kwargs)
            # decrease calls count
            func.level -= 1

            # print function exit
            if max_level_to_display == -1 or func.level <= max_level_to_display:
                print(f'{func.level * indent_str}[{func.level}]<-- {func.__name__}({f_args}) == {res}')

            if func.level == min_level:
                # exit from all nested calls: print result and clear counts
                print(
                    delimiters_count * "-",
                    f'{func.__name__}: end of trace.'
                    f'  Exec time: {datetime.now() - func.time}.'
                    f'  Calls: {func.calls}.'
                    f'  Nested calls max level: {func.max_level}.'
                )

            return res

        return wrapper

    return trace_explorer_internal
