#Generate.py
#Created by Artur Smiechowski 14/02/2021
import pyrosim.pyrosim as pyrosim
import pybullet

length = 1
width = 1
height = 1
rx = 0
ry = 0
rz = 1.5
wx = 3
wy = 3
wz = 0.5

def Create_World():
    pyrosim.Start_SDF("box.sdf")
    pyrosim.Send_Cube(name="Box",pos=[wx,wy,wz],size=[length,width,height])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso",pos=[rx,ry,rz],size=[length,width,height])
    pyrosim.Send_Joint(name="Torso_Leg_Front",parent="Torso",child="Front_Leg",type="revolute",position= "rx+0.5 ry rz-0.5")
    pyrosim.Send_Cube(name="Front_Leg",pos=[rx+1,ry,rz-1],size=[length,width,height])
    pyrosim.Send_Joint(name="Torso_Leg_Back",parent="Torso",child="Back_Leg",type="revolute",position= "rx-0.5 ry rz-0.5")
    pyrosim.Send_Cube(name="Back_Leg",pos=[rx-1,ry,rz-1],size=[length,width,height])
    pyrosim.End()


Create_World()
Create_Robot()
