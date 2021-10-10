import random

from art import logo, vs
from game_data import data

from os import system

def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f'{account_name}, a {account_descr}, from {account_country}'

def check_answer(guess, a_follower, b_follower):
    """Takes the user guess and follower counts and return of they got it right"""
    if a_follower > b_follower:
        return guess == 'a'
    else:
        return guess == 'b'

print(logo)
score = 0
account_b = random.choice(data)
game_should_continue = True

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f'Compare A: {format_data(account_a)}.')
    print(vs)
    print(f'Against B: {format_data(account_b)}.')

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_account = account_a['follower_count']
    b_follower_account = account_b['follower_count']

    is_correct = check_answer(guess=guess, a_follower=a_follower_account, b_follower=b_follower_account)

    system('cls')
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False


