import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y


def divide(x, y):
    if y == 0:
        return "Division by zero not allowed."
    else:
        return x / y

def multiply(x, y):
    return x * y



#Extra Operations
def exponent(x, y):
    return x ** y

def square(x):
    return x ** 2

def square_root(x):
    if x < 0:
        return "Square root of a negative number is not a real number."
    else:
        return math.sqrt(x)

def factorial(x):
    if x < 0:
        return "Factorial not defined."
    elif x == 0:
        return 1
    else:
        return x * factorial(x - 1)

print("Calculator")
print("Select operation to perform==>")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")
print("6. Square")
print("7. Square Root")
print("8. Factorial")
print("9. Quit(Press q)")

while True:
    choice = input("Enter your choice==> ")
    
    if choice == 'q':
        break

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8'):
        num1 = float(input("Enter the number: "))
        
        if choice in ('1', '2', '3', '4', '5'):
            num2 = float(input("Enter the second number"))

        if choice == '1':
            print(f"The sum is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The difference is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The product is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The quotient is: {divide(num1, num2)}")
        elif choice == '5':
            print(f"The result of exponentiation is: {exponent(num1, num2)}")
        elif choice == '6':
            print(f"The square of {num1} is: {square(num1)}")
        elif choice == '7':
            print(f"The square root of {num1} is: {square_root(num1)}")
        elif choice == '8':
            print(f"The factorial of {num1} is: {factorial(int(num1))}")
    else:
        print("Invalid choice. Please choose a valid option.")
        
        
#Output
# Calculator
# Select operation to perform==>
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exponentiation
# 6. Square
# 7. Square Root
# 8. Factorial
# 9. Quit(Press q)
# Enter your choice==> 1
# Enter the number: 3
# Enter the second number4
# The sum is: 7.0

# Enter your choice==> 2
# Enter the number: 5
# Enter the second number2
# The difference is: 3.0

# Enter your choice==> 3
# Enter the number: 6
# Enter the second number7
# The product is: 42.0

# Enter your choice==> 4
# Enter the number: 8
# Enter the second number5
# The quotient is: 1.6

# Enter your choice==> 5
# Enter the number: 5
# Enter the second number3
# The result of exponentiation is: 125.0

# Enter your choice==> 6
# Enter the number: 54
# The square of 54.0 is: 2916.0

# Enter your choice==> 7
# Enter the number: 64
# The square root of 64.0 is: 8.0

# Enter your choice==> 8
# Enter the number: 7
# The factorial of 7.0 is: 5040

# Enter your choice==> 4
# Enter the number: 6
# Enter the second number0
# The quotient is: Division by zero not allowed.

# Enter your choice==> 7
# Enter the number: -6
# The square root of -6.0 is: Square root of a negative number is not a real number.      

# Enter your choice==> 8
# Enter the number: -3
# The factorial of -3.0 is: Factorial not defined.

# Enter your choice==> 9
# Invalid choice. Please choose a valid option.
# Enter your choice==> q