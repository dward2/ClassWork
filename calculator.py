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

def subtract():
    print("Subtract")
    print("More output")
    answer = a - b
    print("{} - {} = {}".format(a, b, answer))


def math_command(a, b):
    c = input("Enter a command: ")
    if c == "a":
        add(a, b)    
    elif c == "s":
        subtract()
    else:
        print("{} is not a valid command".format(c))
        

x, y = calc_input()
math_command(x, y)

print("Finished")

