#!/usr/bin/env python3

import os
import requests
import argparse
from dotenv import load_dotenv
from typing import Dict, Optional
from src import helpers as h


path_to_env = os.path.abspath(__file__ + "/../../.env")
load_dotenv(path_to_env)

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("WEATHER_API_KEY")

DEEGREE_SIGN = u"\u00b0"


def _parse_commandline_arguments() -> argparse.Namespace:
    """Parses commandline arguments and returns argparse.Namespace

    :return: argparse.Namespace
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(
        description="Commandline weather checker",
        prog="weather-checker")

    parser.add_argument("city")
    parser.add_argument(
        "-l",
        "--long",
        action="store_true",
        help="show more detailed weather information")

    # TODO: add date parameter
    args = parser.parse_args()
    return args


def _build_request_url(
        base: str,
        params_dict: Dict[str, str]) -> str:
    """Returns an URL combined from base and parameters

    :param base: base url
    :type base: str

    :param params_dict: dictionary of parameter names and values
    :type params_dict: Dict[str, str]

    :return: a complete url
    :rtype: str
    """
    parameters = "&".join([f"{k}={v}" for k, v in params_dict.items()])
    url = base + "?" + parameters
    return url


def _send_request(request_url: str) -> Optional[dict]:
    """Sends request to the specified URL and returns a dictionary
    containing the response

    :param request_url: url to which the request will be sent
    :type request_url: str

    :return: response in a form of a dictionary or None if the response status
        code is 404 or 401
    :rtype: Optional[dict]

    :raises: ValueError when incorrect response status code
    """
    response = requests.get(request_url)

    if response:
        return response.json()
    else:
        if response.status_code == 404:
            print("\nWeather information not found.\n")
        elif response.status_code == 401:
            print("\nValidation error, please contact the developer.")
        else:
            raise ValueError(f"Invalid response code: {response.status_code}!")
        return None


def _get_weather_data_from_response(response: dict) -> Dict[str, str]:
    """Returns dictionary containing weather information

    :param response: response dictionary
    :type response: dict

    :return: dictionary with weather information
    :rtype: Dict[str, str]
    """
    temperature_k = float(response["main"]["temp"])

    weather = {}
    weather["temp_c"] = str(h.kelvin_to_celsius(temperature_k))

    weather["weather"] = response["weather"][0]["main"].lower()
    weather["humidity"] = response["main"]["humidity"]
    weather["pressure"] = response["main"]["pressure"]
    weather["sunrise"] = h.timestamp_to_time(response["sys"]["sunrise"])
    weather["sunset"] = h.timestamp_to_time(response["sys"]["sunset"])
    weather["country"] = response["sys"]["country"]
    return weather


def _print_weather_information(
        weather: Dict[str, str],
        long: bool = False) -> None:
    """Prints weather information

    :param weather: dictionary with weather information
    :type args: Dict[str, str]

    :param long: print weather in long format if True, default False
    :type long: bool

    :rtype: None
    """
    sunrise_icon = u"\U0001F305"
    moon_icon = u"\U0001F315"
    if long:
        print(f"\n{weather['city']}({weather['country']}) "
              f"| {weather['weather']}\n\n"
              f"Temperature: {weather['temp_c']}{DEEGREE_SIGN}C\n"
              f"Humidity: {weather['humidity']}%\n"
              f"Pressure: {weather['pressure']}hPa\n\n"
              f"{sunrise_icon} {weather['sunrise']} | "
              f"{moon_icon} {weather['sunset']} \n")
    else:
        print(f"\n{weather['city']}({weather['country']}) "
              f"| {weather['weather']} | "
              f"{weather['temp_c']}{DEEGREE_SIGN}C\n")


def main():
    args = _parse_commandline_arguments()

    request_params = {
        "q": args.city,
        "appid": API_KEY
    }
    request_url = _build_request_url(BASE_URL, request_params)
    response = _send_request(request_url)
    if not response:
        return
    weather = _get_weather_data_from_response(response)
    weather["city"] = args.city
    _print_weather_information(weather, long=args.long)


if __name__ == "__main__":
    main()
