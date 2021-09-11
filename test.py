import matplotlib.pyplot as plt
import numpy as np

np1 = np.genfromtxt('D:/USER/Desktop/新增資料夾/活頁簿2.csv', delimiter=',', encoding='ansi',dtype=None)
print(np1)

total_pcu = np1[5]
live = total_pcu.astype(float)
plt.plot(live)
plt.show()