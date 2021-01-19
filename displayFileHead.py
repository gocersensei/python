#
# Display the head (first 10 lines) of a file whose name is
# provided as a command line parameter

import sys

NUM_LINES = 10

# Verify that exactly one command line parameter (in addition to
# the .py file) was supplied


if len(sys.argv) != 2:
    print("You must provide the file name as a command line parameter.")
    # When the quit function is called the program ends immediately.
    quit()

try:
    # Open the file for reading
    inf = open(sys.argv[1],'r')

    # Read the first line from the file
    line = inf.readline()

    # Keep looping until we have either read and displayed
    # 10 lines or we have reached the end of the file

    count = 0
    while count < NUM_LINES and line != "":
        # Remove the trailing newline character and count the line
        line = line.rstrip()
        count = count + 1

        # Display the line
        print(line)

        # Read the next line from the file
        line = inf.readline()

    # Close the file
    inf.close()

except IOError:
    # Display a message if something goes wrong while accessing the file.
    print("An error occurred while accessing the file.")