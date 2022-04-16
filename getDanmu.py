import requests
import io, sys
import csv

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class Danmu():
    def __init__(self):
        # 弹幕接口在 Network - gethistory?roomid={roomid}
        self.url = 'https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory'
        self.header = {
            'Host': 'api.live.bilibili.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/80.0.3987.163 Safari/537.36',
        }
        # 定义post参数
        self.data = {
            'roomid': '5170',  # 直播房间id,不一定是直播间号
            'csrf_token': '',
            'csrf': '',
            'visit_id': '',
        }

    # 获取弹幕接口中data - room的弹幕
    def get_Danmu_room(self):
        html = requests.post(url=self.url, headers=self.header, data=self.data).json()
        for content in html['data']['room']:
            nickname = content['nickname']
            text = content['text']
            timeline = content['timeline']

            msg_json = [{
                '用户': nickname,
                '内容': text,
                '时间': timeline
            }]
            print(msg_json)  # 查看json格式

            # 存为csv文件
            with open('data.csv', 'a', encoding='utf-8') as f1:
                writer = csv.writer(f1)
                writer.writerow([nickname, text, timeline])

    # 获取弹幕接口中data - admin的弹幕（应该是房管或舰长弹幕）
    def get_Danmu_admin(self):
        html = requests.post(url=self.url, headers=self.header, data=self.data).json()
        for content in html['data']['admin']:
            nickname = content['nickname']
            text = content['text']
            timeline = content['timeline']

            msg_json = [{
                '用户': nickname,
                '内容': text,
                '时间': timeline
            }]
            print(msg_json)  # 查看json格式

            # 存为csv文件
            with open('data.csv', 'a', encoding='utf-8') as f1:
                writer = csv.writer(f1)
                writer.writerow([nickname, text, timeline])


if __name__ == '__main__':
    bDanmu = Danmu()
    bDanmu.get_Danmu_room()
    bDanmu.get_Danmu_admin()
