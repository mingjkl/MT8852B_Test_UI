'''
Author: emmovo
Date: 2023-03-28 21:21:11
LastEditors: emmovo
LastEditTime: 2023-03-28 21:24:11
FilePath: \BluetoothKB_Freq_test\test\qthread.py
Description: 

Copyright (c) 2023 by mingjkl@live.com/emmovo.com, All Rights Reserved. 
'''
from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtSerialPort import QSerialPort

class SerialPortThread(QThread):
    dataReceived = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.serialPort = QSerialPort()
        print("SerialPortThread init")

    def run(self):
        self.serialPort.setPortName('COM10')  # 设置串口名
        self.serialPort.setBaudRate(115200)  # 设置波特率
        self.serialPort.open(QSerialPort.ReadWrite)  # 打开串口
        self.serialPort.readyRead.connect(self.handleReadyRead)  # 将 readyRead 信号连接到槽函数
        print("SerialPortThread run")

    def handleReadyRead(self):
        data = self.serialPort.readAll().data().decode()  # 读取串口数据
        self.dataReceived.emit(data)  # 发送信号
        print("SerialPortThread handleReadyRead")

if __name__ == '__main__':
    thread = SerialPortThread()
    thread.dataReceived.connect(lambda data: print(data))
    thread.start()