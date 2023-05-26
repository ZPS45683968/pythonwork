import pandas as pd

# 读取数据
df = pd.read_excel("res.xlsx")

# 按year，Trade Flow，Reporter，Partner分组
grouped = df.groupby(["Year", "Trade Flow", "Partner"])

# 对每个分组内的数据按照年份和Trader排序
sorted_df = grouped.apply(lambda x: x.sort_values(by=["Year", "Trade Flow","Partner"]))

# 输出排序后的结果
sorted_df.to_excel("sorted.xlsx")