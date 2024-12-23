#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer.
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# creating cards
SUITE = "H D S C".split()  # [H, D, S, C]
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()


class Deck:
    def __init__(self):
        # creating all cards
        self.allcards = [(s, r) for s in SUITE for r in RANKS]

    def shuffle(self):
        # shuffle cards
        shuffle(self.allcards)

    def split(self):
        # returning tuple of split cards (half, half)
        return (self.allcards[:26], self.allcards[26:])


class Hand:
    """
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    """

    def __init__(self, cards):
        self.cards = cards

    # when dealing with printing "Hand" object
    def __str__(self):
        # reporting how many cards that a player has
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove(self):
        return self.cards.pop()


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove()
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove())
        return war_cards

    def still_has_cards(self):
        """
        Return True if player still has cards left
        """
        return len(self.hand.cards) != 0


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Create new deck & split it in half:
d = Deck()
d.shuffle()
half1, half2 = d.split()


# Create both players:
comp = Player("computer", Hand(half1))

name = input("What is your name?")
user = Player(name, Hand(half2))


total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Time for a new round")
    print("Here are the current standings:")
    print(user.name + " has the count: " + str(len(user.hand.cards)))
    print(comp.name + " has the count: " + str(len(comp.hand.cards)))
    print("Play a card!\n")

    table_cards = []
    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    # War:
    if c_card[1] == p_card[1]:
        war_count += 1
        print("WAR!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        # high index of ranks = high number
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

    # Not war:
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)


print("Game over, Number of rounds is " + str(total_rounds))
print("WAR happened " + str(war_count) + " times")
