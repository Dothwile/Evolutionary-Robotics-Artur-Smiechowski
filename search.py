#search.py
#Created by Artur Smiechowski 22/03/2021
import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()

'''
highestFitness = phc.parents[0]
for parent in phc.parents:
    if phc.parents[parent].fitness > highestFitness.fitness:
        highestFitness = phc.parents[parent]
'''

'''
for sim_count in range(5):
    os.system("python generate.py")
    os.system("python simulate.py")
'''