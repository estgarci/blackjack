from player import *

# creating game board
game = Game(players=1, points=10000)

# creating deck
deck = Deck()

while(True):

    print('**********BLACKJACK**********')
    print('=============================')
    print('Point balance:', game.players[0].points)

    bet_ammount = input('Enter bet ammount: ')
    print('\n')

    # players turn

    game.players[0].add_hand(deck.draw(1))
    print('Dealer deals you your first card:',
          game.players[0].hands[0].cards[-1])

    # house turn
    game.dealer.add_hand(deck.draw(1))
    print('Dealer\'s first card is:', game.dealer.hands[0].cards[-1])

    # hit or stand
    while(True):
        # players turn
        game.players[0].hands[0].add_card(deck.draw(1))
        print('Dealer deals you anohter card:',
              game.players[0].hands[0].cards[-1])
        print('Your hand:', game.players[0].hands[0].cards)

        hand_points = sum(game.players[0].hands[0].cards)
        print('Your hand\'s total: ', hand_points)

        if hand_points < 21:
            cont = input('Press 1 to HIT or 0 STAND ')
            if cont:
                continue
            elif cont == 0:
                break
        elif hand_points > 21:
            print('you lost!')
            break
        elif hand_points == 21:
            print('you won!')
            break

    if hand_points > 21:
        break

    # house turn
    game.dealer.hands[0].add_card(deck.draw(1))
    print("Dealer's last card is:", game.dealer.hands[0].cards[-1])
    print("Dealer's hand value is:", sum(game.dealer.hands[0].cards))

    if sum(game.players[0].hands[0].cards) > sum(game.dealer.hands[0].cards):
        print('you won!')
        print('')
    else:
        print('**********YOU FUCKING LOST!***********')
        print("dealer's points:", sum(
            game.players[0].hands[0].cards), "your points:", sum(game.dealer.hands[0].cards))

    break
