import numpy as np

import matplotlib.pyplot as plt

# Parameters
mean = 0
std = 1
num_features = 6
entries = 20

features = [np.random.normal(mean, std, entries) for _ in range(num_features)]

# Min max normalization
features = [(feature - np.min(feature)) / (np.max(feature) - np.min(feature)) for feature in features]

angles = np.linspace(0, 2 * np.pi, num_features, endpoint=False).reshape(-1, 1).repeat(entries, axis=1)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# set num_features xticks and labels
ax.set_xticks(angles[:, 0])
ax.set_xticklabels([f'{int(max(np.cos(i/num_features*2*np.pi),0) *10)* ' '}Feature {i}{int(max(-np.cos(i/num_features*2*np.pi),0) *10)* ' '}' for i in range(num_features)])

for i, feature in enumerate(features):
    ax.scatter(angles[i], feature, label=f'Feature {i}')

plt.show()

