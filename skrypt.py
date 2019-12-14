import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from io import StringIO
import csv
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d

# data
dataCsv = '''1,2,1,2
2,2,1,1
1,2,1,1
1,2,1,1
1,2,1,2
1,2,1,1
2,2,1,2
1,5,1,2
1,2,1,1
1,2,1,1
1,2,1,2
2,3,1,1
1,2,1,1
1,2,1,2
1,4,1,2
2,2,1,1
1,2,3,2
2,2,1,2
1,2,1,2
1,2,1,1
2,5,1,2
1,2,1,1
1,1,1,1
1,2,1,1
1,2,1,1
1,2,1,1
1,2,1,2
1,2,1,2
1,2,1,1
1,2,1,2
1,2,1,1
1,2,1,1
1,2,3,2
1,2,1,1
1,2,1,2
1,2,1,1
1,2,1,1
1,4,1,1
1,2,1,2
1,2,1,1
1,1,1,1
1,2,1,1
1,4,1,2
1,2,1,1
2,2,2,1
1,2,1,2
1,4,1,1
1,2,1,1
2,5,1,1
1,2,1,1
1,2,1,2
1,2,1,2
1,2,1,1
1,5,1,1
1,2,1,1
1,5,1,2
1,2,1,1
1,2,1,1
2,1,1,1
1,5,1,1
1,2,1,1
2,2,1,1
1,2,2,2
1,2,1,1
1,2,1,2
1,2,1,1
1,4,1,2
2,2,1,1
1,2,1,1
2,2,1,1
1,3,1,1
1,2,1,2
2,3,1,2
2,2,1,1
2,2,1,2
1,2,1,1
2,2,1,2
1,2,1,1
1,3,1,1
1,2,1,1
2,2,1,2
'''
f = StringIO(dataCsv)
reader = csv.reader(f, delimiter=',')

data = list(reader)
dataX = []
dataY = []
dataZ = []
dataC = []
for row in data:
  # Sex (1 - Woman; 2 - Man)
  dataX.append(int(row[0]))
  # Age (1 - Under 18; 2 - 18-26; 3 - 27-35; 4 - 36-50; 5 - More than 50)
  dataY.append(int(row[1]))
  # Do you like animals? (1 - Yes; 2 - No; 3 - Hard to say)
  dataZ.append(int(row[2]))
  # Do you have animal? (1 - Yes; 2 - No)
  dataC.append(int(row[3]))



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Sex')
ax.set_ylabel('Age')
ax.set_zlabel('Do you like animals?')
plt.title('Owning a pet',fontsize=18)
ax.set_xticklabels([0, 1, 2])
ax.set_yticklabels([0, 1, 2, 3, 4, 5])
ax.set_zticklabels([0, 1, 2, 3])

img = plt.scatter(dataX, dataY, dataZ, c=dataC, cmap='hsv', linewidth=5)
fig.colorbar(img)

plt.show()

# Mateusz Mróz s15192
