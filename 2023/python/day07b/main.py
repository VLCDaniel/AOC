import os
from collections import defaultdict

f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), "r")
input_data = f.read()
f.close()

input_data = input_data.split('\n')
A = [line.split() for line in input_data]

def hand_value(hand):
    joker = chr(ord('9') - 8)
    hand = hand.replace('T', chr(ord('9') + 1))
    hand = hand.replace('J', joker)
    hand = hand.replace('Q', chr(ord('9') + 3))
    hand = hand.replace('K', chr(ord('9') + 4))
    hand = hand.replace('A', chr(ord('9') + 5))
    
    cards = defaultdict(int)
    for card in hand:
        cards[card] += 1

    count = list(cards.values())
    count.sort()

    if joker in cards.keys() and cards[joker] < 5:
        count.remove(cards[joker])
        count[-1] += cards[joker]

    if count == [5]: # Five of a kind
        return (7, hand)
    elif count == [1,4]: # Four of a kind
        return (6, hand)
    elif count == [2,3]: # Full house
        return (5, hand)
    elif count == [1,1,3]: # Three of a kind
        return (4, hand)
    elif count == [1,2,2]: # Two pair
        return (3, hand)
    elif count == [1,1,1,2]: # One pair
        return (2, hand)
    elif count == [1,1,1,1,1]: # High card
        return (1, hand)
    assert False, "FAILED TO CALCULATE STRENGHT OF HAND:{hand}"
            

A = sorted(A, key=lambda hb:hand_value(hb[0]))
sum = 0
for i, (_, b) in enumerate(A):
    sum += int(b) * (i + 1)
print(sum)
