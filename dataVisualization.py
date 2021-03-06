from pyecharts import Bar, Line
from pyecharts import WordCloud
import pandas as pd
from pyecharts import Page
import configparser

# 读取配置文件设置参数
config = configparser.ConfigParser()
config.read("config.ini", encoding='utf-8')
width=int(config["Visual"]["width"])
height=int(config["Visual"]["height"])
title_text_size=int(config["Visual"]["title_text_size"])
title_top=int(config["Visual"]["title_top"])

# 读取用户统计分析结果
data_user = pd.read_csv('./DataSave/user_result.csv')
data_user_df = pd.DataFrame(data_user)
user_x = data_user_df['nickname'].head(100)
user_y = data_user_df['times'].head(100)
# 创建条形图
bar = Bar('用户发言次数统计',
          width=width,
          height=height,
          background_color="#d2d2d2",
          title_pos="center",
          title_text_size=title_text_size,
          title_top=title_top,
          title_color="#3344aa")
bar.add('', user_x, user_y,
        is_more_utils=True,
        xaxis_rotate=20,
        mark_line=['average'],
        mark_point=["max"]
        )

# 读取内容分析结果
data_text = pd.read_csv('./DataSave/text_result.csv')
data_text_df = pd.DataFrame(data_text)
text_x = data_text_df['keywords'].head(100)
text_y = data_text_df['times'].head(100)

# 创建折线图
line = Line('关键词次数统计',
            width=width,
            height=height,
            background_color="#e1e1e1",
            title_pos="center",
            title_text_size=title_text_size,
            title_top=title_top,
            title_color="#3344aa")
line.add('', text_x, text_y,
         is_more_utils=True,
         is_smooth=True,
         xaxis_rotate=20,
         mark_line=['average'],
         mark_point=["max"])

# 创建词云图
wc = WordCloud('关键词词云图',
               width=width,
               height=height,
               background_color="#f1f1f1",
               title_pos="center",
               title_text_size=title_text_size,
               title_top=title_top,
               title_color="#3344aa")
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
page.add(line)
page.add(wc)
page.render('DataSave/result_Visualization.html')
