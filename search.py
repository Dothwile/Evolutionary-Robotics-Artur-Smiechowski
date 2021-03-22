#search.py
#Created by Artur Smiechowski 22/03/2021
import os

for sim_count in range(5):
    os.system("python generate.py")
    os.system("python simulate.py")