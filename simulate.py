#simulate.py
#Created by Artur Smiechowski 14/02/2021
import pybullet as p
import time

physicsClient = p.connect(p.GUI) #Create Physics Client

for step in range(1000):
    #Loop step times
    p.stepSimulation()
    time.sleep(1/60)

p.disconnect() #Disconnect from Physics client
