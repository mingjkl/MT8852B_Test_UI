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
                 'channel_left_enable': False,}


## The log display function on the UI interface
def log_display(msg):
    widgets.textEdit_4.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' LOG: ' + msg) 
    
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
        else:
            global_status['channel_left_enable'] = False
            print('channel left disable')
            log_display('channel left disable')
        if (global_status['right_box_connected'] == True) and (global_status['right_bttc_connected']):
            global_status['channel_right_enable'] = True
            print('channel right enable')
            log_display('channel right enable')
        else:
            global_status['channel_right_enable'] = False
            print('channel right disable')
            log_display('channel right disable')
    else:
        global_status['channel_left_enable'] = False
        global_status['channel_right_enable'] = False
        print('channel left disable')
        print('channel right disable')
        log_display('channel left disable')
        log_display('channel right disable')
        
        


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
        description = "Bluetooth Test"
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
        widgets.default_btn.setEnabled(False)   # disable default button
        widgets.cfg_save_btn.setEnabled(False)  # disable save button

    
        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
        

        widgets.cfg_save_btn.clicked.connect(self.buttonClick)

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

        widgets.textEdit_3.append("123456");
        widgets.textEdit_3.append("尼洛茨");
        widgets.textEdit_3.setDisabled(True);



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
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
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
