#robot.py
#Created by Artur Smiechowski 14/03/2021

import pybullet as p
import pyrosim.pyrosim as pyrosim

class ROBOT:
    
    def __init__(self):
        # Create Sensor and Motor libraries
        self.sensors = {}
        self.motors = {}
        
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        