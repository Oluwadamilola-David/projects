import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {'With music': [304, 257, 174, 214, 69, 317, 387, 47, 157, 0, 332, 308, 317, 286, 236, 299, 206, 278, 188, 43, 0, 0, 0, 0, 0],
        'Without music': [292, 270, 47, 288, 324, 292, 364, 316, 287, 75, 282, 149, 274, 319, 213, 3, 324, 2, 128, 219, 94, 164, 0, 0, 0]}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.scatter(df['With music'], np.arange(len(df['With music'])), color='blue', alpha=0.7)
plt.xlabel('Growth (mm)')
plt.ylabel('Plant Number')
plt.title('Plant Growth with Music')

plt.subplot(1, 2, 2)
plt.scatter(df['Without music'], np.arange(len(df['Without music'])), color='red', alpha=0.7)
plt.xlabel('Growth (mm)')
plt.ylabel('Plant Number')
plt.title('Plant Growth without Music')

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(df['With music'], bins=10, edgecolor='black')
plt.xlabel('Growth (mm)')
plt.ylabel('Frequency')
plt.title('Histogram of Plant Growth with Music')

plt.subplot(1, 2, 2)
plt.hist(df['Without music'], bins=10, edgecolor='black')
plt.xlabel('Growth (mm)')
plt.ylabel('Frequency')
plt.title('Histogram of Plant Growth without Music')

plt.tight_layout()
plt.show()