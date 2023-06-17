import math
import random

HOR = "-"
VER = "|"
SQUARE = "="
EMPTY = " "
DIM = 3

def calculate_index_in_matrix(row, col):
    return row * DIM + col


def calculate_rc_in_matrix(i):
    r = math.floor(i / DIM)
    c = i % DIM
    return r, c


class TicTacToe:
    def __init__(self):
        self.end_of_game = False
        self.players = {}
        self.player1 = ""
        self.player2 = ""
        self.next_player = ""
        self.matrix = {}
        for i in range(9):
            self.matrix[i] = EMPTY
        self.display_board()

    def determine_order_of_play(self, player1):
        if player1 == "human":
            self.player1 = "human"
            self.player2 = "computer"
        else:
            self.player1 = "computer"
            self.player2 = "human"
        self.players[self.player1] = 'X'
        self.players[self.player2] = 'O'
        self.next_player = self.player1

    def display_board(self):
        board = ""
        for i in range(9):
            board += self.matrix[i]
            if i % 3 in  [0, 1]:
                board += " | "
            if i % 3 == 2:
                board += '\n'
            if i in [2, 5]:
                board += "---------\n"
        print("#############")
        print("# TicTacToe #")
        print("#############\n")
        print(board)
        print("------------------------------------------------------------")

    def swap_player(self):
        if self.next_player == 'human':
            self.next_player = 'computer'
        else:
            self.next_player = 'human'

    def calc_open_spaces(self):
        result = 0
        for i in self.matrix:
            if self.matrix[i] == EMPTY:
                result += 1
        return result

    def generate_move(self):
        n = self.calc_open_spaces()
        if n == 0:
            self.end_game()
        ith = random.randint(1, n)
        for i in self.matrix:
            if self.matrix[i] == EMPTY:
                ith -=1
                if ith == 0:
                    return i

    def add_computer_move(self):
        print("Computer move")
        self.add_move(self.generate_move())

    def add_human_move(self, i):
        self.add_move(i)

    def add_move(self, i):
        # print(f"add_move(), i={i}")
        self.matrix[i] = self.players[self.next_player]
        if self.check_winning_pattern():
            if self.next_player == "computer":
                self.end_game(f"{self.next_player} wins !")
            else:
                self.end_game("you win !")
        elif self.calc_open_spaces() == 0:
            self.end_game("it is a draw")
        else:
            self.swap_player()

    def check_winning_pattern(self):
        for row in range(3):
            pattern = ""
            for col in range(3):
                pattern += self.matrix[calculate_index_in_matrix(row, col)]
            if pattern in ['XXX', 'OOO']:
                return True

        for col in range(3):
            pattern = ""
            for row in range(3):
                pattern += self.matrix[calculate_index_in_matrix(row, col)]
            if pattern in ['XXX', 'OOO']:
                return True

        diagonal_index_lst = [0, 4, 8]
        pattern = ""
        for i in diagonal_index_lst:
            pattern += self.matrix[i]
        if pattern in ['XXX', 'OOO']:
            return True

        diagonal_index_lst = [2, 4, 6]
        pattern = ""
        for i in diagonal_index_lst:
            pattern += self.matrix[i]
        if pattern in ['XXX', 'OOO']:
            return True

        return False

    def end_game(self, msg):
        print(msg)
        self.end_of_game = True
