from game_data import data
from random import choice
from art import vs, logo
from os import name, system


# 2 - logo print
def title():
    # define clear function
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    clear()
    print(logo)


# 1: get 2 random choice from data
def get_account(data: list):
    """
    Get random account from game data.

    :param:
        data : list
            Game data

    :return:
        account : dict
            Return a new account from x
    """
    new_account = (choice(data))
    return new_account


# 3 - format a screen output of x account
def formatted_question(account: dict, s: str):
    """
    Returns a question formatted string for output

    :param:
        account : dict
            x account
        s : str
            A or B for the question

    :return:
        str
            Formatted string for output
    """
    return f"Compare {s}: {account['name']} a {account['description']} from {account['country']}"


# 4 - compare persons followers with the answer
def check_answer(x_account_a, x_account_b, answer):
    """
    Compare followers for person / organization

    :param:
        x_account_a : int
            follower_count
        twitter_account_b : int
            follower_count

    :return:
        bool
    """
    if x_account_a > x_account_b and answer == "a":
        return True
    elif x_account_a < x_account_b and answer == "b":
        return True
    return False


def game():
    """
    The game
    """
    score = 0
    answer = ""
    continue_game = True
    x_account_a = get_account(data)
    while continue_game:
        title()
        if answer != "":
            print(f"You got it rigth. Score {score}")
        x_account_b = get_account(data)
        print(formatted_question(x_account_a, "A"))
        print(vs)
        print(formatted_question(x_account_b, "B"))
        answer = input("\nWho have more followers? Type 'A' or 'B' ").lower()
        if check_answer(x_account_a=x_account_a["follower_count"],
                        x_account_b=x_account_b["follower_count"], answer=answer):
            score += 1
            if answer == "b":
                x_account_a = x_account_b
        else:
            title()
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_game = False


game()
