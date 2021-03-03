#simulate.py
#Created by Artur Smiechowski 14/02/2021
import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

physicsClient = p.connect(p.GUI) #Create Physics Client
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#Set World Parameters
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

steps = 1000

f_amplitude = np.pi/3
f_frequency = 1/25
f_phaseOffset = 0

f_targetAngles = f_amplitude*np.sin(f_frequency*np.linspace(0,1000,1000) + f_phaseOffset)

b_amplitude = np.pi/6
b_frequency = 1/25
b_phaseOffset = np.pi/4

b_targetAngles = b_amplitude*np.sin(b_frequency*np.linspace(0,1000,1000) + b_phaseOffset)

#Load World
p.loadSDF("box.sdf")

pyrosim.Prepare_To_Simulate("body.urdf")

backLegSensorValues = np.zeros(steps)
frontLegSensorValues = np.zeros(steps)
print(backLegSensorValues)
print(frontLegSensorValues)

for step in range(steps):
    #Loop step times
    p.stepSimulation()
    backLegSensorValues[step] = pyrosim.Get_Touch_Sensor_Value_For_Link("Back_Leg")
    frontLegSensorValues[step] = pyrosim.Get_Touch_Sensor_Value_For_Link("Front_Leg")

    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,jointName="Torso_Leg_Back",controlMode=p.POSITION_CONTROL,targetPosition=b_targetAngles[step],maxForce=500)
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,jointName="Torso_Leg_Front",controlMode=p.POSITION_CONTROL,targetPosition=f_targetAngles[step],maxForce=500)
    
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
