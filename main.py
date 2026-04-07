# Make sure art.py is in the same directory


import art
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def game_data():
    global user_cards, comp_cards, user, comp
    user_cards = []
    comp_cards = []

    user = 0
    comp = 0

    user_cards.append(deal_card())
    comp_cards.append(deal_card())
def game_logic():
    global comp, user
    user_cards.append(deal_card())
    if 11 in user_cards:
        ace_checker()
    comp_cards.append(deal_card())

    user = sum(user_cards)
    comp = sum(comp_cards)

    user_ask()

def ace_checker():
    global user, user_cards
    user_cards.remove(11)
    while True:
        ask_user = input("You have Ace in your deck, to what you want to change it 11 or 1? ")
        if ask_user == "11":
            user_cards.append(11)
            break
        elif ask_user == "1":
            user_cards.append(1)
            break
        else:
            print("Invalid input, try again")
    user = sum(user_cards)
def user_ask():
    global user, comp, user_cards

    while True:
        print(f"Your cards: {user_cards}\nComputer's cards: {comp_cards}")
        if user >= 21 or comp >= 21:
            calculate_score()
            break

        ask = input("Do you want a new card or it is enough? (yes/enough): ")

        if ask == "yes":
            new_card = deal_card()
            user_cards.append(new_card)
            if new_card == 11:
                ace_checker()
            user = sum(user_cards)

        elif ask == "enough":
            while comp < user and comp < 21:
                comp_cards.append(deal_card())
                comp = sum(comp_cards)

            calculate_score()
            break

        else:
            print("Invalid input, try again")

def game_over():
    while True:
        want = input("\nDo you want to play again?(yes/no): ")
        if want == "yes":
            game_data()
            game_logic()
            break
        elif want == "no":
            print("See you later!")
            break
        else:
            print("Invalid input, please try again!")

def calculate_score():
    print(f"\n\n\nYour cards: {user_cards}\nComputer's cards: {comp_cards}\n")
    if user > 21:
        print("You lost!")
    elif comp > 21:
        print("Congratulations you won!")
    elif user == comp:
        print("It is a draw!")
    elif user == 21:
        print("Congratulations you won!")
    elif comp == 21:
        print("You lost!")
    elif user > comp:
        print("Congratulations you won!")
    else:
        print("You lost!")

    game_over()

print(art.logo)
print("Welcome to blackjack!")
game_data()
game_logic()
