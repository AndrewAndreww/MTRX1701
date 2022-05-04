import re
import matplotlib.pyplot as plt
import math
import numpy as np

filename="velocityObs_cleaned.txt"
txt=open(filename, "r")
contents=txt.read()

timesecs=[]
timemicrosecs=[]
velocity=[]
turnrate=[]

for line in contents.split("\n"):
    timesecs.append(int(line.split()[0]))
    timemicrosecs.append(float(line.split()[1]))
    velocity.append(float(line.split()[2]))
    turnrate.append(float(line.split()[3]))

velocityarray = np.array(velocity)
timesecsarray = np.array(timesecs)
timemicrosecsarray = np.array(timemicrosecs)

print(timemicrosecsarray)

import re
import matplotlib.pyplot as plt
import math
import numpy as np

# filename="velocityObs_cleaned.txt"
# txt=open(filename, "r")
# contents=txt.read()
#
# timesecs=[]
# timemicrosecs=[]
# velocity=[]
# turnrate=[]
#
# for lines in contents.split("\n"):
#     print(lines)

# velocityarray=np.array(velocity)
# timesecsarray=np.array(timesecs)
# timemicrosecsarray=np.array(timemicrosecs)

# changeintime=timesecsarray+timemicrosecsarray
#
# print(timesecsarray)