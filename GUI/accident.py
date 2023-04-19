'''
Author: emmovo
Date: 2023-04-02 18:51:23
LastEditors: emmovo
LastEditTime: 2023-04-03 12:53:42
FilePath: \BluetoothKB_Freq_test\GUI\accident.py
Description: 

Copyright (c) 2023 by mingjkl@live.com/emmovo.com, All Rights Reserved. 
'''
from PySide6.QtWidgets import QMessageBox

import plam_det

warnning_triggered = False

def warnning(widgets, str, enable):
    if enable == True:
        plam_det.log_display(widgets,'ACCIDENT! WARNNING!')
        plam_det.log_display(widgets,str)
        print('ACCIDENT! WARNNING!')
        print(str)

        # if warnning_triggered == False:

        #     widgets.stackedWidget.setCurrentWidget(widgets.home)

        #     warningbox = QMessageBox()
        #     warningbox.setIcon(QMessageBox.Warning)
        #     warningbox.setText(str)
        #     warningbox.setWindowTitle("WARNNING")
        #     warningbox.setStandardButtons(QMessageBox.Ok)
        #     warningbox.exec()

            # warnning_triggered = True