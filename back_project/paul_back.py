#Name: Backgammon
#Date: Started 04/25/2023 - Finished 05/02/2023
#Developer: Paul Muresan
#Description: A game of backgammon. Pieces move based on dice rolled, giving players moves to make. Pieces can be hit if there is only one on a point.
            # Pieces cannot move onto a point occupied by 2 opponent pieces. The first player to move is whoever makes the bigger single die roll.
            # Once all pieces are in the home section, pieces can be moved off the board depending on their location and dice roll. Once all pieces
            # have been cashed out, the player wins.

from Board import *

def tavli():

    game = Board(0)

    game.player_turn("Black")


    print("Thanks for playing!\n",
            f"The winner is {game.winner}!!!\n",
            f"White had {game.points.white_cache} pieces cached\n",
            f"Black had {game.points.black_cache} pieces cached\n")
            


tavli()