<!--
 * @Author: emmovo
 * @Date: 2023-04-18 19:32:57
 * @LastEditors: emmovo
 * @LastEditTime: 2023-04-18 21:03:26
 * @FilePath: \GUI\ui_single.md
 * @Description: 
 * 
 * Copyright (c) 2023 by mingjkl@live.com/emmovo.com, All Rights Reserved. 
-->

1 将ui_main_single.py替换modules中的ui_main.py

2 在self.show()前加入
    widgets.sn_lineedit.setMinimumHeight(40)

3 main.py中的第718行-784行变更：

    if BOX_READY_SYMBOL in str(left_box_data):
                            plam_det.log_display(widgets, 'LEFT BOX READY!')

                            if widgets.sn_lineedit.text() != '':
                                plam_det.log_display(widgets, 'Left SN:' + widgets.sn_lineedit.text())
                                print('LEFT SN:' + widgets.sn_lineedit.text())
                                
                                global_status['left_sn'] = widgets.sn_lineedit.text()
                                global_status['channel_left_ready'] = True

                                widgets.sn_lineedit.clear()
                                widgets.sn_lineedit.setFocus()
                                
                            else:
                                plam_det.log_display(widgets, 'Left SN:NULL')
                                print('LEFT SN:NULL')
                                global_status['left_sn'] = 'NULL'
                                widgets.left_test_result_bar.setFormat('未输入SN码')
                                widgets.left_test_result_bar.setStyleSheet('QProgressBar { font-size: 30px; color: rgb(0, 0, 0); } QProgressBar::chunk { font-size: 20px; background-color: rgb(255, 255, 255); \
                                                    font-weight: bold; color: rgb(0, 0, 0);}')
                # except:
                #     plam_det.log_display(widgets, 'ERROR: LEFT BOX COM READ ERROR!')
                #     print('ERROR: LEFT BOX COM READ ERROR!')
            
            if global_status['right_box_connected'] == True:
                try:
                    if right_box_com.in_waiting:
                        right_box_data = right_box_com.readline()
                        if BOX_READY_SYMBOL in str(right_box_data):
                            plam_det.log_display(widgets, 'RIGHT BOX OPENED!')
                            if widgets.sn_lineedit.text() != '':
                                plam_det.log_display(widgets, 'Right SN:' + widgets.sn_lineedit.text())
                                print('RIGHT SN:' + widgets.sn_lineedit.text())

                                global_status['channel_right_ready'] = True
                                global_status['right_sn'] = widgets.sn_lineedit.text()

                                widgets.sn_lineedit.clear()
                                widgets.sn_lineedit.setFocus()
                                
                            else:
                                plam_det.log_display(widgets, 'Right SN:NULL')
                                print('RIGHT SN:NULL')
                                global_status['right_sn'] = 'NULL'
                                widgets.left_test_result_bar.setFormat('未输入SN码')
                                widgets.left_test_result_bar.setStyleSheet('QProgressBar { font-size: 30px; color: rgb(0, 0, 0); } QProgressBar::chunk { font-size: 20px; background-color: rgb(255, 255, 255); \
                                                    font-weight: bold; color: rgb(0, 0, 0);}')
                except:
                    plam_det.log_display(widgets, 'ERROR: RIGHT BOX COM READ ERROR!')
                    print('ERROR: RIGHT BOX COM READ ERROR!')

4 将第246行的：
        if global_status['channel_left_enable'] == True:
            widgets.left_sn_in.setFocus()
        else:
            if global_status['channel_right_enable'] == True:
                widgets.right_sn_in.setFocus()

    变更为：
        widgets.sn_lineedit.setFocus()

5 在第295行加入：
    widgets.left_data_clean.clicked.connect(self.buttonClick)
    widgets.right_data_clean.clicked.connect(self.buttonClick)

6 在第242行加入：
    if btnName == "left_data_clean":
        test_statisics_clear('left')
    if btnName == "right_data_clean":
        test_statisics_clear('right')

7 在test_statistics.py中加入
    def test_statisics_clear(widgets, channel):
        plam_det.log_display(widgets,'Test statistics clear...')
        print('Test statistics clear...')

        try:
            with open('./Config/test_statistics.json', 'r') as f:
                test_data = json.load(f)
            
            if channel == 'left':
                test_data['test_data']['left_box']['pass_count'] = '0'
                test_data['test_data']['left_box']['fail_count'] = '0'
                test_data['test_data']['left_box']['total_count'] = '0'
                test_data['test_data']['left_box']['fail_rate'] = '0'
            else:
                test_data['test_data']['right_box']['pass_count'] = '0'
                test_data['test_data']['right_box']['fail_count'] = '0'
                test_data['test_data']['right_box']['total_count'] = '0'
                test_data['test_data']['right_box']['fail_rate'] = '0'

            with open('./test/test_statistics.json', 'w') as f:
                json.dump(test_data, f, indent=4)

        except:
            plam_det.log_display(widgets,'Test data clear error!')
            print('Test data clear error!')
            accident.warnning(widgets, '统计文件清除失败', True)
            return False
        else:
            plam_det.log_display(widgets,'Test statistics clear complete!')
            print('Test statistics clear complete!')
            return True

8 将plam_det.py中第5行
        widgets.textEdit_4.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' LOG: ' + msg) 

    改为
        pass

9 将main.py中第905行的：
    global_status['channel_left_enable'] = True     ## for test
    
    屏蔽




            