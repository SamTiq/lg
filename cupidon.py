from player import *

class Cupidon(Player):
    
    def __init__(self, username):

        super().__init__(username)       
        self.power = True 

        
    def getPower(self):
        return self.power
    
    def setPower(self, power):
        self.power = power
    
    def usePower(self, player1, player2):
        print("yesy") #### TO DO #####
