import pandas as pd
import matplotlib.pyplot as plt
 
 
df = pd.read_csv('多年來之比較.csv' , encoding='ansi')

rows = (df['Year'] == 106) & (df['方向'] == '南海路往西') & (df['轉向'] == '左')
columns = ['時間', 'PCU', '轉向比']
result = df.loc[rows, columns]
result.set_index('時間', inplace=True)
 
chart = result.plot(  #圖表類型
		    title='test',  #圖表標題
                    xlabel='時間',  #x軸說明文字
                    ylabel='PCU',  #y軸說明文字
                    legend=True,  # 是否顯示圖例
                    figsize=(10, 5))  # 圖表大小
plt.show()