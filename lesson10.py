# Try and Except

# try:
#     age = int(input("Enter your age: "))
#     print(f"You are {age} years old.")
# except ValueError:
#     print("Please enter a valid number.")
#     # If no exception occured
# else:
#     print(f"Next year, you'll be {age + 1}.")

try: 
    first_number = int(input("Kindly enter your first number: "))
    second_number = int(input("Kindly enter your second number: "))
    print(first_number + second_number)
    print(first_number - second_number)
    print(first_number * second_number)
    print(first_number // second_number)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
        print("Sorry, you can't divide by zero")