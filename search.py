#search.py
#Created by Artur Smiechowski 22/03/2021
import os
from hillclimber import HILL_CLIMBER

hc = HILL_CLIMBER()
hc.Evolve()
hc.Show_Best()
'''
for sim_count in range(5):
    os.system("python generate.py")
    os.system("python simulate.py")
'''