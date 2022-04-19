import logging
import math
import operator


logger = logging.getLogger()
operations = {
    'add': operator.add,
    'truediv': operator.truediv,
    'floordiv': operator.floordiv,
    'and_': operator.and_,
    'xor': operator.xor,
    'or_': operator.or_,
    'pow': operator.pow,
    'is_': operator.is_,
    'is_not': operator.is_not,
    'lshift': operator.lshift,
    'mod': operator.mod,
    'mul': operator.mul,
    'rshift': operator.rshift,
    'sub': operator.sub,
    'lt': operator.lt,
    'le': operator.le,
    'eq': operator.eq,
    'ne': operator.ne,
    'ge': operator.ge,
    'gt': operator.gt,
    'nextafter': math.nextafter,
    'atan2': math.atan2,
    'hypot': math.hypot,
}

allowed_operations = set(operations.keys())


def is_number(num: str) -> [int | float | None]:
    if num.isnumeric():
        return int(num)
    else:
        try:
            num = float(num)
            return num
        except ValueError:
            return None


def figure_out_operation(operator: str, n1: str, n2: str) -> str:
    res = ''
    n1 = is_number(n1)
    n2 = is_number(n2)
    if n1 and n2:
        try:
            if operator in ['rshift', 'lshift']:
                if isinstance(n1, int) and isinstance(n2, int):
                    res = str(operations[operator](n1, n2))
                else:
                    raise ValueError
            else:
                res = str(operations[operator](n1, n2))
        except ValueError:
            logger.warning('Invalid number!')
        except KeyError:
            logger.warning('No such operation!')
        except ZeroDivisionError:
            logger.warning('Zero division!')
    return res
