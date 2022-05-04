import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

f = open("velocityObs_cleaned.txt", "r")
f_read = f.read()
f_split1 = f_read.split("\n")
time_s = []
time_ms = []
vel = []
turn_rate = []
time = []

for data in f_split1:
    time_s.append(int(data.split(" ")[0]))
    time_ms.append(float(data.split(" ")[1]))
    vel.append(float(data.split(" ")[2]))
    turn_rate.append(float(data.split(" ")[3]))

arr_time_s = np.array(time_s)
arr_time_ms = np.array(time_ms) * 10 ** (-6)
arr_vel = np.array(vel)
arr_turn_rate = np.array(turn_rate)
arr_time = arr_time_s + arr_time_ms
arr_time = arr_time - arr_time_s[0]
time = arr_time.tolist()
time.insert(0, 0.0)
del time[-1]
arr_time_new = np.array(time)
arr_turn_rate_cos = np.cos(arr_turn_rate)
arr_turn_rate_sin = np.sin(arr_turn_rate)
arr_turn_rate_cos = arr_turn_rate_cos.tolist()
print(arr_turn_rate_cos)

delta_time = arr_time - arr_time_new

# print(arr_time[:10])
# print(arr_time_new)
# print(delta_time)
# print(arr_vel[:100])
# print(arr_turn_rate[:100])

x = delta_time * arr_vel * arr_turn_rate_cos
x_list = x.tolist()
y = delta_time * arr_vel * arr_turn_rate_sin
y_list = y.tolist()


xData = []

for i in range(len(x_list)):
    if i == 0:
        xData.append(x_list[i])
    else:
        xData.append(x_list[i - 1] + x_list[i])

# print(xData)
