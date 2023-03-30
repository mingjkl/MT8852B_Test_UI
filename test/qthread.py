import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtSerialPort import *

class SerialPortThread(QThread):
    """
    串口接收线程
    """
    def __init__(self, serial_port):
        super().__init__()
        self.serial_port = serial_port
        self.data_ready = False
        self.data = None

    def run(self):
        while True:
            if self.serial_port.waitForReadyRead(100):
                self.data = self.serial_port.readAll()
                self.data_ready = True

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建串口对象
        self.serial_port = QSerialPort(self)
        self.serial_port.setPortName("COM1")
        self.serial_port.setBaudRate(QSerialPort.Baud115200)
        self.serial_port.setDataBits(QSerialPort.Data8)
        self.serial_port.setParity(QSerialPort.NoParity)
        self.serial_port.setStopBits(QSerialPort.OneStop)

        # 打开串口
        if self.serial_port.open(QIODevice.ReadWrite):
            print("串口打开成功")
        else:
            print("串口打开失败")

        # 启动串口接收线程
        self.serial_port_thread = SerialPortThread(self.serial_port)
        self.serial_port_thread.start()

        # 定时器用于更新数据
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(100)

    def update_data(self):
        """
        更新界面数据
        """
        if self.serial_port_thread.data_ready:
            data = self.serial_port_thread.data
            # TODO: 解析数据，更新界面
            print(data)

            # 数据处理完毕，重置标志位
            self.serial_port_thread.data_ready = False

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
