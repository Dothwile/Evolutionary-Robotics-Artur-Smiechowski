# hillclimber.py
#Created by Artur Smiechowski 27/03/2021

from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        
        self.nextAvailableID = 0
        self.parents = {}
        for parent in range(c.populationSize):
            self.parents[parent] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        
    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        #self.Print()
        #self.Select()
    
    def Spawn(self):
        self.children = {}
        for parent in self.parents:
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
    
    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()
    
    def Select(self):
        if self.child.fitness > self.parent.fitness:
            self.parent = self.child
            
    def Print(self):
        print(str(self.parent.fitness) + " " + str(self.child.fitness))
        
    def Show_Best(self):
        #self.parent.Evaluate("GUI")
        pass
    
    def Evaluate(self, solutions):
        for solution in solutions:
            solutions[solution].Start_Simulation("GUI")
        for solution in solutions:
            solutions[solution].Wait_For_Simulation_To_End()