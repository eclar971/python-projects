# Ernest Clark
# Sys project number 1
# 2/1/22

import sys

print("please input you age")
# this is similar to input but it will repeat indefinitely
for user_input in sys.stdin:
    if user_input.rstrip().isdigit():
        # similar to print this will type the following line to the console
        sys.stdout.write("you are " + user_input + "years old\n")
    else:
        # this will print to the console but instead of being in basic white font it will be red indicating an error
        print("this shows an error because you inputted a string", file=sys.stderr)