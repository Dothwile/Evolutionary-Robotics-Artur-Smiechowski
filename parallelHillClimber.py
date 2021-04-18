# hillclimber.py
#Created by Artur Smiechowski 27/03/2021

from solution import SOLUTION
import constants as c
import copy
import os

# Git exmaple

class PARALLEL_HILL_CLIMBER:
    
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del body*.urdf")
        os.system("del world*.sdf")
        
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
        self.Print()
        self.Select()
    
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
        for solution in self.parents:
            if self.children[solution].fitness < self.parents[solution].fitness:
                self.parents[solution] = self.children[solution]
        
    def Print(self):
        print("")
        for solution in self.parents:
            print(str(self.parents[solution].fitness) + " " + str(self.children[solution].fitness))
        print("")
        
    def Show_Best(self):
        lowestFitness = self.parents[0]
        for parent in self.parents:
            if self.parents[parent].fitness < lowestFitness.fitness:
                lowestFitness = self.parents[parent]
        lowestFitness.Start_Simulation("GUI")
    
    def Evaluate(self, solutions):
        for solution in solutions:
            solutions[solution].Start_Simulation("DIRECT")
        for solution in solutions:
            solutions[solution].Wait_For_Simulation_To_End()