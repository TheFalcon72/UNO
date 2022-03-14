from Card import Card

def create_cards():
    deck = []

    for _ in range(4):
        for color in ["red", "green", "blue", "yellow"]:
            for number in range(1, 10):
                deck.append(Card(color, number, None))