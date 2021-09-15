import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('D:/Database/建中/traffic_CKHS/csv/多年pcu比較.csv', encoding='ansi')

rows = (df['方向'] == '合計')
columns = ['98PCU','100PCU','102PCU','103PCU','104PCU','105PCU','106PCU','時間','107PCU','108PCU','109PCU']
result = df.loc[rows, columns].head(10)
result.set_index('時間', inplace=True)
print(result)

chart = result.plot(title='南海重慶南路口年度交通狀況',  #圖表標題
                    xlabel='時間',  #x軸說明文字
                    ylabel='PCU',  #y軸說明文字
                    legend=True,  # 是否顯示圖例
                    figsize=(10, 5),
                    marker='o',
                    linestyle='-',
                    color=('#277da1','#577590','#4d908e','#43aa8b','#90be6d','#f9c74f','#f9844a','#f8961e','#f3722c','#f94144') ) # 圖表大小
plt.xticks(rotation='horizontal')
plt.grid(True, ls='--',color='#f0f0f0')
plt.text(0.5,6700,'PCU=小客車單位(換算)')
plt.savefig('test.png',dpi=600)
plt.show()