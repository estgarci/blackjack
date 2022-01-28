from random import Random


class Game:
    def __init__(self, players, points):
        self.players = []
        for _ in range(0, players):
            self.players.append(Player(points))
        self.__make_deck()
        self.dealer = Dealer()

    def __make_deck(self):
        self.deck = Deck()

    def get_players(self):
        pass

    def print_score(self):
        for i, player in enumerate(self.players):
            print('player ' + i + ':', player.points)


class Player:
    def __init__(self, points):
        self.points = points
    hands = []

    def add_hand(self, card) -> list:

        self.hands.append(Hand(card))

    def bet(self, ammount: int) -> int:
        if (ammount <= self.points):
            self.points -= ammount
            return ammount
        else:
            return None


class Dealer():
    hands = []
    add_hand = Player.add_hand


class Hand:
    def __init__(self, cards):

        if type(cards) == list:
            self.cards = [card for card in cards]
        else:
            self.cards = [cards]

    def __len__(self) -> int:
        return len(self.cards)

    def __repr__(self) -> str:
        return '<Hand>'

    def add_card(self, cards):

        if type(cards) == list:
            for card in cards:
                self.cards.append(card)
        else:
            self.cards.append(cards)

    def sum(self):
        return sum(self.cards)


class Deck:
    def __init__(self):
        suits = ['club', 'diamond', 'heart', 'spade']
        ranks = [str(number) for number in range(
            1, 10)]
        ranks.extend(['A', 'J', 'Q', 'K'])
        cards = list()
        for suit in suits:
            for rank in ranks:
                color = 'red' if (suit == 'diamond' or suit ==
                                  'heart') else 'black'
                cards.append(Card(color, suit, rank))

        self.cards = cards

    def __len__(self) -> int:
        return len(self.cards)

    def draw(self, ammount=1):
        if (len(self) >= ammount):
            rand = Random()
            index = rand.randint(0, len(self) - 1)
            if ammount == 1:
                return self.cards.pop(index)
            else:
                return_cards = []
                for _ in range(ammount):
                    return_cards.append(self.cards.pop(index))
                return return_cards
        else:
            return []


class Card:
    def __init__(self, color: str, suit: str,  rank: str) -> None:
        self.suit = suit
        self.color = color
        self.rank = rank
        self.value = int(rank) if rank.isnumeric() else 10

    def __add__(self, other_card):
        return self.value + other_card

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __str__(self) -> str:
        return self.color + ' ' + self.suit + ' ' + self.rank

    def __repr__(self) -> str:
        return '<Card> ' + self.color + ' ' + self.suit + ' ' + self.rank


# # creating game
# game = Game(players=2, points=10000)


# deck = Deck()

# # creating player


# # creating first hand
# game.players[0].add_hand(deck.draw(1))

# # adding an extra card to players hand
# game.players[0].hands[0].add_card(deck.draw(1))

# # deck should now be 52 cards
# assert len(deck) == 50

# game.players[0].bet(200)

# assert game.players[0].points == 9800

# game.dealer.add_hand(deck.draw(1))

# print(game.dealer.hands[0].cards)
# # print player's hand and value
# # print('cards: ', player_1.hands[0].cards)
# # print('value: ', sum(player_1.hands[0].cards))
