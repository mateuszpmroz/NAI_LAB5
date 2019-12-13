import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from io import StringIO
import csv


dataCsv = '''
-0.86,4.38,
2.58,6.97,
4.17,7.01,
2.6,5.44,
5.13,6.45,
3.23,5.49,
-0.26,4.25,
2.76,5.94,
0.47,4.8,
-3.9,2.7,
0.27,3.26,
2.88,6.48,
-0.54,4.08,
-4.39,0.09,
-1.12,2.74,
2.09,5.8
'''
f = StringIO(dataCsv)
reader = csv.reader(f, delimiter=',')

data = []

for row in reader:
    data = row[0:]


print(data)
plik_wejsciowy = "mydata.txt"
print(data)
X, y = data[:, :-1], data[:, -1]
print(X)
print(y)

num_traing = int(len(X)*0.9)
num_test = len(X) - num_traing

X_tran, y_tran = X[:num_traing], y[:num_traing]
X_test, y_test = X[num_traing:], y[num_traing:]

regressor = linear_model.HuberRegressor()
regressor.fit(X_tran, y_tran)

y_test_pred = regressor.predict(X_test)

plt.scatter(X_test, y_test, color='red')
plt.plot(X_test, y_test_pred, color='black')

plt.show()
