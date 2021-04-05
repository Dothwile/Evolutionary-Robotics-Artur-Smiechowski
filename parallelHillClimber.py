# hillclimber.py
#Created by Artur Smiechowski 27/03/2021

from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    
    def __init__(self):
        self.nextAvailableID = 0
        self.parents = {}
        for parent in range(c.populationSize):
            self.parents[parent] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        
    def Evolve(self):
        '''
        self.parent.Evaluate("GUI")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        '''
        for parent in self.parents:
            self.parents[parent].Start_Simulation("DIRECT")
        for parent in self.parents:
            self.parents[parent].Wait_For_Simulation_To_End()
            
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()
    
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID += 1
    
    def Mutate(self):
        self.child.Mutate()
    
    def Select(self):
        if self.child.fitness > self.parent.fitness:
            self.parent = self.child
            
    def Print(self):
        print(str(self.parent.fitness) + " " + str(self.child.fitness))
        
    def Show_Best(self):
        #self.parent.Evaluate("GUI")
        pass