


def tr_test(a):
    a("tr_test============")


def setting_data_display(widgets,setting_data):

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


def leop_result_display(global_status, widgets, leop_l, leop_m, leop_h, status):

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

        widgets.left_leop_result.setText(status)
        if status == 'PASS':
            widgets.left_leop_result.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
            widgets.label_2.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        else:
            widgets.left_leop_result.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
            widgets.label_2.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")

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

        widgets.right_leop_result.setText(status)
        if status == 'PASS':
            widgets.right_leop_result.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
            widgets.label_149.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        else:
            widgets.right_leop_result.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
            widgets.label_149.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
        


def leicd_result_display(global_status,widgets,leicd_l, leicd_m, leicd_h, status):

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

        # widgets.left_leicd_l_avg_fn.setText(str(leicd_l['avg_fn']))
        # widgets.left_leicd_m_avg_fn.setText(str(leicd_m['avg_fn']))
        # widgets.left_leicd_h_avg_fn.setText(str(leicd_h['avg_fn']))

        # widgets.left_leicd_l_max_p_fn.setText(str(leicd_l['max_p_fn']))
        # widgets.left_leicd_m_max_p_fn.setText(str(leicd_m['max_p_fn']))
        # widgets.left_leicd_h_max_p_fn.setText(str(leicd_h['max_p_fn']))

        # widgets.left_leicd_l_max_n_fn.setText(str(leicd_l['max_n_fn']))
        # widgets.left_leicd_m_max_n_fn.setText(str(leicd_m['max_n_fn']))
        # widgets.left_leicd_h_max_n_fn.setText(str(leicd_h['max_n_fn']))

        # widgets.left_leicd_l_max_dirft_rate.setText(str(leicd_l['max_dirft_rate']))
        # widgets.left_leicd_m_max_dirft_rate.setText(str(leicd_m['max_dirft_rate']))
        # widgets.left_leicd_h_max_dirft_rate.setText(str(leicd_h['max_dirft_rate']))

        # widgets.left_leicd_l_max_dirft.setText(str(leicd_l['max_drift']))
        # widgets.left_leicd_m_max_dirft.setText(str(leicd_m['max_drift']))
        # widgets.left_leicd_h_max_dirft.setText(str(leicd_h['max_drift']))

        # widgets.left_leicd_l_avg_dirft.setText(str(leicd_l['avg_drift']))
        # widgets.left_leicd_m_avg_dirft.setText(str(leicd_m['avg_drift']))
        # widgets.left_leicd_h_avg_dirft.setText(str(leicd_h['avg_drift']))

        widgets.left_leicd_l_state.setText(str(leicd_l['state']))
        widgets.left_leicd_m_state.setText(str(leicd_m['state']))
        widgets.left_leicd_h_state.setText(str(leicd_h['state']))

        widgets.left_leicd_l_avg_fn.setText(str(int(float(leicd_l['avg_fn'])) / 1000))
        widgets.left_leicd_m_avg_fn.setText(str(int(float(leicd_m['avg_fn'])) / 1000))
        widgets.left_leicd_h_avg_fn.setText(str(int(float(leicd_h['avg_fn'])) / 1000))

        widgets.left_leicd_l_max_p_fn.setText(str(int(float(leicd_l['max_p_fn'])) / 1000))
        widgets.left_leicd_m_max_p_fn.setText(str(int(float(leicd_m['max_p_fn'])) / 1000))
        widgets.left_leicd_h_max_p_fn.setText(str(int(float(leicd_h['max_p_fn'])) / 1000))

        widgets.left_leicd_l_max_n_fn.setText(str(int(float(leicd_l['max_n_fn'])) / 1000))
        widgets.left_leicd_m_max_n_fn.setText(str(int(float(leicd_m['max_n_fn'])) / 1000))
        widgets.left_leicd_h_max_n_fn.setText(str(int(float(leicd_h['max_n_fn'])) / 1000))

        widgets.left_leicd_l_max_dirft_rate.setText(str(int(float(leicd_l['max_dirft_rate'])) / 1000))
        widgets.left_leicd_m_max_dirft_rate.setText(str(int(float(leicd_m['max_dirft_rate'])) / 1000))
        widgets.left_leicd_h_max_dirft_rate.setText(str(int(float(leicd_h['max_dirft_rate'])) / 1000))

        widgets.left_leicd_l_max_dirft.setText(str(int(float(leicd_l['max_drift'])) / 1000))
        widgets.left_leicd_m_max_dirft.setText(str(int(float(leicd_m['max_drift'])) / 1000))
        widgets.left_leicd_h_max_dirft.setText(str(int(float(leicd_h['max_drift'])) / 1000))

        widgets.left_leicd_l_avg_dirft.setText(str(int(float(leicd_l['avg_drift'])) / 1000))
        widgets.left_leicd_m_avg_dirft.setText(str(int(float(leicd_m['avg_drift'])) / 1000))
        widgets.left_leicd_h_avg_dirft.setText(str(int(float(leicd_h['avg_drift'])) / 1000))


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

        if status == 'PASS':
            widgets.left_leicd_result.setText('PASS')
            widgets.left_leicd_result.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
            widgets.label_62.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        else:
            widgets.left_leicd_result.setText('FAIL')
            widgets.left_leicd_result.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
            widgets.label_62.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")

    elif global_status['finished_channel'] == 'right':
            
            # widgets.right_leicd_l_avg_fn.setText(str(leicd_l['avg_fn']))
            # widgets.right_leicd_m_avg_fn.setText(str(leicd_m['avg_fn']))
            # widgets.right_leicd_h_avg_fn.setText(str(leicd_h['avg_fn']))
    
            # widgets.right_leicd_l_max_p_fn.setText(str(leicd_l['max_p_fn']))
            # widgets.right_leicd_m_max_p_fn.setText(str(leicd_m['max_p_fn']))
            # widgets.right_leicd_h_max_p_fn.setText(str(leicd_h['max_p_fn']))
    
            # widgets.right_leicd_l_max_n_fn.setText(str(leicd_l['max_n_fn']))
            # widgets.right_leicd_m_max_n_fn.setText(str(leicd_m['max_n_fn']))
            # widgets.right_leicd_h_max_n_fn.setText(str(leicd_h['max_n_fn']))
    
            # widgets.right_leicd_l_max_dirft_rate.setText(str(leicd_l['max_dirft_rate']))
            # widgets.right_leicd_m_max_dirft_rate.setText(str(leicd_m['max_dirft_rate']))
            # widgets.right_leicd_h_max_dirft_rate.setText(str(leicd_h['max_dirft_rate']))
    
            # widgets.right_leicd_l_max_dirft.setText(str(leicd_l['max_drift']))
            # widgets.right_leicd_m_max_dirft.setText(str(leicd_m['max_drift']))
            # widgets.right_leicd_h_max_dirft.setText(str(leicd_h['max_drift']))
    
            # widgets.right_leicd_l_avg_dirft.setText(str(leicd_l['avg_drift']))
            # widgets.right_leicd_m_avg_dirft.setText(str(leicd_m['avg_drift']))
            # widgets.right_leicd_h_avg_dirft.setText(str(leicd_h['avg_drift']))
    
            widgets.right_leicd_l_state.setText(str(leicd_l['state']))
            widgets.right_leicd_m_state.setText(str(leicd_m['state']))
            widgets.right_leicd_h_state.setText(str(leicd_h['state']))

            widgets.right_leicd_l_avg_fn.setText(str(int(float(leicd_l['avg_fn'])) / 1000))
            widgets.right_leicd_m_avg_fn.setText(str(int(float(leicd_m['avg_fn'])) / 1000))
            widgets.right_leicd_h_avg_fn.setText(str(int(float(leicd_h['avg_fn'])) / 1000))

            widgets.right_leicd_l_max_p_fn.setText(str(int(float(leicd_l['max_p_fn'])) / 1000))
            widgets.right_leicd_m_max_p_fn.setText(str(int(float(leicd_m['max_p_fn'])) / 1000))
            widgets.right_leicd_h_max_p_fn.setText(str(int(float(leicd_h['max_p_fn'])) / 1000))

            widgets.right_leicd_l_max_n_fn.setText(str(int(float(leicd_l['max_n_fn'])) / 1000))
            widgets.right_leicd_m_max_n_fn.setText(str(int(float(leicd_m['max_n_fn'])) / 1000))
            widgets.right_leicd_h_max_n_fn.setText(str(int(float(leicd_h['max_n_fn'])) / 1000))

            widgets.right_leicd_l_max_dirft_rate.setText(str(int(float(leicd_l['max_dirft_rate'])) / 1000))
            widgets.right_leicd_m_max_dirft_rate.setText(str(int(float(leicd_m['max_dirft_rate'])) / 1000))
            widgets.right_leicd_h_max_dirft_rate.setText(str(int(float(leicd_h['max_dirft_rate'])) / 1000))

            widgets.right_leicd_l_max_dirft.setText(str(int(float(leicd_l['max_drift'])) / 1000))
            widgets.right_leicd_m_max_dirft.setText(str(int(float(leicd_m['max_drift'])) / 1000))
            widgets.right_leicd_h_max_dirft.setText(str(int(float(leicd_h['max_drift'])) / 1000))

            widgets.right_leicd_l_avg_dirft.setText(str(int(float(leicd_l['avg_drift'])) / 1000))
            widgets.right_leicd_m_avg_dirft.setText(str(int(float(leicd_m['avg_drift'])) / 1000))
            widgets.right_leicd_h_avg_dirft.setText(str(int(float(leicd_h['avg_drift'])) / 1000))
    
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

            if status == 'PASS':
                widgets.right_leicd_result.setText('PASS')
                widgets.right_leicd_result.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
                widgets.label_182.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
            else:
                widgets.right_leicd_result.setText('FAIL')
                widgets.right_leicd_result.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
                widgets.label_182.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")



def less_result_display(global_status, widgets, less_l,less_m,less_h, status):


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

        if status == 'PASS':
            widgets.left_less_result.setText('PASS')
            widgets.left_less_result.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
            widgets.left_less_label.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
        else:
            widgets.left_less_result.setText('FAIL')
            widgets.left_less_result.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
            widgets.left_less_label.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")

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
            
            if status == 'PASS':
                widgets.right_less_result.setText('PASS')
                widgets.right_less_result.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
                widgets.label_220.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
            else:
                widgets.right_less_result.setText('FAIL')
                widgets.right_less_result.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
                widgets.label_220.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")


def result_time_display(global_status,widgets, point, during):
    if global_status['finished_channel'] == 'left':
        widgets.left_test_time_point.setText(str(point))
        widgets.left_test_time_during.setText(str(during))
    else:
        widgets.right_test_time_point.setText(str(point))
        widgets.right_test_time_during.setText(str(during))
    



def result_display_reset(widgets,channel):
    
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

        widgets.left_less_result.setText('NULL')
        widgets.left_less_result.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")

        widgets.left_leicd_result.setText('NULL')
        widgets.left_leicd_result.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")

        widgets.left_leop_result.setText('NULL')
        widgets.left_leop_result.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")

        widgets.label_62.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")
        widgets.left_less_label.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")
        widgets.label_2.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")
        

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

            widgets.right_leop_result.setText('NULL')
            widgets.right_leop_result.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")

            widgets.right_leicd_result.setText('NULL')
            widgets.right_leicd_result.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")

            widgets.right_less_result.setText('NULL')
            widgets.right_less_result.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")

            widgets.label_149.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")
            widgets.label_182.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")
            widgets.label_220.setStyleSheet("color: white; background-color: rgb(40, 44, 52);")

            


def test_total_cnt_display(widgets, channel, total_cnt):
    if channel == 'left':
        widgets.left_test_count.setText(str(total_cnt))
    elif channel == 'right':
        widgets.right_test_count.setText(str(total_cnt))

def test_fail_count_display(widgets, channel, fail_cnt):
    if channel == 'left':
        widgets.left_fail_count.setText(str(fail_cnt))
    elif channel == 'right':
        widgets.right_fail_count.setText(str(fail_cnt))

def test_pass_count_display(widgets, channel, pass_cnt):
    if channel == 'left':
        widgets.left_pass_count.setText(str(pass_cnt))
    elif channel == 'right':
        widgets.right_pass_count.setText(str(pass_cnt))

def test_fail_rate_display(widgets, channel, fail_rate):
    if channel == 'left':
        widgets.left_fail_rate.setText(str(fail_rate))
    elif channel == 'right':
        widgets.right_fail_rate.setText(str(fail_rate))




