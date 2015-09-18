import math, random

class Civilization:
    def __init__(self, nation, leader, seed):
        self.nationName = nation
        self.leaderName = leader
        self.seed = seed
        self.population = random.randint(23, 47)
        self.truePop = float(self.population)
        self.growthRate = 0.02
        self.happiness = 0

    def increasePop(self):
        self.truePop+=(self.truePop*self.growthRate)
        self.population = math.trunc(self.truePop)
        
