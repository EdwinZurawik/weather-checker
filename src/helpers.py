import math
import datetime
from typing import Union


def kelvin_to_celsius(k_degrees: Union[int, float]) -> int:
    """Returns kelvins converted to celsius

    :param k_degrees: temperature in kelvins
    :type k_degrees: float

    :return: temperature converted to celsius without the fractional part
    :rtype: int
    """
    MIN_TEMP_KELVIN=0
    K_C_RATIO = 273.15

    if not isinstance(k_degrees, (int, float)):
        raise TypeError("Incorrect argument type of k_degrees. "
                        f"Expected {int} or {float}, "
                        f"got {type(k_degrees)} instead!")
    if k_degrees < MIN_TEMP_KELVIN:
        raise ValueError("Incorrect value of k_degrees. "
                         f"k_degrees cannot be lower than {MIN_TEMP_KELVIN}!")

    celsius = int(k_degrees - K_C_RATIO)
    return celsius


def timestamp_to_time(timestamp):
    time = datetime.datetime.fromtimestamp(timestamp).strftime("%H:%M")
    return time



