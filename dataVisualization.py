from pyecharts import Bar
from pyecharts import WordCloud
import pandas as pd
from pyecharts import Page


# 读取用户统计分析结果
data_user = pd.read_csv('./DataSave/user_result.csv')
data_user_df = pd.DataFrame(data_user)
user_x = data_user_df['nickname'].head(100)
user_y = data_user_df['times'].head(100)
# 创建条形图
bar = Bar('用户发言次数统计',width=2000,height=600)
bar.add('', user_x, user_y,
        is_datazoom_show=True,
        xaxis_rotate=20)


# 读取内容分析结果
data_text = pd.read_csv('./DataSave/text_result.csv')
data_text_df = pd.DataFrame(data_text)
text_x = data_text_df['keywords'].head(100)
text_y = data_text_df['times'].head(100)
# 创建词云图
wc = WordCloud(width=1000,height=800)
wc.add('',
       attr=text_x,
       value=text_y,
       shape='pentagon',
       rotate_step=0,
       word_size_range=[20, 80]
       )

# 创建展示网页
page = Page(page_title='弹幕数据可视化图表')
page.add(bar)
page.add(wc)
page.render('DataSave/result_Visualization.html')
