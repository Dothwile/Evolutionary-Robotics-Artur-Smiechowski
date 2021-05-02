#search.py
#Created by Artur Smiechowski 22/03/2021
import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()

parents = phc.parents
best = parents[0]
for parent in parents:
    if parent.fitness < best.fitness:
        best = parent

'''
for sim_count in range(5):
    os.system("python generate.py")
    os.system("python simulate.py")
'''