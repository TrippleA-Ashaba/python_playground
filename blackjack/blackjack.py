from art import logo
import random
import time

RULES = """
============================================================================ 
    Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.

=============================================================================

"""


def deal_card():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # jack, king and queen == 10

    card = random.choice(cards)
    return card


def computer():
    stack = list()
    stack.append(deal_card())
    stack.append(deal_card())
    return stack


def player():
    stack = list()
    stack.append(deal_card())
    stack.append(deal_card())
    return stack


def delay(n):
    dots = ""
    num_dots = n  # secs
    for _ in range(num_dots):
        dots += ". "
        print(dots, end="\r")
        time.sleep(1)


def main():
    print(logo)
    print()
    print(RULES)
    computer_cards = computer()
    player_cards = player()
    print(f"Dealers Cards: {computer_cards}")
    print(f"Your cards: {player_cards}")

    delay(2)

    print("================================================")
    print("Do you want to (S)tand, (H)it or (D)ouble down?")
    play = input("> ").strip().lower()

    if play == "s":
        computer_total = sum(computer_cards)
        if computer_total < 17:
            computer_cards.append(deal_card())
            computer_total = sum(computer_cards)
        player_total = sum(player_cards)
        if computer_total >= player_total and (computer_total <= 21):
            print(
                f"Computer Wins! : {computer_cards}:{computer_total} to {player_cards}: {player_total}"
            )
        else:
            print(
                f"You Win! : {player_cards}: {player_total} to {computer_cards}:{computer_total}"
            )

    # print(play)


if __name__ == "__main__":
    main()
