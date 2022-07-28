import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

f = pd.read_csv('air_traffic.csv', index_col = 'month')
print(f)

plt.plot(f['volume'])
plt.show()

tau = 3
S = []
for i in range(tau, len(f) - tau):
	S.append(np.log(f['volume'][i - tau] * f['volume'][i + tau] / f['volume'][i]**2))

plt.plot(S)
plt.show()
