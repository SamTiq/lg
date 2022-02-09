class Player:
    
    def __init__(self, username):
        
        self.username = username
        self.camp = 0 # 0 Pour villageois, 1 pour loup garou et 2 pour en couple
        self.isDead = False
        self.willDie = False
        self.village_vote = None
        self.inLove = False

    def getUsername(self):
        return self.username
    
    def setUsername(self, username):
        self.username = username
    
    def getCamp(self):
            return self.camp
    
    def setCamp(self, camp):
        self.camp = camp

    def getIsDead(self):
            return self.isDead
    
    def setIsDead(self, isDead):
        self.isDead = isDead

    def getWillDie(self):
            return self.willDie
    
    def setWillDie(self, willDie):
        self.willDie = willDie
        
    def getVote(self):
            return self.vote
    
    def setVote(self, vote):
        self.vote = vote