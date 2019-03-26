import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv('data/hist_data.csv', sep=',')

plt.subplot(1,2,1)
plt.hist(df['gt'], bins=100)
# plt.axis([-np.pi/2, np.pi/2, 0, 500])
plt.title('ground truth')

plt.subplot(1,2, 2)
plt.hist(df['pred'], bins=100)
# plt.axis([-np.pi/2, np.pi/2, 0, 500])
plt.title('prediction')

plt.show()