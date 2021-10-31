import numpy as np
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
plt.title('Numbers of blocks NN opened per Game')
plt.xlabel('Game')
ax2 = ax1.twinx()

ax1.set_ylabel('Opened Blocks', color='tab:blue')
ax1.plot(range(len(data)), data, color='tab:blue', alpha=0.75)
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2.set_ylabel('Opened Blocks (Avg of 250 Games)', color='black')
ax2.plot([ 250 * (i + 1) for i in range(len(data_avg))], data_avg, color='black', alpha=1)
ax2.tick_params(axis='y', labelcolor='black')

fig.tight_layout()
plt.show()