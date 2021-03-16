#robot.py
#Created by Artur Smiechowski 14/03/2021

import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    
    def __init__(self):
        
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
            
    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            
    def Sense(self, t):
        for sensor in self.sensors:
            self.sensors.get(sensor).Get_Value(t)
    
    def Act(self, t):
        for motor in self.motors:
            self.motors.get(motor).Set_Value(self.robotId, t)