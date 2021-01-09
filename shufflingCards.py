##
# Create a deck of cards and shuffle it.
#

from random import randrange


# Construct a standard deck of cards with 4 suits and 13 values per suit
# @return a list of cards, with each card represented by two characters


def create_deck():
    # Create a list to store the cards in
    cards = []

    # For each suit and each value
    for suit in ["s", "h", "d", "c"]:
        for value in ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]:
            # Construct the card and add it to the list
            cards.append(value + suit)

        # Return the complete deck of cards
        return cards

    # Shuffle a deck of cards, modifying the deck of cards passed as a parameter
    # @param cards the list of cards to shuffle


def shuffle(cards):
    # For each card
    for i in range(0, len(cards)):
        # Pick a random index
        other_pos = randrange(0, len(cards))

        # Swap the current card with the one at the random position
        temp = cards[i]
        cards[i] = cards[other_pos]
        cards[other_pos] = temp

    # Display a deck of cards before and after it has been shuffled


def main():
    cards = create_deck()
    print("The original deck of cards is: ")
    print(cards)
    print()

    shuffle(cards)
    print("The shuffled deck of card is: ")
    print(cards)


# Call the main program only if this file has not been imported
if __name__ == "__main__":
    main()
