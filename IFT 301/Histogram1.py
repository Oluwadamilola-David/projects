import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

data = {'Height': [175, 158, 166, 175, 160, 165, 166, 170, 170, 172, 184, 182, 180, 191, 189, 181, 180, 180, 170, 176],
        'Breath Held': [22.22, 30.57, 17.47, 22.39, 26.90, 36.85, 27.33, 29.55, 13.87, 34.66, 60.75, 67.41, 42.19, 59.74, 52.64, 43.37, 73.27, 59.09, 51.15, 58.32]}

df = pd.DataFrame(data)

plt.hist(df['Breath Held'], bins=10, edgecolor='black')
plt.xlabel('Breath Held (s)')
plt.ylabel('Frequency')
plt.title('Histogram of Breath Holding Times')
plt.show()

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.scatter(df['Height'], df['Breath Held'], color='blue', alpha=0.7)
plt.xlabel('Height (cm)')
plt.ylabel('Breath Held (s)')
plt.title('Female Breath Holding Times')

plt.subplot(1, 2, 2)
plt.scatter(df['Height'], df['Breath Held'], color='red', alpha=0.7)
plt.xlabel('Height (cm)')
plt.ylabel('Breath Held (s)')
plt.title('Male Breath Holding Times')

plt.tight_layout()
plt.show()