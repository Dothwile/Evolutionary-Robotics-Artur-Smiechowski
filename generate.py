#Generate.py
#Created by Artur Smiechowski 14/02/2021
import pyrosim.pyrosim as pyrosim
import pybullet

pyrosim.Start_SDF("box.sdf")

pyrosim.Send_Cube(name="Box",pos=[0,0,0.5],size=[1,1,1])

pyrosim.End()
