#
# Concatenate one or more files, displaying the result.
#

import sys

# Ensure that at least one command line parameter (in addition to the .py file) has been provided

if len(sys.argv) == 1:
    print("You must provide at least one file name.")
    quit()

# Process all of the files provided on the command line
for i in range(1, len(sys.argv)):
    fname = sys.argv[i]
    try:
        # Open the current file for reading
        inf = open(fname, "r")

        # Display the file
        for line in inf:
            print(line, end="")

        # Close the file
        inf.close()

    except:
        # Display a message, but do not quit so that the program will go on to the process subsequent files
        print("Couldn't open/display", fname)