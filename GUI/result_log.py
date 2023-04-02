import os
import datetime
import plam_det
import csv
from datetime import date
import accident

RESULT_LOG_TEST = False

if RESULT_LOG_TEST == True:
        leop_l = {'avg':'leop_l_avg', 'max':'leop_l_max', 'min':'leop_l_min', 'peak_to_avg':'leop_l_pta', 
                'failed':'leop_l_failed', 'tested':'leop_l_tested','state':'leop_l_state', 'valid':'leop_l_valid'}

        leop_m = {'avg':'leop_m_avg', 'max':'leop_m_max', 'min':'leop_m_min', 'peak_to_avg':'leop_m_pta',
                'failed':'leop_m_failed', 'tested':'leop_m_tested','state':'leop_m_state', 'valid':'leop_m_valid'}

        leop_h = {'avg':'leop_h_avg', 'max':'leop_h_max', 'min':'leop_h_min', 'peak_to_avg':'leop_h_pta',
                'failed':'leop_h_failed', 'tested':'leop_h_tested','state':'leop_h_state', 'valid':'leop_h_valid'}

        leop_result = {'leop_l':leop_l, 'leop_m':leop_m, 'leop_h':leop_h}
        

        leop_result['status'] = 'leop_status'

        leicd_l = {'avg_fn':'leicd_l_avg_fn', 'max_p_fn':'leicd_l_max_p_fn', 'max_n_fn':'leicd_l_max_n_fn',
                'max_dirft_rate':'leicd_l_max_dirft_rate', 'avg_drift':'leicd_l_avg_drift', 'max_drift':'leicd_l_max_drift',
                'failed':'leicd_l_failed', 'tested':'leicd_l_tested','state':'leicd_l_state', 'valid':'leicd_l_valid'}

        leicd_m = {'avg_fn':'leicd_m_avg_fn', 'max_p_fn':'leicd_m_max_p_fn', 'max_n_fn':'leicd_m_max_n_fn',
                'max_dirft_rate':'leicd_m_max_dirft_rate', 'avg_drift':'leicd_m_avg_drift', 'max_drift':'leicd_m_max_drift',
                'failed':'leicd_m_failed', 'tested':'leicd_m_tested','state':'leicd_m_state', 'valid':'leicd_m_valid'}

        leicd_h = {'avg_fn':'leicd_h_avg_fn', 'max_p_fn':'leicd_h_max_p_fn', 'max_n_fn':'leicd_h_max_n_fn',
                'max_dirft_rate':'leicd_h_max_dirft_rate', 'avg_drift':'leicd_h_avg_drift', 'max_drift':'leicd_h_max_drift',
                'failed':'leicd_h_failed', 'tested':'leicd_h_tested','state':'leicd_h_state', 'valid':'leicd_h_valid'}

        leicd_result = {'leicd_l':leicd_l, 'leicd_m':leicd_m, 'leicd_h':leicd_h}

        leicd_result['status'] = 'leicd_status'


        less_l = {'valid':'less_l_valid', 'over_fer_%':'less_l_over_fer_%', 'total_frames_counted_dut':'less_l_total_frames_counted_dut',
                'total_frames_sent_tester':'less_l_total_frames_sent_tester','state':'less_l_state'}

        less_m = {'valid':'less_m_valid', 'over_fer_%':'less_m_over_fer_%', 'total_frames_counted_dut':'less_m_total_frames_counted_dut',
                'total_frames_sent_tester':'less_m_total_frames_sent_tester','state':'less_m_state'}

        less_h = {'valid':'less_h_valid', 'over_fer_%':'less_h_over_fer_%', 'total_frames_counted_dut':'less_h_total_frames_counted_dut',
                'total_frames_sent_tester':'less_h_total_frames_sent_tester','state':'less_h_state'}

        less_result = {'less_l':less_l, 'less_m':less_m, 'less_h':less_h}

        less_result['status'] = 'less_status'



def result_txt_log(widgets, sn, start_time, end_time, during_time, leop, leicd, less, test_result):

        try:
                result_time = datetime.datetime.now().strftime("%H-%M-%S")

                if test_result == 'pass':
                        result = 'PASS'
                else:
                        result = 'FAIL'

                leop_result = leop['status']

                start_time = start_time
                end_time = end_time

                leop_l_max = leop['leop_l']['max']   
                leop_m_max = leop['leop_m']['max']
                leop_h_max = leop['leop_h']['max']

                leop_l_min = leop['leop_l']['min']
                leop_m_min = leop['leop_m']['min']
                leop_h_min = leop['leop_h']['min']

                leop_l_peak = leop['leop_l']['peak_to_avg']
                leop_m_peak = leop['leop_m']['peak_to_avg']
                leop_h_peak = leop['leop_h']['peak_to_avg']

                leop_l_avg = leop['leop_l']['avg']
                leop_m_avg = leop['leop_m']['avg']
                leop_h_avg = leop['leop_h']['avg']

                leop_l_result = leop['leop_l']['state']
                leop_m_result = leop['leop_m']['state']
                leop_h_result = leop['leop_h']['state']

                leicd_result = leicd['status']

                leicd_l_avg = leicd['leicd_l']['avg_fn']
                leicd_m_avg = leicd['leicd_m']['avg_fn']
                leicd_h_avg = leicd['leicd_h']['avg_fn']

                leicd_l_p_fn = leicd['leicd_l']['max_p_fn']
                leicd_m_p_fn = leicd['leicd_m']['max_p_fn']
                leicd_h_p_fn = leicd['leicd_h']['max_p_fn']

                leicd_l_n_fn = leicd['leicd_l']['max_n_fn']
                leicd_m_n_fn = leicd['leicd_m']['max_n_fn']
                leicd_h_n_fn = leicd['leicd_h']['max_n_fn']

                leicd_l_avg_drift = leicd['leicd_l']['avg_drift']
                leicd_m_avg_drift = leicd['leicd_m']['avg_drift']
                leicd_h_avg_drift = leicd['leicd_h']['avg_drift']

                leicd_l_drift_rate = leicd['leicd_l']['max_dirft_rate']
                leicd_m_drift_rate = leicd['leicd_m']['max_dirft_rate']
                leicd_h_drift_rate = leicd['leicd_h']['max_dirft_rate']

                leicd_l_max_drift = leicd['leicd_l']['max_drift']
                leicd_m_max_drift = leicd['leicd_m']['max_drift']
                leicd_h_max_drift = leicd['leicd_h']['max_drift']

                leicd_l_result = leicd['leicd_l']['state']
                leicd_m_result = leicd['leicd_m']['state']
                leicd_h_result = leicd['leicd_h']['state']

                less_result = less['status']

                less_l_fer = less['less_l']['over_fer_%']
                less_m_fer = less['less_m']['over_fer_%']
                less_h_fer = less['less_h']['over_fer_%']

                less_l_tx = less['less_l']['total_frames_sent_tester']
                less_m_tx = less['less_m']['total_frames_sent_tester']
                less_h_tx = less['less_h']['total_frames_sent_tester']

                less_l_rx = less['less_l']['total_frames_counted_dut']
                less_m_rx = less['less_m']['total_frames_counted_dut']
                less_h_rx = less['less_h']['total_frames_counted_dut']

                less_l_result = less['less_l']['state']
                less_m_result = less['less_m']['state']
                less_h_result = less['less_h']['state']

                today = datetime.date.today().strftime("%Y-%m-%d")

        
                if result == 'FAIL':
                        sub_dir_path = os.path.join(today, 'FAIL')
                else:
                        sub_dir_path = os.path.join(today, 'PASS')

                sub_dir_path = os.path.join("TXT", sub_dir_path)
                sub_dir_path = os.path.join("result_log", sub_dir_path)

                if not os.path.exists(sub_dir_path):
                        os.makedirs(sub_dir_path)
                        print('Directory created')
                        
                else:
                        print("Directory already exists")

                file_path = os.path.join(sub_dir_path, sn + ' ' + result_time + ' ' + result + '.txt') 
                with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(start_time + '# 正在进行测试...' + '\r')
                        f.write(start_time + '# 产品序列号   ' + sn + '\r')
                        f.write(end_time + '# 脚本运行结束' + '\r')
                        f.write('输出功率测试 >> ' + leop_result + '\r')
                        f.write('跳频关            低通道     中通道     高通道    上下限' + '\r')
                        f.write('最大功率          ' + str(leop_l_max) + '      ' + str(leop_m_max) + '      ' + str(leop_m_max) + '      <=5.0dBm' + '\r')
                        f.write('最小功率          ' + str(leop_l_min) + '      ' + str(leop_m_min) + '      ' + str(leop_m_min) + '      >=-5.0dBm' + '\r')
                        f.write('峰值功率          ' + str(leop_l_peak) + '      ' + str(leop_m_peak) + '      ' + str(leop_m_peak) + '      <=10.0dBm' + '\r')
                        f.write('平均功率          ' + str(leop_l_avg) + '      ' + str(leop_m_avg) + '      ' + str(leop_m_avg) + '      ' + '\r')
                        f.write('测试结果          ' + leop_l_result + '      ' + leop_m_result + '      ' + leop_h_result + '      ' + '\r')
                        f.write('载波频率偏移与漂移测试 >> ' + leicd_result + '\r')
                        f.write('跳频关            低通道     中通道     高通道    上下限' + '\r')
                        f.write('平均频偏          ' + str(leicd_l_avg) + '      ' + str(leicd_m_avg) + '      ' + str(leicd_h_avg) + '      ' + '\r')
                        f.write('最大频偏+ve       ' + str(leicd_l_p_fn) + '      ' + str(leicd_m_p_fn) + '      ' + str(leicd_h_p_fn) + '      <=150kHz' + '\r')
                        f.write('最大频偏-ve       ' + str(leicd_l_n_fn) + '      ' + str(leicd_m_n_fn) + '      ' + str(leicd_h_n_fn) + '      <=150kHz' + '\r')
                        f.write('频偏漂移率        ' + str(leicd_l_drift_rate) + '      ' + str(leicd_m_drift_rate) + '      ' + str(leicd_h_drift_rate) + '      <=0.5%' + '\r')
                        f.write('最大频偏漂移      ' + str(leicd_l_max_drift) + '      ' + str(leicd_m_max_drift) + '      ' + str(leicd_h_max_drift) + '      <=0.5%' + '\r')
                        f.write('平均频偏漂移      ' + str(leicd_l_avg_drift) + '      ' + str(leicd_m_avg_drift) + '      ' + str(leicd_h_avg_drift) + '      <=0.5%' + '\r')
                        f.write('测试结果          ' + leicd_l_result + '      ' + leicd_m_result + '      ' + leicd_h_result + '      ' + '\r')
                        f.write('误码率测试 >> ' + less_result + '\r')
                        f.write('跳频关            低通道     中通道     高通道    上下限' + '\r')
                        f.write('误码率            ' + str(less_l_fer) + '      ' + str(less_m_fer) + '      ' + str(less_h_fer) + '      <=1.0%' + '\r')
                        f.write('发送帧数          ' + str(less_l_tx) + '      ' + str(less_m_tx) + '      ' + str(less_h_tx) + '      ' + '\r')
                        f.write('接收帧数          ' + str(less_l_rx) + '      ' + str(less_m_rx) + '      ' + str(less_h_rx) + '      ' + '\r')
                        f.write('测试结果          ' + less_l_result + '      ' + less_m_result + '      ' + less_h_result + '      ' + '\r')
                        f.write('\r')
                        f.write('>>>>> 测试完成  ' + end_time)
                        f.write('\r')
                        f.write('>>>>> 测试耗时  ' + str(datetime.timedelta(seconds=during_time)))

                print('Write result txt log success')
                if widgets != None:
                        plam_det.log_display(widgets, 'Write result txt log success')
        
        except:
                print('Error: write result txt log failed')
                if widgets != None:
                        plam_det.log_display(widgets, 'Error: write result txt log failed')
                        accident.warnning(widgets,'TXT 文件导出失败',True)


def result_csv_log(widgets, sn, start_time, end_time, during_time, leop, leicd, less, test_result, channel):

        try:
                top_line = ['开始测试时间', 
                '测试耗时',
                '测试位置',
                '项目名称',
                '测试结果',
                '蓝牙地址',
                '输出功率-测试结果',
                '输出功率-低频-最大(dBm)',
                '输出功率-低频-最小(dBm)',
                '输出功率-低频-峰值(dBm)',
                '输出功率-低频-平均(dBm)',
                '输出功率-低频-结果',
                '输出功率-中频-最大(dBm)',
                '输出功率-中频-最小(dBm)',
                '输出功率-中频-峰值(dBm)',
                '输出功率-中频-平均(dBm)',
                '输出功率-中频-结果',
                '输出功率-高频-最大(dBm)',
                '输出功率-高频-最小(dBm)',
                '输出功率-高频-峰值(dBm)',
                '输出功率-高频-平均(dBm)',
                '输出功率-高频-结果',
                '频偏漂移-测试结果',
                '平均频偏-低频(kHz)',
                '最大+ve频偏-低频(kHz)',
                '最大-ve频偏-低频(kHz)',
                '漂移速率-低频(kHz)',
                '最大漂移-低频(kHz)',
                '平均漂移-低频(kHz)',
                '频偏漂移-低频-结果',
                '平均频偏-中频(kHz)',
                '最大+ve频偏-中频(kHz)',
                '最大-ve频偏-中频(kHz)',
                '漂移速率-中频(kHz)',
                '最大漂移-中频(kHz)',
                '平均漂移-中频(kHz)',
                '频偏漂移-中频-结果',
                '平均频偏-高频(kHz)',
                '最大+ve频偏-高频(kHz)',
                '最大-ve频偏-高频(kHz)',
                '漂移速率-高频(kHz)',
                '最大漂移-高频(kHz)',
                '平均漂移-高频(kHz)',
                '频偏漂移-高频-结果',
                '单时隙灵敏度-测试结果',
                '误码率-低频(%)',
                '误帧率-低频-结果',
                '误码率-中频(%)',
                '误帧率-中频-结果',
                '误码率-高频(%)',
                '误帧率-高频-结果']
                
                if channel == 'left':
                        pos = 'P1'
                elif channel == 'right':
                        pos = 'P2'
                
                add_line = [start_time,                 # 开始测试时间
                during_time,                        # 测试耗时
                pos,                                # 测试位置
                'TK-045',                           # 项目名称
                test_result.upper(),                # 测试结果
                sn,                                 # 蓝牙地址
                leop['status'].upper(),                     # 输出功率-测试结果
                leop['leop_l']['max'],              # 输出功率-低频-最大(dBm)
                leop['leop_l']['min'],              # 输出功率-低频-最小(dBm)
                leop['leop_l']['peak_to_avg'],      # 输出功率-低频-峰值(dBm)
                leop['leop_l']['avg'],              # 输出功率-低频-平均(dBm)
                leop['leop_l']['state'].upper(),            # 输出功率-低频-结果
                leop['leop_m']['max'],              # 输出功率-中频-最大(dBm)
                leop['leop_m']['min'],              # 输出功率-中频-最小(dBm)
                leop['leop_m']['peak_to_avg'],      # 输出功率-中频-峰值(dBm)
                leop['leop_m']['avg'],              # 输出功率-中频-平均(dBm)
                leop['leop_m']['state'].upper(),           # 输出功率-中频-结果
                leop['leop_h']['max'],              # 输出功率-高频-最大(dBm)
                leop['leop_h']['min'],              # 输出功率-高频-最小(dBm)
                leop['leop_h']['peak_to_avg'],      # 输出功率-高频-峰值(dBm)
                leop['leop_h']['avg'],              # 输出功率-高频-平均(dBm)
                leop['leop_h']['state'].upper(),            # 输出功率-高频-结果
                leicd['status'].upper(),                    # 频偏漂移-测试结果
                leicd['leicd_l']['avg_fn'],            # 平均频偏-低频(kHz)
                leicd['leicd_l']['max_p_fn'],            # 最大+ve频偏-低频(kHz)
                leicd['leicd_l']['max_n_fn'],            # 最大-ve频偏-低频(kHz)
                leicd['leicd_l']['max_dirft_rate'],     # 漂移速率-低频(kHz)
                leicd['leicd_l']['max_drift'],      # 最大漂移-低频(kHz)
                leicd['leicd_l']['avg_drift'],      # 平均漂移-低频(kHz)
                leicd['leicd_l']['state'].upper(),          # 频偏漂移-低频-结果
                leicd['leicd_m']['avg_fn'],            # 平均频偏-中频(kHz)
                leicd['leicd_m']['max_p_fn'],            # 最大+ve频偏-中频(kHz)
                leicd['leicd_m']['max_n_fn'],            # 最大-ve频偏-中频(kHz)
                leicd['leicd_m']['max_dirft_rate'],     # 漂移速率-中频(kHz)
                leicd['leicd_m']['max_drift'],      # 最大漂移-中频(kHz)
                leicd['leicd_m']['avg_drift'],      # 平均漂移-中频(kHz)
                leicd['leicd_m']['state'].upper(),          # 频偏漂移-中频-结果
                leicd['leicd_h']['avg_fn'],            # 平均频偏-高频(kHz)
                leicd['leicd_h']['max_p_fn'],            # 最大+ve频偏-高频(kHz)
                leicd['leicd_h']['max_n_fn'],            # 最大-ve频偏-高频(kHz)
                leicd['leicd_h']['max_dirft_rate'],     # 漂移速率-高频(kHz)
                leicd['leicd_h']['max_drift'],      # 最大漂移-高频(kHz)
                leicd['leicd_h']['avg_drift'],      # 平均漂移-高频(kHz)
                leicd['leicd_h']['state'].upper(),          # 频偏漂移-高频-结果
                less['status'].upper(),                     # 信号灵敏度-测试结果
                less['less_l']['over_fer_%'],       # 误码率-低频(%)
                less['less_l']['state'].upper(),            # 误码率-低频-结果
                less['less_m']['over_fer_%'],       # 误帧率-中频(%)
                less['less_m']['state'].upper(),            # 误帧率-中频-结果
                less['less_h']['over_fer_%'],       # 误帧率-高频(%)
                less['less_h']['state'].upper()            # 误帧率-高频-结果
                ]

                today = date.today().strftime("%Y-%m-%d")
                csv_path = os.path.join("result_log//CSV", f"{today}.csv")
                 # 检查是否存在以今天日期命名的 csv 文件
                if os.path.exists(csv_path):
                        # 如果文件存在，则以追加模式打开文件，续写内容
                        with open(csv_path, 'a', newline='') as csvfile:
                                writer = csv.writer(csvfile)
                                # 在文件最后一行添加新的一行数据
                                writer.writerow(add_line)
                        print('File exists, appending data...')
                else:   
                        # 如果文件不存在，则以写模式打开文件，创建新的 csv 文件
                        with open(csv_path, 'w', newline='') as csvfile:
                                writer = csv.writer(csvfile)
                                # 添加表头
                                writer.writerow(top_line)
                                # 添加第一行数据
                                writer.writerow(add_line)
                        print('File does not exist, creating file...')

                print('Write result csv log success')
                if widgets != None:
                        plam_det.log_display(widgets, 'Write result csv log success')

        except:
                print('Error: write result csv log failed')
                if widgets != None:
                        plam_det.log_display(widgets, 'Error: write result csv log failed')
                        accident.warnning(widgets,'CSV 文件导出失败',True)


def output(widgets, sn, start_time, end_time, during_time, leop, leicd, less, test_result, channel):

        result_txt_log(widgets, sn, start_time, end_time, during_time, leop, leicd, less, test_result)
        result_csv_log(widgets, sn, start_time, end_time, during_time, leop, leicd, less, test_result, channel)


if RESULT_LOG_TEST == True:
        widgets = None
        result_txt_log(widgets, 'sn', "14:37:22", "14:37:32", 9, leop_result, leicd_result, less_result, 'fail')
        result_csv_log(widgets, 'sn', "14:37:22", "14:37:32", 9, leop_result, leicd_result, less_result, 'fail', 'right')