import pandas as pd

data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
dup = df.drop_duplicates()  # 数据去重复
dup.columns = ["nickname", "text", "timeline"]  # 给各列加上列名
print(dup)  # 预览处理好的数据
dup.to_csv('CleanData.csv', encoding='utf-8')  # 保存数据csv格式
