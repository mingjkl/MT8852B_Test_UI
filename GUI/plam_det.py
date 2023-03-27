import time

## The log display function on the UI interface
def log_display(widgets,msg):
    widgets.textEdit_4.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' LOG: ' + msg) 

def mt8852b_check(global_status, widgets):
    log_display(widgets,'mt8852b checking...')
    if global_status['mt8852b_connected'] == True:
        global_status['mt8852b_connected'] = True
        print('mt8852b connected')
        log_display(widgets,'mt8852b connected')
        widgets.mt8852b_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        widgets.mt8852b_status.setText('MT8852B已连接')
        return True
    else:
        global_status['mt8852b_connected'] = False
        widgets.mt8852b_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
        widgets.mt8852b_status.setText('MT8852B连接失败')
        print('mt8852b connect failed')
        log_display(widgets,'mt8852b connect failed')
        return False
    

def left_box_check(global_status, widgets):
    log_display(widgets,'left box checking...')
    if global_status['left_box_connected'] == True:
        global_status['left_box_connected'] = True
        print('left box connected')
        log_display(widgets,'left box connected')
        widgets.left_box_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        widgets.left_box_status.setText('左屏蔽盒已连接')
        return True
    else:
        global_status['left_box_connected'] = False
        widgets.left_box_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
        widgets.left_box_status.setText('左屏蔽盒连接失败')
        print('left box connect failed')
        log_display(widgets,'left box connect failed')
        return False
    

def right_box_check(global_status, widgets):
    log_display(widgets,'right box checking...')
    if global_status['right_box_connected'] == True:
        global_status['right_box_connected'] = True
        print('right box connected')
        log_display(widgets,'right box connected')
        widgets.right_box_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        widgets.right_box_status.setText('右屏蔽盒已连接')
        return True
    else:
        global_status['right_box_connected'] = False
        widgets.right_box_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
        widgets.right_box_status.setText('右屏蔽盒连接失败')
        print('right box connect failed')
        log_display(widgets,'right box connect failed')
        return False

def left_bttc_check(global_status, widgets):
    log_display(widgets,'left bttc checking...')
    if global_status['left_bttc_connected'] == True:
        global_status['left_bttc_connected'] = True
        print('left bttc connected')
        log_display(widgets,'left bttc connected')
        widgets.left_bttc_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        widgets.left_bttc_status.setText('左BTTC已连接')
        return True
    else:
        global_status['left_bttc_connected'] = False
        widgets.left_bttc_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
        widgets.left_bttc_status.setText('左BTTC连接失败')
        print('left bttc connect failed')
        log_display(widgets,'left bttc connect failed')
        return False

def right_bttc_check(global_status, widgets):
    log_display(widgets,'right bttc checking...')
    if global_status['right_bttc_connected'] == True:
        global_status['right_bttc_connected'] = True
        print('right bttc connected')
        log_display(widgets,'right bttc connected')
        widgets.right_bttc_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        widgets.right_bttc_status.setText('右BTTC已连接')
        return True
    else:
        global_status['right_bttc_connected'] = False
        widgets.right_bttc_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
        widgets.right_bttc_status.setText('右BTTC连接失败')
        print('right bttc connect failed')
        log_display(widgets,'right bttc connect failed')
        return False
    
    
def signal_ctrl_check(global_status, widgets):
    log_display(widgets,'signal ctrl checking...')
    if global_status['signal_ctrl_connected'] == True:
        global_status['signal_ctrl_connected'] = True
        print('signal ctrl connected')
        log_display(widgets,'signal ctrl connected')
        widgets.signal_switch_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        widgets.signal_switch_status.setText('射频信号切换器已连接')
        return True
    else:
        global_status['signal_ctrl_connected'] = False
        widgets.signal_switch_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
        widgets.signal_switch_status.setText('射频信号切换器连接失败')
        print('signal ctrl connect failed')
        log_display(widgets,'signal ctrl connect failed')
        return False
    
def mes_serice_check(global_status, widgets):
    log_display(widgets,'mes service checking...')
    if global_status['mes_service_connected'] == True:
        global_status['mes_service_connected'] = True
        print('mes service connected')
        log_display(widgets,'mes service connected')
        widgets.mes_serice_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        widgets.mes_serice_status.setText('MES服务已连接')
        return True
    else:
        global_status['mes_service_connected'] = False
        widgets.mes_serice_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
        widgets.mes_serice_status.setText('MES服务连接失败')
        print('mes service connect failed')
        log_display(widgets,'mes service connect failed')
        return False
    
def channel_ready_check(global_status, widgets):
    log_display(widgets,'channel ready checking...')

    if (global_status['setting_loaded'] == True) and (global_status['mt8852b_connected'] == True) \
        and (global_status['signal_ctrl_connected'] == True):
        if (global_status['left_box_connected'] == True) and (global_status['left_bttc_connected']):
            global_status['channel_left_enable'] = True
            print('channel left enable')
            log_display(widgets,'channel left enable')
            widgets.left_channel_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
            widgets.left_channel_status.setText('左通道就绪')
        else:
            global_status['channel_left_enable'] = False
            print('channel left disable')
            log_display(widgets,'channel left disable')
            widgets.left_channel_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
            widgets.left_channel_status.setText('左通道关闭')

        if (global_status['right_box_connected'] == True) and (global_status['right_bttc_connected']):
            global_status['channel_right_enable'] = True
            print('channel right enable')
            log_display(widgets,'channel right enable')
            widgets.right_channel_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
            widgets.right_channel_status.setText('右通道就绪')
        else:
            global_status['channel_right_enable'] = False
            print('channel right disable')
            log_display(widgets,'channel right disable')
            widgets.right_channel_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
            widgets.right_channel_status.setText('右通道关闭')
    else:
        global_status['channel_left_enable'] = False
        global_status['channel_right_enable'] = False
        print('channel left disable')
        print('channel right disable')
        log_display(widgets,'channel left disable')
        log_display(widgets,'channel right disable')
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