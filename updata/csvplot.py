'''
Author: emmovo
Date: 2023-05-05 08:47:36
LastEditors: emmovo
LastEditTime: 2023-05-05 10:11:29
FilePath: \python\csvplot.py
Description: 

Copyright (c) 2023 by mingjkl@live.com/emmovo.com, All Rights Reserved. 
'''


import csv
import matplotlib.pyplot as plt

# 打开 CSV 文件并读取数据
with open('2023-05-05.csv') as f:
    reader = csv.reader(f)
    next(reader)  # 跳过第一行标题行
    data = [(float(row[7]), row[2]) for row in reader]

# 将数据分成两组
data_p1 = [(x, color) for x, color in data if color == 'P1']
data_p2 = [(x, color) for x, color in data if color == 'P2']

# 绘制两个散点图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

for i, (x, _) in enumerate(data_p1):
    ax1.scatter(i, x, color='red', s=3)
ax1.set_xlabel('Index')
ax1.set_ylabel('Data')
ax1.set_title('Scatter Plot P1')

for i, (x, _) in enumerate(data_p2):
    ax2.scatter(i, x, color='blue', s=3)
ax2.set_xlabel('Index')
ax2.set_ylabel('Data')
ax2.set_title('Scatter Plot P2')

plt.show()


#  def refresh_ui(self):
#         # 在此处更新 UI
#         self.button.setText("Clicked")
#         self.update() 

# from PySide6.QtCore import QTimer
#   # 创建定时器
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.refresh_ui)  # 连接超时信号和槽函数
#         self.timer.start(1000)  # 设置定时器时间间隔为1000毫秒