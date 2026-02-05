import random

pc_number = random.randint(1, 200)

while True:
    player_input = input("Guess the number (1-200): ")
    if not player_input.isdigit():
        print("It's just numbers! You can guess it.")
        continue
    player_num = int(player_input)
    if player_num == pc_number:
        print("Well done, you did it.")
        break
    elif player_num > pc_number:
        print("Too high")
    else:
        print("Too low")