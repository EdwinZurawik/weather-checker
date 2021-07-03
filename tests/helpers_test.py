import pytest

from src import helpers as h


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
