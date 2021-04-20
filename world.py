#world.py
#Created by Artur Smiechowski 14/03/2021

import pybullet as p

class WORLD:
    
    def __init__(self, solutionID):
        p.loadSDF("world" + str(solutionID) + ".sdf")
        #print("Loaded world")
        self.planeId = p.loadURDF("plane.urdf")
        #print("Loaded plane")