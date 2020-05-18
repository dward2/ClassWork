# calculator.py
a = input("Enter the first number: ")
b = input("Enter the second number: ")
a = int(a)
b = int(b)
print("The numbers you entered are {} and {}".format(a, b))

c = input("Enter a command: ")

if c == "a":
    print("Add")
    answer = a + b
    print("{} + {} = {}".format(a, b, answer))
elif c == "s":
    print("Subtract")
    answer = a - b
    print("{} - {} = {}".format(a, b, answer))
elif c == "m":
    print("Multiply")
    answer = a * b
    print("{} * {} = {}".format(a, b, answer))
elif c == "d":
    print("Divide")
    answer = a / b
    print("{} / {} = {}".format(a, b, answer))
else:
    print("{} is not a valid command".format(c))
    
print("Finished")

