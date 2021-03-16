#Simulation.py
#Created by Artur Smiechowski 14/03/2021

import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import constants as c
from world import WORLD
from robot import ROBOT

class SIMULATION:

    def __init__(self):
                
        self.physicsClient = p.connect(p.GUI) #Create Physics Client
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        #Set World Parameters
        p.setGravity(0,0,c.g)

        # Create a World object
        self.world = WORLD()
        # Create a Robot object
        self.robot = ROBOT()
        
    def Run(self):
        for step in range(c.sim_length):
            #Loop step times
            p.stepSimulation()
            
            self.robot.Sense(step)
            self.robot.Act(step)

            time.sleep(1/60)
            
            self.robot.SaveSensorValues()
            self.robot.SaveMotorValues()
            
    def __del__(self):
        p.disconnect()

        