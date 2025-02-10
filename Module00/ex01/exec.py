#reverse characters in a string
#reverse alpha: uppercase to lowercase / lowercase to uppercase

#import sys Linke C's #include library
#sys.argv	Gets command-line arguments
#len(sys.argv)	Checks number of arguments
#print()	Displays output
#sys.exit(1)	Stops execution if no arguments are given
#" ".join(list)	Joins elements into a single string

#[start:end:step]: The general slicing format
#[start]: Where to start (optional).
#[end]: Where to stop (optional).
#[step]: The step or how much to move between each element (optional).

#string[:] -> Takes the entire string
#[1:] → Starts from the second element and goes to the end (used for excluding the first element).
#[::-1] → Reverses the sequence (used for flipping the order).
#step = -1: Means "go backwards"! Move through the string or list in reverse order.
#.swapcase()	Swaps uppercase/lowercase

# import sys

# if len(sys.argv[1:]) < 1:
#     # print("\n")
#     sys.exit(0)

# input = " ".join(sys.argv[1:])
# output = input[::-1].swapcase()
# print(output)


import sys

if len(sys.argv[1:]) >= 1:
    input = " ".join(sys.argv[1:])
    output = input[::-1].swapcase()
    print(output)
# sys.exit(0)