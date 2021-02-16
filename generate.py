#Generate.py
#Created by Artur Smiechowski 14/02/2021
import pyrosim.pyrosim as pyrosim
import pybullet

length = 1
width = 1
height = 1
x = 0
y = 0
z = 0

def Create_World():
    pyrosim.Start_SDF("boxs.sdf")
    pyrosim.Send_Cube(name="Box",pos=[x,y,z],size=[length,width,height])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso",pos=[x,y,z],size=[length,width,height])
    pyrosim.End()


Create_World()
Create_Robot()
