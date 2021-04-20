import numpy as np

g = -9.8

sim_length = 300
sim_freq = 1/60

f_amp = np.pi/3
f_freq = 1/25
f_phase = 0

b_amp = np.pi/6
b_freq = 1/25
b_phase = np.pi/4

max_force = 500
motorJointRange = 0.2

numSensorNeurons = 9
numMotorNeurons = 8

numberOfGenerations = 5
populationSize = 5