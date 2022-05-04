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


print(len(xData))
print(len(yData))

# fig, ax = plt.subplots()
# ax.grid()
# print(plt.subplots())
# ax.set_title("Dead Reckoning Positioning")
# ax.set_xlabel("X position (m)")
# ax.set_ylabel("Y position (m)")
#
# ax.set_xlim(min(xData), max(xData))
# ax.set_ylim(min(yData), max(yData))
#
# line, = ax.plot([], [])
#
# def init():
#     line.set_data([], [])
#     return line,
#
#
# def animate(i):
#     x = xData[:i + 1]
#     y = yData[:i + 1]
#     line.set_data(x, y)  # plot each x point and ypoint at each frame
#     return line,
#
# anim = FuncAnimation(fig, animate, init_func=init, frames=len(xData), interval=0.01)
# anim.save('animation.gif')
