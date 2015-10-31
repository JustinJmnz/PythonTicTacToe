'''
Created on Oct 1, 2015

@author: justin
'''
from Player import Player
from Deck import Deck
import os
import numpy
from builtins import range
import TicTacToe
class TicTacToe(object):

    def __init__(self):
        '''
        :return: TicTacToe object
        '''
        self.turn = 1
        self.deckList = [Deck()]
        self.player1 = Player()
        self.player2 = Player()
    def validateInput(self, num):
        '''
        Validates User input based on ValueError and if that spot is available or not
        :param: Number to be validated
        :return: Same param if validated
        '''
        try:
            num = int(num)
        except ValueError:
            print('Not an integer')
            return -1
        if num < 0 or num > 8:
            print('Not between 0-8')
            return -1
        x,y = self.getCoordinate(num)
        deck = self.deckList[-1]  # Get last element in deckList
        boardP1 = deck.getP1Board()
        boardP2 = deck.getP2Board()
        if boardP1[x,y] == 1 or boardP2[x,y] == 1:
            print('Spot taken')
            return -1
        self.fillBoard(num)
        
        return num
    def getCoordinate(self, num):
        '''
        Gets a coordinate within the board of a point entered by a user
        :param: Number 0-8, a spot in the matrix
        :return: A tuple of coordinates of the param 
        '''
        if num == 0:
            return (0,0)
        elif num == 1:
            return (0,1)
        elif num == 2:
            return (0,2)
        elif num == 3:
            return (1,0)
        elif num == 4:
            return (1,1)
        elif num == 5:
            return (1,2)
        elif num == 6:
            return (2,0)
        elif num == 7:
            return (2,1)
        elif num == 8:
            return (2,2)
    def fillBoard(self, num):
        '''
        Fills the board with 0 or 1 depending on user input and turn
        :param: Number that user entered
        :return: Nothing
        '''
        
        deck = self.deckList[len(self.deckList) - 1]  # Get last element in deckList
        boardP1 = deck.getP1Board()  # Getting the board
        boardP2 = deck.getP2Board()
        x,y = self.getCoordinate(num)
        if self.turn == 1:
            boardP1[x,y] = 1
            #print(boardP1)
        else:
            boardP2[x,y] = 1
            #print(boardP2)
        visualBoard = deck.getVisualBoard()
        visualBoard = self.fillVisualBoard(boardP1, boardP2, visualBoard)
        print(visualBoard)
    def fillVisualBoard(self, boardP1, boardP2, visualBoard):
        '''
        Fills the board the user will display
        :param: The board used for logic, and the board used for output
        :return: The board used for output
        '''
        for i in range(0, len(boardP1)):  # For Player 1
            for j in range(0, len(boardP1)):
                if boardP1[i,j] == 1:
                    visualBoard[i,j] = self.player1.mark
                   
        for i in range(0, len(boardP2)):  # For Player 2
            for j in range(0, len(boardP2)):
                if boardP2[i,j] == 1:
                    visualBoard[i,j] = self.player2.mark
        return visualBoard
    def getUserInput(self):
        '''
        Asks user for input and calls a function to validate it
        :return: The number the user entered IF it is validated
        '''
        if self.turn == 1:
            choice = input(self.player1.name + ': Enter 0-8\n')
            os.system("clear")  # Does not work in IDEs

            #turn = 2
        elif self.turn == 2:
            choice = input(self.player2.name + ': Enter 0-8\n')
            os.system("clear")  # Does not work in IDEs
            #turn = 1
        choice = self.validateInput(choice)
        if choice == -1:
            #print('Choice = -1')
            return self.getUserInput()
        return choice
    def checkWinner(self):
        '''
        Checks to see if there is a winner
        :return: The winner as a player object
        '''
        deck = self.deckList[len(self.deckList) - 1]
        boardP1 = deck.getP1Board()
        boardP2 = deck.getP2Board()
        # Player 1
        s = boardP1[0,:]  
        sumR1P1 = s.sum()
        s = boardP1[1,:]
        sumR2P1 = s.sum()
        s = boardP1[2,:]
        sumR3P1  = s.sum()
        s = boardP1[:,0]
        sumC1P1 = s.sum()
        s = boardP1[:,1]
        sumC2P1 = s.sum()
        s = boardP1[:,2]
        sumC3P1 = s.sum()
        s = boardP1.diagonal()
        sumDiagP1 = s.sum()
        s = numpy.fliplr(boardP1).diagonal()
        sumDiag2P1 = s.sum()
        
        # Player 2
        s = boardP2[0,:]  
        sumR1P2 = s.sum()
        s = boardP2[1,:]
        sumR2P2 = s.sum()
        s = boardP2[2,:]
        sumR3P2  = s.sum()
        s = boardP2[:,0]
        sumC1P2 = s.sum()
        s = boardP2[:,1]
        sumC2P2 = s.sum()
        s = boardP2[:,2]
        sumC3P2 = s.sum()
        s = boardP2.diagonal()
        sumDiagP2 = s.sum()
        s = numpy.fliplr(boardP2).diagonal()
        sumDiag2P2 = s.sum()
        # Checking for winner
        if sumR1P1 == 3 or sumR2P1 == 3 or sumR3P1 == 3 or sumC1P1 == 3 or sumC2P1 == 3 or sumC3P1 == 3 or sumDiagP1 == 3 or sumDiag2P1 == 3:
            return self.player1
        if sumR1P2 == 3 or sumR2P2 == 3 or sumR3P2 == 3 or sumC1P2 == 3 or sumC2P2 == 3 or sumC3P2 == 3 or sumDiagP2 == 3 or sumDiag2P2 == 3:
            return self.player2
        if (numpy.bitwise_or(boardP1, boardP2) == deck.getTieBoard()).all():
            return -1
    def startGame(self):
        '''
        Main game loop
        '''  
        while True:  # Main loop
            choice = self.getUserInput()
            winner = self.checkWinner()
            if winner == self.player1:
                print(self.player1.name + ' is the winner')
                self.player1.setWin()
                self.player2.setLost()
                break;
            elif winner == self.player2:
                print(self.player2.name + ' is the winner')
                self.player2.setWin()
                self.player1.setLost()
                break;
            elif winner == -1:
                print('Tie game!')
                self.player1.setTie()
                self.player2.setTie()
                break;
            if self.turn == 1:
                self.turn = 2
            else:
                self.turn = 1
            # os.system("clear")  # Does not work in IDEs
    def main(self):
        print('Welcome to TicTacToe.')
        print("       |     |     \n  {0}  | {1} |  {2}\n  _____|_____|_____\n       |     |     \n  {3}  | {4} |  {5}\n  _____|_____|_____\n       |     |     \n  {6}  | {7} |  {8}\n")
        player1Name = input('Player 1: Enter your name\n')
        player2Name = input('Player 2: Enter your name\n')
        self.player1.setName(player1Name)
        self.player2.setName(player2Name)
        player1Mark = input(self.player1.name + ': Enter your mark\n')
        player2Mark = input(self.player2.name + ': Enter your mark\n')
        if player1Mark == player2Mark:
            print('You both cannot have the same mark\n')
            return
        else:
            self.player1.setMark(player1Mark)
            self.player2.setMark(player2Mark)
        
        while True:
            self.startGame()
            playOn = input('Do you want to play again..? y/n\n')
            if playOn == 'Y' or playOn == 'y':
                self.deckList.append(Deck())
                winning = self.player1.__cmp__(self.player2)
                if winning == self.player1:
                    print(self.player1.name + ' is winning')
                    print(self.player1.name + ' score: ' + str(self.player1.getScore()))
                    print(self.player2.name + ' score: ' + str(self.player2.getScore()))
                elif winning == self.player2:
                    print(self.player2.name + ' is winning')
                    print(self.player2.name + ' score: ' + str(self.player2.getScore()))
                    print(self.player1.name + ' score: ' + str(self.player1.getScore()))
                else:
                    print('Score is a tie')
                    print(self.player2.name + ' score: ' + str(self.player2.getScore()))
                    print(self.player1.name + ' score: ' + str(self.player1.getScore()))
            else:
                break;
            