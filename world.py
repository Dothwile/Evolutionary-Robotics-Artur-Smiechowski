#world.py
#Created by Artur Smiechowski 14/03/2021

import pybullet as p

class WORLD:
    
    def __init__(self):
        
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")