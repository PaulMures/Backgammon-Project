#
#
#
#

class Bar():

    def __init__(self):

        self.white_bar = []
        self.black_bar = []

    def hit(self,piece):

        if piece.side == "White":
            self.white_bar.append(piece)
            piece.position = 0
        elif piece.side == "Black":
            self.black_bar.append(piece)
            piece.position = 0

    def return_from_shadow_realm(self,turn,roll_1,roll_2,points,selected_roll):

        if turn == "White":

            return_position = 0 + selected_roll
            points.point_library[return_position].append(self.white_bar[-1])
            self.white_bar.remove(-1)

        elif turn == "Black":

            return_position = 24 - selected_roll
            points.point_library[return_position].append(self.black_bar[-1])
            self.black_bar.remove(-1)