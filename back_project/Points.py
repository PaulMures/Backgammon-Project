#
#
#
#

from Bar import *
from Piece import *

class Points():
            
    def __init__(self,game_dice):
            
        self.moving_piece = 0
        self.hit_bar = Bar()
        self.white_cache = 0
        self.black_cache = 0

        w_1 = Piece("White",1) #White piece 1
        w_2 = Piece("White",1) #White piece 2
        w_3 = Piece("White",12) #White piece 3
        w_4 = Piece("White",12) #White piece 4
        w_5 = Piece("White",12) #White piece 5
        w_6 = Piece("White",12) #White piece 6
        w_7 = Piece("White",12) #White piece 7
        w_8 = Piece("White",17) #White piece 8
        w_9 = Piece("White",17) #White piece 9
        w_10 = Piece("White",17) #White piece 10
        w_11 = Piece("White",19) #White piece 11
        w_12 = Piece("White",19) #White piece 12
        w_13 = Piece("White",19) #White piece 13
        w_14 = Piece("White",19) #White piece 14
        w_15 = Piece("White",19) #White piece 15

        b_1 = Piece("Black",24) #Black piece 1
        b_2 = Piece("Black",24) #Black piece 2
        b_3 = Piece("Black",13) #Black piece 3
        b_4 = Piece("Black",13) #Black piece 4
        b_5 = Piece("Black",13) #Black piece 5
        b_6 = Piece("Black",13) #Black piece 6
        b_7 = Piece("Black",13) #Black piece 7
        b_8 = Piece("Black",8) #Black piece 8
        b_9 = Piece("Black",8) #Black piece 9
        b_10 = Piece("Black",8) #Black piece 10
        b_11 = Piece("Black",6) #Black piece 11
        b_12 = Piece("Black",6) #Black piece 12
        b_13 = Piece("Black",6) #Black piece 13
        b_14 = Piece("Black",6) #Black piece 14
        b_15 = Piece("Black",6) #Black piece 15

        self.point_library = {1:[w_1,w_2],2:[],3:[],4:[],5:[],6:[b_15,b_14,b_13,b_12,b_11],7:[],8:[b_10,b_9,b_8],9:[],10:[],11:[],12:[w_3,w_4,w_5,w_6,w_7],13:[b_7,b_6,b_5,b_4,b_3],14:[],15:[],16:[],17:[w_8,w_9,w_10],18:[],19:[w_11,w_12,w_13,w_14,w_15],20:[],21:[],22:[],23:[],24:[b_2,b_1]}

    def move(self,playing_dice,turn):

        move_completed = False

        while move_completed == False:

            if (turn == "White" and len(self.hit_bar.white_bar) == 0) or (turn == "Black" and len(self.hit_bar.black_bar) == 0):

                #Move Piece/Turn Code
                print(f"\nYour rolls are {playing_dice.die_1} and {playing_dice.die_2}\n")
                selected_point = int(input("Which position would you like to move a piece from? (Enter 0 if no legal moves)\n"))

                if selected_point == 0:
                    move_completed = True
                if selected_point == 69:
                    if turn == "White":
                        self.white_cache = 15
                        move_completed = True
                    elif turn == "Black":
                        self.black_cache = 15
                        move_completed = True
                
                if move_completed == False:

                    while len(self.point_library[selected_point]) != 0 and self.point_library[selected_point][0].side != turn:

                        print("\n!!!ERROR!!! Not your point\n")

                        print(f"\nYour rolls are {playing_dice.die_1} and {playing_dice.die_2}\n")
                        selected_point = int(input("Which position would you like to move a piece from?\n"))

                    while len(self.point_library[selected_point]) == 0:

                        print("\n!!!ERROR!!! You have no pieces on that point\n")

                        print(f"\nYour rolls are {playing_dice.die_1} and {playing_dice.die_2}\n")
                        selected_point = int(input("Which position would you like to move a piece from?\n"))

                    if (self.point_library[selected_point][0].side == turn) and (len(self.point_library[selected_point]) != []): #If you have a piece present and the point is yours...
                        
                        piece = self.point_library[selected_point][-1]

                        selected_move = int(input(f"How much would you like to move? {playing_dice.die_1} or {playing_dice.die_2}\n")) #Move selection

                        if piece.side == "White":
                            new_position = int(piece.position) + selected_move #New position calculation
                        elif piece.side == "Black":
                            new_position = int(piece.position) - selected_move #New position calculation

                        place_change = piece #Piece relocator

                        #While the new position cannot be moved onto...
                        while new_position <= 24 and new_position > 0 and len(self.point_library[new_position]) >= 2 and self.point_library[new_position][0].side != turn:

                            print("\n!!!ERROR!!! You cannot move onto your opponents domain\n")

                            selected_move = int(input(f"How much would you like to move? {playing_dice.die_1} or {playing_dice.die_2}\n")) #Move selection
                            if piece.side == "White":
                                new_position = int(piece.position) + selected_move #New position calculation
                            elif piece.side == "Black":
                                new_position = int(piece.position) - selected_move #New position calculation
                                place_change = piece #Piece relocator

                        #Validate move, then move
                        if (selected_move == playing_dice.die_1 and playing_dice.die_1 != 0) or (selected_move == playing_dice.die_2 and playing_dice.die_2 != 0):

                            #Cache piece
                            #!!!!!!!!!!!!!!!!!!!!!! Cannot validate that all pieces are in final box
                            if (piece.side == "White" and piece.position >= 18) or (piece.side == "Black" and piece.position <= 6):

                                if piece.side == "White":
                                    cache_requirement = 24 - int(piece.position)

                                    if int(selected_move) >= cache_requirement:
                                        del self.point_library[piece.position][-1] #Remove piece from old place
                                        self.white_cache += 1
                                        print("\nCache those motes Guardian!")

                                        if selected_move == playing_dice.die_1:
                                            playing_dice.die_1 = 0
                                        elif selected_move == playing_dice.die_2:
                                            playing_dice.die_2 = 0
                                            
                                    elif len(self.point_library[new_position]) == 1 and self.point_library[new_position][0].side != turn: #If new position is occupied by enemy team but one piece, hit

                                        #Hit
                                        hit_piece = self.point_library[new_position][0]
                                        self.hit_bar.hit(hit_piece)
                                        del self.point_library[new_position][0]
                                        print("You're going to the shadow realm!\n")

                                        #Move piece
                                        del self.point_library[piece.position][-1] #Remove piece from old place
                                        place_change.position = new_position
                                        self.point_library[new_position].append(place_change) #Add piece to new place

                                        if selected_move == playing_dice.die_1:
                                            playing_dice.die_1 = 0
                                        elif selected_move == playing_dice.die_2:
                                            playing_dice.die_2 = 0
                                        
                                        if playing_dice.die_1 == 0 and playing_dice.die_2 == 0:
                                            move_completed = True

                                    elif (len(self.point_library[new_position])) != 0 and piece.side == (self.point_library[new_position][0].side) or (self.point_library[new_position] == []): #If new position is occupied by your side or empty
                            
                                        del self.point_library[piece.position][-1] #Remove piece from old place
                                        place_change.position = new_position
                                        self.point_library[new_position].append(place_change) #Add piece to new place

                                        if selected_move == playing_dice.die_1:
                                            playing_dice.die_1 = 0
                                        elif selected_move == playing_dice.die_2:
                                            playing_dice.die_2 = 0

                                        if playing_dice.die_1 == 0 and playing_dice.die_2 == 0:
                                            move_completed = True

                                elif piece.side == "Black":
                                    cache_requirement = int(piece.position)

                                    if int(selected_move) >= cache_requirement:
                                        del self.point_library[piece.position][-1] #Remove piece from old place
                                        self.black_cache += 1
                                        print("\nCache those motes Guardian!")

                                        if selected_move == playing_dice.die_1:
                                            playing_dice.die_1 = 0
                                        elif selected_move == playing_dice.die_2:
                                            playing_dice.die_2 = 0

                                    elif len(self.point_library[new_position]) == 1 and self.point_library[new_position][0].side != turn: #If new position is occupied by enemy team but one piece, hit

                                        #Hit
                                        hit_piece = self.point_library[new_position][0]
                                        self.hit_bar.hit(hit_piece)
                                        del self.point_library[new_position][0]
                                        print("You're going to the shadow realm!\n")

                                        #Move piece
                                        del self.point_library[piece.position][-1] #Remove piece from old place
                                        place_change.position = new_position
                                        self.point_library[new_position].append(place_change) #Add piece to new place

                                        if selected_move == playing_dice.die_1:
                                            playing_dice.die_1 = 0
                                        elif selected_move == playing_dice.die_2:
                                            playing_dice.die_2 = 0
                                        
                                        if playing_dice.die_1 == 0 and playing_dice.die_2 == 0:
                                            move_completed = True

                                    elif (len(self.point_library[new_position])) != 0 and piece.side == (self.point_library[new_position][0].side) or (self.point_library[new_position] == []): #If new position is occupied by your side or empty
                            
                                        del self.point_library[piece.position][-1] #Remove piece from old place
                                        place_change.position = new_position
                                        self.point_library[new_position].append(place_change) #Add piece to new place

                                        if selected_move == playing_dice.die_1:
                                            playing_dice.die_1 = 0
                                        elif selected_move == playing_dice.die_2:
                                            playing_dice.die_2 = 0

                                        if playing_dice.die_1 == 0 and playing_dice.die_2 == 0:
                                            move_completed = True
                                    

                                if playing_dice.die_1 == 0 and playing_dice.die_2 == 0:
                                    move_completed = True

                            #Hit
                            elif len(self.point_library[new_position]) == 1 and self.point_library[new_position][0].side != turn: #If new position is occupied by enemy team but one piece, hit

                                #Hit
                                hit_piece = self.point_library[new_position][0]
                                self.hit_bar.hit(hit_piece)
                                del self.point_library[new_position][0]
                                print("You're going to the shadow realm!\n")

                                #Move piece
                                del self.point_library[piece.position][-1] #Remove piece from old place
                                place_change.position = new_position
                                self.point_library[new_position].append(place_change) #Add piece to new place

                                if selected_move == playing_dice.die_1:
                                    playing_dice.die_1 = 0
                                elif selected_move == playing_dice.die_2:
                                    playing_dice.die_2 = 0
                                
                                if playing_dice.die_1 == 0 and playing_dice.die_2 == 0:
                                    move_completed = True

                            #Position is yours or empty
                            elif (len(self.point_library[new_position])) != 0 and piece.side == (self.point_library[new_position][0].side) or (self.point_library[new_position] == []): #If new position is occupied by your side or empty
                                
                                del self.point_library[piece.position][-1] #Remove piece from old place
                                place_change.position = new_position
                                self.point_library[new_position].append(place_change) #Add piece to new place

                                if selected_move == playing_dice.die_1:
                                    playing_dice.die_1 = 0
                                elif selected_move == playing_dice.die_2:
                                    playing_dice.die_2 = 0

                                if playing_dice.die_1 == 0 and playing_dice.die_2 == 0:
                                    move_completed = True

                        else:
                            print("\n!!!ERROR!!! That is not a legal move\n")

            #If piece in hit bar
            elif (len(self.hit_bar.black_bar) != 0 and turn == "Black") or (len(self.hit_bar.white_bar) != 0 and turn == "White"):

                #Move Piece/Turn Code
                if turn == "Black":
                    print(f"\nYou have {len(self.hit_bar.black_bar)} pieces in the hit bar")
                elif turn == "White":
                    print(f"\nYou have {len(self.hit_bar.white_bar)} pieces in the hit bar")

                print(f"\nYour rolls are {playing_dice.die_1} and {playing_dice.die_2}\n")
                selected_roll = int(input(f"Which roll would you like to use? {playing_dice.die_1} or {playing_dice.die_2} or 0 if no legal moves)"))

                if selected_roll == 0:
                    move_completed = True
                if selected_roll == 69:
                    if turn == "White":
                        self.white_cache = 15
                        move_completed = True
                    elif turn == "Black":
                        self.black_cache = 15
                        move_completed = True

                self.hit_bar.return_from_shadow_realm(turn,playing_dice.die_1,playing_dice.die_2,self,selected_roll)

                if selected_roll == playing_dice.die_1:
                    playing_dice.die_1 = 0
                elif selected_roll == playing_dice.die_2:
                    playing_dice.die_2 = 0

                if playing_dice.die_1 == 0 and playing_dice.die_2 == 0:
                    move_completed = True