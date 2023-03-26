# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform
import json
import time
import serial
import serial.tools.list_ports

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

# GLOBAL VARIABLES
# ///////////////////////////////////////////////////////////////


## Create a global state variable
global_status = {'setting_loaded': False,
                 'left_box_connected': False,
                 'right_box_connected': False,
                 'left_bttc_connected': False,
                 'right_bttc_connected': False,
                 'signal_ctrl_connected': False,
                 'mt8852b_connected': True,         ## debug
                 'mes_service_connected': False,
                 'channel_right_enable': False,
                 'channel_left_enable': False,
                 'channel_left_ready': False,
                 'channel_right_ready': False,
                 'finished_channel':'NULL'}


## The log display function on the UI interface
def log_display(msg):
    widgets.textEdit_4.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' LOG: ' + msg) 


def setting_data_display(setting_data):
    widgets.left_leop_avg_ucl.setText('<= '+setting_data['leop_config']['avg_ucl']+' dBm')
    widgets.left_leop_avg_lcl.setText('>= '+setting_data['leop_config']['avg_lcl']+' dBm')
    widgets.left_leop_peak_ucl.setText('<= '+setting_data['leop_config']['peak_ucl']+' dBm')

    widgets.right_leop_avg_ucl.setText('<= '+setting_data['leop_config']['avg_ucl']+' dBm')
    widgets.right_leop_avg_lcl.setText('>= '+setting_data['leop_config']['avg_lcl']+' dBm')
    widgets.right_leop_peak_ucl.setText('<= '+setting_data['leop_config']['peak_ucl']+' dBm')

    widgets.left_leicd_p_fn_ucl.setText('<= '+setting_data['leicd_config']['p_fn_ucl']+' kHz')
    widgets.left_leicd_n_fn_ucl.setText('<= '+setting_data['leicd_config']['p_fn_ucl']+' kHz')
    widgets.left_leicd_drift_range.setText('< '+setting_data['leicd_config']['drift_range']+' kHz')
    widgets.left_leicd_drift_rate.setText('< '+setting_data['leicd_config']['drift_rate']+' kHz/50us')

    widgets.right_leicd_p_fn_ucl.setText('<= '+setting_data['leicd_config']['p_fn_ucl']+' kHz')
    widgets.right_leicd_n_fn_ucl.setText('<= '+setting_data['leicd_config']['p_fn_ucl']+' kHz')
    widgets.right_leicd_drift_range.setText('< '+setting_data['leicd_config']['drift_range']+' kHz')
    widgets.right_leicd_drift_rate.setText('< '+setting_data['leicd_config']['drift_rate']+' kHz/50us')

    widgets.left_less_fer.setText('<= '+setting_data['less_config']['fer']+' %')
    widgets.right_less_fer.setText('<= '+setting_data['less_config']['fer']+' %')

## Loading the setting.json file
def setting_load():
     # SETTING RELOAD
        log_display('Setting loading...')
        print('Setting loading...')
        try:
            with open('D:/WorkingData/BluetoothKB_Freq_test/test/setting.json', 'r') as f:
                setting_data = json.load(f)

            widgets.left_box_com.addItem(setting_data['connect']['left_box_com'])
            widgets.right_box_com.addItem(setting_data['connect']['right_box_com'])
            widgets.left_bbtc_com.addItem(setting_data['connect']['left_bttc_com'])
            widgets.right_bbtc_com.addItem(setting_data['connect']['right_bttc_com'])
            widgets.signal_ctrl_com.addItem(setting_data['connect']['signal_ctrl_com'])
            widgets.connect_time_le.setText(setting_data['connect']['connect_time'])

            widgets.leop_packet_cnt_le.setText(setting_data['leop_config']['packet_cnt'])
            widgets.leop_freq_l_le.setText(setting_data['leop_config']['low_freq'])
            widgets.leop_freq_m_le.setText(setting_data['leop_config']['mid_freq'])
            widgets.leop_freq_h.setText(setting_data['leop_config']['high_freq'])
            widgets.leop_avg_ucl_le.setText(setting_data['leop_config']['avg_ucl'])
            widgets.leop_avg_lcl_le.setText(setting_data['leop_config']['avg_lcl'])
            widgets.leop_peak_ucl_le.setText(setting_data['leop_config']['peak_ucl'])


            widgets.leicd_packet_cnt_le.setText(setting_data['leicd_config']['packet_cnt'])
            widgets.leicd_freq_l_le.setText(setting_data['leicd_config']['low_freq'])
            widgets.leice_p_fn_ucl_le.setText(setting_data['leicd_config']['p_fn_ucl'])
            widgets.leicd_freq_m_le.setText(setting_data['leicd_config']['mid_freq'])
            widgets.leicd_n_fn_lcl_le.setText(setting_data['leicd_config']['n_fn_lcl'])
            widgets.leicd_drift_rate_le.setText(setting_data['leicd_config']['drift_rate'])
            widgets.leicd_freq_h_le.setText(setting_data['leicd_config']['high_freq'])
            widgets.leicd_drift_range_le.setText(setting_data['leicd_config']['drift_range'])
            widgets.leicd_packet_drift_rang_le.setText(setting_data['leicd_config']['packet_drift_range'])

            widgets.less_packet_cnt_le.setText(setting_data['less_config']['packet_cnt'])
            widgets.less_freq_l_le.setText(setting_data['less_config']['low_freq'])
            widgets.less_freq_m_le.setText(setting_data['less_config']['mid_freq'])
            widgets.less_freq_h_le.setText(setting_data['less_config']['high_freq'])
            widgets.less_op_le.setText(setting_data['less_config']['op'])
            widgets.less_fer_le.setText(setting_data['less_config']['fer'])

            

        except:
            print('setting.json load error')
            log_display('Setting load error')
            widgets.setting_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
            widgets.setting_status.setText('配置文件加载失败')
            global_status['setting_loaded'] = False
            return {}
        else:
            widgets.setting_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
            widgets.setting_status.setText('配置文件加载完成')
            print('setting.json load success')
            log_display('Setting load success')
            global_status['setting_loaded'] = True
            setting_data_display(setting_data)
            return setting_data

## Read and detect COM port
def com_list_cherk(setting_info):   
    log_display('COM list checking...')
    com_list = serial.tools.list_ports.comports()
    comlist_len = len(com_list)
    for i in range(0, comlist_len):
        print(com_list[i])
        log_display(str(com_list[i]))
        if global_status['setting_loaded'] == True:
            if setting_info['connect']['left_box_com'] == str(com_list[i].name):    
                log_display('Left box COM port found!')
                global_status['left_box_connected'] = True
            if setting_info['connect']['right_box_com'] == str(com_list[i].name):
                log_display('Right box COM port found!')
                global_status['right_box_connected'] = True
            if setting_info['connect']['left_bttc_com'] == str(com_list[i].name):
                log_display('Left BTTC COM port found!')
                global_status['left_bttc_connected'] = True
            if setting_info['connect']['right_bttc_com'] == str(com_list[i].name):
                log_display('Right BTTC COM port found!')
                global_status['right_bttc_connected'] = True
            if setting_info['connect']['signal_ctrl_com'] == str(com_list[i].name):
                log_display('Signal controller COM port found!')
                global_status['signal_ctrl_connected'] = True
        else:
            log_display('Setting file not loaded, please check!')
            
    

            
## Save setting to setting.json
def setting_save():
    setting_data = {
        'connect': {
            'left_box_com': widgets.left_box_com.currentText(),
            'right_box_com': widgets.right_box_com.currentText(),
            'left_bttc_com': widgets.left_bbtc_com.currentText(),
            'right_bttc_com': widgets.right_bbtc_com.currentText(),
            'signal_ctrl_com': widgets.signal_ctrl_com.currentText(),
            'connect_time': widgets.connect_time_le.text()
        },
        'leop_config': {
            'packet_cnt': widgets.leop_packet_cnt_le.text(),
            'low_freq': widgets.leop_freq_l_le.text(),
            'mid_freq': widgets.leop_freq_m_le.text(),
            'high_freq': widgets.leop_freq_h.text(),
            'avg_ucl': widgets.leop_avg_ucl_le.text(),
            'avg_lcl': widgets.leop_avg_lcl_le.text(),
            'peak_ucl': widgets.leop_peak_ucl_le.text()
        },
        'leicd_config': {
            'packet_cnt': widgets.leicd_packet_cnt_le.text(),
            'low_freq': widgets.leicd_freq_l_le.text(),
            'p_fn_ucl': widgets.leice_p_fn_ucl_le.text(),
            'mid_freq': widgets.leicd_freq_m_le.text(),
            'n_fn_lcl': widgets.leicd_n_fn_lcl_le.text(),
            'drift_rate': widgets.leicd_drift_rate_le.text(),
            'high_freq': widgets.leicd_freq_h_le.text(),
            'drift_range': widgets.leicd_drift_range_le.text(),
            'packet_drift_range': widgets.leicd_packet_drift_rang_le.text()
        },
        'less_config': {
            'packet_cnt': widgets.less_packet_cnt_le.text(),
            'low_freq': widgets.less_freq_l_le.text(),
            'mid_freq': widgets.less_freq_m_le.text(),
            'high_freq': widgets.less_freq_h_le.text(),
            'op': widgets.less_op_le.text(),
            'fer': widgets.less_fer_le.text()
        }
    }
    with open('D:/WorkingData/BluetoothKB_Freq_test/test/setting.json', 'w') as f:
        json.dump(setting_data, f, indent=1)


## Test setting disable
def setting_disable():
    widgets.left_box_com.setEnabled(False)
    widgets.right_box_com.setEnabled(False)
    widgets.left_bbtc_com.setEnabled(False)
    widgets.right_bbtc_com.setEnabled(False)
    widgets.signal_ctrl_com.setEnabled(False)
    widgets.connect_time_le.setEnabled(False)

    widgets.leop_packet_cnt_le.setEnabled(False)
    widgets.leop_freq_l_le.setEnabled(False)
    widgets.leop_freq_m_le.setEnabled(False)
    widgets.leop_freq_h.setEnabled(False)
    widgets.leop_avg_ucl_le.setEnabled(False)
    widgets.leop_avg_lcl_le.setEnabled(False)
    widgets.leop_peak_ucl_le.setEnabled(False)

    widgets.leicd_packet_cnt_le.setEnabled(False)
    widgets.leicd_freq_l_le.setEnabled(False)
    widgets.leice_p_fn_ucl_le.setEnabled(False)
    widgets.leicd_freq_m_le.setEnabled(False)
    widgets.leicd_n_fn_lcl_le.setEnabled(False)
    widgets.leicd_drift_rate_le.setEnabled(False)
    widgets.leicd_freq_h_le.setEnabled(False)
    widgets.leicd_drift_range_le.setEnabled(False)
    widgets.leicd_packet_drift_rang_le.setEnabled(False)

    widgets.less_packet_cnt_le.setEnabled(False)
    widgets.less_freq_l_le.setEnabled(False)
    widgets.less_freq_m_le.setEnabled(False)
    widgets.less_freq_h_le.setEnabled(False)
    widgets.less_op_le.setEnabled(False)
    widgets.less_fer_le.setEnabled(False)
    widgets.less_IFR_LE.setEnabled(False)

def mt8852b_check():
    log_display('mt8852b checking...')
    if global_status['mt8852b_connected'] == True:
        global_status['mt8852b_connected'] = True
        print('mt8852b connected')
        log_display('mt8852b connected')
        widgets.mt8852b_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        widgets.mt8852b_status.setText('MT8852B已连接')
        return True
    else:
        global_status['mt8852b_connected'] = False
        widgets.mt8852b_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
        widgets.mt8852b_status.setText('MT8852B连接失败')
        print('mt8852b connect failed')
        log_display('mt8852b connect failed')
        return False

def left_box_check():
    log_display('left box checking...')
    if global_status['left_box_connected'] == True:
        global_status['left_box_connected'] = True
        print('left box connected')
        log_display('left box connected')
        widgets.left_box_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        widgets.left_box_status.setText('左屏蔽盒已连接')
        return True
    else:
        global_status['left_box_connected'] = False
        widgets.left_box_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
        widgets.left_box_status.setText('左屏蔽盒连接失败')
        print('left box connect failed')
        log_display('left box connect failed')
        return False
    

def right_box_check():
    log_display('right box checking...')
    if global_status['right_box_connected'] == True:
        global_status['right_box_connected'] = True
        print('right box connected')
        log_display('right box connected')
        widgets.right_box_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        widgets.right_box_status.setText('右屏蔽盒已连接')
        return True
    else:
        global_status['right_box_connected'] = False
        widgets.right_box_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
        widgets.right_box_status.setText('右屏蔽盒连接失败')
        print('right box connect failed')
        log_display('right box connect failed')
        return False

def left_bttc_check():
    log_display('left bttc checking...')
    if global_status['left_bttc_connected'] == True:
        global_status['left_bttc_connected'] = True
        print('left bttc connected')
        log_display('left bttc connected')
        widgets.left_bttc_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        widgets.left_bttc_status.setText('左BTTC已连接')
        return True
    else:
        global_status['left_bttc_connected'] = False
        widgets.left_bttc_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
        widgets.left_bttc_status.setText('左BTTC连接失败')
        print('left bttc connect failed')
        log_display('left bttc connect failed')
        return False

def right_bttc_check():
    log_display('right bttc checking...')
    if global_status['right_bttc_connected'] == True:
        global_status['right_bttc_connected'] = True
        print('right bttc connected')
        log_display('right bttc connected')
        widgets.right_bttc_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        widgets.right_bttc_status.setText('右BTTC已连接')
        return True
    else:
        global_status['right_bttc_connected'] = False
        widgets.right_bttc_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
        widgets.right_bttc_status.setText('右BTTC连接失败')
        print('right bttc connect failed')
        log_display('right bttc connect failed')
        return False
    
    
def signal_ctrl_check():
    log_display('signal ctrl checking...')
    if global_status['signal_ctrl_connected'] == True:
        global_status['signal_ctrl_connected'] = True
        print('signal ctrl connected')
        log_display('signal ctrl connected')
        widgets.signal_switch_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        widgets.signal_switch_status.setText('射频信号切换器已连接')
        return True
    else:
        global_status['signal_ctrl_connected'] = False
        widgets.signal_switch_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
        widgets.signal_switch_status.setText('射频信号切换器连接失败')
        print('signal ctrl connect failed')
        log_display('signal ctrl connect failed')
        return False
    
def mes_serice_check():
    log_display('mes service checking...')
    if global_status['mes_service_connected'] == True:
        global_status['mes_service_connected'] = True
        print('mes service connected')
        log_display('mes service connected')
        widgets.mes_serice_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        widgets.mes_serice_status.setText('MES服务已连接')
        return True
    else:
        global_status['mes_service_connected'] = False
        widgets.mes_serice_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
        widgets.mes_serice_status.setText('MES服务连接失败')
        print('mes service connect failed')
        log_display('mes service connect failed')
        return False
    
def channel_ready_check():
    log_display('channel ready checking...')

    if (global_status['setting_loaded'] == True) and (global_status['mt8852b_connected'] == True) \
        and (global_status['signal_ctrl_connected'] == True):
        if (global_status['left_box_connected'] == True) and (global_status['left_bttc_connected']):
            global_status['channel_left_enable'] = True
            print('channel left enable')
            log_display('channel left enable')
            widgets.left_channel_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
            widgets.left_channel_status.setText('左通道就绪')
        else:
            global_status['channel_left_enable'] = False
            print('channel left disable')
            log_display('channel left disable')
            widgets.left_channel_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
            widgets.left_channel_status.setText('左通道关闭')

        if (global_status['right_box_connected'] == True) and (global_status['right_bttc_connected']):
            global_status['channel_right_enable'] = True
            print('channel right enable')
            log_display('channel right enable')
            widgets.right_channel_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
            widgets.right_channel_status.setText('右通道就绪')
        else:
            global_status['channel_right_enable'] = False
            print('channel right disable')
            log_display('channel right disable')
            widgets.right_channel_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
            widgets.right_channel_status.setText('右通道关闭')
    else:
        global_status['channel_left_enable'] = False
        global_status['channel_right_enable'] = False
        print('channel left disable')
        print('channel right disable')
        log_display('channel left disable')
        log_display('channel right disable')
        widgets.left_channel_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
        widgets.left_channel_status.setText('左通道关闭')
        widgets.right_channel_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
        widgets.right_channel_status.setText('右通道关闭')

    if (global_status['channel_left_enable'] == False) and (global_status['channel_right_enable'] == False):
        widgets.start_test_btn.setEnabled(False)    # disable start test button
        widgets.start_test_btn.setStyleSheet("color: rgb(128,138,135);")
    else:
        widgets.start_test_btn.setEnabled(True)    # disable start test button
        widgets.start_test_btn.setStyleSheet("color: white;")
        
def leop_result_display(leop_l, leop_m, leop_h):
    log_display('leop result display...')

    # print('===================================================================')
    # print('输出功率测试结果：',leop_pass)
    # print('================= 低通道 ==== 中通道 ==== 高通道 =====================')
    # print('最大功率：         ', leop_l['max'], '      ',leop_m['max'],'      ',leop_h['max'])
    # print('平均功率：         ', leop_l['avg'], '      ',leop_m['avg'],'      ',leop_h['avg'])
    # print('最小功率：         ', leop_l['min'], '      ',leop_m['min'],'      ',leop_h['min'])
    # print('峰值功率：         ', leop_l['peak_to_avg'], '      ',leop_m['peak_to_avg'],'      ',leop_h['peak_to_avg'])
    # print('测试结果：         ', leop_l['state'], '      ',leop_m['state'],'      ',leop_h['state'])

    if global_status['finished_channel'] == 'left':
        widgets.left_leop_l_max.setText(str(leop_l['max']))
        widgets.left_leop_m_max.setText(str(leop_m['max']))
        widgets.left_leop_h_max.setText(str(leop_h['max']))

        widgets.left_leop_l_avg.setText(str(leop_l['avg']))
        widgets.left_leop_m_avg.setText(str(leop_m['avg']))
        widgets.left_leop_h_avg.setText(str(leop_h['avg']))

        widgets.left_leop_l_min.setText(str(leop_l['min']))
        widgets.left_leop_m_min.setText(str(leop_m['min']))
        widgets.left_leop_h_min.setText(str(leop_h['min']))

        widgets.left_leop_l_peak.setText(str(leop_l['peak_to_avg']))
        widgets.left_leop_m_peak.setText(str(leop_m['peak_to_avg']))
        widgets.left_leop_h_peak.setText(str(leop_h['peak_to_avg']))

        widgets.left_leop_l_status.setText(str(leop_l['state']))
        widgets.left_leop_m_status.setText(str(leop_m['state']))
        widgets.left_leop_h_status.setText(str(leop_h['state']))

        if leop_l['state'] == 'PASS':
            widgets.left_leop_l_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        else:
            widgets.left_leop_l_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")

        if leop_m['state'] == 'PASS':
            widgets.left_leop_m_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        else:
            widgets.left_leop_m_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")

        if leop_h['state'] == 'PASS':
            widgets.left_leop_h_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        else:
            widgets.left_leop_h_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")

    elif global_status['finished_channel'] == 'right':
        widgets.right_leop_l_max.setText(str(leop_l['max']))
        widgets.right_leop_m_max.setText(str(leop_m['max']))
        widgets.right_leop_h_max.setText(str(leop_h['max']))

        widgets.right_leop_l_avg.setText(str(leop_l['avg']))
        widgets.right_leop_m_avg.setText(str(leop_m['avg']))
        widgets.right_leop_h_avg.setText(str(leop_h['avg']))

        widgets.right_leop_l_min.setText(str(leop_l['min']))
        widgets.right_leop_m_min.setText(str(leop_m['min']))
        widgets.right_leop_h_min.setText(str(leop_h['min']))

        widgets.right_leop_l_peak.setText(str(leop_l['peak_to_avg']))
        widgets.right_leop_m_peak.setText(str(leop_m['peak_to_avg']))
        widgets.right_leop_h_peak.setText(str(leop_h['peak_to_avg']))

        widgets.right_leop_l_status.setText(str(leop_l['state']))
        widgets.right_leop_m_status.setText(str(leop_m['state']))
        widgets.right_leop_h_status.setText(str(leop_h['state']))

        if leop_l['state'] == 'PASS':
            widgets.right_leop_l_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        else:
            widgets.right_leop_l_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")

        if leop_m['state'] == 'PASS':
            widgets.right_leop_m_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        else:
            widgets.right_leop_m_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")

        if leop_h['state'] == 'PASS':
            widgets.right_leop_h_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        else:
            widgets.right_leop_h_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")


def leicd_result_display(leicd_l, leicd_m, leicd_h):

    log_display('leicd result display...')
    # print('===================================================================')
    # print('载波频率偏移和漂移测试：',leicd_pass)
    # print('================= 低通道 ==== 中通道 ==== 高通道 =====================')
    # print('平均频偏：         ', leicd_l['avg_fn'], '      ',leicd_m['avg_fn'],'      ',leicd_h['avg_fn'])
    # print('最大频偏+ve：      ', leicd_l['max_p_fn'], '      ',leicd_m['max_p_fn'],'      ',leicd_h['max_p_fn'])
    # print('最大频偏-ve：      ', leicd_l['max_n_fn'], '      ',leicd_m['max_n_fn'],'      ',leicd_h['max_n_fn'])
    # print('漂移速率：         ', leicd_l['max_dirft_rate'], '      ',leicd_m['max_dirft_rate'],'      ',leicd_h['max_dirft_rate'])
    # print('最大漂移：         ', leicd_l['max_drift'], '      ',leicd_m['max_drift'],'      ',leicd_h['max_drift'])
    # print('平均漂移：         ', leicd_l['avg_drift'], '      ',leicd_m['avg_drift'],'      ',leicd_h['avg_drift'])
    # print('测试结果：         ', leicd_l['state'], '      ',leicd_m['state'],'      ',leicd_h['state'])

    if global_status['finished_channel'] == 'left':

        widgets.left_leicd_l_avg_fn.setText(str(leicd_l['avg_fn']))
        widgets.left_leicd_m_avg_fn.setText(str(leicd_m['avg_fn']))
        widgets.left_leicd_h_avg_fn.setText(str(leicd_h['avg_fn']))

        widgets.left_leicd_l_max_p_fn.setText(str(leicd_l['max_p_fn']))
        widgets.left_leicd_m_max_p_fn.setText(str(leicd_m['max_p_fn']))
        widgets.left_leicd_h_max_p_fn.setText(str(leicd_h['max_p_fn']))

        widgets.left_leicd_l_max_n_fn.setText(str(leicd_l['max_n_fn']))
        widgets.left_leicd_m_max_n_fn.setText(str(leicd_m['max_n_fn']))
        widgets.left_leicd_h_max_n_fn.setText(str(leicd_h['max_n_fn']))

        widgets.left_leicd_l_max_dirft_rate.setText(str(leicd_l['max_dirft_rate']))
        widgets.left_leicd_m_max_dirft_rate.setText(str(leicd_m['max_dirft_rate']))
        widgets.left_leicd_h_max_dirft_rate.setText(str(leicd_h['max_dirft_rate']))

        widgets.left_leicd_l_max_dirft.setText(str(leicd_l['max_drift']))
        widgets.left_leicd_m_max_dirft.setText(str(leicd_m['max_drift']))
        widgets.left_leicd_h_max_dirft.setText(str(leicd_h['max_drift']))

        widgets.left_leicd_l_avg_dirft.setText(str(leicd_l['avg_drift']))
        widgets.left_leicd_m_avg_dirft.setText(str(leicd_m['avg_drift']))
        widgets.left_leicd_h_avg_dirft.setText(str(leicd_h['avg_drift']))

        widgets.left_leicd_l_state.setText(str(leicd_l['state']))
        widgets.left_leicd_m_state.setText(str(leicd_m['state']))
        widgets.left_leicd_h_state.setText(str(leicd_h['state']))

        if leicd_l['state'] == 'PASS':
            widgets.left_leicd_l_state.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        else:
            widgets.left_leicd_l_state.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")

        if leicd_m['state'] == 'PASS':
            widgets.left_leicd_m_state.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        else:
            widgets.left_leicd_m_state.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")

        if leicd_h['state'] == 'PASS':
            widgets.left_leicd_h_state.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        else:
            widgets.left_leicd_h_state.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")

    elif global_status['finished_channel'] == 'right':
            
            widgets.right_leicd_l_avg_fn.setText(str(leicd_l['avg_fn']))
            widgets.right_leicd_m_avg_fn.setText(str(leicd_m['avg_fn']))
            widgets.right_leicd_h_avg_fn.setText(str(leicd_h['avg_fn']))
    
            widgets.right_leicd_l_max_p_fn.setText(str(leicd_l['max_p_fn']))
            widgets.right_leicd_m_max_p_fn.setText(str(leicd_m['max_p_fn']))
            widgets.right_leicd_h_max_p_fn.setText(str(leicd_h['max_p_fn']))
    
            widgets.right_leicd_l_max_n_fn.setText(str(leicd_l['max_n_fn']))
            widgets.right_leicd_m_max_n_fn.setText(str(leicd_m['max_n_fn']))
            widgets.right_leicd_h_max_n_fn.setText(str(leicd_h['max_n_fn']))
    
            widgets.right_leicd_l_max_dirft_rate.setText(str(leicd_l['max_dirft_rate']))
            widgets.right_leicd_m_max_dirft_rate.setText(str(leicd_m['max_dirft_rate']))
            widgets.right_leicd_h_max_dirft_rate.setText(str(leicd_h['max_dirft_rate']))
    
            widgets.right_leicd_l_max_dirft.setText(str(leicd_l['max_drift']))
            widgets.right_leicd_m_max_dirft.setText(str(leicd_m['max_drift']))
            widgets.right_leicd_h_max_dirft.setText(str(leicd_h['max_drift']))
    
            widgets.right_leicd_l_avg_dirft.setText(str(leicd_l['avg_drift']))
            widgets.right_leicd_m_avg_dirft.setText(str(leicd_m['avg_drift']))
            widgets.right_leicd_h_avg_dirft.setText(str(leicd_h['avg_drift']))
    
            widgets.right_leicd_l_state.setText(str(leicd_l['state']))
            widgets.right_leicd_m_state.setText(str(leicd_m['state']))
            widgets.right_leicd_h_state.setText(str(leicd_h['state']))
    
            if leicd_l['state'] == 'PASS':
                widgets.right_leicd_l_state.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
            else:
                widgets.right_leicd_l_state.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")

            if leicd_m['state'] == 'PASS':
                widgets.right_leicd_m_state.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
            else:
                widgets.right_leicd_m_state.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")

            if leicd_h['state'] == 'PASS':
                widgets.right_leicd_h_state.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
            else:
                widgets.right_leicd_h_state.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")


def less_result_display(less_l,less_m,less_h):

    log_display('less_result_display')

    # print('===================================================================')
    # print('灵敏度测试(发射功率 -85dBm)：',less_pass)
    # print('================= 低通道 ==== 中通道 ==== 高通道 =====================')
    # print('误帧率：           ', less_l['over_fer_%'], '      ',less_m['over_fer_%'],'      ',less_h['over_fer_%'])
    # print('发送包数：         ', less_l['total_frames_sent_tester'], '      ',
    #     less_m['total_frames_sent_tester'],'      ',less_h['total_frames_sent_tester'])
    # print('接收包数：         ', less_l['total_frames_counted_dut'], '      ',
    #         less_m['total_frames_counted_dut'],'      ',less_h['total_frames_counted_dut'])
    # print('测试结果：         ', less_l['state'], '      ',less_m['state'],'      ',less_h['state'])

    if global_status['finished_channel'] == 'left':

        widgets.left_less_l_over_fer.setText(str(less_l['over_fer_%']))
        widgets.left_less_m_over_fer.setText(str(less_m['over_fer_%']))
        widgets.left_less_h_over_fer.setText(str(less_h['over_fer_%']))

        widgets.left_less_l_total_frames_sent_tester.setText(str(less_l['total_frames_sent_tester']))
        widgets.left_less_m_total_frames_sent_tester.setText(str(less_m['total_frames_sent_tester']))
        widgets.left_less_h_total_frames_sent_tester.setText(str(less_h['total_frames_sent_tester']))

        widgets.left_less_l_total_frames_counted_dut.setText(str(less_l['total_frames_counted_dut']))
        widgets.left_less_m_total_frames_counted_dut.setText(str(less_m['total_frames_counted_dut']))
        widgets.left_less_h_total_frames_counted_dut.setText(str(less_h['total_frames_counted_dut']))

        widgets.left_less_l_status.setText(str(less_l['state']))
        widgets.left_less_m_status.setText(str(less_m['state']))
        widgets.left_less_h_status.setText(str(less_h['state']))

        if less_l['state'] == 'PASS':
            widgets.left_less_l_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        else:
            widgets.left_less_l_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")

        if less_m['state'] == 'PASS':
            widgets.left_less_m_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        else:
            widgets.left_less_m_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")

        if less_h['state'] == 'PASS':
            widgets.left_less_h_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        else:
            widgets.left_less_h_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")

    else:
            
            widgets.right_less_l_over_fer.setText(str(less_l['over_fer_%']))
            widgets.right_less_m_over_fer.setText(str(less_m['over_fer_%']))
            widgets.right_less_h_over_fer.setText(str(less_h['over_fer_%']))
    
            widgets.right_less_l_total_frames_sent_tester.setText(str(less_l['total_frames_sent_tester']))
            widgets.right_less_m_total_frames_sent_tester.setText(str(less_m['total_frames_sent_tester']))
            widgets.right_less_h_total_frames_sent_tester.setText(str(less_h['total_frames_sent_tester']))
    
            widgets.right_less_l_total_frames_counted_dut.setText(str(less_l['total_frames_counted_dut']))
            widgets.right_less_m_total_frames_counted_dut.setText(str(less_m['total_frames_counted_dut']))
            widgets.right_less_h_total_frames_counted_dut.setText(str(less_h['total_frames_counted_dut']))
    
            widgets.right_less_l_status.setText(str(less_l['state']))
            widgets.right_less_m_status.setText(str(less_m['state']))
            widgets.right_less_h_status.setText(str(less_h['state']))
    
            if less_l['state'] == 'PASS':
                widgets.right_less_l_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
            else:
                widgets.right_less_l_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
    
            if less_m['state'] == 'PASS':
                widgets.right_less_m_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
            else:
                widgets.right_less_m_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
    
            if less_h['state'] == 'PASS':
                widgets.right_less_h_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
            else:
                widgets.right_less_h_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")


def result_time_display(point, during):
    if global_status['finished_channel'] == 'left':
        widgets.left_test_time_point.setText(str(point))
        widgets.left_test_time_during.setText(str(during))
    else:
        widgets.right_test_time_point.setText(str(point))
        widgets.right_test_time_during.setText(str(during))
    

def result_display_reset(channel):
    
    if channel == 'left':


        widgets.left_leop_l_max.setText('-')
        widgets.left_leop_m_max.setText('-')
        widgets.left_leop_h_max.setText('-')

        widgets.left_leop_l_min.setText('-')
        widgets.left_leop_m_min.setText('-')
        widgets.left_leop_h_min.setText('-')

        widgets.left_leop_l_avg.setText('-')
        widgets.left_leop_m_avg.setText('-')
        widgets.left_leop_h_avg.setText('-')

        widgets.left_leop_l_peak.setText('-')
        widgets.left_leop_m_peak.setText('-')
        widgets.left_leop_h_peak.setText('-')

        widgets.left_leop_l_status.setText('-')
        widgets.left_leop_m_status.setText('-')
        widgets.left_leop_h_status.setText('-')

        widgets.left_leop_l_status.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")
        widgets.left_leop_m_status.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")
        widgets.left_leop_h_status.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")


        widgets.left_leicd_l_avg_fn.setText('-')
        widgets.left_leicd_m_avg_fn.setText('-')
        widgets.left_leicd_h_avg_fn.setText('-')

        widgets.left_leicd_l_max_p_fn.setText('-')
        widgets.left_leicd_m_max_p_fn.setText('-')
        widgets.left_leicd_h_max_p_fn.setText('-')

        widgets.left_leicd_l_max_n_fn.setText('-')
        widgets.left_leicd_m_max_n_fn.setText('-')
        widgets.left_leicd_h_max_n_fn.setText('-')

        widgets.left_leicd_l_max_dirft_rate.setText('-')
        widgets.left_leicd_m_max_dirft_rate.setText('-')
        widgets.left_leicd_h_max_dirft_rate.setText('-')

        widgets.left_leicd_l_max_dirft.setText('-')
        widgets.left_leicd_m_max_dirft.setText('-')
        widgets.left_leicd_h_max_dirft.setText('-')

        widgets.left_leicd_l_avg_dirft.setText('-')
        widgets.left_leicd_m_avg_dirft.setText('-')
        widgets.left_leicd_h_avg_dirft.setText('-')

        widgets.left_leicd_l_state.setText('-')
        widgets.left_leicd_m_state.setText('-')
        widgets.left_leicd_h_state.setText('-')

        widgets.left_leicd_l_state.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")
        widgets.left_leicd_m_state.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")
        widgets.left_leicd_h_state.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")



        widgets.left_less_l_over_fer.setText('-')
        widgets.left_less_m_over_fer.setText('-')
        widgets.left_less_h_over_fer.setText('-')

        widgets.left_less_l_total_frames_sent_tester.setText('-')
        widgets.left_less_m_total_frames_sent_tester.setText('-')
        widgets.left_less_h_total_frames_sent_tester.setText('-')

        widgets.left_less_l_total_frames_counted_dut.setText('-')
        widgets.left_less_m_total_frames_counted_dut.setText('-')
        widgets.left_less_h_total_frames_counted_dut.setText('-')

        widgets.left_less_l_status.setText('-')
        widgets.left_less_m_status.setText('-')
        widgets.left_less_h_status.setText('-')

        widgets.left_less_l_status.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")
        widgets.left_less_m_status.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")
        widgets.left_less_h_status.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")

        widgets.left_test_time_point.setText('-')
        widgets.left_test_time_during.setText('-')

    elif channel == 'right':
            
            widgets.right_leop_l_max.setText('-')
            widgets.right_leop_m_max.setText('-')
            widgets.right_leop_h_max.setText('-')
    
            widgets.right_leop_l_min.setText('-')
            widgets.right_leop_m_min.setText('-')
            widgets.right_leop_h_min.setText('-')
    
            widgets.right_leop_l_avg.setText('-')
            widgets.right_leop_m_avg.setText('-')
            widgets.right_leop_h_avg.setText('-')
    
            widgets.right_leop_l_peak.setText('-')
            widgets.right_leop_m_peak.setText('-')
            widgets.right_leop_h_peak.setText('-')
    
            widgets.right_leop_l_status.setText('-')
            widgets.right_leop_m_status.setText('-')
            widgets.right_leop_h_status.setText('-')
    
            widgets.right_leop_l_status.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")
            widgets.right_leop_m_status.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")
            widgets.right_leop_h_status.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")
    
    
            widgets.right_leicd_l_avg_fn.setText('-')
            widgets.right_leicd_m_avg_fn.setText('-')
            widgets.right_leicd_h_avg_fn.setText('-')
    
            widgets.right_leicd_l_max_p_fn.setText('-')
            widgets.right_leicd_m_max_p_fn.setText('-')
            widgets.right_leicd_h_max_p_fn.setText('-')
    
            widgets.right_leicd_l_max_n_fn.setText('-')
            widgets.right_leicd_m_max_n_fn.setText('-')
            widgets.right_leicd_h_max_n_fn.setText('-')
    
            widgets.right_leicd_l_max_dirft_rate.setText('-')
            widgets.right_leicd_m_max_dirft_rate.setText('-')
            widgets.right_leicd_h_max_dirft_rate.setText('-')
    
            widgets.right_leicd_l_max_dirft.setText('-')
            widgets.right_leicd_m_max_dirft.setText('-')
            widgets.right_leicd_h_max_dirft.setText('-')
    
            widgets.right_leicd_l_avg_dirft.setText('-')
            widgets.right_leicd_m_avg_dirft.setText('-')
            widgets.right_leicd_h_avg_dirft.setText('-')
    
            widgets.right_leicd_l_state.setText('-')
            widgets.right_leicd_m_state.setText('-')
            widgets.right_leicd_h_state.setText('-')

            widgets.right_leicd_l_state.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")
            widgets.right_leicd_m_state.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")
            widgets.right_leicd_h_state.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")

            widgets.right_less_l_over_fer.setText('-')
            widgets.right_less_m_over_fer.setText('-')
            widgets.right_less_h_over_fer.setText('-')

            widgets.right_less_l_total_frames_sent_tester.setText('-')
            widgets.right_less_m_total_frames_sent_tester.setText('-')
            widgets.right_less_h_total_frames_sent_tester.setText('-')

            widgets.right_less_l_total_frames_counted_dut.setText('-')
            widgets.right_less_m_total_frames_counted_dut.setText('-')
            widgets.right_less_h_total_frames_counted_dut.setText('-')

            widgets.right_less_l_status.setText('-')
            widgets.right_less_m_status.setText('-')
            widgets.right_less_h_status.setText('-')

            widgets.right_less_l_status.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")
            widgets.right_less_m_status.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")
            widgets.right_less_h_status.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")

            widgets.right_test_time_point.setText('-')
            widgets.right_test_time_during.setText('-')



        

        
    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Bluetooth Test"
        description = "HCD-BTTP 蓝牙性能测试平台 [MT8852B]"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        # widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # SETTING INIT
        log_display('Start init...')

        widgets.default_btn.setEnabled(False)   # disable default button
        widgets.cfg_save_btn.setEnabled(False)  # disable save button

        widgets.start_test_btn.setEnabled(False)    # disable start test button
        widgets.start_test_btn.setStyleSheet("color: rgb(128,138,135);")

        setting_data = setting_load()  # load setting from file

        mt8852b_check() # check mt8852b

        com_list_cherk(setting_data)    # check com list
        left_box_check()    # check left box
        right_box_check()   # check right box
        left_bttc_check()   # check left bbtc
        right_bttc_check()  # check right bbtc
        signal_ctrl_check() # check signal ctrl
        mes_serice_check()  # check mes service

        channel_ready_check()   # check channel ready

        setting_disable();  # disable setting

        ## TEST RESULT
        global_status['finished_channel'] = 'left'
        leop_l = {'max': 1, 'avg': 2, 'min': 3, 'peak_to_avg': 4, 'state': 'PASS'}
        leop_m = {'max': 5, 'avg': 6, 'min': 7, 'peak_to_avg': 8, 'state': 'FAIL'}
        leop_h = {'max': 9, 'avg': 10, 'min': 11, 'peak_to_avg': 12, 'state': 'PASS'}

        leop_result_display(leop_l, leop_m, leop_h)


        leicd_l = {'avg_fn': 1, 'max_p_fn': 2, 'max_n_fn': 3, 'max_dirft_rate': 4, 'max_drift': 5, 'avg_drift': 6, 'state': 'PASS'}
        leicd_m = {'avg_fn': 7, 'max_p_fn': 8, 'max_n_fn': 9, 'max_dirft_rate': 10, 'max_drift': 11, 'avg_drift': 12, 'state': 'FAIL'}
        leicd_h = {'avg_fn': 13, 'max_p_fn': 14, 'max_n_fn': 15, 'max_dirft_rate': 16, 'max_drift': 17, 'avg_drift': 18, 'state': 'PASS'}
        leicd_result_display(leicd_l, leicd_m, leicd_h)

        less_l = {'over_fer_%': 1, 'total_frames_sent_tester': 2, 'total_frames_counted_dut': 3, 'state': 'PASS'}
        less_m = {'over_fer_%': 4, 'total_frames_sent_tester': 5, 'total_frames_counted_dut': 6, 'state': 'FAIL'}
        less_h = {'over_fer_%': 7, 'total_frames_sent_tester': 8, 'total_frames_counted_dut': 9, 'state': 'PASS'}
        less_result_display(less_h, less_m, less_l)

        result_time_display('123','456')

        result_display_reset(global_status['finished_channel'])


        widgets.left_test_result_bar.setAlignment(Qt.AlignCenter)
        widgets.left_test_result_bar.setMinimumHeight(100)

        widgets.left_test_result_bar.setValue(35)
        widgets.left_test_result_bar.setFormat('测试中...')

        widgets.left_test_result_bar.setStyleSheet("QProgressBar::chunk {font-size: 20px; font-weight: bold; color: rgb(255, 255, 255); background-color: rgb(255, 255, 0);};")

        widgets.left_test_result_bar.setStyleSheet('QProgressBar { font-size: 30px; color: rgb(0, 0, 0); } QProgressBar::chunk { font-size: 20px; background-color: rgb(255, 255, 0); \
                                                   font-weight: bold; color: rgb(0, 0, 0);}')

        # widgets.left_test_result_bar.setValue(100)
        # widgets.left_test_result_bar.setFormat('FAIL')
        # widgets.left_test_result_bar.setStyleSheet("QProgressBar::chunk {background-color: rgb(255, 0, 0);};")

        # widgets.left_test_result_bar.setValue(100)
        # widgets.left_test_result_bar.setFormat('PASS')
        # widgets.left_test_result_bar.setStyleSheet("QProgressBar::chunk {background-color: rgb(34, 139, 34);};")

        widgets.right_test_result_bar.setAlignment(Qt.AlignCenter)
        widgets.right_test_result_bar.setMinimumHeight(100)

        widgets.right_test_result_bar.setValue(100)

        widgets.right_test_result_bar.setFormat('PASS')
        widgets.right_test_result_bar.setStyleSheet('QProgressBar { font-size: 30px; color: rgb(0, 0, 0); } QProgressBar::chunk { font-size: 20px; background-color: rgb(34, 139, 34); \
                                                    font-weight: bold; color: rgb(0, 0, 0);}')

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_test_data.clicked.connect(self.buttonClick)
        widgets.btn_config.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
        
        widgets.cfg_save_btn.clicked.connect(self.buttonClick)
        widgets.start_test_btn.clicked.connect(self.buttonClick)
        widgets.test_config_btn.clicked.connect(self.buttonClick)

        widgets.setting_status.clicked.connect(self.buttonClick)
        widgets.mt8852b_status.clicked.connect(self.buttonClick)
        widgets.left_box_status.clicked.connect(self.buttonClick)
        widgets.right_box_status.clicked.connect(self.buttonClick)
        widgets.left_bttc_status.clicked.connect(self.buttonClick)
        widgets.right_bttc_status.clicked.connect(self.buttonClick)
        widgets.signal_switch_status.clicked.connect(self.buttonClick)
        widgets.mes_serice_status.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))



    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_test_data" or btnName == "start_test_btn":
            widgets.stackedWidget.setCurrentWidget(widgets.test_data_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_config" or btnName == "test_config_btn":
            widgets.stackedWidget.setCurrentWidget(widgets.test_config_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_save":
            print("Save BTN clicked!")

        if btnName == "cfg_save_btn":
            setting_save()

        if btnName == "setting_status":
            if global_status['setting_loaded'] == False:
                setting_load()
                channel_ready_check()
        
        if btnName == "mt8852b_status":
            if global_status['mt8852b_connected'] == False:
                mt8852b_check()
                channel_ready_check()
        
        if btnName == "left_box_status":
            if global_status['left_box_connected'] == False:
                com_list_cherk(setting_load())
                left_box_check()
                channel_ready_check()
        
        if btnName == "right_box_status":
            if global_status['right_box_connected'] == False:
                com_list_cherk(setting_load())
                right_box_check()
                channel_ready_check()
        
        if btnName == "left_bttc_status":
            if global_status['left_bttc_connected'] == False:
                com_list_cherk(setting_load())
                left_bttc_check()
                channel_ready_check()
        
        if btnName == "right_bttc_status":
            if global_status['right_bttc_connected'] == False:
                com_list_cherk(setting_load())
                right_bttc_check()
                channel_ready_check()

        if btnName == "signal_switch_status":
            if global_status['signal_switch_connected'] == False:
                com_list_cherk(setting_load())
                signal_ctrl_check()
                channel_ready_check()

        if btnName == "mes_serice_status":
            if global_status['mes_service_connected'] == False:
                mes_serice_check()

        

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
