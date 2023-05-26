# 读取data文件夹下的所有csv文件，取出需要的字段，保存到一个新的csv文件中
import os
import pandas as pd

# 读取data文件夹下的所有csv文件
path = r'D:\Pythonproject\python1105\data\塔吉克斯坦'
res = pd.DataFrame()
for dirs in os.listdir(path):
    # 如果是文件夹，且为空文件夹
    if not os.listdir(os.path.join(path, dirs)):
        continue

    for file in os.listdir(os.path.join(path, dirs)):
        # 读取csv文件
        df = pd.read_csv(os.path.join(path, dirs, file))
        # 取出需要的字段
        df = df[['Classification', 'Period', 'Trade Flow', 'Reporter Code', 'Reporter', 'Reporter ISO', 'Partner Code',
                 'Partner', 'Partner ISO', 'Commodity Code', 'Commodity', 'Trade Value (US$)']]
        res = res.append(df)

# 保存到新的csv文件中
res = res.groupby(["Period", "Trade Flow", "Partner"])
res = res.apply(lambda x: x.sort_values(by=["Period", "Trade Flow", "Partner"]))
res.to_excel(os.path.join(path,'{}-总.xlsx'.format('塔吉克斯坦')))
