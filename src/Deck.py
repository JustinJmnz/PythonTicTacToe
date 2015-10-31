import numpy as np

class Deck(object):
    
    def __init__(self):
        '''
        :return: Deck object
        '''
        self.player1Board = np.matrix([[0,0,0],[0,0,0],[0,0,0]])
        self.player2Board = np.matrix([[0,0,0],[0,0,0],[0,0,0]])
        self.tieBoard = np.matrix([[1,1,1],[1,1,1],[1,1,1]])
        self.visualBoard = np.matrix([['','',''],['','',''],['','','']])
        self.player1Choices = []
        self.player2Choices = []
        
    def __str__(self):
        '''
        Output of the board
        :return: The board used for output
        '''
        return self.visualBoard
    def getTieBoard(self):
        '''
        :return: Board used for tie game
        '''
        return self.tieBoard
    def getP1Board(self):
        '''
        :return: Board used for logic
        '''
        return self.player1Board
    def getP2Board(self):
        '''
        :return: Board used for logic
        '''
        return self.player2Board
    def getVisualBoard(self):
        '''
        :return: Board used for output
        '''
        return self.visualBoard