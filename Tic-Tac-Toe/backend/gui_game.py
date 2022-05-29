import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
from tkinter import simpledialog


class Player:
    def __init__(self, number: int, name: str):
        self.marker_pos = []
        self.number = number
        if number == 0:
            self.marker = ' X '
        elif number == 1:
            self.marker = ' O '
        self.name = name
        if not name:
            self.win = tk.Tk()
            lbl = tk.Label(master=self.win, text=f'Player {number+1} name:', font=("Arial", 16))
            self.entry = tk.Entry(master=self.win, font=("Arial", 16))
            btn = tk.Button(master=self.win, text='Submit', command=self.get_name, font=("Arial", 16))
            lbl.pack()
            self.entry.pack()
            btn.pack()
            self.win.mainloop()

    def get_name(self):
        self.name = self.entry.get()
        self.win.destroy()


class UITicTacToe(tk.Tk):
    def __init__(self, name1: str = None, name2: str = None):
        self.player_list = [Player(0, name1), Player(1, name2)]
        self.name1 = self.player_list[0].name
        self.name2 = self.player_list[1].name

        super().__init__()

        self.grid_pos = []
        self.buttons_dict = {}
        self.geometry("600x600")
        self.my_font = font.Font(size=35)
        self.selection = None
        for i in range(3):
            self.columnconfigure(i, weight=1, minsize=75)
            self.rowconfigure(i, weight=1, minsize=85)
            for j in range(3):
                frame = tk.Frame(
                    master=self,
                    relief=tk.RAISED,
                    borderwidth=1
                )
                frame.grid_rowconfigure(0, weight=1)
                frame.grid_columnconfigure(0, weight=1)
                frame.grid(row=i, column=j, sticky="nsew")
                coord = str(i) + "_" + str(j)
                self.grid_pos.append((i, j))
                self.buttons_dict[coord] = tk.Button(master=frame, text="")
                self.buttons_dict[coord]["command"] = lambda x=i, y=j: self.select_space(x, y)
                self.buttons_dict[coord].grid(row=0, column=0, sticky="nsew")
        self.grid_indices = list(range(len(self.grid_pos)))
        self.active_player = 0
        self.selected = []
        self.done = False
        self.replay = 'N'
        print(
            f"""
                    Welcome to Tic-Tac-Toe!!!\n
                    {self.player_list[0].name} goes first with marker 'X'\n
                    {self.player_list[1].name} goes second with marker 'O'\n
                    First player with 3 markers in a row wins!
                    """
        )

    def select_space(self, x, y) -> None:
        self.buttons_dict[f'{x}_{y}']['text'] = self.player_list[self.active_player].marker
        self.buttons_dict[f'{x}_{y}']['font'] = self.my_font
        self.buttons_dict[f'{x}_{y}']['state'] = 'disabled'
        grid_selection = self.grid_pos.index((x, y))
        self.selected.append(grid_selection)
        self.grid_indices.remove(grid_selection)
        self.player_list[self.active_player].marker_pos.append(grid_selection)
        self.check_winner()
        self.check_grid()

    def close_win(self):
        self.destroy()

    def check_winner(self) -> None:
        if len(self.player_list[self.active_player].marker_pos) >= 3:
            x_list = []
            y_list = []
            for i in self.player_list[self.active_player].marker_pos:
                x_list.append(self.grid_pos[i][0])
                y_list.append(self.grid_pos[i][1])
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
                msg = ('Winner, winner...Chicken Dinner!\n' +
                       f'***Great Job {self.player_list[self.active_player].name}!***\n' +
                       'Would you like to play again?'
                       )
                self.replay = messagebox.askyesno(title="Winner!", message=msg)
                self.close_win()
                if not self.replay:
                    self.done = True
            else:
                self.active_player = abs(self.player_list[self.active_player].number - 1)
        else:
            self.active_player = abs(self.player_list[self.active_player].number - 1)

    def check_grid(self) -> None:
        can_player_win = 0
        for player in self.player_list:
            x_list = []
            y_list = []
            index_list = []
            for i in player.marker_pos:
                x_list.append(self.grid_pos[i][0])
                y_list.append(self.grid_pos[i][1])
                index_list.append(i)
            for i in self.grid_indices:
                x_list.append(self.grid_pos[i][0])
                y_list.append(self.grid_pos[i][1])
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
            msg = ('No more moves!\n' +
                   'Play again?'
                   )
            self.replay = messagebox.askyesno(title="Winner!", message=msg)
            self.close_win()
            if not self.replay:
                self.done = True
        else:
            pass
