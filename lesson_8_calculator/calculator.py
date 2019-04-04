x = float(input("Add a number"))

y = float(input("Add another number "))

operation = str(input("Choose Operation: +, -, * or /"))

while operation not in ("+","-","*","/"):
    print("Incorrect operator.")

    operation = str(input("Please choose from: +, -, *, /"))

if operation == "+":
    print(x+y)
elif operation == "-":
    print(x-y)
elif operation == "*":
    print(x*y)
elif operation == "/":
    print (x/y)