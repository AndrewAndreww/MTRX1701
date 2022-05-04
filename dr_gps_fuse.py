import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


###Dead Reckoning Data

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
delta_time = arr_time - arr_time_new

arr_heading = arr_turn_rate * delta_time
heading_list = arr_heading.tolist()

def nums_cumulative_sum(nums_list):
    return [sum(nums_list[:i + 1]) for i in range(len(nums_list))]

headingData = nums_cumulative_sum(heading_list)
# print(headingData)

headingData = np.array(headingData)
headingData_cos = np.cos(headingData)
headingData_sin = np.sin(headingData)

x = delta_time * arr_vel * headingData_cos
x_list = x.tolist()

y = delta_time * arr_vel * headingData_sin
y_list = y.tolist()

xData = nums_cumulative_sum(x_list)
yData = nums_cumulative_sum(y_list)


###GPS data

f = open("positionObs_cleaned.txt", "r")
f_read = f.read()
f_split1 = f_read.split("\n")
time_s_gps = []
time_ms_gps = []
x_gps = []
y_gps = []

for data in f_split1:
    time_s_gps.append(int(data.split()[0]))
    time_ms_gps.append(float(data.split()[1]))
    x_gps.append(float(data.split()[2]))
    y_gps.append(float(data.split()[3]))

arr_time_s_gps = np.array(time_s_gps)
arr_time_ms_gps = np.array(time_ms_gps) * 10 ** (-6)
arr_x_gps = np.array(x_gps)
arr_y_gps = np.array(y_gps)
arr_time_gps = arr_time_s_gps + arr_time_ms_gps
arr_time_gps = arr_time_gps - arr_time_s_gps[0]
time_gps = arr_time_gps.tolist()
time_gps.insert(0, 0.0)
del time_gps[-1]
arr_time_new_gps = np.array(time_gps)
delta_time_gps = arr_time_gps - arr_time_new_gps

###Fuse (?)

# print(len(xData)/len(x_gps))
#
# print(len(x_gps)*8)
list_of_indices = []
num = len(xData)/len(x_gps)

for x in range(0, len(x_gps)):
    num1 = round(num + x*num)
    list_of_indices.append(num1)

print(list_of_indices)

arr_list_of_indices = np.array(list_of_indices)
arr_list_of_indices = arr_list_of_indices - 1
list_of_indices = arr_list_of_indices.tolist()

xData_array = np.array(xData)
accessed_series_x = xData_array[list_of_indices]
accessed_list_x = list(accessed_series_x)

yData_array = np.array(yData)
accessed_series_y = yData_array[list_of_indices]
accessed_list_y = list(accessed_series_y)


accessed_list_x_arr = np.array(accessed_list_x)
accessed_list_y_arr = np.array(accessed_list_y)

x_fuse = accessed_list_x_arr + (arr_x_gps - accessed_list_x_arr)*0.9
y_fuse = accessed_list_y_arr + (arr_x_gps - accessed_list_y_arr)*0.9

print(x_fuse)
print(y_fuse)

plt.grid()
plt.plot(x_fuse, y_fuse)
plt.title("GPS Positioning Fuse")
plt.xlabel("X axis (m)")
plt.ylabel("Y axis (m)")
plt.savefig("gps_plot_fuse_0.9.png")