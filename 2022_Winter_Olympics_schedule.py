# coding=utf-8
import datetime
import time
import demjson

def get_date():
    return time.strftime("%m/%d")

# 获取赛事日程
def get_Winter_Olympics_schedule(date_text):
    result = ""  # 最终返回文本
    Winter_Olympics_schedule_name = '2022_Winter_Olympics.json'  # json文件路径

    # 读取数据
    with open(Winter_Olympics_schedule_name, 'r', encoding='utf-8') as fo:
        schedule_Data = demjson.decode(fo.read())
        fo.close()
        if schedule_Data[0][date_text]:
            dateID = schedule_Data[0][date_text][0]
            schedule_text=dateID
            schedule_date_text=schedule_text['date']  # date_text为冬奥会第几天
            schedule_date_tody=schedule_text['today']  # date_text为星期几

            result = date_text+" " + schedule_date_tody +"\n"
            for i in range(len(schedule_Data)-2):  # 排除掉第一个日期json
                if schedule_Data[i+1][schedule_date_text] != "":
                    result = result + schedule_Data[i+1][""]+":\n"+ schedule_Data[i+1][schedule_date_text]+"\n\n"
            return result
        else:
            return "获取失败"

if __name__ == '__main__':
    # print(get_Winter_Olympics_schedule("02/05"))  # 指定日期
    print(get_Winter_Olympics_schedule(get_date()))  # 当日