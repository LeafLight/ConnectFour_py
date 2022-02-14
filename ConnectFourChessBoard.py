#!/bin/python3
#-*-coding:UTF-8-*-
#Author:LeafLight
#Date: 2022-02-14
########################################
#main
#Create a class of chessbox, which contains chess board,chess pieces,and rules.
import os
import numpy as np
class ChessBox:
    def __init__(self):
        #The chessboard,which is vertical and has 7*7 places for chess pieces
        self.BoardLen = 7
        #Win by Connecting 4
        self.WinLen = 4
        #ChessBoard
        self.ChessBoard = np.array([['-' for col in range(self.BoardLen)] for row in range(self.BoardLen)])
        #Two players, who use 'o' and 'x' respectively, drop their chess pieces in turns.
        #first-move: "o"
        self.Players = ["o","x"]
        #Change truns by 'not':because python will equal 1 to True and 0 to False,which helps in this case.
        self.CurrentPlayer = True
        #An index marker for convenience
        self.IndexMarker = np.array([str(index) for index in range(self.BoardLen)])
        #available depth for each col
        self.Depth = [self.BoardLen for col in range(self.BoardLen)]
        #Winner Flag
        self.Player0Win = False
        self.Player1Win = False
        #Greeting
        print("Hi!")
        print("____________________")
        ########################################
        #GAME STEPS
        #clear 
        self.Clear()
        #Show the empty chessboard
        self.ShowChessBoard()
        #Game in truns
        while (not self.Player0Win) & (not self.Player1Win):
            self.DropChessPieces()
            self.ChangeTurn()
            self.Clear()
            self.ShowChessBoard()
            self.CheckChessBoard()

    def DropChessPieces(self):
        #An overflow falg
        OverFlowFlag = True
        while OverFlowFlag:
            #read an input to decide the col to drop the chess piece
            ColForDrop = int(input("It's %s's turn.The col for dropping:"%(self.Players[self.CurrentPlayer])))
            if self.Depth[ColForDrop] > 0:
                OverFlowFlag = False
            else:
                print("not any avaluable for that col, another col, please...")
        #drop the chess piece
        self.Depth[ColForDrop] = self.Depth[ColForDrop] - 1
        self.ChessBoard[self.Depth[ColForDrop], ColForDrop] = self.Players[self.CurrentPlayer]
    def Clear(self):
        #clear the chessboard
        os.system("clear")
    def ChangeTurn(self):
        #change the trun
        self.CurrentPlayer = not self.CurrentPlayer
    def ShowChessBoard(self):
        #show the chessboard
        for i in range(self.BoardLen):
            print(self.ChessBoard[i])
        print("____________________")
        print(self.IndexMarker)
    def CheckChessBoard(self):
        #check if anyone wins the game
        # Check Unit:4*4(WinLen * WinLen)
        # loop over every check unit
        for i in range(self.BoardLen-self.WinLen+1):
            for j in range(self.BoardLen-self.WinLen+1):
                CheckUnit = self.ChessBoard[i:i+self.WinLen, j:j+self.WinLen]
                #Check all the rows of the units
                for row in range(self.WinLen):
                    if sum(CheckUnit[row,:] == self.Players[0]) == self.WinLen:
                        self.Player0Win = True
                        print("Player %s won the game!"%self.Players[0])
                    if sum(CheckUnit[row,:] == self.Players[1]) == self.WinLen:
                        self.Player1Win = True
                        print("Player %s won the game!"%self.Players[1])
                #Check all the cols of the units
                for col in range(self.WinLen):
                    if sum(CheckUnit[:,col] == self.Players[0]) == self.WinLen:
                        self.Player0Win = True
                        print("Player %s won the game!"%self.Players[0])
                    if sum(CheckUnit[:,col] == self.Players[1]) == self.WinLen:
                        self.Player1Win = True
                        print("Player %s won the game!"%self.Players[1])
                #Check all the diagonals of the units
                if (sum(np.diagonal(CheckUnit) == self.Players[0]) == self.WinLen) | (sum(np.diagonal(np.fliplr(CheckUnit)) == self.Players[0]) == self.WinLen):
                    self.Player0Win = True
                    print("Player %s won the game!"%self.Players[0])
                if (sum(np.diagonal(CheckUnit) == self.Players[1]) == self.WinLen) | (sum(np.diagonal(np.fliplr(CheckUnit)) == self.Players[1]) == self.WinLen):
                    self.Player1Win = True
                    print("Player %s won the game!"%self.Players[1])
Game = ChessBox()
