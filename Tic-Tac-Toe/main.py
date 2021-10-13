import numpy as np


class Player:
    def __init__(self, number, name=None):
        self.marker_pos = []
        self.number = number
        if number == 0:
            self.marker = ' X '
        elif number == 1:
            self.marker = ' O '
        self.name = name
        if not name:
            self.name = input(f'Player {number+1}, what is your name: ')


class TicTacToe:
    def __init__(self, name1=None, name2=None):
        self.grid_pos = [
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1), (2, 2)
        ]
        self.grid_indices = list(range(len(self.grid_pos)))
        self.player_list = [Player(0, name1), Player(1, name2)]
        self.name1 = self.player_list[0].name
        self.name2 = self.player_list[1].name
        self.active_player = 0
        self.selected = []
        self.done = False
        self.game_board = np.array([
            ['(0)', '(1)', '(2)'],
            ['(3)', '(4)', '(5)'],
            ['(6)', '(7)', '(8)']
        ])
        self.replay = 'N'
        print(
            f"""
            Welcome to Tic-Tac-Toe!!!\n
            {self.player_list[0].name} goes first with marker 'X'\n
            {self.player_list[1].name} goes second with marker 'O'\n
            First player with 3 markers in a row wins!
            """
        )

    def print_game_board(self):
        print(
            f"""
            -------------------
            |     |     |     |
            | {self.game_board[0,0]} | {self.game_board[0,1]} | {self.game_board[0,2]} |
            |     |     |     |
            -------------------
            |     |     |     |
            | {self.game_board[1,0]} | {self.game_board[1,1]} | {self.game_board[1,2]} |
            |     |     |     |
            -------------------
            |     |     |     |
            | {self.game_board[2,0]} | {self.game_board[2,1]} | {self.game_board[2,2]} |
            |     |     |     |
            -------------------
            """
        )

    def check_winner(self):
        if len(self.player_list[self.active_player].marker_pos) >= 3:
            x_list = []
            y_list = []
            for i in self.player_list[self.active_player].marker_pos:
                x_list.append(self.grid_pos[i][0])
                y_list.append(self.grid_pos[i][0])
            count_x = [x_list.count(0), x_list.count(1), x_list.count(2)]
            count_y = [y_list.count(0), y_list.count(1), y_list.count(2)]
            diagonal_down = (
                    self.player_list[self.active_player].marker_pos.count(0) +
                    self.player_list[self.active_player].marker_pos.count(4) +
                    self.player_list[self.active_player].marker_pos.count(8)
            )
            diagonal_up = (
                    self.player_list[self.active_player].marker_pos.count(6) +
                    self.player_list[self.active_player].marker_pos.count(4) +
                    self.player_list[self.active_player].marker_pos.count(2)
            )
            if count_x.count(3) >= 1 or count_y.count(3) >= 1 or diagonal_up == 3 or diagonal_down == 3:
                print(
                    'Winner, winner...Chicken Dinner!\n' +
                    f'***Great Job {self.player_list[self.active_player].name}!***'
                )
                self.print_game_board()
                self.replay = input('Play Again? (Y/N): ')
                if self.replay == 'N' or self.replay == 'n':
                    self.done = True
            else:
                self.active_player = abs(self.player_list[self.active_player].number - 1)
        else:
            self.active_player = abs(self.player_list[self.active_player].number - 1)

    def check_grid(self):
        can_player_win = 0
        for player in self.player_list:
            x_list = []
            y_list = []
            index_list = []
            for i in player.marker_pos:
                x_list.append(self.grid_pos[i][0])
                y_list.append(self.grid_pos[i][0])
                index_list.append(i)
            for i in self.grid_indices:
                x_list.append(self.grid_pos[i][0])
                y_list.append(self.grid_pos[i][0])
                index_list.append(i)
            count_x = [x_list.count(0), x_list.count(1), x_list.count(2)]
            count_y = [y_list.count(0), y_list.count(1), y_list.count(2)]
            diagonal_down = (
                    index_list.count(0) +
                    index_list.count(4) +
                    index_list.count(8)
            )
            diagonal_up = (
                    index_list.count(6) +
                    index_list.count(4) +
                    index_list.count(2)
            )
            if count_x.count(3) >= 1 or count_y.count(3) >= 1 or diagonal_up == 3 or diagonal_down == 3:
                can_player_win += 1
        if can_player_win == 0:
            print('No more moves!')
            self.print_game_board()
            self.replay = input('Play Again? (Y/N): ')
            if self.replay == 'N' or self.replay == 'n':
                self.done = True
        else:
            pass

    def play_turn(self):
        print(f'{self.player_list[self.active_player].name}\'s turn!')
        print(f'Current grid\n')
        self.print_game_board()
        grid_selection = int(input(f'{self.player_list[self.active_player].name}, please make a selection: '))
        while self.selected.count(grid_selection) != 0:
            grid_selection = int(input(f'Grid Position {grid_selection} not available. Please select from available: '))
        self.selected.append(grid_selection)
        self.grid_indices.remove(grid_selection)
        self.game_board[self.grid_pos[grid_selection]] = self.player_list[self.active_player].marker
        self.player_list[self.active_player].marker_pos.append(grid_selection)
        self.check_winner()
        self.check_grid()


if __name__ == '__main__':
    game = TicTacToe()
    while not game.done:
        game.play_turn()
        if game.replay == 'Y' or game.replay == 'y':
            game = TicTacToe(game.name1, game.name2)
