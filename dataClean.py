import pandas as pd

data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
# print(df)
dup = df.drop_duplicates()  # 数据去重
print(dup)
dup.to_csv('CleanData.csv',encoding='utf-8',index=False)