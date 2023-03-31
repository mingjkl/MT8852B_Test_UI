
import os
import datetime

# 14:37:22# 正在进行测试...
# 14:37:23# 产品序列号   A4C138A55AB2
# 14:37:31# 脚本运行结束
# 输出功率测试 >> PASS
# 跳频关            低通道     中通道     高通道    上下限
# 最大功率          1.48      2.16      0.21      <=5.0dBm
# 最小功率          1.48      2.15      0.21      >=-5.0dBm
# 峰值功率          0.11      0.15      0.13      <=10.0dBm
# 平均功率          1.48      2.16      0.21      
# 测试结果          PASS      PASS      PASS      
# 载波频率偏移与漂移测试 >> PASS
# 跳频关            低通道     中通道     高通道    上下限
# 平均频偏          24.3      24.8      25.3      
# 最大频偏+ve       25.1      25.8      26.3      <=150kHz
# 最大频偏-ve       22.6      23.8      24.2      <=150kHz
# 漂移速率          -2.8      2.15      -2.18     <19kHz/50us
# 最大漂移          -3        -3        2         <50kHz
# 平均漂移          0         0         0         
# 测试结果          PASS      PASS      PASS      
# 单时隙灵敏度测试,发射功率(dBm):-85.0  >> FAIL
# 跳频关            低通道     中通道     高通道    上下限    
# 误帧率            83.000    100.000   78.200    <=30.80
# 发送包数          500       500       500       
# 接收包数          85        0         109       
# 测试结果          FAIL      FAIL      FAIL      

# >>>>> 测试完成  14:37:31
# >>>>> 测试耗时  0:00:09

sn = "A4C138A55BD2"
result_time = datetime.datetime.now().strftime("%H-%M-%S")
result = "PASS"
leop_result = "PASS"

start_time = "14:37:22"
end_time = "14:37:31"

leop_l_max = 1.48
leop_m_max = 2.16
leop_h_max = 0.21

leop_l_min = 1.48
leop_m_min = 2.15
leop_h_min = 0.21

leop_l_peak = 0.11
leop_m_peak = 0.15
leop_h_peak = 0.13

leop_l_avg = 1.48
leop_m_avg = 2.16
leop_h_avg = 0.21

leop_l_result = "PASS"
leop_m_result = "PASS"
leop_h_result = "PASS"

leicd_result = "PASS"
leicd_l_avg = 24.3
leicd_m_avg = 24.8
leicd_h_avg = 25.3

leicd_l_p_fn = 25.1
leicd_m_p_fn = 25.8
leicd_h_p_fn = 26.3

leicd_l_n_fn = 22.6
leicd_m_n_fn = 23.8
leicd_h_n_fn = 24.2

leicd_l_drift_rate = -2.8
leicd_m_drift_rate = 2.15
leicd_h_drift_rate = -2.18

leicd_l_max_drift = -3
leicd_m_max_drift = -3
leicd_h_max_drift = 2

leicd_l_avg_drift = 0
leicd_m_avg_drift = 0
leicd_h_avg_drift = 0

leicd_l_result = "PASS"
leicd_m_result = "PASS"
leicd_h_result = "PASS"

less_result = "FAIL"
less_l_fer = 83.000
less_m_fer = 100.000
less_h_fer = 78.200

less_l_tx = 500
less_m_tx = 500
less_h_tx = 500

less_l_rx = 85
less_m_rx = 0
less_h_rx = 109

less_l_result = "FAIL"
less_m_result = "FAIL"
less_h_result = "FAIL"

during_time = 9


today = datetime.date.today().strftime("%Y-%m-%d")

sub_dir_path = os.path.join("result_log", today)

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


