x = int(input("Add a number:"))
y = int(input("Add another number:"))

# abs for negativ numbers
x = abs(x)
y = abs(y)

# in case of "0"
if x == 0 or y == 0:
    print("No common divider.")
else:
    while x != y:
        if x > y:
            x = x-y
        else:
            y = y-x
    print(x)
