# calculator.py

def calc_input():
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")
    a = int(a)
    b = int(b)
    print("The numbers you entered are {} and {}".format(a, b))
    return a, b

def add(a, b):
    print("Add")
    answer = a + b
    print("{} + {} = {}".format(a, b, answer))

def subtract(a, b):
    print("Subtract")
    answer = a - b
    print("{} - {} = {}".format(a, b, answer))

def multiply(a, b):
    print("Multiply")
    answer = a * b
    print("{} * {} = {}".format(a, b, answer))
    
def divide(a, b):
    print("Divide")
    answer = a / b
    print("{} * {} = {}".format(a, b, answer))

def math_command(a, b):
    c = input("Enter a command: ")
    if c == "a":
        add(a, b)    
    elif c == "s":
        subtract(a, b)
    elif c == "m":
        multiply(a, b)
    elif c == "d":
        divide(a, b)
    else:
        print("{} is not a valid command".format(c))
        

x, y = calc_input()
math_command(x, y)

print("Finished")

