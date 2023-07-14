#
#
#
#

from Dice import *
from Points import *
import tkinter

class Board():

    def __init__(self,dice_controller):

        self.playing_dice = Dice(dice_controller)
        self.points = Points(self.playing_dice)
        self.winner = ""
        self.game_state = False

    def play_screen(self,white_cache,black_cache,white_bar,black_bar,die_1,die_2,point_library):

        #Window
        self.game_window = tkinter.Tk()
        self.game_window.geometry("1200x450")
        self.game_window.title("Backgammon")

        #Colours
        TABLE_GREEN = "#225e19"
        BOARD_WOOD = "#694026"
        BLACK_WOOD = "#1f120b"
        WHITE_WOOD = "#634e41"
        DICE_WHITE = "#bfb9b6"
        DARK_BOX = "#241207"

        #Canvas
        self.canvas = tkinter.Canvas(self.game_window,bg=TABLE_GREEN,width=1200,height=450)

        #Score Board
        self.canvas.create_text(1050,200,text="SCORE",font=("Times",50)) #Score
        self.canvas.create_text(1025,250,text=white_cache,font=("Times",35))
        self.canvas.create_text(1075,250,text=black_cache,font=("Times",35),fill="black")

        #Hit Bank
        self.canvas.create_rectangle(780,50,900,425,fill=DARK_BOX)
        self.canvas.create_text(840,100,text="White Bar") #White box
        self.canvas.create_text(840,150,text=len(white_bar)) #White hit pieces
        self.canvas.create_text(840,300,text="Black Bar") #Black box
        self.canvas.create_text(840,350,text=len(black_bar)) #Black hit pieces

        #Dice
        self.canvas.create_text(1050,50,text="DICE",font=("Times",50)) #Dice Title
        self.canvas.create_rectangle(1025,100,1050,125,fill=DICE_WHITE,outline="black") #Die 1
        self.canvas.create_text(1037.5,112.5,text=die_1,fill="black")
        self.canvas.create_rectangle(1060,100,1085,125,fill=DICE_WHITE,outline="black") #Die 2
        self.canvas.create_text(1072.5,112.5,text=die_2,fill="black")

        #Shapes
        self.canvas.create_rectangle(50,50,780,425,fill=BOARD_WOOD,width=5,outline="black") #Board

        self.canvas.create_polygon(60,425,70,300,80,425,width=3,fill=BLACK_WOOD) #Point 1
        self.canvas.create_text(70,400,text=len(point_library[1]),font=("Times",15)) #Pieces Indicator 1
        self.canvas.create_text(70,280,text=1,font=("Times",15)) #Location
        if len(point_library[1]) != 0:
            self.canvas.create_text(70,420,text=(point_library[1][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(90,425,100,300,110,425,width=3,fill=WHITE_WOOD) #Point 2
        self.canvas.create_text(100,400,text=len(point_library[2]),font=("Times",15)) #Pieces Indicator 2
        self.canvas.create_text(100,280,text=2,font=("Times",15)) #Location
        if len(point_library[2]) != 0:
            self.canvas.create_text(100,420,text=(point_library[2][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(120,425,130,300,140,425,width=3,fill=BLACK_WOOD) #Point 3
        self.canvas.create_text(130,400,text=len(point_library[3]),font=("Times",15)) #Pieces Indicator 3
        self.canvas.create_text(130,280,text=3,font=("Times",15)) #Location
        if len(point_library[3]) != 0:
            self.canvas.create_text(130,420,text=(point_library[3][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(150,425,160,300,170,425,width=3,fill=WHITE_WOOD) #Point 4
        self.canvas.create_text(160,400,text=len(point_library[4]),font=("Times",15)) #Pieces Indicator 4
        self.canvas.create_text(160,280,text=4,font=("Times",15)) #Location
        if len(point_library[4]) != 0:
            self.canvas.create_text(160,420,text=(point_library[4][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(180,425,190,300,200,425,width=3,fill=BLACK_WOOD) #Point 5
        self.canvas.create_text(190,400,text=len(point_library[5]),font=("Times",15)) #Pieces Indicator 5
        self.canvas.create_text(190,280,text=5,font=("Times",15)) #Location
        if len(point_library[5]) != 0:
            self.canvas.create_text(190,420,text=(point_library[5][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(210,425,220,300,230,425,width=3,fill=WHITE_WOOD) #Point 6
        self.canvas.create_text(220,400,text=len(point_library[6]),font=("Times",15)) #Pieces Indicator 6
        self.canvas.create_text(220,280,text=6,font=("Times",15)) #Location
        if len(point_library[6]) != 0:
            self.canvas.create_text(220,420,text=(point_library[6][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(240,425,250,300,260,425,width=3,fill=BLACK_WOOD) #Point 7
        self.canvas.create_text(250,400,text=len(point_library[7]),font=("Times",15)) #Pieces Indicator 7
        self.canvas.create_text(250,280,text=7,font=("Times",15)) #Location
        if len(point_library[7]) != 0:
            self.canvas.create_text(250,420,text=(point_library[7][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(270,425,280,300,290,425,width=3,fill=WHITE_WOOD) #Point 8
        self.canvas.create_text(280,400,text=len(point_library[8]),font=("Times",15)) #Pieces Indicator 8
        self.canvas.create_text(280,280,text=8,font=("Times",15)) #Location
        if len(point_library[8]) != 0:
            self.canvas.create_text(280,420,text=(point_library[8][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(300,425,310,300,320,425,width=3,fill=BLACK_WOOD) #Point 9 
        self.canvas.create_text(310,400,text=len(point_library[9]),font=("Times",15)) #Pieces Indicator 9
        self.canvas.create_text(310,280,text=9,font=("Times",15)) #Location
        if len(point_library[9]) != 0:
            self.canvas.create_text(310,420,text=(point_library[9][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(330,425,340,300,350,425,width=3,fill=WHITE_WOOD) #Point 10
        self.canvas.create_text(340,400,text=len(point_library[10]),font=("Times",15)) #Pieces Indicator 10
        self.canvas.create_text(340,280,text=10,font=("Times",15)) #Location
        if len(point_library[10]) != 0:
            self.canvas.create_text(340,420,text=(point_library[10][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(360,425,370,300,380,425,width=3,fill=BLACK_WOOD) #Point 11
        self.canvas.create_text(370,400,text=len(point_library[11]),font=("Times",15)) #Pieces Indicator 11
        self.canvas.create_text(370,280,text=11,font=("Times",15)) #Location
        if len(point_library[11]) != 0:
            self.canvas.create_text(370,420,text=(point_library[11][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(390,425,400,300,410,425,width=3,fill=WHITE_WOOD) #Point 12
        self.canvas.create_text(400,400,text=len(point_library[12]),font=("Times",15)) #Pieces Indicator 12
        self.canvas.create_text(400,280,text=12,font=("Times",15)) #Location
        if len(point_library[12]) != 0:
            self.canvas.create_text(400,420,text=(point_library[12][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(420,425,430,300,440,425,width=3,fill=BLACK_WOOD) #Point 13
        self.canvas.create_text(430,400,text=len(point_library[13]),font=("Times",15)) #Pieces Indicator 13
        self.canvas.create_text(430,280,text=13,font=("Times",15)) #Location
        if len(point_library[13]) != 0:
            self.canvas.create_text(430,420,text=(point_library[13][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(450,425,460,300,470,425,width=3,fill=WHITE_WOOD) #Point 14
        self.canvas.create_text(460,400,text=len(point_library[14]),font=("Times",15)) #Pieces Indicator 14
        self.canvas.create_text(460,280,text=14,font=("Times",15)) #Location
        if len(point_library[14]) != 0:
            self.canvas.create_text(460,420,text=(point_library[14][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(480,425,490,300,500,425,width=3,fill=BLACK_WOOD) #Point 15
        self.canvas.create_text(490,400,text=len(point_library[15]),font=("Times",15)) #Pieces Indicator 15
        self.canvas.create_text(490,280,text=15,font=("Times",15)) #Location
        if len(point_library[15]) != 0:
            self.canvas.create_text(490,420,text=(point_library[15][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(510,425,520,300,530,425,width=3,fill=WHITE_WOOD) #Point 16
        self.canvas.create_text(520,400,text=len(point_library[16]),font=("Times",15)) #Pieces Indicator 16
        self.canvas.create_text(520,280,text=16,font=("Times",15)) #Location
        if len(point_library[16]) != 0:
            self.canvas.create_text(520,420,text=(point_library[16][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(540,425,550,300,560,425,width=3,fill=BLACK_WOOD) #Point 17
        self.canvas.create_text(550,400,text=len(point_library[17]),font=("Times",15)) #Pieces Indicator 17
        self.canvas.create_text(550,280,text=17,font=("Times",15)) #Location
        if len(point_library[17]) != 0:
            self.canvas.create_text(550,420,text=(point_library[17][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(570,425,580,300,590,425,width=3,fill=WHITE_WOOD) #Point 18
        self.canvas.create_text(580,400,text=len(point_library[18]),font=("Times",15)) #Pieces Indicator 18
        self.canvas.create_text(580,280,text=18,font=("Times",15)) #Location
        if len(point_library[18]) != 0:
            self.canvas.create_text(580,420,text=(point_library[18][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(600,425,610,300,620,425,width=3,fill=BLACK_WOOD) #Point 19
        self.canvas.create_text(610,400,text=len(point_library[19]),font=("Times",15)) #Pieces Indicator 19
        self.canvas.create_text(610,280,text=19,font=("Times",15)) #Location
        if len(point_library[19]) != 0:
            self.canvas.create_text(610,420,text=(point_library[19][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(630,425,640,300,650,425,width=3,fill=WHITE_WOOD) #Point 20
        self.canvas.create_text(640,400,text=len(point_library[20]),font=("Times",15)) #Pieces Indicator 20
        self.canvas.create_text(640,280,text=20,font=("Times",15)) #Location
        if len(point_library[20]) != 0:
            self.canvas.create_text(640,420,text=(point_library[20][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(660,425,670,300,680,425,width=3,fill=BLACK_WOOD) #Point 21
        self.canvas.create_text(670,400,text=len(point_library[21]),font=("Times",15)) #Pieces Indicator 21
        self.canvas.create_text(670,280,text=21,font=("Times",15)) #Location
        if len(point_library[21]) != 0:
            self.canvas.create_text(670,420,text=(point_library[21][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(690,425,700,300,710,425,width=3,fill=WHITE_WOOD) #Point 22
        self.canvas.create_text(700,400,text=len(point_library[22]),font=("Times",15)) #Pieces Indicator 22
        self.canvas.create_text(700,280,text=22,font=("Times",15)) #Location
        if len(point_library[22]) != 0:
            self.canvas.create_text(700,420,text=(point_library[22][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(720,425,730,300,740,425,width=3,fill=BLACK_WOOD) #Point 23
        self.canvas.create_text(730,400,text=len(point_library[23]),font=("Times",15)) #Pieces Indicator 23
        self.canvas.create_text(730,280,text=23,font=("Times",15)) #Location
        if len(point_library[23]) != 0:
            self.canvas.create_text(730,420,text=(point_library[23][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.create_polygon(750,425,760,300,770,425,width=3,fill=WHITE_WOOD) #Point 24
        self.canvas.create_text(760,400,text=len(point_library[24]),font=("Times",15)) #Pieces Indicator 24
        self.canvas.create_text(760,280,text=24,font=("Times",15)) #Location
        if len(point_library[24]) != 0:
            self.canvas.create_text(760,420,text=(point_library[24][-1].side[0]),font=("Times",15)) #Side Indicator

        self.canvas.pack()
        #self.game_window.mainloop()

    def player_turn(self,turn):

        while self.game_state == False:

            #Win mechanic
            if (self.points.white_cache == 15) or (self.points.black_cache == 15):

                if self.points.white_cache == 15:
                    self.winner = "White"
                elif self.points.black_cache == 15:
                    self.winner = "Black"

                self.game_state = True
            
            else:

                if turn == "White":
                    turn = "Black"
                elif turn == "Black":
                    turn = "White"

                print(f"\nIt is {turn}'s turn")
            
                #Play screen and move
                #self.game_window.destroy()
                self.playing_dice.roll()
                self.play_screen(self.points.white_cache,self.points.black_cache,self.points.hit_bar.white_bar,self.points.hit_bar.black_bar,self.playing_dice.die_1,self.playing_dice.die_2,self.points.point_library)

            
                self.points.move(self.playing_dice,turn)
                #self.canvas.update()
                self.game_window.destroy()