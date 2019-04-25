import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv('data/output_matched.csv', sep=',')

df['gt_theta'][df['gt_theta']<0] += np.pi
df['pred_theta'][df['pred_theta']<0] += np.pi

#%% ground truth
plt.subplot(3,4,1)
plt.hist(df['gt_length'], bins=np.linspace(0,13,100))
plt.axis([0, 13, 0, 1000])
plt.title('ground truth: length')

plt.subplot(3,4,2)
plt.hist(df['gt_width'], bins=np.linspace(0,4,100))
plt.axis([0, 3, 0, 400])
plt.title('ground truth: width')

plt.subplot(3,4,3)
plt.hist(df['gt_height'], bins=np.linspace(0,4,100))
plt.axis([0, 4, 0, 800])
plt.title('ground truth: height')

plt.subplot(3,4,4)
plt.hist(df['gt_theta'], bins=np.linspace(0,np.pi,100))
plt.axis([0, np.pi, 0, 800])
plt.title(r'ground truth: $\alpha$')

#%% prediction
plt.subplot(3,4,5)
plt.hist(df['pred_length'], bins=np.linspace(0,13,100))
plt.axis([0, 13, 0, 1000])
plt.title('prediction: length')

plt.subplot(3,4,6)
plt.hist(df['pred_width'], bins=np.linspace(0,4,100))
plt.axis([0, 3, 0, 400])
plt.title('prediction: width')

plt.subplot(3,4,7)
plt.hist(df['pred_height'], bins=np.linspace(0,4,100))
plt.axis([0, 4, 0, 800])
plt.title('prediction: height')

plt.subplot(3,4,8)
plt.hist(df['pred_theta'], bins=np.linspace(0,np.pi,100))
plt.axis([0, np.pi, 0, 800])
plt.title(r'prediction: $\alpha$')

#%% difference

diff_length = df['pred_length'] - df['gt_length']
diff_width = df['pred_width'] - df['gt_width']
diff_height = df['pred_height'] - df['gt_height']
diff_theta = df['pred_theta'] - df['gt_theta']

q = np.quantile(diff_length, [0.025, 0.975])
plt.subplot(3,4,9)
plt.gca().add_patch(plt.Rectangle((q[0],0),q[1]-q[0],1000, color=(0.7,0.7,0.7)))
plt.hist(diff_length, bins=100)
plt.axis([-12.5, 12.5, 0, 1000])
plt.title('difference: length')

q = np.quantile(diff_width, [0.025, 0.975])
plt.subplot(3,4,10)
plt.gca().add_patch(plt.Rectangle((q[0],0),q[1]-q[0],400, color=(0.7,0.7,0.7)))
plt.hist(diff_width, bins=100)
plt.axis([-3, 3, 0, 400])
plt.title('difference: width')

q = np.quantile(diff_height, [0.025, 0.975])
plt.subplot(3,4,11)
plt.gca().add_patch(plt.Rectangle((q[0],0),q[1]-q[0],800, color=(0.7,0.7,0.7)))
plt.hist(diff_height, bins=100)
plt.axis([-3, 3, 0, 800])
plt.title('difference: height')

q = np.quantile(diff_theta, [0.025, 0.975])
plt.subplot(3,4,12)
plt.gca().add_patch(plt.Rectangle((q[0],0),q[1]-q[0],1000, color=(0.7,0.7,0.7)))
plt.hist(diff_theta, bins=100)
plt.axis([-np.pi, np.pi, 0, 800])
plt.title(r'difference: $\alpha$')

plt.show()