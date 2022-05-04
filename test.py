import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

f = open("velocityObs_cleaned.txt", "r")
f_read = f.read()
f_split1 = f_read.split("\n")
time_s_list = []
time_ms_list = []
vel_list = []
turn_rate_list = []
time_list = []
x_list = []
y_list = []

for data in f_split1:
    time_s = int(data.split(" ")[0])
    time_s = time_s - 1115116000
    time_ms = float(data.split(" ")[1]) * 10 ** (-6)
    vel = float(data.split(" ")[2])
    turn_rate = float(data.split(" ")[3])
    time = time_s + time_ms
    time_new =


print(time_list)







