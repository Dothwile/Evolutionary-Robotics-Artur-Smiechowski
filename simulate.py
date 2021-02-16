#simulate.py
#Created by Artur Smiechowski 14/02/2021
import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI) #Create Physics Client
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#Set World Parameters
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")

#Load World
p.loadSDF("boxs.sdf")

for step in range(1000):
    #Loop step times
    p.stepSimulation()
    time.sleep(1/60)

p.disconnect() #Disconnect from Physics client
