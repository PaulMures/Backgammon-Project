#
#
#
#

import random

class Dice():

    def __init__(self,controller):

        self.die_1 = 0
        self.die_2 = 0
        if controller == 0:
            self.initial_turn = True

            #Starting roll 
            white_roll = random.randint(1,6)
            black_roll = random.randint(1,6)

            while white_roll == black_roll:

                white_roll = random.randint(1,6)
                black_roll = random.randint(1,6)

            if white_roll > black_roll:
                self.first_turn = "White"
            elif black_roll > white_roll:
                self.first_turn = "Black"

            self.initial_turn = False
        controller += 1
        self.controller = controller

    def roll(self):

        self.die_1 = random.randint(1,6)
        self.die_2 = random.randint(1,6)