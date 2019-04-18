import random
import json
import datetime

current_time = datetime.datetime.now()
print(current_time)

secret = random.randint(1, 30)
attempts = 0


with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print(str(score_list))

score_file.close()

sorted_score_list = sorted(score_list, key=lambda kv: kv['attempts'])[:3]

player = str(input("What's your name? "))

for score_dict in sorted_score_list:
    print(score_dict["player_name"] + " has attempts " + str(score_dict["attempts"])
          + " date: " + str(score_dict.get("date")) + " secret_number: " + str(score_dict["secret_number"])
          + " wrong_guesses: " + str(score_dict["wrong_guesses"]))

wrong_guesses = []

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "player_name": player,
                           "secret_number": secret, "wrong_guesses": wrong_guesses})

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
    wrong_guesses.append(guess)
