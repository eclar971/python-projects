# Ernest Clark
# Weather cyo project 7
# 1/19/2022

import requests
import pydoc

# apply user inputs to the url and request from the api
def user_input(location, unit):
    """
    :param location: string, where you would like to look up
    :param unit: string, the unit system you'd like to use
    :return r: class, api request for the previously inputted
    """
    global par
    par["q"] = location
    par["units"] = unit
    r = requests.get(url, params=par)
    return r


if __name__ == '__main__':
    api_key = "02d98d190b69f1cfe1f71d667ac770be"
    url = "http://api.openweathermap.org/data/2.5/weather/"
    par = {
        "q": "",
        "appid": api_key,
        "units": ""
    }
    acceptable_units = ['standard', 'metric', 'imperial']
    redo = "y'"
    # Allows for multiple runs of the program to happen
    while "y" in redo:
        user_location = input("Please enter the city that you'd like to look up the current weather for?\n")
        if user_location != user_location.capitalize():
            user_location = user_location.capitalize()
        user_units = input("Please enter the unit system that you'd like to use (default is imperial)"
                           " or type help for a list of applicable "
                           "units?\n")
        # Check and allow for corrections to the requested unit type
        while user_units.lower() not in acceptable_units or "help" in user_units.lower():
            if user_units == "":
                user_units = "imperial"
            else:
                print(f"heres a list or acceptable units {acceptable_units}")
                user_units = input("Please enter the unit system that you'd like to use (default is imperial) or type "
                                   "help for a list of applicable "
                                   "units?\n")
        else:
            user_units = user_units.lower()
        req = user_input(user_location, user_units)
        # allows you to re-enter city if there is an error at a api status level
        while req.status_code != 200:
            b = req.json()
            print(b["message"])
            if "city" in b["message"] or "geo" in b["message"]:
                user_location = input("Please enter the city that you'd like to look up the current weather for?\n")
                if user_location != user_location.capitalize():
                    user_location = user_location.capitalize()
            req = user_input(user_location, user_units)
        b = req.json()
        # convert unit name to preferred abbreviation
        if user_units == "imperial":
            user_units = "°f"
        elif user_units == "metric":
            user_units = "°c"
        elif user_units == "standard":
            user_units = "K"
        print(f"\nRequested location {b['name']} in {user_units}")
        print(f"    Current temperature is {b['main']['temp']} {user_units}")
        print(f"    It currently feels like {b['main']['feels_like']} {user_units}")
        print(f"    The lowest the temperature today will be {b['main']['temp_min']} {user_units}")
        print(f"    the highest the temperature today will be {b['main']['temp_max']} {user_units}")

        redo = input("\nwould you like to check another location? (y/n)\n")
        print(type(req))
    else:
        pydoc.help(user_input)
        input("program closing please press enter to finish process")


