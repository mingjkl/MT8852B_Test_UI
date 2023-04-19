'''
Author: emmovo
Date: 2023-04-02 22:31:39
LastEditors: emmovo
LastEditTime: 2023-04-03 09:48:07
FilePath: \BluetoothKB_Freq_test\GUI\debug.py
Description: 

Copyright (c) 2023 by mingjkl@live.com/emmovo.com, All Rights Reserved. 
'''

import mt8852b_ctrl
import time
import serial
import serial.tools.list_ports


def debug_log_display(widgets, msg):
    widgets.debug_log.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' DBG: ' + msg)


 
def bttc_send(widgets, com, msg):
    data = 0xAA
    data_bytes = data.to_bytes(1, byteorder='little')
    com.write(data_bytes)
    str = msg
    str = str + '\r\n'
    RS232_str = str.encode('utf-8')
    com.write(RS232_str)
    print('BTTC Send: ', msg)
    debug_log_display(widgets, 'BTTC Send: ' + msg)


def btn_handle(widget, btnName, global_status, global_com_list):
    print("debug_gpib_list_get_btn")
    if btnName == "debug_gpib_list_get_btn":
        try:
            gpib_list = mt8852b_ctrl.get_gpib_list()
            print('gpib_list: ', gpib_list)
            debug_log_display(widget, 'gpib_list: ' + str(gpib_list))
        except:
            print('get_gpib_list failed')
            debug_log_display(widget, 'Get gpib list failed')

    if btnName == "debug_mt8852b_get_id_btn":
        print("debug_mt8852b_get_id_btn")
        if global_status['mt8852b_connected'] == True:
            try:
                id = mt8852b_ctrl.get_id()
                print('MT8852b ID:: ', id)
                debug_log_display(widget, 'MT8852b ID: ' + str(id))
            except:
                print('get_id failed')
                debug_log_display(widget, 'Get MT8852b ID failed')

    if btnName == "debug_left_bttc_connect_btn":
        print("debug_left_bttc_connect_btn")
        if global_status['left_bttc_connected'] == True:
            # try:
                bttc_send(widget, global_com_list['left_bttc_com'], 'CONN')
                print('left bttc signal connect success')
                debug_log_display(widget, 'LEFT BTTC SIGNAL CONNECT!')
            # except:
            #     print('left bttc signal connect failed')
            #     debug_log_display(widget, 'LEFT BTTC SIGNAL CONNECT failed')
        else:
            print('left bttc not connected')
            debug_log_display(widget, 'LEFT BTTC NOT CONNECTED!')
        


    if btnName == "debug_left_bttc_disconnect_btn":
        print("debug_left_bttc_disconnect_btn")
        if global_status['left_bttc_connected'] == True:
            try:
                bttc_send(widget, global_com_list['left_bttc_com'], 'DCONN')
                print('left bttc signal disconnect success')
                debug_log_display(widget, 'LEFT BTTC SIGNAL DISCONNECT!')
            except:
                print('left bttc signal disconnect failed')
                debug_log_display(widget, 'LEFT BTTC SIGNAL DISCONNECT failed')
        else:
            print('left bttc not connected')
            debug_log_display(widget, 'LEFT BTTC NOT CONNECTED!')

    if btnName == "debug_right_bttc_connect_btn":
        print("debug_right_bttc_connect_btn")
        if global_status['right_bttc_connected'] == True:
            try:
                bttc_send(widget, global_com_list['right_bttc_com'], 'CONN')
                print('right bttc signal connect success')
                debug_log_display(widget, 'RIGHT BTTC SIGNAL CONNECT!')
            except:
                print('right bttc signal connect failed')
                debug_log_display(widget, 'RIGHT BTTC SIGNAL CONNECT failed')
        else:
            print('right bttc not connected')
            debug_log_display(widget, 'RIGHT BTTC NOT CONNECTED!')

    if btnName == "debug_right_bttc_disconnect_btn":
        print("debug_right_bttc_disconnect_btn")
        if global_status['right_bttc_connected'] == True:
            try:
                bttc_send(widget, global_com_list['right_bttc_com'], 'DCONN')
                print('right bttc signal disconnect success')
                debug_log_display(widget, 'RIGHT BTTC SIGNAL DISCONNECT!')
            except:
                print('right bttc signal disconnect failed')
                debug_log_display(widget, 'RIGHT BTTC SIGNAL DISCONNECT failed')
        else:
            print('right bttc not connected')
            debug_log_display(widget, 'RIGHT BTTC NOT CONNECTED!')

    if btnName == "debug_set_ant1_btn":
        print("debug_set_ant1_btn")
        if global_status['signal_ctrl_connected'] == True:
            try:
                bttc_send(widget, global_com_list['signal_ctrl_com'], 'ANT1')
                print('set ant1 success')
                debug_log_display(widget, 'SET ANT1!')
            except:
                print('set ant1 failed')
                debug_log_display(widget, 'SET ANT1 failed')
        else:
            print('signal ctrl not connected')
            debug_log_display(widget, 'SIGNAL CTRL NOT CONNECTED!')

    if btnName == "debug_set_ant2_btn":
        print("debug_set_ant2_btn")
        if global_status['signal_ctrl_connected'] == True:
            try:
                bttc_send(widget, global_com_list['signal_ctrl_com'], 'ANT2')
                print('set ant2 success')
                debug_log_display(widget, 'SET ANT2!')
            except:
                print('set ant2 failed')
                debug_log_display(widget, 'SET ANT2 failed')
        else:
            print('signal ctrl not connected')
            debug_log_display(widget, 'SIGNAL CTRL NOT CONNECTED!')

    if btnName == "debug_set_ant3_btn":
        print("debug_set_ant3_btn")
        if global_status['signal_ctrl_connected'] == True:
            try:
                bttc_send(widget, global_com_list['signal_ctrl_com'], 'ANT3')
                print('set ant2 success')
                debug_log_display(widget, 'SET ANT2!')
            except:
                print('set ant2 failed')
                debug_log_display(widget, 'SET ANT2 failed')
        else:
            print('signal ctrl not connected')
            debug_log_display(widget, 'SIGNAL CTRL NOT CONNECTED!')

    if btnName == "debug_set_ant4_btn":
        print("debug_set_ant4_btn")
        if global_status['signal_ctrl_connected'] == True:
            try:
                bttc_send(widget, global_com_list['signal_ctrl_com'], 'ANT4')
                print('set ant2 success')
                debug_log_display(widget, 'SET ANT2!')
            except:
                print('set ant2 failed')
                debug_log_display(widget, 'SET ANT2 failed')
        else:
            print('signal ctrl not connected')
            debug_log_display(widget, 'SIGNAL CTRL NOT CONNECTED!')

    if btnName == "debug_com_list_get_btn":
        print("debug_com_list_get_btn")
        try:
            com_list = serial.tools.list_ports.comports()
            comlist_len = len(com_list)
            for i in range(0, comlist_len):
                print(com_list[i])
                debug_log_display(widget, str(com_list[i]))
        except:
            print('ERROR:COM list checking failed!')
            debug_log_display(widget, 'ERROR:COM list checking failed!')
