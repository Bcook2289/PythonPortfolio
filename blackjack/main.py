import random
from time import sleep

deck = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suit = [' of Hearts', ' of Diamonds', ' of Clubs', ' of Spades']

hand = []
card = []


def create_deck():

    for d in deck:
        for s in suit:
            card.append(d + s)

    return card


def deal_card(game_deck):

    deal_hand = []
    if len(game_deck) > 48:
        for x in range(2):
            h = random.choice(game_deck)
            i = game_deck.index(h)
            game_deck.pop(i)
            deal_hand.append(h)

        return deal_hand

    else:
        c = random.choice(game_deck)
        i = game_deck.index(c)
        game_deck.pop(i)

        return c


def get_total(d_hand):
    total = 0
    for d in range(len(d_hand)):
        total += card_dict[d_hand[d]]
        if total < 21 and "Ace" in d_hand[d]:
            total += 10
            if total > 21:
                total -= 10

    return total


def display_cards(d_hand):
    cards = f"{d_hand[0]}"
    if len(d_hand) > 2:
        for h in range(1, len(d_hand)):
            cards += f", {d_hand[h]}"
        return cards
    else:
        return f"{d_hand[0], d_hand[1]}"


def new_game():
    c = create_deck()
    card_value = []
    for x in range(1, 14):
        for i in range(1, 5):
            if x > 10:
                card_value.append(10)
            else:
                card_value.append(x)

    c_dict = dict(zip(c, card_value))
    return c_dict


card_dict = new_game()

user_hand = deal_card(game_deck=card)
comp_hand = deal_card(game_deck=card)
comp_turn = "y"
play = input("Do you want to play a game of blackjack? type 'y' or 'n': ").lower()

while play == 'y':
    user_total = get_total(user_hand)
    comp_total = get_total(comp_hand)
    print(f"Computer has: Face and {comp_hand[1]}")
    print(f"You have: {display_cards(user_hand)}")

    if user_total == 21:
        play = 'n'
        sleep(1)
        break
    elif user_total > 21:
        play = 'n'
        sleep(1)
        break

    print(f"Total: {user_total}.")

    user_response = input(f"Hit?\nY/N ").lower()

    if user_response == 'y':
        user_hand.append(deal_card(game_deck=card))
        print(display_cards(user_hand))
        user_total = get_total(user_hand)
    elif user_response == 'n':
        play = 'n'
        sleep(1)
    else:
        print("Invalid input")
    print(f"User total: {user_total}")

while comp_turn:
    print(f"Computer: {display_cards(comp_hand)}")
    print(f"Computer Total: {comp_total}")
    if comp_total == 21:
        comp_turn = 'n'
        sleep(1)
        break
    elif comp_total > 21:
        comp_turn = 'n'
        sleep(1)
        break
    elif comp_total > 16:
        comp_turn = 'n'
        sleep(1)
        break
    elif user_total > 21:
        comp_turn = 'n'
        sleep(1)
        break
    else:
        print("Computer hits")
        comp_hand.append(deal_card(game_deck=card))
        comp_total = get_total(comp_hand)
        sleep(1)

if user_total > 21:
    print("You lose")
elif comp_total > 21:
    print("You win!")
elif user_total < comp_total:
    print("You lose.")
elif user_total == comp_total:
    print("Draw")
else:
    print("You win!")
