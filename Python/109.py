import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('未命名.csv', encoding='big5')

rows = (df['方向'] == '合計')
columns = ['方向','時間',	'直行大型車',	'直行小型車',	'直行機車',	'直行PCU']
result = df.loc[rows, columns].head(10)
result.set_index('時間', inplace=True)
print(result)

chart = result.plot(title='南海重慶南路口交通狀況, 109/5/19',  #圖表標題
                    xlabel='時間',  #x軸說明文字
                    ylabel='車輛數',  #y軸說明文字
                    legend=True,  # 是否顯示圖例
                    figsize=(10, 5),  
                    marker='o',
                    linestyle='-')  # 圖表大小
plt.grid(True, ls='-.')
plt.text(2.5,420,'PCU=小客車單位(換算)')
plt.show()