# Give some random 10 digit mobile number as user input using the input() 
# function and store it in a variable.
gvn_mobilenumb = input("Enter some random 10 digit mobile number = ")

# Check if the length of the given mobile number is greater than or less than 10
# using the if conditional statement
if len(gvn_mobilenumb) > 10 or len(gvn_mobilenumb) < 10:
    # If it is true then print "Invalid Mobile number. Mobile number must have 10 digits"
    print("Invalid Mobile number. Mobile number must have 10 digits")
else:
    # Else Check if first digit of the given mobile number is 7 or 8 or 9 using the if conditional statement
    if gvn_mobilenumb[0] == '7' or gvn_mobilenumb[0] == '8' or gvn_mobilenumb[0] == '9':
        # Handling the errors using the try-except blocks
        try:
            # If it is true, then convert the given mobile number to an Integer using the
            # int() function and store it in the same variable.
            gvn_mobilenumb = int(gvn_mobilenumb)
            # Print the given mobile number is a valid number
            print("The given mobile number is a Valid Number")
        except:
            # Print "Invalid Mobile number. Mobile number must not contain any characters"
            print('Invalid Mobile number. Mobile number must not contain any characters')
    else:
        # Else print "Invalid Mobile number. Mobile number must begin with 7 or 8 or 9"
        print("Invalid Mobile number. Mobile number must begin with 7 or 8 or 9")
