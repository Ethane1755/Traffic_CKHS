import pandas as pd
import matplotlib.pyplot as plt
 
 
df = pd.read_csv('多年來之比較.csv')
 
rows = (df['年別'] == 2019) & (df['縣市別'] == '臺北市')
columns = ['細分', '1月', '2月', '3月']
result = df.loc[rows, columns].head(100)
result.set_index('細分', inplace=True)
 
chart = result.plot(kind='bar',  #圖表類型
		    title='2019年臺北市各景點旅客人數',  #圖表標題
                    xlabel='細分(景點名稱)',  #x軸說明文字
                    ylabel='人數',  #y軸說明文字
                    legend=True,  # 是否顯示圖例
                    figsize=(10, 5))  # 圖表大小
plt.show()