# Somethings wrong getting constant indent and capt errors that I am not executing.

def main():


# Problem 1
# Create a printNumbers function to print integers from -25 to 20 to the console (print in the function)

# def print_numbers():
#     x = range(-25,20)
#     for idx in x:
#         return idx



# Problem 2
# Create a function called checkPassword. Send two string variables to the checkPassword function to check if the strings are equal. Return true if they are equal and false if they are not equal. Print the function's return value.

def checkPassword():
    askUser = int(input("Enter Password: "))
    askUser2 = int(input("Enter another pw: "))
    if askUser == askUser2:
        return ("Correct")
    else:
        return(askUser2)

# Problem 3
#
# Write a function that determines if a number passed to it is odd or even. Pass a number of your choosing (using input a good idea) and then using the result from the function, print if the number was even or not.
#
# examples:
# The number 12 is an even number!
# The number 5 is an odd number!



























main()