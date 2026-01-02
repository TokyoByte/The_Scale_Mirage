import pandas as pd
import numpy as np

data = pd.read_csv("/home/fornax/Documents/Programs/The Scale Mirage/rawData.csv")

print(data.head())
print(data.size)
print(len(data))
x = data["x"].tolist()
y = data["y"].tolist()

print(len(x))
print(x[0])

import matplotlib.pyplot as plt

plt.scatter(x,y) #Didn't see any pattern, Notices that coordinate values are huge
plt.xlabel("X coordinates")
plt.ylabel("Y Coordinates")
plt.title("scattered data")
plt.show()
#------------------------------#

plt.hist(x, bins=100) #visualizing the frequency of ranges (bins) in the data
plt.hist(y, bins=100)
plt.yscale("log")     #using log to compress the large values
plt.xlabel("Value range")
plt.ylabel("Frequency")
plt.title("Frequency histogram")
plt.show()
#------------------------------#

plt.scatter(x, y, s=1) #Zooming in the desired area we got from histogram above and reducing the size of dot
plt.xlim(-5, 20) 
plt.ylim(-5, 20)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Visual codeword")
plt.show() # DATABIZ

#-------------------Extracting the desired value--------------#

x_true = []
y_true = []

for i in x:
    if i >= -5 and i <= 20:
        x_true.append(i)

for i in y:
    if i >= -5 and i <= 20:
        y_true.append(i)

plt.scatter(x_true, y_true)
plt.show()