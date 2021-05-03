#robot.py
#Created by Artur Smiechowski 14/03/2021

import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as np
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

class ROBOT:
    
    def __init__(self, solutionID):
        
        self.solutionID = solutionID
        self.robot = p.loadURDF("body" + str(solutionID) + ".urdf")
                
        pyrosim.Prepare_To_Simulate("body" + str(solutionID) + ".urdf")
        
        self.nn = NEURAL_NETWORK("brain" + str(self.solutionID) + ".nndf")
        os.system("del brain" + str(solutionID) + ".nndf")
        
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
         for neuron in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuron):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuron)
                desiredAngle = self.nn.Get_Value_Of(neuron)*c.motorJointRange
                self.motors.get(jointName).Set_Value(self.robot, desiredAngle)
                
                
    def Think(self):
        self.nn.Update()
        #self.nn.Print() # Prints out Motor and Sensor Neuron Values Each Simulation Step
        
    def Get_Fitness(self):
        #positionOfLinkZero = p.getLinkState(self.robot,0)[0]
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        #xCoordinateOfLinkZero = positionOfLinkZero[0]
        basePosition = basePositionAndOrientation[0]
        zPosition = basePosition[2]
        
        # longestJump = 0
        # currentRun = 0
        # for step in range(c.sim_length):
        #     if(not (self.sensors["LowerBackLeg"].values[step]+1 and self.sensors["LowerFrontLeg"].values[step]+1 and self.sensors["LowerLeftLeg"].values[step]+1 and self.sensors["LowerRightLeg"].values[step]+1)):
        #         currentRun += 1
        #     else:
        #         currentRun = 0
                
        #     if(currentRun > longestJump):
        #         longestJump = currentRun
        
        self.sensors["LowerBackLeg"].Save_Sensor_Values()
        self.sensors["LowerFrontLeg"].Save_Sensor_Values()
        self.sensors["LowerLeftLeg"].Save_Sensor_Values()
        self.sensors["LowerRightLeg"].Save_Sensor_Values()
        
        longestJump = 0
        currentJump = 0
        for step in range(c.sim_length):
            if((self.sensors["LowerBackLeg"].values[step] == -1) and (self.sensors["LowerFrontLeg"].values[step] == -1) and (self.sensors["LowerLeftLeg"].values[step] == -1) and (self.sensors["LowerRightLeg"].values[step] == -1)):
                currentJump += 1
            else:
                currentJump = 0
            
            if(currentJump > longestJump):
                longestJump = currentJump
        
        fitness = longestJump
        
        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        f.write(str(fitness))
        f.close()
        os.rename("tmp" + str(self.solutionID) + ".txt ", "fitness" + str(self.solutionID) + ".txt")

        return p.getLinkState(self.robot,0)
