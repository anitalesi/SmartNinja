print("Welcome to Fizzbuzz!")
while True:
    user = int(input("Add number between 1 and 100\n"))
    i = 1
    while user not in range(1, 101):
        user = int(input("Add number between 1 and 100\n"))
    for i in range(1, user+1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
    user = str(input("Would you like to add another? yes/no\n"))
    if user.lower() == "yes":
        continue
    else:
        break

print("Good-bye!")