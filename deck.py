import random
import itertools

face_card = itertools.product(["Ace", "King", "Queen", "Jack"], [
                              "Spade", "Club", "Diamond", "Heart"])
normal_card = itertools.product(
    range(2, 11), ["Spade", "Club", "Diamond", "Heart"])

cards = list(face_card) + list(normal_card)

random.shuffle(cards)

print(len(cards))

for i in range(5):
    print(cards[i][0])
