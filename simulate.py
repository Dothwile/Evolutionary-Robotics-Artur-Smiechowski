#simulate.py
#Created by Artur Smiechowski 14/02/2021

import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c
from simulation import SIMULATION

'''




f_targetAngles = c.f_amp*np.sin(c.f_freq*np.linspace(0,c.sim_length,c.sim_length) + c.f_phase)
b_targetAngles = c.b_amp*np.sin(c.b_freq*np.linspace(0,c.sim_length,c.sim_length) + c.b_phase)

backLegSensorValues = np.zeros(c.sim_length)
frontLegSensorValues = np.zeros(c.sim_length)
print(backLegSensorValues)
print(frontLegSensorValues)

for step in range(c.sim_length):
    #Loop step times
    p.stepSimulation()
    backLegSensorValues[step] = pyrosim.Get_Touch_Sensor_Value_For_Link("Back_Leg")
    frontLegSensorValues[step] = pyrosim.Get_Touch_Sensor_Value_For_Link("Front_Leg")

    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,jointName="Torso_Leg_Back",controlMode=p.POSITION_CONTROL,targetPosition=b_targetAngles[step],maxForce=c.max_force)
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,jointName="Torso_Leg_Front",controlMode=p.POSITION_CONTROL,targetPosition=f_targetAngles[step],maxForce=c.max_force)
    
    time.sleep(1/60)

p.disconnect() #Disconnect from Physics client

# \ in filepath names trip formatting issues, thus the leading 'r' to declare literal
#np.save(r'data\SensorDat1',backLegSensorValues)
np.save(r'data\frontLegSensorValues',frontLegSensorValues)

#np.save(r'data\targetAngles',targetAngles)

#np.save(r'data\f_targetAngles',f_targetAngles)
#np.save(r'data\b_targetAngles',b_targetAngles)

print(backLegSensorValues)
print(frontLegSensorValues)
'''
'''
physicsClient = p.connect(p.GUI) #Create Physics Client
p.setAdditionalSearchPath(pybullet_data.getDataPath())
'''
simulation = SIMULATION()
