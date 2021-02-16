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

for x1 in range(6):
    for y1 in range(6):
        for n in range(10):
            pyrosim.Send_Cube(name="Box",pos=[x+x1,y+y1,z+n],size=[length*0.9**n,width*0.9**n,height*0.9**n])


#pyrosim.Send_Cube(name="Box",pos=[x,y,z],size=[length,width,height])
#pyrosim.Send_Cube(name="Box2",pos=[0.25,y,1.5],size=[length,width,height])

pyrosim.End()
