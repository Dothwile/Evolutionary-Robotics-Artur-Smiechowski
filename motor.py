#motor.py
#Created by Artur Smiechowski 14/03/2021

import numpy as np
import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:
    
    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = np.zeros(c.sim_length)
        
        self.amplitude = c.f_amp
        self.frequency = c.f_freq
        self.offset = c.f_phase
    
    def Set_Value(self, robot, cur_step):
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = robot,
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL, targetPosition = self.amplitude*np.sin(self.frequency*np.linspcae(0, c.sim_length, c.sim_length) + self.offset)[cur_step], maxForce = 30)