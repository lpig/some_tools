import math

def roundup_int(x: int, num_digits: int) -> int:
    """
    round up like excel roundup
    向上取证方法，暂时只支持整数

    **One**::
        >>> num = roundup_int(123,-1)
        >>> num
        130

    """
    if num_digits > 0:
        raise TypeError(f'is over 0! digit:{num_digits}')

    num_digits = abs(num_digits)
    _num_digits = 1 * math.pow(10, num_digits)
    _num = x if x % _num_digits == 0 else x + _num_digits - x % _num_digits

    return int(_num)
