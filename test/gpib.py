
import pyvisa
import time

def print_log(log):
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), log)

def MT8852B_Write(order):
    device.write(order)
    print_log("MT8852B Write: " + order)


def MT8852B_Query(order):
    res = device.query(order)

    print_log("MT8852B Query: " + order)
    print_log("MT8852B Result: " + res)

    return res

def MT8852B_Connect_Cheak():
    ID = MT8852B_Query('*IDN?')

    if "MT8852B" in ID:
        print_log("MT8852B ID: " + ID)
        return True
    else:
        print_log("MT8852B Lost")
        return False
    


start_time = time.time()
    


rm = pyvisa.ResourceManager()   # 打开资源管理器
rm_list = rm.list_resources()   # 获取设备列表
print('LOG: device list:',rm_list)

device = rm.open_resource(rm_list[0])   # 打开设备
MT8852B_Connect_Cheak()

# MT8852B_Write('OPMD SCRIPT,SCPTSEL 10')       # 选择脚本3
# MT8852B_Write('*CLS')
# # Cheak_MT8852B_Connect()

# MT8852B_Write('SYSCFG AUTH,STATE,OFF')    # 关闭认证
# MT8852B_Write('OPMD SCRIPT')         # 打开脚本
# MT8852B_Write('SCRIPT 10')        # 选择脚本10
# MT8852B_Write('TXPWR 10,-60')    # 设置功率
# MT8852B_Write('SCPTTSTGP 10,STDTSTS,OFF')   # 关闭标准测试
# MT8852B_Write('SCPTTSTGP 10,EDRTSTS,OFF')   # 关闭EDR测试
# MT8852B_Write('SCPTTSTGP 10,BLETSTS,OFF')    # 关闭BLE测试
# MT8852B_Write('PATHOFF 10,FIXED')    # 设置路径为固定
# MT8852B_Write('FIXEDOFF 10,-23')   # 设置固定偏移
# MT8852B_Write('SYSCFG CONFIG,LKTIMO,10')   # 设置锁定超时时间
# MT8852B_Write('SYSCFG EUTSRCE,BLE2WIRE')  # 设置EUT源为BLE2WIRE
# MT8852B_Write('SYSCFG EUTR232,115200')   # 设置EUT串口波特率
# MT8852B_Write('SYSCFG CONFIG,RANGE,AUTO')    # 设置功率范围为自动

# time.sleep(5);

# MT8852B_Write('*CLS')

# MT8852B_Write('RUN')    # 运行脚本

# # esr = device.query('*ESR?')    # 查询错误状态寄存器
# # print('ESR:',esr)

# ins = MT8852B_Write('*INS?')   # 查询脚本运行状态


# ## 一直在重复esr和ins的查询，直到ins为0?

# MT8852B_Query('ORESULT TEST,0,LEOP')     # 查询测试结果
# MT8852B_Query('XRESULT LEOP,HOPOFFL')    # 清除测试结果 //quert result?
# MT8852B_Query('XRESULT LEOP,HOPOFFM')   # 清除测试结果
# MT8852B_Query('XRESULT LEOP,HOPOFFH')   # 清除测试结果

# MT8852B_Query('ORESULT TEST,0,LEICD')   # 查询测试结果
# MT8852B_Query('XRESULT LEICD,HOPOFFL')  # 清除测试结果
# MT8852B_Query('XRESULT LEICD,HOPOFFM')  # 清除测试结果
# MT8852B_Query('XRESULT LEICD,HOPOFFH')  # 清除测试结果

# MT8852B_Query('ORESULT TEST,0,LESS')    # 查询测试结果
# MT8852B_Query('XRESULT LESS,HOPOFFL')   # 清除测试结果  
# MT8852B_Query('XRESULT LESS,HOPOFFM')   # 清除测试结果
# MT8852B_Query('XRESULT LESS,HOPOFFH')   # 清除测试结果

# MT8852B_Query('ORESULT TEST,0,LEMI')   # 查询测试结果
# MT8852B_Query('ORESULT TEST,0,LEMP')   # 查询测试结果
# MT8852B_Query('ORESULT TEST,0,LEPRI')   # 查询测试结果

# MT8852B_Write('*CLS')
# MT8852B_Connect_Cheak()

# MT8852B_Query('*ETF?')  # 查询测试结果
# MT8852B_Query('*EETF?')  # 查询测试结果

# MT8852B_Write('DISCONNECT')   # 断开连接
# MT8852B_Write('ERRLST')  # 查询错误列表
# MT8852B_Write('*CLS')

# MT8852B_Write('OPMD SCRIPT,SCPTSEL 10')
# MT8852B_Write('*CLS')
# MT8852B_Connect_Cheak()  # 检查连接
# MT8852B_Write('*CLS')

# MT8852B_Write('ERRLST')  # 查询错误列表
# MT8852B_Write('*CLS')
# MT8852B_Write('DISCONNECT')   # 断开连接
# MT8852B_Write('SYSCFG AUTH,STATE,OFF')    # 关闭认证
# MT8852B_Write('OPMD SCRIPT')     # 打开脚本
# MT8852B_Write('SCRIPT 10')      # 选择脚本10
# MT8852B_Write('TXPWR 10,-60')   # 设置功率
# MT8852B_Write('SCPTTSTGP 10,STDTSTS,OFF')   # 关闭标准测试
# MT8852B_Write('SCPTTSTGR 10,EDRTSTS,OFF')   # 关闭EDR测试
# MT8852B_Write('SCPTTSTGR 10,BLETSTS,ON')    # 关闭BLE测试
# MT8852B_Write('PATHOFF 10,FIXED')    # 设置路径为固定
# MT8852B_Write('FIXEDOFF 10,-23')   # 设置固定偏移
# MT8852B_Write('SYSCFG CONFIG,LKTIMO,10')   # 设置锁定超时时间
# MT8852B_Write('SYSCFG EUTSRCE,BLE2WIRE')  # 设置EUT源为BLE2WIRE
# MT8852B_Write('SYSCFG EUTR232,115200')   # 设置EUT串口波特率
# MT8852B_Write('SYSCFG CONFIG,RANGE,AUTO')    # 设置功率范围为自动
# MT8852B_Write('*CLS')
# MT8852B_Write('RUN')    # 运行脚本

# time.sleep(5);

# MT8852B_Query('*ESR?')  # 查询错误状态寄存器
# MT8852B_Connect_Cheak()  # 检查连接
# ## 延时0.5s
# MT8852B_Query('*ESR?')  # 查询错误状态寄存器
# MT8852B_Connect_Cheak()  # 检查连接
# ## 延时0.8s
# MT8852B_Query('*ESR?')  # 查询错误状态寄存器
# MT8852B_Connect_Cheak()  # 检查连接
# ## 延时0.8s
# MT8852B_Query('*ESR?')  # 查询错误状态寄存器
# MT8852B_Connect_Cheak()  # 检查连接

# MT8852B_Query('ORESULT TEST,0,LEOP')     # 查询测试结果
# MT8852B_Query('XRESULT LEOP,HOPOFFL')    # 清除测试结果 //quert result?
# MT8852B_Query('XRESULT LEOP,HOPOFFM')   # 清除测试结果
# MT8852B_Query('XRESULT LEOP,HOPOFFH')   # 清除测试结果

# MT8852B_Query('ORESULT TEST,0,LEICD')   # 查询测试结果
# MT8852B_Query('XRESULT LEICD,HOPOFFL')  # 清除测试结果
# MT8852B_Query('XRESULT LEICD,HOPOFFM')  # 清除测试结果
# MT8852B_Query('XRESULT LEICD,HOPOFFH')  # 清除测试结果

# MT8852B_Query('ORESULT TEST,0,LESS')    # 查询测试结果
# MT8852B_Query('XRESULT LESS,HOPOFFL')   # 清除测试结果
# MT8852B_Query('XRESULT LESS,HOPOFFM')   # 清除测试结果
# MT8852B_Query('XRESULT LESS,HOPOFFH')   # 清除测试结果

# MT8852B_Query('ORESULT TEST,0,LEMI')   # 查询测试结果
# MT8852B_Query('ORESULT TEST,0,LEMP')   # 查询测试结果
# MT8852B_Query('ORESULT TEST,0,LEPRI')   # 查询测试结果
# MT8852B_Write('*CLS')
# MT8852B_Connect_Cheak()
# MT8852B_Query('*ETF?')  # 查询测试结果
# MT8852B_Query('*EETF?')  # 查询测试结果
# MT8852B_Write('ERRLST')  # 查询错误列表
# MT8852B_Write('DISCONNECT')   # 断开连接



MT8852B_Write('*CLS')

MT8852B_Write('OPMD SCRIPT');  # 打开脚本
MT8852B_Write('SCPTSEL 10');    # 选择脚本10

opc = MT8852B_Query('*OPC?')   # 查询操作完成
if opc == '1':
    print_log('LOG: Select Script 10 Success')
else:
    print_log('LOG: Select Script 10 Fail')

MT8852B_Write('ULPDUTTSTEND')   # 清除测试结果 //?

MT8852B_Write('SYSCFG EUTSRCE,BLE2WIRE')  # 设置EUT源为BLE2WIRE
MT8852B_Write('SYSCFG EUTR232,115200')   # 设置EUT串口波特率
MT8852B_Write('SYSCFG CONFIG,RANGE,AUTO')    # 设置功率范围为自动

MT8852B_Write('SCPTSEL 10')   # 选择脚本10
MT8852B_Write('CLS')
MT8852B_Write('OPMD SCRIPT')     # 打开脚本
MT8852B_Write('SCPTSEL 10')      # 选择脚本10
opc = MT8852B_Query('*OPC?')
if opc == '1':
    print_log('LOG: Select Script 10 Success')
else:
    print_log('LOG: Select Script 10 Fail')

MT8852B_Write("SCPTTSTGR 10,STDTSTS,OFF")   # 关闭标准测试
MT8852B_Write("SCPTTSTGR 10,EDRTSTS,OFF")   # 关闭EDR测试
MT8852B_Write("SCPTTSTGR 10,BLETSTS,ON")   # 开启BLE测试

## =============== debug ===============

## leop test setting
# MT8852B_Write("OPMD SCRIPT")     # 打开脚本
MT8852B_Write("LEOPCFG 10,LFREQSEL,ON")  # 开启低频测试
MT8852B_Write("LEOPCFG 10,MFREQSEL,ON")  # 开启中频测试
MT8852B_Write("LEOPCFG 10,HFREQSEL,ON")  # 开启高频测试

MT8852B_Write("LEOPCFG 10,LTXFREQ,FREQ,2402MHZ")  # 设置低频发送频率
MT8852B_Write("LEOPCFG 10,MTXFREQ,FREQ,2440MHZ")  # 设置中频发送频率
MT8852B_Write("LEOPCFG 10,HTXFREQ,FREQ,2480MHZ")  # 设置高频发送频率

MT8852B_Write("LEOPCFG 10,NUMPKTS,10")

# MT8852B_Query("OPTSTATUS?") # 查询测试状态
# MT8852B_Query("SCPTSEL?")   # 查询脚本选择

MT8852B_Write("LEOPCFG 10, AVGMXLIM,10DBM") # 设置最大平均功率
MT8852B_Write("LEOPCFG 10, AVGMNLIM,-20DBM") # 设置最小平均功率
MT8852B_Write("LEOPCFG 10, PEAKLIM,3DBM") # 设置最大功率

MT8852B_Write("SCPTCFG 10,LEOP,ON")   # 开启LEOP测试


## leicd test setting
MT8852B_Write("LEICDCFG 10,LFREQSEL,ON")  # 开启低频测试
MT8852B_Write("LEICDCFG 10,MFREQSEL,ON")  # 开启中频测试
MT8852B_Write("LEICDCFG 10,HFREQSEL,ON")  # 开启高频测试

MT8852B_Write("LEICDCFG 10,LTXFREQ,FREQ,2402MHZ")  # 设置低频发送频率
MT8852B_Write("LEICDCFG 10,MTXFREQ,FREQ,2440MHZ")  # 设置中频发送频率
MT8852B_Write("LEICDCFG 10,HTXFREQ,FREQ,2480MHZ")  # 设置高频发送频率

MT8852B_Write("LEICDCFG 10,NUMPKTS,10")

MT8852B_Write("LEICDCFG 10,MXPOSLIM,150KHZ")   # 设置最大频偏
MT8852B_Write("LEICDCFG 10,MXNEGLIM,150KHZ")   # 设置最小频偏
MT8852B_Write("LEICDCFG 10,DFTBLERATE,20KHZ")   # 设置DFT测试速率
MT8852B_Write("LEICDCFG 10,DFTBLELIM,50KHZ")   # 设置DFT测试速率
MT8852B_Write("SCPTEUTCFG 10,LEICD,ON")   # 开启LEICD测试

## less test setting
MT8852B_Write("LESSCFG 10,DIRTYTX,ON")   # 开启脏发射测试
MT8852B_Write("OPMD SCRIPT")     # 打开脚本
MT8852B_Write("LESSCFG 10,TXPWR,-70")   # 开启脏发射测试



## less test setting



## =============== debug ===============

MT8852B_Write("RUN")    # 运行脚本
# device.set_visa_attribute(VI_ATTR_TMO_VALUE, 12000)  # 设置超时时间
opc = MT8852B_Query('*OPC?')   # 查询操作完成
if opc == '1':
    print_log('LOG: Select Script 10 Success')
else:
    print_log('LOG: Select Script 10 Fail')

# device.set_visa_attribute(VI_ATTR_TMO_VALUE, 20000)  # 设置超时时间
MT8852B_Query('*ESR?')   # 查询错误状态寄存器

## while
MT8852B_Query('*INS?')   # 查询仪器状态
## end while

ins = MT8852B_Query('*INS?')
print_log('LOG: Wait for Script 10 Result')
while int(ins) != 46:
    ins = device.query('*INS?')   # 查询仪器状态
    time.sleep(1)
print_log('LOG: Script 10 Run Success')

# device.set_visa_attribute(VI_ATTR_TMO_VALUE, 3000)  # 设置超时时间

MT8852B_Write('OPMD SCRIPT')     # 打开脚本
MT8852B_Query('ERRLST') # 查询错误列表
MT8852B_Query('*ESR?')   # 查询错误状态寄存器

opt = MT8852B_Query('OPTSTATUS?')  # 查询测试结果
if '15' in opt:
    print_log('LOG: AFH (Adaptive frequency hopping) support')
if '17' in opt:
    print_log('LOG: Allows IQ data output for EDR measurements')
if '25' in opt:
    print_log('LOG: EDR Measurements support')
if '27' in opt:
    print_log('LOG: BLE Measurements support')
if '29' in opt:
    print_log('LOG:  BLE Measurements only')
if '34' in opt:
    print_log('LOG: BLE Data Length Extension support')
if '35' in opt:
    print_log('LOG:  BLE 2LE support')
if '36' in opt:
    print_log('LOG:  BLE BLR support')
if '37' in opt:
    print_log('LOG: BLE AoA/AoD support')
if '70' in opt:
    print_log('LOG: Platform Enhanced option')


## ================================================================================================
## ================================== LEOP->BLE Output power ======================================
## ================================================================================================


##======================================= LOW FREQUENCY ============================================

MT8852B_Query('SCPTSEL?')
MT8852B_Query('OPTSTATUS?')

##  LEOP->BLE Output power, HOPOFFL->Hopping OFF, low frequency
res = MT8852B_Query('XRESULT LEOP,HOPOFFL') 
res_items = res.split(',')

## BLE Output power result
leop_l = {'avg':res_items[3], 'max':res_items[4], 'min':res_items[5], 'peak_to_avg':res_items[6], 
        'failed':res_items[7], 'tested':res_items[8],'state':res_items[9], 'valid':res_items[2]}

##======================================= MID FREQUENCY ============================================

MT8852B_Query('SCPTSEL?')
MT8852B_Query('OPTSTATUS?')

##  LEOP->BLE Output power, HOPOFFL->Hopping OFF, mid frequency
res = MT8852B_Query('XRESULT LEOP,HOPOFFM') 
res_items = res.split(',')

## BLE Output power result
leop_m = {'avg':res_items[3], 'max':res_items[4], 'min':res_items[5], 'peak_to_avg':res_items[6], 
        'failed':res_items[7], 'tested':res_items[8],'state':res_items[9], 'valid':res_items[2]}


##======================================= HIGH FREQUENCY ============================================

MT8852B_Query('SCPTSEL?')
MT8852B_Query('OPTSTATUS?')

##  LEOP->BLE Output power, HOPOFFL->Hopping OFF, high frequency
res = MT8852B_Query('XRESULT LEOP,HOPOFFH') 
res_items = res.split(',')

## BLE Output power result
leop_h = {'avg':res_items[3], 'max':res_items[4], 'min':res_items[5], 'peak_to_avg':res_items[6], 
        'failed':res_items[7], 'tested':res_items[8],'state':res_items[9], 'valid':res_items[2]}

## ================================================================================================
## ================= LEICD->BLE Carrier Frequency Offset and Drift Test Results ===================
## ================================================================================================

##======================================= LOW FREQUENCY ============================================

MT8852B_Query('SCPTSEL?')
MT8852B_Query('OPTSTATUS?')
MT8852B_Query('*IDN?')

## BLE Carrier Frequency Offset and Drift Test Results
## HOPOFFL->Hopping OFF, low frequency
res = MT8852B_Query('XRESULT LEICD,HOPOFFL,1')  
res_items = res.split(',')
leicd_l = {'valid':res_items[2], 'avg_fn':res_items[3], 'max_p_fn':res_items[4], 'max_n_fn':res_items[5],
         'max_dirft_rate':res_items[6], 'avg_drift':res_items[7], 'max_drift':res_items[8], 'failed':res_items[9],
         'tested':res_items[10], 'state':res_items[11]}

##======================================= MID FREQUENCY ============================================

MT8852B_Query('SCPTSEL?')
MT8852B_Query('OPTSTATUS?')
MT8852B_Query('*IDN?')

## BLE Carrier Frequency Offset and Drift Test Results
## HOPOFFL->Hopping OFF, mid frequency
res = MT8852B_Query('XRESULT LEICD,HOPOFFM,1')  
res_items = res.split(',')
leicd_m = {'valid':res_items[2], 'avg_fn':res_items[3], 'max_p_fn':res_items[4], 'max_n_fn':res_items[5],
         'max_dirft_rate':res_items[6], 'avg_drift':res_items[7], 'max_drift':res_items[8], 'failed':res_items[9],
         'tested':res_items[10], 'state':res_items[11]}


##======================================= HIGH FREQUENCY ============================================

MT8852B_Query('SCPTSEL?')
MT8852B_Query('OPTSTATUS?')
MT8852B_Query('*IDN?')

## BLE Carrier Frequency Offset and Drift Test Results
## HOPOFFL->Hopping OFF, high frequency
res = MT8852B_Query('XRESULT LEICD,HOPOFFH,1')  
res_items = res.split(',')
leicd_h = {'valid':res_items[2], 'avg_fn':res_items[3], 'max_p_fn':res_items[4], 'max_n_fn':res_items[5],
         'max_dirft_rate':res_items[6], 'avg_drift':res_items[7], 'max_drift':res_items[8], 'failed':res_items[9],
         'tested':res_items[10], 'state':res_items[11]}

## ================================================================================================
## ==================== LEMI->BLE Modulation Characteristics Test Results ========================
## ================================================================================================

##======================================= LOW FREQUENCY ============================================

MT8852B_Query('SCPTSEL?')
MT8852B_Query('OPTSTATUS?')
MT8852B_Query('*IDN?')

## BLE Modulation Characteristics Test Results
## HOPOFFL->Hopping OFF, low frequency

res = MT8852B_Query('XRESULT LEMI,HOPOFFL')  
res_items = res.split(',')
lemi_l = {'valid':res_items[2], 'delta_f1_max_hz':res_items[3], 'delta_f1_ave_hz':res_items[4], 'delta_f2_max_hz':res_items[5],
         'delta_f2_avg_hz':res_items[6], 'delta_f2/f1_avg':res_items[7], 'delta_f2_max_failed_limit':res_items[8], 'delta_f2_max_count':res_items[9],
         'failed':res_items[10], 'tested':res_items[11], 'state':res_items[12], 'delta_f2_%_pass':res_items[13]}

##======================================= MID FREQUENCY ============================================

MT8852B_Query('SCPTSEL?')
MT8852B_Query('OPTSTATUS?')
MT8852B_Query('*IDN?')

## BLE Modulation Characteristics Test Results
## HOPOFFL->Hopping OFF, mid frequency

res = MT8852B_Query('XRESULT LEMI,HOPOFFM')  
res_items = res.split(',')
lemi_m = {'valid':res_items[2], 'delta_f1_max_hz':res_items[3], 'delta_f1_ave_hz':res_items[4], 'delta_f2_max_hz':res_items[5],
         'delta_f2_avg_hz':res_items[6], 'delta_f2/f1_avg':res_items[7], 'delta_f2_max_failed_limit':res_items[8], 'delta_f2_max_count':res_items[9],
         'failed':res_items[10], 'tested':res_items[11], 'state':res_items[12], 'delta_f2_%_pass':res_items[13]}

##======================================= HIGH FREQUENCY ============================================

MT8852B_Query('SCPTSEL?')
MT8852B_Query('OPTSTATUS?')
MT8852B_Query('*IDN?')

## BLE Modulation Characteristics Test Results
## HOPOFFL->Hopping OFF, high frequency

res = MT8852B_Query('XRESULT LEMI,HOPOFFH')  
res_items = res.split(',')
lemi_h = {'valid':res_items[2], 'delta_f1_max_hz':res_items[3], 'delta_f1_ave_hz':res_items[4], 'delta_f2_max_hz':res_items[5],
         'delta_f2_avg_hz':res_items[6], 'delta_f2/f1_avg':res_items[7], 'delta_f2_max_failed_limit':res_items[8], 'delta_f2_max_count':res_items[9],
         'failed':res_items[10], 'tested':res_items[11], 'state':res_items[12], 'delta_f2_%_pass':res_items[13]}


## ================================================================================================
## ======================== LESS->BLE Receiver Sensitivity Test Results ===========================
## ================================================================================================

##======================================= LOW FREQUENCY ============================================

MT8852B_Query('SCPTSEL?')
MT8852B_Query('OPTSTATUS?')
MT8852B_Query('*IDN?')

## BLE Receiver Sensitivity Test Results
## HOPOFFL->Hopping OFF, low frequency

res = MT8852B_Query('XRESULT LESS,HOPOFFL')  
res_items = res.split(',')
less_l = {'valid':res_items[2], 'over_fer_%':res_items[3], 'total_frames_counted_dut':res_items[4], 'total_frames_sent_tester':res_items[5],
         'state':res_items[6]}

##======================================= MID FREQUENCY ============================================

MT8852B_Query('SCPTSEL?')
MT8852B_Query('OPTSTATUS?')
MT8852B_Query('*IDN?')

## BLE Receiver Sensitivity Test Results
## HOPOFFL->Hopping OFF, mid frequency

res = MT8852B_Query('XRESULT LESS,HOPOFFM')  
res_items = res.split(',')
less_m = {'valid':res_items[2], 'over_fer_%':res_items[3], 'total_frames_counted_dut':res_items[4], 'total_frames_sent_tester':res_items[5],
         'state':res_items[6]}

##======================================= HIGH FREQUENCY ============================================

MT8852B_Query('SCPTSEL?')
MT8852B_Query('OPTSTATUS?')
MT8852B_Query('*IDN?')

## BLE Receiver Sensitivity Test Results
## HOPOFFL->Hopping OFF, high frequency

res = MT8852B_Query('XRESULT LESS,HOPOFFH')  
res_items = res.split(',')
less_h = {'valid':res_items[2], 'over_fer_%':res_items[3], 'total_frames_counted_dut':res_items[4], 'total_frames_sent_tester':res_items[5],
         'state':res_items[6]}


## ================================================================================================
## ======================== LEMP->BLE Maximum Input Signal Level Test Results =====================
## ================================================================================================

##======================================= LOW FREQUENCY ============================================

MT8852B_Query('SCPTSEL?')
MT8852B_Query('OPTSTATUS?')
MT8852B_Query('*IDN?')

## BLE Maximum Input Signal Level Test Results
## HOPOFFL->Hopping OFF, low frequency

res = MT8852B_Query('XRESULT LEMP,HOPOFFL')  
res_items = res.split(',')
lemp_l = {'valid':res_items[2], 'overall_fer_%':res_items[3], 'total_frames_count_dut':res_items[4], 'total_frames_sent_tester':res_items[5], 
        'state':res_items[6]}

##======================================= MID FREQUENCY ============================================

MT8852B_Query('SCPTSEL?')
MT8852B_Query('OPTSTATUS?')
MT8852B_Query('*IDN?')

## BLE Maximum Input Signal Level Test Results
## HOPOFFL->Hopping OFF, mid frequency

res = MT8852B_Query('XRESULT LEMP,HOPOFFM')  
res_items = res.split(',')
lemp_m = {'valid':res_items[2], 'overall_fer_%':res_items[3], 'total_frames_count_dut':res_items[4], 'total_frames_sent_tester':res_items[5], 
        'state':res_items[6]}

##======================================= HIGH FREQUENCY ============================================

MT8852B_Query('SCPTSEL?')
MT8852B_Query('OPTSTATUS?')
MT8852B_Query('*IDN?')

## BLE Maximum Input Signal Level Test Results
## HOPOFFL->Hopping OFF, high frequency

res = MT8852B_Query('XRESULT LEMP,HOPOFFH')  
res_items = res.split(',')
lemp_h = {'valid':res_items[2], 'overall_fer_%':res_items[3], 'total_frames_count_dut':res_items[4], 'total_frames_sent_tester':res_items[5], 
        'state':res_items[6]}


MT8852B_Query('SCPTSEL?')
MT8852B_Query('OPTSTATUS?')
MT8852B_Query('*IDN?')


## ================================================================================================
## ===================================== Result LOG  ==============================================
## ================================================================================================

##======================================= LEOP Result ============================================

leop_pass_cnt = 0

if "PASS" in leop_l['state']:
    leop_pass_cnt += 1
    leop_l['state'] = 'PASS'
else:
    leop_l['state'] = 'FAIL'

if "PASS" in leop_m['state']:
    leop_pass_cnt += 1
    leop_m['state'] = 'PASS'
else:
    leop_m['state'] = 'FAIL'

if "PASS" in leop_h['state']:
    leop_pass_cnt += 1
    leop_h['state'] = 'PASS'
else:
    leop_h['state'] = 'FAIL'


if leop_pass_cnt == 3:
    leop_pass = 'PASS'  
else:
    leop_pass = 'FAIL'

print('===================================================================')
print('输出功率测试结果：',leop_pass)
print('================= 低通道 ==== 中通道 ==== 高通道 =====================')
print('最大功率：         ', leop_l['max'], '      ',leop_m['max'],'      ',leop_h['max'])
print('平均功率：         ', leop_l['avg'], '      ',leop_m['avg'],'      ',leop_h['avg'])
print('最小功率：         ', leop_l['min'], '      ',leop_m['min'],'      ',leop_h['min'])
print('峰值功率：         ', leop_l['peak_to_avg'], '      ',leop_m['peak_to_avg'],'      ',leop_h['peak_to_avg'])
print('测试结果：         ', leop_l['state'], '      ',leop_m['state'],'      ',leop_h['state'])

leop_l.clear()
leop_m.clear()
leop_h.clear()
leop_pass = '0'
leop_pass_cnt = 0

## ================================================================================================

##======================================= LEICD Result ============================================

leicd_pass_cnt = 0

if "PASS" in leicd_l['state']:
    leicd_pass_cnt += 1
    leicd_l['state'] = 'PASS'
else:
    leicd_l['state'] = 'FAIL'

if "PASS" in leicd_m['state']:
    leicd_pass_cnt += 1
    leicd_m['state'] = 'PASS'
else:
    leicd_m['state'] = 'FAIL'

if "PASS" in leicd_h['state']:
    leicd_pass_cnt += 1
    leicd_h['state'] = 'PASS'
else:
    leicd_h['state'] = 'FAIL'

if leicd_pass_cnt == 3:
    leicd_pass = 'PASS'
else:
    leicd_pass = 'FAIL'

print('===================================================================')
print('载波频率偏移和漂移测试：',leicd_pass)
print('================= 低通道 ==== 中通道 ==== 高通道 =====================')
print('平均频偏：         ', leicd_l['avg_fn'], '      ',leicd_m['avg_fn'],'      ',leicd_h['avg_fn'])
print('最大频偏+ve：      ', leicd_l['max_p_fn'], '      ',leicd_m['max_p_fn'],'      ',leicd_h['max_p_fn'])
print('最大频偏-ve：      ', leicd_l['max_n_fn'], '      ',leicd_m['max_n_fn'],'      ',leicd_h['max_n_fn'])
print('漂移速率：         ', leicd_l['max_dirft_rate'], '      ',leicd_m['max_dirft_rate'],'      ',leicd_h['max_dirft_rate'])
print('最大漂移：         ', leicd_l['max_drift'], '      ',leicd_m['max_drift'],'      ',leicd_h['max_drift'])
print('平均漂移：         ', leicd_l['avg_drift'], '      ',leicd_m['avg_drift'],'      ',leicd_h['avg_drift'])
print('测试结果：         ', leicd_l['state'], '      ',leicd_m['state'],'      ',leicd_h['state'])

leicd_l.clear()
leicd_m.clear()
leicd_h.clear()
leicd_pass = '0'
leicd_pass_cnt = 0

## ================================================================================================
##======================================= LESS Result ============================================

less_pass_cnt = 0
if "PASS" in less_l['state']:
    less_pass_cnt += 1
    less_l['state'] = 'PASS'
else:
    less_l['state'] = 'FAIL'

if "PASS" in less_m['state']:
    less_pass_cnt += 1
    less_m['state'] = 'PASS'
else:
    less_m['state'] = 'FAIL'

if "PASS" in less_h['state']:
    less_pass_cnt += 1
    less_h['state'] = 'PASS'
else:
    less_h['state'] = 'FAIL'

if less_pass_cnt == 3:
    less_pass = 'PASS'
else:
    less_pass = 'FAIL'

print('===================================================================')
print('灵敏度测试(发射功率 -85dBm)：',less_pass)
print('================= 低通道 ==== 中通道 ==== 高通道 =====================')
print('误帧率：           ', less_l['over_fer_%'], '      ',less_m['over_fer_%'],'      ',less_h['over_fer_%'])
print('发送包数：         ', less_l['total_frames_sent_tester'], '      ',
      less_m['total_frames_sent_tester'],'      ',less_h['total_frames_sent_tester'])
print('接收包数：         ', less_l['total_frames_counted_dut'], '      ',
        less_m['total_frames_counted_dut'],'      ',less_h['total_frames_counted_dut'])
print('测试结果：         ', less_l['state'], '      ',less_m['state'],'      ',less_h['state'])

less_l.clear()
less_m.clear()
less_h.clear()
less_pass = '0'
less_pass_cnt = 0

## ================================================================================================


end_time = time.time()

print('spend time:',end_time - start_time)

