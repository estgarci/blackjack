from game import *
from actions import *

# creating game board
game = Game(players=1, points=10000)

# creating deck
deck = Deck()


while(True):

    # initialize game
    print('**********BLACKJACK**********')
    print('=============================')
    print_points(game.players[0].points)

    # make initial bet
    while True:
        bet_ammount = int(input('Enter bet ammount: '))
        if game.players[0].bet(bet_ammount):
            print('You make an initial bet of', bet_ammount)
            print('\n')
            break
        print(
            'You do not have enough points to make that bet, try a different ammout: ')

    # players turn
    game.players[0].add_hand(deck.draw(1))
    print('Dealer deals you your first card:',
          game.players[0].hands[0].cards[-1])

    # house turn
    game.dealer.add_hand(deck.draw(1))
    print('Dealer\'s first card is:', game.dealer.hands[0].cards[-1])
    if (game.dealer.hands[0].cards[-1].rank == 'A'):
        print("Dealer has an ACE, do you want to place an insurance bet?\nEnter an ammount equal or less than", bet_ammount * .5)
        insurance_bet = input('Enter ammount or press 0 to deny insurance: ')
        if insurance_bet.isnumeric():
            insurance_bet = int(insurance_bet)
            game.player[0].bet(insurance_bet)
        else:
            print('Ammount not valid')
            insurance_bet = 0
    else:
        insurance_bet = 0

    # hit or stand
    while(True):
        # players turn
        game.players[0].hands[0].add_card(deck.draw(1))
        print('Dealer deals you anohter card:',
              game.players[0].hands[0].cards[-1])
        print('Your hand:', game.players[0].hands[0].cards)
        hand_points = sum(game.players[0].hands[0].cards)
        print('Your hand\'s total: ', hand_points)
        # hand can take another card
        if hand_points < 21:
            # ask if double down
            if bet_ammount <= game.players[0].points:
                print("Would you like to double down?")
                double_down = input("Enter 1 to DOUBLE DOWN or 0 to deny: ")
                if double_down is not '0':
                    game.players[0].bet(bet_ammount)
                    bet_ammount *= 2
                    print("You DOUBLE DOWN and increase your bet to:",
                          bet_ammount)
                continue
            # ask hit or stand
            cont = int(input('Press 1 to HIT or 0 STAND: '))
            if cont == 1:
                print('you HIT')
                continue
            elif cont == 0:
                print('you STAND')
                # house plays last round
                game.dealer.hands[0].add_card(deck.draw(1))
                print("Dealer's last card is:", game.dealer.hands[0].cards[-1])
                dealers_hand_sum = sum(
                    game.dealer.hands[0].cards)
                player1_hand_sum = sum(game.players[0].hands[0].cards)
                print("Dealer's hand value is:", sum(
                    game.dealer.hands[0].cards))

                if insurance_bet is not 0 and dealers_hand_sum == 21:
                    won = True
                    break
                if player1_hand_sum > dealers_hand_sum:
                    won = True
                    break
                elif dealers_hand_sum == 21:
                    won = True
                    break
                elif player1_hand_sum == dealers_hand_sum:
                    won = 'draw'
                else:
                    print("dealer's points:", sum(
                        game.players[0].hands[0].cards), "your points:", sum(game.dealer.hands[0].cards))
                    won = False
                    break
        elif hand_points == 21:
            won = True
            break
        elif hand_points > 21:
            won = False
            break

    # end of game checks
    if won:
        total_pool = (bet_ammount + insurance_bet) * 2
        game.players[0].points += total_pool
        print('You WON!')
        print('Your earings are:', total_pool)
        print_points(game.players[0].points)
    elif won == 'draw':
        game.players[0].points += bet_ammount
        print('Game resulted in a DRAW, you get your initial bet back.')
        print('Your point balance is:', game.players[0].points)
    else:
        print('You LOST, you now have:', game.players[0].points, 'points')
    break
