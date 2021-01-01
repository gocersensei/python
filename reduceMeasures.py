##
# Reduce an imperial measurement so that it is expressed
# using the largest possible units of measure. For example,
# 59 teaspoons is reduced to 1 cup, 3 tablespoons, 2 teaspoons.
#

TSP_PER_TBSP = 3
TSP_PER_CUP = 48

# Reduce an imperial measurement so that it is expressed using
# the largest possible units of measure.
# @param num the number of units that need to be reduced
# @param unit the unit of measure (cup, tablespoon or teaspoon)
# return a string representing the measurement in reduced form

def reduceMeasure(num, unit):
    # Compute the number of teaspoons that the parameters represent
    unit = unit.lower()

    if unit == "teaspoon" or unit == "teaspoons":
        teaspoons = num
    elif unit == "tablespoon" or unit == "tablespoons":
        teaspoons = num * TSP_PER_TBSP
    elif unit == "cup" or unit == "cups":
        teaspoons = num * TSP_PER_CUP
    # Convert the number of teaspoons to the largest possible
    # units of measure

    cups = teaspoons // TSP_PER_CUP
    teaspoons = teaspoons - cups * TSP_PER_CUP
    tablespoons = teaspoons // TSP_PER_TBSP
    teaspoons = teaspoons - tablespoons * TSP_PER_TBSP

    # Generate the result string
    result = ""

    # Add the number of cups to the result string (if any)

    if cups > 0:
        result = result + str(cups) + "cup"
        # make cup plural if there is more than one
        if cups > 1:
            result = result + "s"

    # Add the number of tablespoons to the result string (if any)
    if tablespoons > 0:
        # Include a comma if there were some cups
        if result != "":
            result = result + ", "

        result = result + str(tablespoons) + " tablespoon"
        # Make tablespoon plural if there is more than one
        if tablespoons > 1:
            result = result + "s"

    # Add the number of teaspoons to the result string (if any)
    if teaspoons > 0:
        # Include a comma if there were some cups and/or tablespoons
        if result != "":
            result = result + "s"

    # Handle the case where the number of units was 0
    if result == "":
        result = "0 teaspoons"

    return result

def launchNow():
    print("59 teaspoons is %s." % reduceMeasure(59, "teaspoons"))
    print("59 tablespoons is %s." % reduceMeasure(59, "tablespoons"))
    print("1 teaspoon is %s." % reduceMeasure(1, "teaspoon"))
    print("1 tablespoon is %s." % reduceMeasure(1, "tablespoon"))
    print("1 cup is %s." % reduceMeasure(1, "cup"))
    print("4 cups is %s." % reduceMeasure(4, "cups"))
    print("3 teaspoons is %s." % reduceMeasure(3, "teaspoons"))
    print("6 teaspoons is %s." % reduceMeasure(6, "teaspoons"))
    print("95 teaspoons is %s." % reduceMeasure(95, "teaspoons"))
    print("96 teaspoons is %s." % reduceMeasure(96, "teaspoons"))
    print("97 teaspoons is %s." % reduceMeasure(97, "teaspoons"))
    print("98 teaspoons is %s." % reduceMeasure(98, "teaspoons"))
    print("99 teaspoons is %s." % reduceMeasure(99, "teaspoons"))

# Call the main function
launchNow()