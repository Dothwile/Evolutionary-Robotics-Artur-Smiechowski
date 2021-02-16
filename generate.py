#Generate.py
#Created by Artur Smiechowski 14/02/2021
import pyrosim.pyrosim as pyrosim
import pybullet

pyrosim.Start_SDF("boxs.sdf")

length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5

pyrosim.Send_Cube(name="Box",pos=[x,y,z],size=[length,width,height])
pyrosim.Send_Cube(name="Box2",pos=[x,y,z],size=[length,width,height])

pyrosim.End()
