#sensor.py
#Created by Artur Smiechowski 14/03/2021

import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim

class SENSOR:
    
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.sim_length)
        
    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        
    def Save_Sensor_Values(self):
        np.save("data/" + self.linkName + ".npy",self.values)