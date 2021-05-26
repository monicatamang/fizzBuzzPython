# Creating a function that checks whether a number is divisble by 3, 5, both or not at all
def check_if_divisble(test_number):
    # If the number is divisble by 3 and not divisble by 5, print "Fizz" to the terminal
    if(test_number % 3 == 0 and test_number % 5 != 0):
        print("Fizz")
    # If the number is divisble by 5 and not divisble by 3, print "Buzz" to the terminal
    elif(test_number % 5 == 0 and test_number % 3 != 0):
        print("Buzz")
    # If the number is divisble by both 3 and 5, print "FizzBuzz" to the terminal
    elif(test_number % 3 == 0 and test_number % 5 == 0):
        print("FizzBuzz")
    # If the number is not divisble by either 3 or 5, print a message to the terminal
    else:
        print(f"{test_number} is not divisble by 3 or 5")

# Creating an array of 15 numbers
numbers = [3, 5, 15, 18, 21, 29, 33, 36, 54, 65, 72, 80, 88, 94, 100]
# For each number in the array, call the function to check whether it is divisble by 3, 5, both or not at all
for number in numbers:
    is_divisble = check_if_divisble(number)