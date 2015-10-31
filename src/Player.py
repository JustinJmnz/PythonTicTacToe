'''
Created on Oct 1, 2015

@author: justin
'''

class Player(object):

    def __init__(self):
        '''
        :return: A new Player
        '''
        self.name = None
        self.mark = None
        self.statistics = [0, 0, 0]  # [Win, Tie, Lost]

    def setWin(self):
        '''
        Will add a win to statistics
        '''
        self.statistics[0] += 1
    def setTie(self):
        '''
        Will add a tie to statistics
        '''
        self.statistics[1] += 1
    def setLost(self):
        '''
        Will add a lose to statistics
        '''
        self.statistics[2] += 1
    def setName(self, name):
        '''
        :param name: Set name of player
        '''
        self.name = name
    def setMark(self, mark):
        '''
        :param mark: Set mark of player
        '''
        self.mark = mark
    def getScore(self):
        '''
        Computes Score 
        :return: Statistics of player
        '''
        score = ((self.statistics[0] * 2) + self.statistics[1] - self.statistics[2])
        return score
    def __str__(self):
        '''
        :return: String representation of values inside Player
        '''
        return "Name: " + self.name + "\nMark: " + self.mark + "\nScore: " + self.getScore() + "\n"
    def __cmp__(self, player):
        '''
        Compares the players and returns the one winning
        :param: A Player 
        :return: Winner
        '''
        if self.getScore() > player.getScore():
            return self
        elif self.getScore() < player.getScore():
            return player
        else:
            return None
        


