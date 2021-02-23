#Analyze.py
#Created by Artur Smiechowski 22/02/2021
import numpy as np
import matplotlib.pyplot as plt

# 'r' added in front of path to avoid triiping formatting issues from \
backLegSensorValues = np.load(r'data\SensorDat1.npy')
frontLegSensorValues = np.load(r'data\frontLegSensorValues.npy')

plt.plot(backLegSensorValues,label='back_leg',linewidth=3)
plt.plot(frontLegSensorValues,label='front_leg')
plt.legend()
plt.show()
