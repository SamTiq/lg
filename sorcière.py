from player import *

class Sorcière(Player):
    
    def __init__(self, username):

        super().__init__(username)
        self.potion_heal = True 
        self.potion_death = True
        
    def getPotionHeal(self):
        return self.potion_heal
    
    def setPotionHeal(self, potion_heal):
        self.potion_heal = potion_heal
    
    def getPotionDeath(self):
        return self.potion_death
    
    def setPotionDeath(self, potion_death):
        self.potion_death = potion_death
    
    def usePotionHealth(self, player):
        print("test") #### TO DO #####
        
    def usePotionDeath(self, player):
        print("test") #### TO DO #####