import time
import serial

def thread_com_init():
    ser = serial.Serial('COM8', 115200)
    # print(ser)
    return ser

def BTT_RS232_Send(str):
    str = str + '\r\n'
    RS232_str = str.encode('utf-8')

    # print(RS232_str)
    serial = thread_com_init()
    if serial.isOpen():
        print('Serial Open Successful\n')
    else:
        print("Serial Open Fail!\n")

    # try:
    data = 0xAA
    data_bytes = data.to_bytes(1, byteorder='little')  # 转换为字节
    # print(data_bytes)
    serial.write(data_bytes)
    serial.write(RS232_str)
    time.sleep(1)
    count = serial.inWaiting()
    if count > 0:
        data_bytes = serial.readline()
        data_str = data_bytes.decode('utf-8')  # 将数据转换为字符串
        # print(data_str)
    # serial.close()

    if data_str == str:     # CONN DCONN ANTn
        print(data_str[:count-2])
        return 0
    elif data_str[:count-3] == 'BTTCID':    # *ID?
        print(data_str[:count-2])
        return "ID" + data_str[count-3]
    else:
        print(data_str)
        return 1
    
if __name__ == "__main__":

    ret = BTT_RS232_Send("CONN")
    print(f"BTT_RS232_ret:{ret}")

    time.sleep(5)

    ret = BTT_RS232_Send("DCONN")
    print(f"BTT_RS232_ret:{ret}")

    time.sleep(5)

    ret = BTT_RS232_Send("ANT1")
    print(f"BTT_RS232_ret:{ret}")

    time.sleep(5)

    ret = BTT_RS232_Send("*ID?")
    print(f"BTT_RS232_ret:{ret}")