# 'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠',
# 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥',
# 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦',
# 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣'
# playing card unicode: https://en.wikipedia.org/wiki/playing_cards_in_Unicode
import random


def playing_card():
    rank = list("A23456789") + ["10"] + list("JQK")
    suit = ("\u2660", "\u2665", "\u2666", "\u2663")
    # https: // en.wikipedia.org / wiki / Playing_cards_in_Unicode
    # deck = []
    # for s in suit:
    #     for r in rank:
    #         deck.append(r + s)

    deck = [r + s for s in suit for r in rank]
    deck2 = [(r, s) for s in suit for r in rank]
    # print(deck)
    # print(deck2)
    return deck


d = playing_card()
random.shuffle(d)
print(d)
