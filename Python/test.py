import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('D:/Database/建中/traffic_CKHS/csv/多年pcu比較.csv', encoding='ansi')

rows = (df['方向'] == '合計')
columns = ['106PCU','時間','107PCU','108PCU','109PCU']
result = df.loc[rows, columns].head(10)
result.set_index('時間', inplace=True)
print(result)

chart = result.plot.bar(title='南海重慶南路口年度交通狀況',  #圖表標題
                    xlabel='時間',  #x軸說明文字
                    ylabel='PCU',  #y軸說明文字
                    legend=True,  # 是否顯示圖例
                    figsize=(10, 5))  # 圖表大小
plt.xticks(rotation='horizontal')
plt.text(0.09,6700,'PCU=小客車單位(換算)')
plt.show()