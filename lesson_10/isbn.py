number = int(input("Please choose a 10-digit ISBN"))

digit = 0
i = 1
isbn = 0

for i in range(1, 11):
    digit = number % 10
    isbn = isbn + i*digit
    print(digit)
    number //= 10

if isbn % 11 == 0:
    print("Valid.")
else:
    print("Invalid")

