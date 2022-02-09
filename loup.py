from player import *

class Loup(Player):
    
    def __init__(self, username):

        super().__init__(username)
        
        self.loup_vote = None 
        self.camp = 1
        
    def getLoupVote(self):
        return self.loup_vote
    
    def setLoupVote(self, loup_vote):
        self.loup_vote = loup_vote
    