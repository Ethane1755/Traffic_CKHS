import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('csv/多年來之比較.csv' , encoding='ansi')

rows = (df['Year']==106) & (df['方向']=='南海路往西') &(df['轉向']=='左')
columns = ['時間', 'PCU']
result = df.loc[rows, columns]
result.set_index('時間', inplace=True)

fig, axes=plt.subplots(2,2)
ax=result.plot(kind='bar', #圖表類型
		    title='test',  #圖表標題
            xlabel='時間',  #x軸說明文字
            ylabel='PCU',  #y軸說明文字
            legend =True,  # 是否顯示圖例
            figsize=(10, 5),
            ax=axes[0,0]# 圖表大小
            ) 


result.plot(kind='line',
            color='r', #圖表類型
		    title='test',  #圖表標題
            xlabel='時間',  #x軸說明文字
            ylabel='PCU',  #y軸說明文字 # 是否顯示圖例
            figsize=(10, 5),
            ax=axes[0,0],
            grid=True
            ) 

result.plot(kind='line',
            color='r', #圖表類型
		    title='test',  #圖表標題
            xlabel='時間',  #x軸說明文字
            ylabel='PCU',  #y軸說明文字 # 是否顯示圖例
            figsize=(10, 5),
            ax=axes[1,0],
            grid=True
            ) 
plt.xticks(rotation=45)

ax1=result.plot(kind='bar', #圖表類型
		    title='test',  #圖表標題
            xlabel='時間',  #x軸說明文字
            ylabel='PCU',  #y軸說明文字
            legend =True,  # 是否顯示圖例
            figsize=(10, 5),
            ax=axes[1,1],# 圖表大小
            ) 
ax.xaxis.set_ticks([])
ax1.xaxis.set_ticks([])
plt.tight_layout()
plt.show()
