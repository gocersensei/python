# Check whether or not a password is good
# A good password is at least 8 characters
# long and contains an uppercase letter, a lower case letter and a number
# @param password the password to check
# @return True if the password is good, False otherwise

def check_password(password):
    has_upper = False
    has_lower = False
    has_num = False

    # Check each character in the password and see which requirement it meets
    for ch in password:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_num = True
    # If the password has all 4 properties
    if len(password) >= 8 and has_upper and has_lower and has_num:
        return True
    # The password is missing at least one property
    return False

    # Demonstrate the password checking function


def main():
    p = input("Enter a password: ")
    if check_password(p):
        print("That's a good password.")
    else:
        print("That isn't a good password.")


# Call the main function only if the files has not been imported into another program

if __name__ == "__main__":
    main()
