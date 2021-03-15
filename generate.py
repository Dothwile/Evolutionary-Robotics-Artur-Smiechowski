#Generate.py
#Created by Artur Smiechowski 14/02/2021
import pyrosim.pyrosim as pyrosim
import pybullet

length = 1
width = 1
height = 1
rx = 0
ry = 0
rz = 0.5

wx = 3
wy = 3
wz = 0.5

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box",pos=[wx,wy,wz],size=[length,width,height])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso",pos=[rx,ry,rz+1],size=[length,width,height])
    pyrosim.Send_Joint(name="Torso_Leg_Front",parent="Torso",child="Front_Leg",type="revolute",position= "0.5 0 1")
    pyrosim.Send_Cube(name="Front_Leg",pos=[rx+0.5,ry,rz-1],size=[length,width,height])
    pyrosim.Send_Joint(name="Torso_Leg_Back",parent="Torso",child="Back_Leg",type="revolute",position= "-0.5 0 1")
    pyrosim.Send_Cube(name="Back_Leg",pos=[rx-0.5,ry,rz-1],size=[length,width,height])
    pyrosim.End()


Create_World()
Create_Robot()
