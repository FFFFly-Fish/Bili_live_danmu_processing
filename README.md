# Bili_live_danmu_processing
对B站直播弹幕的获取，保存，数据清洗与分析及可视化
## 使用方式
- 在配置文件`config.ini`中设置好运行时间`Runtime`，获取弹幕间隔`Sleeptime`与直播间号`[data]`中的`roomid`
- 然后执行`run_getDanmu.py`
- 获取的临时数据文件会存放在`DataSave`文件夹的`data.csv`中，临时文件中数据将在程序正常运行结束后**被清除**。
- 数据去重后得到的数据会存放在`CleanData.csv`中，分别是昵称，内容，发送时间和用户id。
- 数据分析的结果`text_result.csv`和`user_result.csv`，分别保存**关键词数量**数据和**用户发言次数**数据
- 数据可视化的结果`result_Visualization。html`中为用户发言次数绘制了**柱状图**，以及为关键词数据绘制了**词云图**
  - **注意：`DataSave`文件夹中的数据会被下一次执行操作追加的数据覆盖，请及时做好备份，以免数据出错**
## 更新日志
**2022.04.21**
- 修复了如果DataSave文件夹不存在会报错的bug，在run_getDanmu加上了不存在则创建一个的指令

**2022.04.19**

- 更新可视化文件dataVisualization.py
  - 增加折线图和优化展示效果
  - 增加配置文件接入，可直接在配置文件中修改宽度高度和标题属性
  
**2022.04.18**
- 更新配置文件`config.ini`
    - 可以在配置文件中修改运行时间`Runtime`，获取弹幕间隔`Sleeptime`与直播间号`data`中的`roomid`
- 优化弹幕分析`dataAnalysis.py`的白名单和相似词语合并

**2022.04.17**
- 建立数据可视化文件`dataVisualization.py`
  - 可以利用`text_result.csv`和`user_result.csv`生成柱状图和词云图
- 在`run_getDanmu.py`加入运行数据可视化模块

**2022.04.16**
- 建立数据分析文件`dataAnalysis.py`
  - 可以分析`CleanData.csv`中的**关键词数量**数据和**用户发言次数**数据
- 建立`dataClean.py`
  - 用于处理重复数据
- 建立`run_getDanmu.py`
  - 统合运行爬虫与数据分析程序

**2022.04.15**
- 建立工程
  - 建立`getDanmu.py`爬虫程序，获取B站直播弹幕
