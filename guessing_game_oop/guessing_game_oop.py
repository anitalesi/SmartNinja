import random
import json
import datetime


class Result():  # class
    def __init__(self, player_name, score):
        self.date = datetime.datetime.now()
        self.player_name = player_name
        self.score = score


def play_game(player_name, level):
    secret = random.randint(1, 30)
    score = 0

    while True:
        guess = int(input("Please guess the secret number between 1 and 30"))
        score += 1
        result_list = get_score()
        result = Result(player_name, score)  # das Objekt

        result_list.append({player_name, datetime.datetime.now(), score})

        with open("result.txt", "w") as result_file:  # das Objekt wird in eine json Datei gespeichert
            json.dump(result.__dict__, result_file, default=str, indent=3)  # json string

        if guess == secret:
            print("You have guessed it {}!".format(player_name))
            break

        elif guess > secret:
            if level.lower() == "easy":
                print("Your guess is not correct ... try something smaller:")
            else:
                print("Try something else:")

        elif guess < secret:
            if level.lower() == "easy":
                print("Your guess is not correct ... try something bigger:")
            else:
                print("Try something else:")
    return score


def get_score():
    with open("result.txt", "r")as read_file:
        score = json.load(read_file)
    return score


def print_score():
    result_list = get_score()
    print(result_list)


def user_input():
    player_name = str(input("What's your name?"))

    while True:
        selection = input("Would you like to play a new game? a), would you like to see the score? b) quit? c)")

        if selection.lower() == "a":
            difficulty = str(input("Please select the difficulty: easy/hard"))
            score = play_game(player_name, difficulty)    # score wird als variable ausgeführt
            result = Result(player_name, score)           # das Objekt

            with open("result.txt", "w") as result_file:  # das Objekt wird in eine json Datei gespeichert
                json.dump(result.__dict__, result_file, default=str, indent=3)  # json string

        elif selection.lower() == "b":
            with open("result.txt", "r") as read_file:
                result = json.load(read_file)
                print(result)

        else:
            print("goodbye!")
            break


if __name__ == "__main__":
    user_input()
