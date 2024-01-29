import random
def main():
    display_banner()
    play_game()

def play_game():
    player_num = 1
    game_finished = False
    game_string = create_game_string()
    while not game_finished:
        display_game_string(game_string)
        print("PLAYER NUMBER: " + str(player_num))
        position_num = get_position_number_from_user()
        if position_num == "cheat":
            congratulate_player(player_num)
            return  
        move_num = get_number_places_to_move()
        game_string = move_dollar_to_the_left(game_string, position_num, move_num)
        game_finished = check_game_finished(game_string)
        if game_finished:
            congratulate_player(player_num)
        else:
            player_num = get_next_player_num(player_num)
    
def display_banner():
    print("*" * 15)
    print("COIN STRIP GAME")
    print("*" * 15)
    return display_banner

def get_position_number_from_user():
    while True:
        user_input = input("Enter position number of coin (1-9): ")
        if user_input.lower() == "cheat":
            return "cheat"
        try:
            coin_position = int(user_input)
            if 1 <= coin_position <= 9:
                return coin_position
            else:
                print("____________________________________________")
                print("Invalid input: Please enter a number between 1 and 9.")
        except ValueError:
            print("____________________________________________")
            print("Invalid input: Please enter a valid integer.")

def get_number_places_to_move():
    CoinMoves = int(input("Enter number of places to move coin: "))
    return CoinMoves

def create_game_string():
    game_string = ' $ $ $ $ '
    i = 0
    while i < 4:
        game_string = move_random_character_to_end(game_string)
        i = i + 1
        return game_string 


def move_random_character_to_end(game_string):
    randomindex = random.randint(0, 8)
    game_string = game_string[:randomindex] + game_string[randomindex+1:] + game_string[randomindex] 
    return game_string
    
def display_game_string (game_string):
    print("")
    print("123456789")
    print("-" * 9)
    print(game_string)
    print("")
    
def get_next_player_num(player_number):
    if player_number == 1:
        return 2
    else:
        return 1

def move_dollar_to_the_left(game_string, position_number, to_move):
    new_position = position_number - to_move
    if new_position < 1 or new_position > len(game_string):
        print("____________________________")
        print("Invalid move: Out of bounds!")
        print("____________________________")
        return game_string
    else:
        game_string = game_string[:new_position - 1] + '$' + game_string[new_position - 1:position_number - 1] + game_string[position_number:]
        return game_string

def check_game_finished(game_string):
    if game_string[0:4] =="$$$$":
        return True 
    else:
        return False   
    
def congratulate_player(player_number):
    print("")
    print("=============================")
    print("** Y O U   H A V E   W O N **")
    print("       PLAYER NUMBER:",player_number        )
    print("=============================")
    print("")
main()
