print("Greetings!")

while True:
    km = float(input("Please enter numbers of kilometer:"))
    mile = 0.6 * km
    print(mile)
    user = str(input("would you like to add another? yes/no:"))
    if user.lower() == "no":
        break
print("Good-bye!")






