# Ernest Clark
# TS final Project
# 1/25/2022

taxes = 0


# use previously gathered info to get you total income for the past two weeks
def bi_weekly_salary(hours, wage=12.5):
    """

    :param wage: float: the hourly wage of the user
    :param hours: float or list: hours worked by user as a total or a list of days
    :return: income: float: total money earned before taxes
    """
    if type(hours) == list:
        condensed_hours = 0
        for i in hours:
            condensed_hours += i
        income = wage * condensed_hours
        return income
    else:
        income = wage * hours
        return income


# Request the user to input their hourage for everyday in the past two weeks or as a total based on their preference
def hour_grabber():
    """

    :return: hours: float: total number of hours the individual put in
    """
    global two_weeks_hours
    method_of_hours = input("do you know the total amount of hours you worked in the past two weeks or just "
                            "your daily hours (total/daily)\n")
    while method_of_hours.lower() != 'total' and method_of_hours.lower() != 'daily':
        method_of_hours = input("please input either daily or total\n")
    # gather users hour as a total for the past two weeks
    while "total" in method_of_hours:
        hours = input("please enter the total hours worked this week or quit to re-choose the method "
                      "by which you are inputting your hours\n")
        if hours == "quit":
            print("understood restarting process\n")
            hour_grabber()
        else:
            is_float = False
            # error check to confirm that the user inputs a str that typecasts to a float
            while not is_float:
                try:
                    hours = float(hours)
                except ValueError:
                    hours = input("please input your total hours as in number format (35.45)")
                else:
                    is_float = True
            else:
                return hours
    # gather users hours as individual days for the past two weeks
    while "daily" in method_of_hours:
        print("please enter your previous 14 days' hours or quit to re-choose the method "
              "by which you are inputting your hours\n")
        # ask for the hours worked for the past 14 day or two weeks
        for i in range(14):
            hours = input(f"Day {i + 1} hours\n")
            if hours == "quit":
                print("understood restarting process\n")
                hour_grabber()
                break
            else:
                is_float = False
                # error check to confirm that the user inputs a str that typecasts to a float
                while not is_float:
                    try:
                        hours = float(hours)
                    except ValueError:
                        hours = input("please input your total hours as in number format (35.45)")
                    else:
                        is_float = True
                    finally:
                        two_weeks_hours.append(hours)
        else:
            return


# take the users income and deduct the taxes they are paying based on state
def tax_reduction(total_earnings, *applicable_taxes):
    """

    :param total_earnings: float: total earnings before taxes in two weeks
    :param applicable_taxes: list: all the taxes that the individual will be paying
    :return: total_income: float: total earnings after taxes
    """
    global taxes
    condensed_taxes = 0
    # produce a total value from a list of individual daily hours
    for i in applicable_taxes:
        condensed_taxes += i
    taxes = total_earnings * condensed_taxes
    total_income = total_earnings - taxes
    return total_income


if __name__ == "__main__":
    two_weeks_hours = []
    state_income_taxes = {'Alabama': .02,
                          'Alaska': 0,
                          'Arizona': .0259,
                          'Arkansas': .02,
                          'California': .01,
                          'Colorado': .0455,
                          'Connecticut': .03,
                          'Delaware': .022,
                          'Florida': 0,
                          'Georgia': .01,
                          'Hawaii': .014,
                          'Idaho': .032,
                          'Illinois': .01125,
                          'Indian': .0495,
                          'Iowa': .0323,
                          'Kansas': .0033,
                          'Kentucky': .0310,
                          'Louisiana': .05,
                          'Maine': .02,
                          'Maryland': .058,
                          'Massachusetts': .02,
                          'Michigan': .05,
                          'Minnesota': .0535,
                          'Mississippi': .03,
                          'Missouri': .015,
                          'Montana': .01,
                          'Nebraska': .0246,
                          'Nevada': 0,
                          'New Hampshire': .05,
                          'New Jersey': .014,
                          'New Mexico': .017,
                          'New York': .04,
                          'North Carolina': .0525,
                          'North Dakota': .11,
                          'Ohio': .285,
                          'Oklahoma': .005,
                          'Oregon': .475,
                          'Pennsylvania': .307,
                          'Rhode Island': .375,
                          'South Carolina': 0,
                          'South Dakota': 0,
                          'Tennessee': 0,
                          'Texas': 0,
                          'Utah': .0495,
                          'Vermont': .0335,
                          'Virgina': .02,
                          'Washington': 0,
                          'West Virgina': .03,
                          'Wisconsin': .0354,
                          'Wyoming': 0
                          }
    print("This program will calculate your bi-weekly earnings while also taking into account taxes\n")
    redo = 'start over'
    # allow the user to run through the program multiple times
    while 'start over' in redo.lower() or 'change' in redo.lower():
        # allows the user to change individual elements of what you previously entered
        while redo == "change":
            changing = input('what would you like to change hours or pay\n')
            while changing != 'hours' and changing != 'pay':
                changing = input('please enter hours or pay\n')
            if changing == 'pay':
                pay = input('understood please re-enter your wage\n')
                is_float = False
                # error check to confirm that the user inputs a str that typecasts to a float
                while not is_float:
                    try:
                        pay = float(pay)
                    except ValueError:
                        pay = input("please input your wage in number format (35.45)\n")
                    else:
                        is_float = True
            if changing == 'hours':
                two_weeks_hours = []
                total_hours = hour_grabber()
            if len(two_weeks_hours) > 0:
                income = bi_weekly_salary(two_weeks_hours, pay)
            else:
                income = bi_weekly_salary(total_hours, pay)
            income_after_taxes = tax_reduction(income, .153, .062, .0145, state_income_taxes[state])
            print(f"Your Bi-Weekly earning accounting for taxes is approximately {round(income_after_taxes, 2)}$")
            print(f"You paid approximately {round(taxes, 2)}$ in taxes")
            redo = input("would you like to start over again or change some of the info you previously entered "
                         "or exit (start over/change/exit)\n")
            while redo != 'start over' and redo != 'change' and redo != 'exit':
                redo = input('please enter start over or change')
        # allows the user to completely restart the program and re-enter all the values
        while redo == "start over":
            two_weeks_hours = []
            total_hours = hour_grabber()
            pay = input("Please input your hourly wage\n")
            is_float = False
            # error check to confirm that the user inputs a str that typecasts to a float
            while not is_float:
                try:
                    pay = float(pay)
                except ValueError:
                    pay = input("Please input your hourly wage in number format (23.12)\n")
                else:
                    is_float = True
            if len(two_weeks_hours) > 0:
                income = bi_weekly_salary(two_weeks_hours, pay)
            else:
                income = bi_weekly_salary(total_hours, pay)
            state = input("what state do you live in (please select one within the US)\n")
            # make sure the users input is one of the 50 states
            while state not in state_income_taxes.keys():
                state = input("please input one of the 50 US states\n")
            income_after_taxes = tax_reduction(income, .153, .062, .0145, state_income_taxes[state])
            print(f"Your Bi-Weekly earning accounting for taxes is approximately {round(income_after_taxes, 2)}$")
            print(f"You paid approximately {round(taxes, 2)}$ in taxes")
            redo = input("would you like to start over again or change some of the info you previously entered "
                         "or exit (start over/change/exit)\n")
            while redo != 'start over' and redo != 'change' and redo != 'exit':
                redo = input('please enter start over or change')
    else:
        input("Program exiting please click enter to complete process")
