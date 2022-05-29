#from backend.text_game import TicTacToe
from backend.gui_game import UITicTacToe

if __name__ == '__main__':
    game = UITicTacToe()
    while not game.done:
        game.mainloop()
        if game.replay:
            game = UITicTacToe(game.name1, game.name2)
    # game = TicTacToe()
    # while not game.done:
    #     game.play_turn()
    #     if game.replay == 'Y' or game.replay == 'y':
    #         game = TicTacToe(game.name1, game.name2)
