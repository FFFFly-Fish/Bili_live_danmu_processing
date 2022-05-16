import pandas as pd
import jieba

# 读取文件
data = pd.read_csv('./DataSave/CleanData.csv')
df = pd.DataFrame(data)
user = df['nickname']  # 获取昵称列
text = df['text']  # 获取内容列

# 读取关键词白名单
file=open('whitelist.txt',encoding='utf-8')
file_1=list(file)
whitelists=[x.strip() for x in file_1]  #去除换行符

# 用户发言数量统计
def user_count():
    user_list = user.to_list()
    counts = {}
    for i in user_list:
        counts[i] = counts.get(i, 0) + 1

    user_result = list(counts.items())
    user_result.sort(key=lambda x: x[1], reverse=True)
    user_column_name = ['nickname', 'times']
    user_df = pd.DataFrame(columns=user_column_name, data=user_result)
    print(user_df)
    return user_df


# 关键词频率统计
def keyword_count():
    text_str = text.str.cat(sep=' ')  # 将dataframe数据转换为str
    text_cut = jieba.lcut(text_str)  # 使用jieba进行分词

    counts = {}
    for word in text_cut:
        if word in whitelists:  # 关键字白名单
            counts[word] = counts.get(word, 0) + 1
        elif word == "哈哈":  # 设置近似词语合并
            rword = "哈哈哈"
        elif word == "哈哈哈哈":
            rword = "哈哈哈"
        elif len(word) == 1:  # 排除单个汉字和标点符号
            continue
        else:
            rword = word
        counts[rword] = counts.get(rword, 0) + 1

    text_result = list(counts.items())
    text_result.sort(key=lambda x: x[1], reverse=True)  # 从大到小排序

    text_column_name = ['keywords', 'times']
    text_df = pd.DataFrame(columns=text_column_name, data=text_result)  # 转换回dataframe数据并保存
    print(text_df)
    return text_df


if __name__ == '__main__':
    user_count().to_csv('./DataSave/user_result.csv', encoding='utf-8')
    keyword_count().to_csv('./DataSave/text_result.csv', encoding='utf-8')

