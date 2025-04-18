import random
import time

cards = ("Ace", "King", "Queen", "Jack", 10, 9, 8, 7, 6, 5, 4, 3, 2)
suits = ("Club♣️", "Diamonds♦️", "Hearts❤️", "Spades♠️")
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Blackjack:
    def __init__(self):
        self.cards = []
        self.blackjack = False
        self.game_end = False
        self.bust = False
        self.under_17 = False
        

    def draw_card(self):
        rank = random.choice(cards)
        suit = random.choice(suits)
        card = Card(rank, suit)
        self.cards.append(card)

    def get_value(self):
        value = 0

        ace_count = 0
        for card in self.cards:
            if card.rank == "Ace" :
                value += 11
                ace_count += 1
            elif card.rank in ("King", "Queen", "Jack"):
                value += 10
            else:
                value += int(card.rank) if isinstance(card.rank, int) else 0
        while value > 21 and ace_count >0 :
            value -= 10
            ace_count -= 1
        return value
    def reset(self):
        self.cards = []
        self.blackjack = False
        self.game_end = False
        self.bust = False
        self.under_17 = False

    def check_bust(self):
        if self.get_value() >21:
            self.bust = True
        else:
            pass

    def hit_stand(self):
        self.choice = input("Would you like to hit or stand? ").capitalize().strip()
        return self.choice
    def check_blackjack(self):
        if self.get_value() == 21:
            self.blackjack = True
            print("You got blackjack ")
        else:
            pass
    def dealer_hit(self):
        if self.get_value() < 17:
            self.under_17 = True
        else:
            self.under_17 = False
#Main
def main():
    print("***************")
    print("Welcome to project blackjack v2")
    player = Blackjack()
    dealer = Blackjack()
    balance = 100
    play = True
    #Main game loop
    while True:
        player.cards = []
        dealer.cards = []
        while True:
            try :
                print(f"Your current balance: {balance}")
                bet = int(input("Please enter your bet amount: ").strip())
                print("***************")
                if bet <= 0:
                    print("Invalid bet, bet must be >0!")
                    print("***************")
                    continue
                elif bet > balance:
                    print("Invalid bet, you do not have that money! ")
                    print("***************")
                    continue
                else:
                    break
            except ValueError:
                print("Please enter an valid bet! ")
                print("***************")
            player.reset()
            dealer.reset()
            play = True
        #Getting card
        i = 0
        while i <2:
            player.draw_card()
            dealer.draw_card()
            i += 1
        print("Your hand:")
        for card in player.cards:
            print(card)
        print(f"Current total: {player.get_value()}")
        print("Dealer current hand:")
        print(f"{dealer.cards[0]} and UNKNOWN!")
        print("***************")
        player.check_blackjack()
        dealer.check_blackjack()
        if dealer.blackjack and player.blackjack == False:
            play = False

        #hit or stand
        while play:
            if player.blackjack:
                break
            player.hit_stand()
            if player.choice == "Hit":
                player.draw_card()
                print("Your current hand:")
                for card in player.cards:
                    print(card)
                print(f"Current total: {player.get_value()}")
                print("***************")
                if player.get_value() > 21:
                    play = False
                player.check_blackjack()
                if player.blackjack:
                    break
                continue
            else:
                break
        while play:
            print("Dealer hand: ")
            for card in dealer.cards:
                print(card)
            print(f"Dealer current total: {dealer.get_value()}")
            print("***************")
            dealer.dealer_hit()
            if dealer.under_17:
                dealer.draw_card()
                time.sleep(1)
                continue
            else:
                break
        #Game ending

        player_total = player.get_value()
        dealer_total = dealer.get_value()
        print(f"Your final hand value: {player_total}")
        print(f"Dealer's final hand value: {dealer_total}")
        print("***************")

        if player_total > 21:
            print("You busted!")
            print(f"You lost {bet}")
            balance -= bet
        elif dealer_total > 21:
            print("Dealer busted. You win!")
            print(f"You won {bet}")
            balance += bet
        elif player.blackjack and not dealer.blackjack:
            print("Blackjack! You win!")
            print(f"You won {bet * 1.5}")
            balance += bet * 1.5
        elif dealer.blackjack and not player.blackjack:
            print("Dealer has blackjack. You lose.")
            print(f"You lost {bet}")
            balance -= bet
        elif player_total > dealer_total:
            print("You win!")
            print(f"You won {bet}")
            balance += bet
        elif player_total < dealer_total:
            print("You lose.")
            print(f"You lost {bet}")
            balance -= bet
        else:
            print("It's a draw. Bet returned.")


        while True:
            play_again = input("Do you want to play again? (Y/N)").capitalize().strip()
            print("***************")
            player_choices = ("Yes", "Y", "No", "N")
            if play_again not in player_choices:
                print("Invalid choice, please enter an valid option!")
                print("***************")
                continue
            elif play_again == player_choices[0] or player_choices[1]:
                print("Okay, restarting simulation! ")
                print("***************")
                break
            else:
                print("Thank you for playing the game! ")
                print("***************")
                exit()

if __name__ == "__main__":
    main()

