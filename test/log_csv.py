'''
Author: emmovo
Date: 2023-03-31 22:12:16
LastEditors: emmovo
LastEditTime: 2023-04-01 00:24:39
FilePath: \BluetoothKB_Freq_test\test\log_csv.py
Description: 

Copyright (c) 2023 by mingjkl@live.com/emmovo.com, All Rights Reserved. 
'''
import csv
import os
from datetime import date


today = date.today().strftime("%Y-%m-%d")
csv_path = os.path.join("result_log//CSV", f"{today}.csv")

top_line = ['开始测试时间', 
            '测试耗时',
            '测试位置',
            '项目名称',
            '测试结果',
            '蓝牙地址',
            '输出功率-测试结果',
            '输出功率-低频-最大(dBm)',
            '输出功率-低频-最小(dBm)',
            '输出功率-低频-峰值(dBm)',
            '输出功率-低频-平均(dBm)',
            '输出功率-低频-结果',
            '输出功率-中频-最大(dBm)',
            '输出功率-中频-最小(dBm)',
            '输出功率-中频-峰值(dBm)',
            '输出功率-中频-平均(dBm)',
            '输出功率-中频-结果',
            '输出功率-高频-最大(dBm)',
            '输出功率-高频-最小(dBm)',
            '输出功率-高频-峰值(dBm)',
            '输出功率-高频-平均(dBm)',
            '输出功率-高频-结果',
            '频偏漂移-测试结果',
            '平均频偏-低频(kHz)',
            '最大+ve频偏-低频(kHz)',
            '最大-ve频偏-低频(kHz)',
            '漂移速率-低频(kHz)',
            '最大漂移-低频(kHz)',
            '平均漂移-低频(kHz)',
            '频偏漂移-低频-结果',
            '平均频偏-中频(kHz)',
            '最大+ve频偏-中频(kHz)',
            '最大-ve频偏-中频(kHz)',
            '漂移速率-中频(kHz)',
            '最大漂移-中频(kHz)',
            '平均漂移-中频(kHz)',
            '频偏漂移-中频-结果',
            '平均频偏-高频(kHz)',
            '最大+ve频偏-高频(kHz)',
            '最大-ve频偏-高频(kHz)',
            '漂移速率-高频(kHz)',
            '最大漂移-高频(kHz)',
            '平均漂移-高频(kHz)',
            '频偏漂移-高频-结果',
            '单时隙灵敏度-测试结果',
            '误码率-低频(%)',
            '误帧率-低频-结果',
            '误码率-中频(%)',
            '误帧率-中频-结果',
            '误码率-高频(%)',
            '误帧率-高频-结果']


# 检查是否存在以今天日期命名的 csv 文件
if os.path.exists(csv_path):
    # 如果文件存在，则以追加模式打开文件，续写内容
    with open(csv_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # 在文件最后一行添加新的一行数据
        writer.writerow(['John', 'Doe', '25'])
    print('File exists, appending data...')
else:   
    # 如果文件不存在，则以写模式打开文件，创建新的 csv 文件
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # 添加表头
        writer.writerow(top_line)
        # 添加第一行数据
        writer.writerow(['Jane', 'Doe', '30'])
    print('File does not exist, creating file...')
