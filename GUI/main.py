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

import tr_dis
import plam_det
import setting_ctrl
import mt8852b_ctrl

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



## Read and detect COM port
def com_list_cherk(setting_info):   
    plam_det.log_display(widgets,'COM list checking...')
    com_list = serial.tools.list_ports.comports()
    comlist_len = len(com_list)
    for i in range(0, comlist_len):
        print(com_list[i])
        plam_det.log_display(widgets,str(com_list[i]))
        if global_status['setting_loaded'] == True:
            if setting_info['connect']['left_box_com'] == str(com_list[i].name):    
                plam_det.log_display(widgets,'Left box COM port found!')
                global_status['left_box_connected'] = True
            if setting_info['connect']['right_box_com'] == str(com_list[i].name):
                plam_det.log_display(widgets,'Right box COM port found!')
                global_status['right_box_connected'] = True
            if setting_info['connect']['left_bttc_com'] == str(com_list[i].name):
                plam_det.log_display(widgets,'Left BTTC COM port found!')
                global_status['left_bttc_connected'] = True
            if setting_info['connect']['right_bttc_com'] == str(com_list[i].name):
                plam_det.log_display(widgets,'Right BTTC COM port found!')
                global_status['right_bttc_connected'] = True
            if setting_info['connect']['signal_ctrl_com'] == str(com_list[i].name):
                plam_det.log_display(widgets,'Signal controller COM port found!')
                global_status['signal_ctrl_connected'] = True
        else:
            plam_det.log_display(widgets,'Setting file not loaded, please check!')
            
    


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
        plam_det.log_display(widgets,'Start init...')

        device_id = mt8852b_ctrl.connect(widgets)
        mt8852b_ctrl.init(widgets,device_id)

        mt8852b_ctrl.leop_result_read(widgets,device_id) # read leop result
        mt8852b_ctrl.leicd_result_read(widgets,device_id) # read leicd result
        mt8852b_ctrl.less_result_read(widgets,device_id) # read less result

        widgets.default_btn.setEnabled(False)   # disable default button
        widgets.cfg_save_btn.setEnabled(False)  # disable save button

        widgets.start_test_btn.setEnabled(False)    # disable start test button
        widgets.start_test_btn.setStyleSheet("color: rgb(128,138,135);")

        setting_data = setting_ctrl.setting_load(widgets,global_status)  # load setting from file

        plam_det.mt8852b_check(global_status, widgets) # check mt8852b

        com_list_cherk(setting_data)    # check com list
        plam_det.left_box_check(global_status, widgets)    # check left box
        plam_det.right_box_check(global_status, widgets)   # check right box
        plam_det.left_bttc_check(global_status, widgets)   # check left bbtc
        plam_det.right_bttc_check(global_status, widgets)  # check right bbtc
        plam_det.signal_ctrl_check(global_status, widgets) # check signal ctrl
        plam_det.mes_serice_check(global_status, widgets)  # check mes service

        plam_det.channel_ready_check(global_status, widgets)   # check channel ready

        setting_ctrl.setting_disable(widgets);  # disable setting

        ## TEST RESULT
        global_status['finished_channel'] = 'right'
        leop_l = {'max': 1, 'avg': 2, 'min': 3, 'peak_to_avg': 4, 'state': 'PASS'}
        leop_m = {'max': 5, 'avg': 6, 'min': 7, 'peak_to_avg': 8, 'state': 'FAIL'}
        leop_h = {'max': 9, 'avg': 10, 'min': 11, 'peak_to_avg': 12, 'state': 'PASS'}

        tr_dis.leop_result_display(global_status,widgets,leop_l, leop_m, leop_h)


        leicd_l = {'avg_fn': 1, 'max_p_fn': 2, 'max_n_fn': 3, 'max_dirft_rate': 4, 'max_drift': 5, 'avg_drift': 6, 'state': 'PASS'}
        leicd_m = {'avg_fn': 7, 'max_p_fn': 8, 'max_n_fn': 9, 'max_dirft_rate': 10, 'max_drift': 11, 'avg_drift': 12, 'state': 'FAIL'}
        leicd_h = {'avg_fn': 13, 'max_p_fn': 14, 'max_n_fn': 15, 'max_dirft_rate': 16, 'max_drift': 17, 'avg_drift': 18, 'state': 'PASS'}
        tr_dis.leicd_result_display(global_status,widgets,leicd_l, leicd_m, leicd_h)

        less_l = {'over_fer_%': 1, 'total_frames_sent_tester': 2, 'total_frames_counted_dut': 3, 'state': 'PASS'}
        less_m = {'over_fer_%': 4, 'total_frames_sent_tester': 5, 'total_frames_counted_dut': 6, 'state': 'FAIL'}
        less_h = {'over_fer_%': 7, 'total_frames_sent_tester': 8, 'total_frames_counted_dut': 9, 'state': 'PASS'}
        tr_dis.less_result_display(global_status,widgets,less_h, less_m, less_l)

        tr_dis.result_time_display(global_status,widgets,'123','456')


        tr_dis.test_total_cnt_display(widgets,global_status['finished_channel'],789)
        tr_dis.test_fail_count_display(widgets,global_status['finished_channel'],456)
        tr_dis.test_pass_count_display(widgets,global_status['finished_channel'],123)
        tr_dis.test_fail_rate_display(widgets,global_status['finished_channel'],13.2)

        # tr_dis.result_display_reset(widgets,global_status['finished_channel'])


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
            setting_ctrl.setting_save(widgets)

        if btnName == "setting_status":
            if global_status['setting_loaded'] == False:
                setting_ctrl.setting_load(widgets)
                plam_det.channel_ready_check(global_status, widgets)
        
        if btnName == "mt8852b_status":
            if global_status['mt8852b_connected'] == False:
                plam_det.mt8852b_check(global_status, widgets)
                plam_det.channel_ready_check(global_status, widgets)
        
        if btnName == "left_box_status":
            if global_status['left_box_connected'] == False:
                com_list_cherk(setting_ctrl.setting_load(widgets))
                plam_det.left_box_check(global_status, widgets)
                plam_det.channel_ready_check(global_status, widgets)
        
        if btnName == "right_box_status":
            if global_status['right_box_connected'] == False:
                com_list_cherk(setting_ctrl.setting_load(widgets))
                plam_det.right_box_check(global_status, widgets)
                plam_det.channel_ready_check(global_status, widgets)
        
        if btnName == "left_bttc_status":
            if global_status['left_bttc_connected'] == False:
                com_list_cherk(setting_ctrl.setting_load(widgets))
                plam_det.left_bttc_check(global_status, widgets)
                plam_det.channel_ready_check(global_status, widgets)
        
        if btnName == "right_bttc_status":
            if global_status['right_bttc_connected'] == False:
                com_list_cherk(setting_ctrl.setting_load(widgets))
                plam_det.right_bttc_check(global_status, widgets)
                plam_det.channel_ready_check(global_status, widgets)

        if btnName == "signal_switch_status":
            if global_status['signal_switch_connected'] == False:
                com_list_cherk(setting_ctrl.setting_load(widgets))
                plam_det.signal_ctrl_check(global_status, widgets)
                plam_det.channel_ready_check(global_status, widgets)

        if btnName == "mes_serice_status":
            if global_status['mes_service_connected'] == False:
                plam_det.mes_serice_check(global_status, widgets)

        

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
