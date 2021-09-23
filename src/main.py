import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Initial data
f = pd.read_csv('air_traffic.csv')
print(f)

plt.plot(f['volume'])
plt.show()

#Exclusion of a trend
tau = 3
S = []
for i in range(tau, len(f) - tau):
	S.append(np.log(f['volume'][i - tau] * f['volume'][i + tau] / f['volume'][i]**2))

plt.plot(S)
plt.show()
