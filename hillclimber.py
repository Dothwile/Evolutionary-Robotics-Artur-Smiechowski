# hillclimber.py
#Created by Artur Smiechowski 27/03/2021

from solution import SOLUTION

class HILL_CLIMBER:
    
    def __init__(self):
        self.parent = SOLUTION()
        
    def Evolve(self):
        self.parent.Evaluate()