while True:
    n = int(input("Please choose a number\n"))
    x = 1
    result = 0

    for x in range(1, n):
        if n % x == 0:
            result = result+x
    if result > n:
            print("Abundant number")
            print("Abundance:" + str(result-n))
    else:
        print("Not abundant number")
    user = str(input("Would you like to choose another? yes/no\n"))
    if user.lower() == "yes":
        continue
    else:
        break

