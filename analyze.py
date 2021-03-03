#Analyze.py
#Created by Artur Smiechowski 22/02/2021
import numpy as np
import matplotlib.pyplot as plt

# 'r' added in front of path to avoid triiping formatting issues from \
'''
backLegSensorValues = np.load(r'data\SensorDat1.npy')
frontLegSensorValues = np.load(r'data\frontLegSensorValues.npy')

plt.plot(backLegSensorValues,label='back_leg',linewidth=3)
plt.plot(frontLegSensorValues,label='front_leg')
plt.legend()
plt.show()
'''
'''
targetAngles = np.load(r'data\targetAngles.npy')

plt.plot(np.linspace(0,1000, 1000),targetAngles,label='Target Angles')
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.legend()
plt.show()
'''
f_targetAngles = np.load(r'data\f_targetAngles.npy')
b_targetAngles = np.load(r'data\b_targetAngles.npy')


plt.plot(np.linspace(0,1000, 1000),f_targetAngles,label='Front Leg Target Angles')
plt.plot(np.linspace(0,1000, 1000),b_targetAngles,label='Back Leg Target Angles')
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.legend()
plt.show()
