

#sys.argv: Access command-line arguments.
#int() converts a string or another numeric type to an integer.
#try-except Handle errors and exceptions.

import sys

# If more than one argument is provided or if the argument is not an integer, print an error message.
# If no argument is provided, do nothing or print an usage.

#no arg
if len(sys.argv) < 2:
    print("Usage: python3 whois.py <number>")
#more than one arg
elif len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
#convert to int
else:
    try:
        num = int(sys.argv[1])
    except ValueError:  # Only catch ValueError for invalid integer input
        print("AssertionError: argument is not an integer")
        sys.exit(1)  # Exit the program to avoid further checks if the conversion fails

    if num == 0: 
        print("I'm Zero.")
    elif num % 2 != 0:
        print("I'm Odd.")
    else:
        print("I'm Even.")