#
# Display the tail (last lines) of a file whose name is
# provided as a command line parameter.
#

import sys

NUM_LINES = 10

# Verify that exactly one command line parameter (in addition
# to the .py file) was provided

if len(sys.argv) != 2:
    print("The file name must be provided as a command line parameter.")
    quit()

    try:
        # Open the file for reading
        inf = open(sys.argv[1],"r")

        # Read through the file, always saving the NUM_LINES most recent lines
        lines = []
        for line in inf:
            # Add the most recent line to the end of the list
            lines.append(line)
            # If we now have more than NUM_LINES lines then remove the oldest one
            if len(lines) > NUM_LINES:
                lines.pop(0)

        # Close the file
        inf.close()

    except:
        print("An error occurred while processing the file.")
        quit()

    # Display the last lines of the file
    for line in lines:
        print(line, end="")
