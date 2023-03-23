
import serial
import serial.tools.list_ports
import time

comlist = serial.tools.list_ports.comports()
comlist_len = len(comlist)
for i in range(0, comlist_len):
    print(comlist[i])

ser = serial.Serial('COM10', 115200, timeout=1)
data = ser.readline()
print(data)

while True:
    if ser.in_waiting:
        data = ser.readline()
        # print(data)
        if "OPEN" in data.decode('utf-8'):
            print('OPEN')
        elif 'CLOSE' in data.decode('utf-8'):
            print('CLOSE')
        else:
            print('ERROR')
    time.sleep(0.1)
   

