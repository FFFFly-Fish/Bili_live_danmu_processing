import pandas as pd
import jieba

# 读取文件
data = pd.read_csv('./DataSave/CleanData.csv')
df = pd.DataFrame(data)
user = df['nickname']  # 获取昵称列
text = df['text']  # 获取内容列

# 用户发言数量统计
def user_count():
    user_list=user.to_list()
    counts={}
    for i in user_list:
        counts[i] = counts.get(i, 0)+1

    user_result=list(counts.items())
    user_result.sort(key=lambda x: x[1], reverse=True)
    user_column_name=['nickname', 'times']
    user_df = pd.DataFrame(columns=user_column_name,data=user_result)
    user_df.to_csv('./DataSave/user_result.csv',encoding='utf-8')
    print(user_df)

# 关键词频率统计
def keyword_count():
    text_str = text.str.cat(sep=' ')  # 将dataframe数据转换为str
    text_cut = jieba.lcut(text_str)  # 使用jieba进行分词

    counts = {}
    for i in text_cut:
        if len(i) > 1:
            counts[i] = counts.get(i, 0) + 1  # 选择出非单字
        elif i == "草":
            counts[i] = counts.get(i, 0) + 1  # 关键字过滤

    text_result = list(counts.items())
    text_result.sort(key=lambda x: x[1], reverse=True)  # 从大到小排序

    text_column_name = ['keywords', 'times']
    text_df = pd.DataFrame(columns=text_column_name, data=text_result)  # 转换回dataframe数据并保存
    text_df.to_csv('./DataSave/text_result.csv', encoding='utf-8')
    print(text_df)

user_count()
keyword_count()

