from tictactoe import *

my_tictactoe = TicTacToe()

answer = ""
while not answer in ["y", "n"]:
    answer = input("do you want to start ? y/n ").lower()
    if answer == "y":
        my_tictactoe.determine_order_of_play("human")
    else:
        my_tictactoe.determine_order_of_play("computer")


while not my_tictactoe.end_of_game:
    if my_tictactoe.next_player == 'human':
        print("Your move")
        row = "0"
        while row not in ["1", "2", "3"]:
            row = input("Pls enter row number (1, 2 or 3): ")
        col = "0"
        while col not in ["1", "2", "3"]:
            col = input("Pls enter column number (1, 2 or 3): ")
        row = int(row) - 1
        col = int(col) - 1
        i = row * 3 + col
        my_tictactoe.add_human_move(i)
    else:
        my_tictactoe.add_computer_move()
    my_tictactoe.display_board()

