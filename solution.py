#Display the art
from art import logo, vs
from game_data import data
import random

def format_data(account):
    """format the account data into printable format"""
    account_name = account_a["name"]
    account_descr = account_a["description"]
    account_country = account_a["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)


#make the game repeatable
while game_should_continue:
    #generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    #ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #clear the screen
    print("\n" * 20)
    print(logo)

    ##get follower count of each accounr
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # check if it is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)


    ##use if statement to check if user is correct.


    # give user feedback on their quess.
    #score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, thet's wrong. Final score: {score}")
        game_should_continue = False
