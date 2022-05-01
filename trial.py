import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

f = open("velocityObs_cleaned.txt", "r")
f_read = f.read()
f_split1 = f_read.split("\n")
time_s = []
time_ms = []
vel = []
turn_rate = []

for data in f_split1:
    time_s.append(int(data.split()[0]))
    time_ms.append(float(data.split()[1]))
    vel.append(float(data.split()[2]))
    turn_rate.append(float(data.split()[3]))

arr_time_s = np.array(time_s)
arr_time_ms = np.array(time_ms) * 10**(-6)
arr_vel = np.array(vel)
arr_turn_rate = np.array(turn_rate)

arr_time = arr_time_s + arr_time_ms
