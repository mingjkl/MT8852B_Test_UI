import plam_det
import json
import tr_dis
import accident
import serial

from PySide6.QtWidgets import QMessageBox

def com_display(widgets, list):

    list_len = len(list)
    for i in list:
        widgets.left_box_com.addItem(i.name)
        widgets.right_box_com.addItem(i.name)
        widgets.left_bbtc_com.addItem(i.name)
        widgets.right_bbtc_com.addItem(i.name)
        widgets.signal_ctrl_com.addItem(i.name)


## Loading the setting.json file
def setting_load(widgets, global_status):
     # SETTING RELOAD
        plam_det.log_display(widgets,'Setting loading...')
        print('Setting loading...')
        try:
            with open('./Config/setting.json', 'r') as f:
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

            global_status['left_fixed_offset'] = setting_data['left_fixed_offset']
            global_status['right_fixed_offset'] = setting_data['right_fixed_offset']


        except:
            print('setting.json load error')
            plam_det.log_display(widgets,'Setting load error')
            widgets.setting_status.setStyleSheet("color: black; background-color: rgb(250, 128, 114);")
            widgets.setting_status.setText('配置文件加载失败')
            global_status['setting_loaded'] = False
            accident.warnning(widgets,'配置文件加载失败',True)
            return {}
        else:
            widgets.setting_status.setStyleSheet("color: black; background-color: rgb(0, 255, 127);")
            widgets.setting_status.setText('配置文件加载完成')
            print('setting.json load success')
            plam_det.log_display(widgets,'Setting load success')
            global_status['setting_loaded'] = True
            tr_dis.setting_data_display(widgets, setting_data)
            return setting_data
        

## Save setting to setting.json
def setting_save(widgets):
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

    try:
        with open('./Config/setting.json', 'w') as f:
            json.dump(setting_data, f, indent=1)
        print("Setting success")

        warningbox = QMessageBox()
        warningbox.setIcon(QMessageBox.Information)
        warningbox.setText('Save successful!')
        warningbox.setWindowTitle("Success")
        warningbox.setStandardButtons(QMessageBox.Ok)
        warningbox.exec()


    except:
        print("Setting fail")

        warningbox = QMessageBox()
        warningbox.setIcon(QMessageBox.Warning)
        warningbox.setText('Save Failed')
        warningbox.setWindowTitle("WARNNING")
        warningbox.setStandardButtons(QMessageBox.Ok)
        warningbox.exec()


## Test setting disable
def setting_disable(widgets):
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



