import pytest

from src import helpers as h


# kelvin_to_celsius() tests
def test_kelvin_to_celsius_zero_kelvin():
    expected_temperature = -273

    temperature = h.kelvin_to_celsius(0)

    assert temperature == expected_temperature


def test_kelvin_to_celsius_zero_celsius():
    expected_temperature = 0

    temperature = h.kelvin_to_celsius(273.15)

    assert temperature == expected_temperature


def test_kelvin_to_celsius_ten_celsius():
    expected_temperature = 10

    temperature = h.kelvin_to_celsius(283.15)

    assert temperature == expected_temperature


def test_kelvin_to_celsius_incorrect_argument_type():
    with pytest.raises(TypeError) as e:
        h.kelvin_to_celsius("incorrect type")

    assert str(e.value) == \
        "Incorrect argument type of k_degrees. " \
        "Expected <class 'int'> or <class 'float'>, " \
        "got <class 'str'> instead!"


def test_kelvin_to_celsius_kelvin_below_zero():
    with pytest.raises(ValueError) as e:
        h.kelvin_to_celsius(-1)

    assert str(e.value) == \
        "Incorrect value of k_degrees. k_degrees cannot be lower than 0!"


# timestamp_to_time() tests
def test_timestamp_to_time_correct():
    expected_time = "21:55"

    converted_time = h.timestamp_to_time(1625342136)

    assert converted_time == expected_time


def test_timestamp_to_time_incorrect_argument_type():
    with pytest.raises(ValueError) as e:
        h.timestamp_to_time("incorrect type")
    assert str(e.value) == "Incorrect argument type of timestamp. " \
        f"Expected {int}, got {str} instead!"
