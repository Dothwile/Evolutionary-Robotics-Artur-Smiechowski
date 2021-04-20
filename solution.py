#solution.py
#Created by Artur Smiechowski 28/03/2021

import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c

class SOLUTION:
    
    def __init__(self, myID):
        self.myID = myID
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)*2-1
        
    def Evaluate(self, directOrGUI):
        '''
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        
        os.system("start /B python simulate.py " + str(directOrGUI) + " " + str(self.myID))
        
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
        f = open("fitness" + str(self.myID) + ".txt")
        self.fitness = float(f.read())
        print(self.fitness)
        f.close()
        '''
        pass
        
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        
        os.system("start /B python simulate.py " + str(directOrGUI) + " " + str(self.myID))
    
    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
        f = open("fitness" + str(self.myID) + ".txt")
        self.fitness = float(f.read())
        print(self.fitness)
        f.close()
        os.system("del fitness" + str(self.myID) + ".txt")
        
    def Create_World(self):
        pyrosim.Start_SDF("world" + str(self.myID) + ".sdf")
        pyrosim.Send_Cube(name="Box", pos=[-5,5,0.5] , size=[1,1,1])
        pyrosim.End()
    
    def Create_Body(self):
        pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0.0,0,1.0] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = "0 0.5 1", jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = "0 -0.5 1", jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[0.2,1,0.2])
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = "-0.5 0 1", jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0] , size=[1,0.2,0.2])
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = "0.5 0 1", jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0] , size=[1,0.2,0.2])
        
        pyrosim.Send_Joint( name = "FrontLeg_LowerFrontLeg" , parent= "FrontLeg" , child = "LowerFrontLeg" , type = "revolute", position = "0 1 0", jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "BackLeg_LowerBackLeg" , parent= "BackLeg" , child = "LowerBackLeg" , type = "revolute", position = "0 -1 0", jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LowerBackLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "LeftLeg_LowerLeftLeg" , parent= "LeftLeg" , child = "LowerLeftLeg" , type = "revolute", position = "-1 0 0", jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "RightLeg_LowerRightLeg" , parent= "RightLeg" , child = "LowerRightLeg" , type = "revolute", position = "1 0 0", jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LowerRightLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        
        pyrosim.End()
        
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        #pyrosim.Start_NeuralNetwork("brain.nndf")
        
        # Neurons
        
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "LowerFrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "LowerBackLeg")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LowerLeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "LowerRightLeg")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "FrontLeg_LowerFrontLeg")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "BackLeg_LowerBackLeg")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "LeftLeg_LowerLeftLeg")
        pyrosim.Send_Motor_Neuron( name = 16 , jointName = "RightLeg_LowerRightLeg")
        
        # Synapses
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])
        
        pyrosim.End()
        
    def Mutate(self):
        self.weights[random.randint(0,c.numMotorNeurons),random.randint(0,1)] = random.random()*2-1
        
    def Set_ID(self, ID):
        self.myID = ID