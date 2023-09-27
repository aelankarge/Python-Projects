import random

game_list = {
    '1': None,
    '2': None,
    '3': None,
    '4': None,
    '5': None
}
print(game_list)

def are_numbers_in_order(game_list):
    values = [game_list[str(i)] for i in range(1, 6) if game_list[str(i)] is not None]
    return values == sorted(values)

def play_number_order_game():
    for i in range(5):
        randomnumber = random.randint(1, 500)
        
        while True:
            print("\nGenerated random number:", randomnumber)
            print("Assign", randomnumber, "to a place between 1 - 5")
            assigned_number = input()
        
            if assigned_number not in ["1", "2", "3", "4", "5"]:
                print("Invalid input! Please enter a number between 1 and 5.")
        
            if game_list[assigned_number] is not None:
                print(f'{assigned_number} is already occupied, please choose a different spot.')
            else:
                game_list[assigned_number] = randomnumber
                print(game_list)
                break
        
        if not are_numbers_in_order(game_list):
            print('\nOops! The numbers are not in ascending order. You lost!')
            break
        elif all(value is not None for value in game_list.values()):
            print('\nYou won!')
            break
        else:
            print('\nNumbers are in order! Keep playing!')

            
play_number_order_game()