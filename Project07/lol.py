#######################################################################################################################
#
# Computer Project 07
#
#######################################################################################################################


from uno import Card, Deck, Player

# Use these in your input statement
"\n:~Enter number of players (2-5) ~:"
"\t:~Choose a card color (Red, Green, Blue, Yellow, or Wild) ~:"
"\t:~Choose a card value (0-9, Skip, Reverse, +2, Color Change, +4) ~:"
"\t:~Choose a new color (Red, Green, Blue, Yellow) ~:"
"\t:~Choose a valid color (Red, Green, Blue, Yellow) ~:"
"\n:~Do you want to play a game of UNO? (yes/no) ~:"
"\n:~Do you want to play another round? (yes/no) ~:"

# Use these in your print statement
"Please enter a number between 2 and 5."
"\n{}'s turn. Current card: {}"
"\tYour hand: {}"
"\tPlayable cards: {}"
"\tInvalid card choice. Please choose a valid card from your hand."
"\tNo playable cards. Drawing a card."
"\nGame state:"
"\t{} is skipped!"
"\tDirection reversed!"
"\t{} draws two cards!"
"\tColor Changed to {}!"
"\t{} draws four cards!"
"\n-----{player.name} has won the round-----"
"Thanks for playing!\nGo Green!! Go White!!"

# Write your functions definitions here
def get_num_players():
    while True:
        try:
            num_players = int(input("\n:~Enter number of players (2-5) ~:"))
            if 2 <= num_players <= 5:
                return num_players
            else:
                print("Please enter a number between 2 and 5.")
        except ValueError:
            print("Please enter a number between 2 and 5.")

def initialize_game(num_players):
    deck = Deck()
    players = {}
    for i in range(num_players):
        pile = []
        for y in range(5):
            pile.append(deck.deal_card())
        players[i + 1] = pile
    return deck, players

def print_game_state(players):
    print("\nGame state:")
    for player_num, hand in players.items():
        num_cards = len(hand)
        print(f"Player #{player_num} - {num_cards} cards")


def play_turn(num_players, deck, players, current_card, discard_pile, direction):
    list_players = ["Player{}".format(i + 1) for i in range(num_players)]
    number_of_players = len(list_players)
    current_player_index = 0

    while True:
        curr_player = Player(current_player_index + 1)
        print(f"\n{curr_player.name}'s turn. Current card: {current_card}")
        print(f"\tYour hand: {players[current_player_index + 1]}")

        playable_cards = []

        for card in players[current_player_index + 1]:
            color_match = (card.color == current_card.color)
            value_match = (card.value == current_card.value)
            is_wild_card = card.is_wild

            if color_match or value_match or is_wild_card:
                playable_cards.append(card)
        if playable_cards != []:
            print(f"\tPlayable cards: {playable_cards}")
        if not playable_cards:
            print("\tNo playable cards. Drawing a card.")
            if deck.is_empty():
                deck.reset_deck(discard_pile)
                discard_pile.clear()
                current_card = deck.deal_card()
                discard_pile.append(current_card)
                #current_card = deck.deal_card()



            drawn_card = deck.deal_card()

            if drawn_card:
                players[current_player_index + 1].append(drawn_card)
                print_game_state(players)

            else:
                print(f"No cards to draw for Player #{current_player_index + 1}.")


                print_game_state(players)
            current_player_index = (current_player_index + direction) % number_of_players
            continue


        while True:
            user_input_color = input("\t:~Choose a card color (Red, Green, Blue, Yellow, or Wild) ~:")
            user_input_value = input("\t:~Choose a card value (0-9, Skip, Reverse, +2, Color Change, +4) ~:")

            selected_card = next((card for card in playable_cards if
                                  (card.color == user_input_color and card.value == user_input_value)), None)
            if selected_card is not None:
                discard_pile.append(selected_card)
            if not selected_card:
                print("\tInvalid card choice. Please choose a valid card from your hand.")
                print(f"\tPlayable cards: {playable_cards}")
                continue

            players[current_player_index + 1].remove(selected_card)
            current_card = selected_card

            if selected_card.value == 'Skip':
                if direction == 1:
                    current_player_index = (current_player_index + 1) % number_of_players
                    print(f"\tPlayer #{current_player_index+1} is skipped!")
                else:
                    current_player_index = (current_player_index-1) % number_of_players
                    print(f"\tPlayer #{current_player_index+1} is skipped!")

            elif selected_card.is_wild and selected_card.value == 'Color Change':
                new_color = input("\t:~Choose a new color (Red, Green, Blue, Yellow) ~:")
                while new_color not in Card.color_list:
                    new_color = input("\t:~Choose a valid color (Red, Green, Blue, Yellow) ~:")
                current_card.color = new_color
                print(f"\tColor Changed to {current_card.color}!")

            elif selected_card.value == 'Reverse':
                direction *= -1
                print("\tDirection reversed!")

                if direction == 1:
                    current_player_index = (current_player_index + 1) % number_of_players
                    print_game_state(players)
                    break
                else:
                    current_player_index = (current_player_index - 1) % number_of_players
                    print_game_state(players)
                    break
                    # Move to next player

            elif selected_card.value == '+2':
                next_player_index = (current_player_index + direction) % number_of_players
                print(f"\tPlayer #{next_player_index +1} draws two cards!")
                for _ in range(2):
                    drawn_card = deck.deal_card()
                    if drawn_card:
                        players[next_player_index + 1].append(drawn_card)
                current_player_index = next_player_index
            elif selected_card.is_wild and selected_card.value == '+4':
                next_player_index = (current_player_index + direction) % number_of_players
                for _ in range(4):
                    drawn_card = deck.deal_card()
                    if drawn_card:
                        players[next_player_index + 1].append(drawn_card)
                new_color = input("\t:~Choose a new color (Red, Green, Blue, Yellow) ~:")
                while new_color not in Card.color_list:
                    new_color = input("\t:~Choose a valid color (Red, Green, Blue, Yellow) ~:")
                current_card.color = new_color
                print(f"\tColor Changed to {current_card.color}!")
                print(f"\tPlayer #{next_player_index +1} draws four cards!")
                current_player_index = next_player_index

            # Move to the next player at the end of the turn
            for player_num, hand in players.items():
                if len(hand) == 0:
                    print(f"\n-----Player #{player_num} has won the round-----")
                    return
            current_player_index = (current_player_index + direction) % number_of_players
            print_game_state(players)
            break


def main():
    banner = """🌟🌟🌟 Welcome to the *Ultimate UNO Showdown*! 🌟🌟🌟

    💥 Prepare yourself for a thrilling, card-flipping adventure
    where alliances waver, strategies unfold, and only the
    sharpest tactician will claim the ultimate victory! 💥

    💥 Will you reverse the tide, skip ahead of your rivals,
    or drop that Wild Draw Four at the perfect moment to leave
    them in disarray? Let the games begin! 💥
    """
    print(banner)

    user_choice = input("\n:~Do you want to play a game of UNO? (yes/no) ~:")
    if user_choice.lower() != "yes":
        print("Thanks for playing!\nGo Green!! Go White!!")
        return
    while True:
        num_players = get_num_players()
        deck, players = initialize_game(num_players)
        current_card = deck.deal_card()
        discard_pile = []
        discard_pile.append(current_card)
        direction = 1
        play_turn(num_players, deck, players, current_card, discard_pile, direction)
        user_choice = input("\n:~Do you want to play another round? (yes/no) ~:")
        if user_choice.lower() != "yes":
            print("Thanks for playing!\nGo Green!! Go White!!")
            return
        else:
            continue





# DO NOT MODIFY THE FOLLOWING 2 LINES.
# DO NOT WRITE ANYTHING AFTER THE FOLLOWING 2 LINES OF CODES
# All your code should be either in the main function
# or in another function.
if __name__ == "__main__":
    main()
