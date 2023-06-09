import pyvisa
import time
import accident

import plam_det

device = None

def print_log(widgets,msg):
    plam_det.log_display(widgets, msg)
    print("LOG: " + msg)

def get_id():
    try:
        ID = device.query('*IDN?')
        return ID
    except:
        return 'NULL'

def connect_check(widgets, device, global_status):
    
    try:
        ID = device.query('*IDN?')
        if "MT8852B" in ID:
            print_log(widgets, "MT8852B ID: " + ID)
            print_log(widgets, "MT8852B Connected")
            global_status['mt8852b_connected'] = True
            widgets.MT8852_ID.setText(ID)
            widgets.MT8852_status_label.setText("已连接")
            return True
        else:
            global_status['mt8852b_connected'] = False
            print_log(widgets, "MT8852B Lost")
            widgets.MT8852_ID.setText("NULL")
            widgets.MT8852_status_label.setText("未连接")
            return False
        
    except:
        global_status['mt8852b_connected'] = False
        print_log(widgets, "MT8852B Lost")
        accident.warnning(widgets,'MT8852B 连接失败',True)
        return False
    

def MT8852B_Write(widgets,device, order):
    device.write(order)
    print_log(widgets, "MT8852B Write: " + order)

def MT8852B_Query(widgets,device, order):

    try:
        res = device.query(order)

        print_log(widgets,"MT8852B Query: " + order)
        print_log(widgets,"MT8852B Result: " + res)
    except:
        accident.warnning(widgets,'MT8852B 查询失败',True)
        res = 'NULL'

    return res

def get_gpib_list():
    try:
        rm = pyvisa.ResourceManager()   # 打开资源管理器
        rm_list = rm.list_resources()   # 获取设备列表
        return rm_list
    except:
        print('get_gpib_list failed')
        return None

def connect(widgets, global_status):
    
    try:
        rm = pyvisa.ResourceManager()   # 打开资源管理器
        rm_list = rm.list_resources()   # 获取设备列表
        print(rm_list)

        for i in rm_list:
            print_log(widgets,'device: '+i)
            if 'GPIB0::27::INSTR' in i:             ## for test
                device = rm.open_resource(i)
                connect_check(widgets, device, global_status)
                print_log(widgets,'GPIB init success')
                return device
            else:
                 print_log(widgets,'GPIB init failed')

        return None
        
    except:
        print_log(widgets,'mt8852b connect failed')
        accident.warnning(widgets,'MT8852B 连接失败',True)
        return None
    

def params_init(widgets, device):
    
    # MT8852B_Write('SYSCFG AUTH,STATE,OFF')    # 关闭认证
    # # MT8852B_Write('OPMD SCRIPT')         # 打开脚本
    # # MT8852B_Write('SCRIPT 10')        # 选择脚本10
    # MT8852B_Write('TXPWR 10,-60')    # 设置功率
    # # MT8852B_Write('SCPTTSTGP 10,STDTSTS,OFF')   # 关闭标准测试
    # # MT8852B_Write('SCPTTSTGP 10,EDRTSTS,OFF')   # 关闭EDR测试
    # # MT8852B_Write('SCPTTSTGP 10,BLETSTS,OFF')    # 关闭BLE测试
    # MT8852B_Write('PATHOFF 10,FIXED')    # 设置路径为固定
    # MT8852B_Write('FIXEDOFF 10,-23')   # 设置固定偏移
    # MT8852B_Write('SYSCFG CONFIG,LKTIMO,10')   # 设置锁定超时时间
    # MT8852B_Write('SYSCFG EUTSRCE,BLE2WIRE')  # 设置EUT源为BLE2WIRE
    # MT8852B_Write('SYSCFG EUTR232,115200')   # 设置EUT串口波特率
    # MT8852B_Write('SYSCFG CONFIG,RANGE,AUTO')    # 设置功率范围为自动

    ## =============== debug ===============

    ## leop test setting
    # MT8852B_Write("OPMD SCRIPT")     # 打开脚本
    MT8852B_Write(widgets,device,"LEOPCFG 10,LFREQSEL,ON")  # 开启低频测试
    MT8852B_Write(widgets,device,"LEOPCFG 10,MFREQSEL,ON")  # 开启中频测试
    MT8852B_Write(widgets,device,"LEOPCFG 10,HFREQSEL,ON")  # 开启高频测试

    MT8852B_Write(widgets,device,"LEOPCFG 10,LTXFREQ,FREQ,2402MHZ")  # 设置低频发送频率
    MT8852B_Write(widgets,device,"LEOPCFG 10,MTXFREQ,FREQ,2440MHZ")  # 设置中频发送频率
    MT8852B_Write(widgets,device,"LEOPCFG 10,HTXFREQ,FREQ,2480MHZ")  # 设置高频发送频率

    MT8852B_Write(widgets,device,"LEOPCFG 10,NUMPKTS,10")

    # MT8852B_Query("OPTSTATUS?") # 查询测试状态
    # MT8852B_Query("SCPTSEL?")   # 查询脚本选择

    MT8852B_Write(widgets,device,"LEOPCFG 10, AVGMXLIM,5DBM") # 设置最大平均功率
    MT8852B_Write(widgets,device,"LEOPCFG 10, AVGMNLIM,-5DBM") # 设置最小平均功率
    MT8852B_Write(widgets,device,"LEOPCFG 10, PEAKLIM,10DBM") # 设置最大功率

    MT8852B_Write(widgets,device,"SCPTCFG 10,LEOP,ON")   # 开启LEOP测试


    ## leicd test setting
    MT8852B_Write(widgets,device,"LEICDCFG 10,LFREQSEL,ON")  # 开启低频测试
    MT8852B_Write(widgets,device,"LEICDCFG 10,MFREQSEL,ON")  # 开启中频测试
    MT8852B_Write(widgets,device,"LEICDCFG 10,HFREQSEL,ON")  # 开启高频测试

    MT8852B_Write(widgets,device,"LEICDCFG 10,LTXFREQ,FREQ,2402MHZ")  # 设置低频发送频率
    MT8852B_Write(widgets,device,"LEICDCFG 10,MTXFREQ,FREQ,2440MHZ")  # 设置中频发送频率
    MT8852B_Write(widgets,device,"LEICDCFG 10,HTXFREQ,FREQ,2480MHZ")  # 设置高频发送频率

    MT8852B_Write(widgets,device,"LEICDCFG 10,NUMPKTS,10")

    MT8852B_Write(widgets,device,"LEICDCFG 10,MXPOSLIM,150KHZ")   # 设置最大频偏
    MT8852B_Write(widgets,device,"LEICDCFG 10,MXNEGLIM,150KHZ")   # 设置最小频偏
    MT8852B_Write(widgets,device,"LEICDCFG 10,DFTBLERATE,19KHZ")   # 设置DFT测试速率
    MT8852B_Write(widgets,device,"LEICDCFG 10,DFTBLELIM,50KHZ")   # 设置DFT测试速率
    MT8852B_Write(widgets,device,"SCPTCFG 10,LEICD,ON")   # 开启LEICD测试

    ## less test setting

    MT8852B_Write(widgets,device,"LESSCFG 10,LFREQSEL,ON")  # 开启低频测试
    MT8852B_Write(widgets,device,"LESSCFG 10,MFREQSEL,ON")  # 开启中频测试
    MT8852B_Write(widgets,device,"LESSCFG 10,HFREQSEL,ON")  # 开启高频测试

    MT8852B_Write(widgets,device,"LESSCFG 10,DIRTYTX,ON")   # OFF脏发射测试
    MT8852B_Write(widgets,device,"OPMD SCRIPT")     # 打开脚本
    MT8852B_Write(widgets,device,"LESSCFG 10,TXPWR,-85")   # 开启脏发射测试

    MT8852B_Write(widgets,device,"LESSCFG 10,FERLIM,30.8") 
    MT8852B_Write(widgets,device,"LESSCFG 10,NUMPKTS,500") 

    MT8852B_Write(widgets,device,"SCPTCFG 10,LEICD,ON")

    

    # print('for test')
    ## less test setting
    ## =============== debug ===============


def init(widgets,device, global_status):

    if global_status['mt8852b_connected'] == True:

        MT8852B_Write(widgets,device,'*CLS')

        MT8852B_Write(widgets,device,'OPMD SCRIPT');  # 打开脚本
        MT8852B_Write(widgets,device,'SCPTSEL 10');    # 选择脚本10

        opc = MT8852B_Query(widgets, device, '*OPC?')   # 查询操作完成
        if opc == '1':
            print_log(widgets,'LOG: Select Script 10 Success')
        else:
            print_log(widgets,'LOG: Select Script 10 Fail')

        MT8852B_Write(widgets,device,'ULPDUTTSTEND')   # 清除测试结果 //?

        MT8852B_Write(widgets,device,'SYSCFG EUTSRCE,BLE2WIRE')  # 设置EUT源为BLE2WIRE
        MT8852B_Write(widgets,device,'SYSCFG EUTR232,115200')   # 设置EUT串口波特率
        MT8852B_Write(widgets,device,'SYSCFG CONFIG,RANGE,AUTO')    # 设置功率范围为自动

        MT8852B_Write(widgets,device,'SCPTSEL 10')   # 选择脚本10
        MT8852B_Write(widgets,device,'CLS')
        MT8852B_Write(widgets,device,'OPMD SCRIPT')     # 打开脚本
        MT8852B_Write(widgets,device,'SCPTSEL 10')      # 选择脚本10
        opc = MT8852B_Query(widgets,device,'*OPC?')
        if opc == '1':
            print_log(widgets,'LOG: Select Script 10 Success')
        else:
            print_log(widgets,'LOG: Select Script 10 Fail')

        MT8852B_Write(widgets,device,'TXPWR 10,-60')   # 设置功率        ## for debug
        MT8852B_Write(widgets,device,'PATHOFF 10,FIXED')    # 设置路径为固定     ## for debug

        if global_status['finished_channel'] == 'left':
            fix_offset = 'FIXEDOFF 10,' + global_status['left_fixed_offset'] + 'DB'
        else:
            fix_offset = 'FIXEDOFF 10,' + global_status['right_fixed_offset'] + 'DB'

        # MT8852B_Write(widgets,device,'FIXEDOFF 10,-23DB')   # 设置固定偏移     ## for debug
        MT8852B_Write(widgets,device,fix_offset)   # 设置固定偏移     ## for debug

        print(fix_offset)

        params_init(widgets,device)

        MT8852B_Write(widgets,device,"SCPTTSTGR 10,STDTSTS,OFF")   # 关闭标准测试
        MT8852B_Write(widgets,device,"SCPTTSTGR 10,EDRTSTS,OFF")   # 关闭EDR测试
        MT8852B_Write(widgets,device,"SCPTTSTGR 10,BLETSTS,ON")   # 开启BLE测试

        
        MT8852B_Write(widgets,device,"RUN")    # 运行脚本
        # device.set_visa_attribute(VI_ATTR_TMO_VALUE, 12000)  # 设置超时时间
        opc = MT8852B_Query(widgets,device,'*OPC?')   # 查询操作完成
        if opc == '1':
            print_log(widgets,'LOG: Select Script 10 Success')
        else:
            print_log(widgets,'LOG: Select Script 10 Fail')

        # device.set_visa_attribute(VI_ATTR_TMO_VALUE, 20000)  # 设置超时时间
        MT8852B_Query(widgets,device,'*ESR?')   # 查询错误状态寄存器

        ## while
        MT8852B_Query(widgets,device,'*INS?')   # 查询仪器状态
        ## end while
        ins = 0
        ins = MT8852B_Query(widgets,device,'*INS?')
        print_log(widgets,'LOG: Wait for Script 10 Result')


        # if global_status['finished_channel'] == 'left':
        #     bar_text = global_status['left_sn'] + '  测试中...'
        # else:
        #     bar_text = global_status['right_sn'] + '  测试中...'

        # widgets.left_test_result_bar.setValue(100)
        # widgets.left_test_result_bar.setFormat(bar_text)
        # widgets.left_test_result_bar.setStyleSheet('QProgressBar { font-size: 30px; color: rgb(0, 0, 0); } QProgressBar::chunk { font-size: 20px; background-color: rgb(255, 255, 0); \
        #                                     font-weight: bold; color: rgb(0, 0, 0);}')
        
        # for i in range(1,10):
        #     time.sleep(0.5)
        #     widgets.left_test_result_bar.setValue(i * 10)

        timeout = False
        while_time = 0


        # while int(ins) != 46:
        #     ins = device.query('*INS?')   # 查询仪器状态
        #     time.sleep(1)
        #     while_time = while_time + 1
        #     # if global_status['finished_channel'] == 'left':
        #     #     widgets.left_test_result_bar.setValue(10 + while_time * 6)
        #     # else:
        #     #     widgets.right_test_result_bar.setValue(10 + while_time * 6)

        #     if while_time > 14:
        #         # if global_status['finished_channel'] == 'left':
        #         #     widgets.left_test_result_bar.setValue(95)
        #         # else:
        #         #     widgets.right_test_result_bar.setValue(95)

        #         print_log(widgets,'LOG: Script 10 Run Timeout')
        #         accident.warnning(widgets,'MT8852B 测试超时',True)
        #         timeout = True
        #         break

        #     if global_status['finished_channel'] == 'left':
        #         widgets.left_test_result_bar.setValue(100)
        #     else:
        #         widgets.right_test_result_bar.setValue(100)
            
        #     time.sleep(1)

        ## ==================== for test =========================

        for wait_time_cnt in range(1, 20):
            ins = device.query('*INS?')   # 查询仪器状态
            if int(ins) == 46:
                if global_status['finished_channel'] == 'left':
                    widgets.left_test_result_bar.setValue(100)
                else:
                    widgets.right_test_result_bar.setValue(100)
                timeout = False
                break
            else:
                if wait_time_cnt >= 19:
                    timeout = True
                time.sleep(1)
            

        ## ===================== for test ========================


        if timeout == False:
            print_log(widgets,'LOG: Script 10 Run Success')

            # device.set_visa_attribute(VI_ATTR_TMO_VALUE, 3000)  # 设置超时时间

            MT8852B_Write(widgets,device,'OPMD SCRIPT')     # 打开脚本
            MT8852B_Query(widgets,device,'ERRLST') # 查询错误列表
            MT8852B_Query(widgets,device,'*ESR?')   # 查询错误状态寄存器

            opt = MT8852B_Query(widgets, device, 'OPTSTATUS?')  # 查询测试结果
            if '15' in opt:
                print_log(widgets,'LOG: AFH (Adaptive frequency hopping) support')
            if '17' in opt:
                print_log(widgets,'LOG: Allows IQ data output for EDR measurements')
            if '25' in opt:
                print_log(widgets,'LOG: EDR Measurements support')
            if '27' in opt:
                print_log(widgets,'LOG: BLE Measurements support')
            if '29' in opt:
                print_log(widgets,'LOG:  BLE Measurements only')
            if '34' in opt:
                print_log(widgets,'LOG: BLE Data Length Extension support')
            if '35' in opt:
                print_log(widgets,'LOG:  BLE 2LE support')
            if '36' in opt:
                print_log(widgets,'LOG:  BLE BLR support')
            if '37' in opt:
                print_log(widgets,'LOG: BLE AoA/AoD support')
            if '70' in opt:
                print_log(widgets,'LOG: Platform Enhanced option')
            
            return True
        else:
            return False

    else:
        print_log(widgets,'MT8852B init failed')

        return False


def pass_to_pass(state):
    if 'PASS' in state:
        return 'PASS'
    else:
        return 'FAIL'


def leop_result_read(widgets,device):

    
    ## ================================================================================================
    ## ================================== LEOP->BLE Output power ======================================
    ## ================================================================================================

    ##======================================= LOW FREQUENCY ============================================

    MT8852B_Query(widgets,device,'SCPTSEL?')
    MT8852B_Query(widgets,device,'OPTSTATUS?')

    ##  LEOP->BLE Output power, HOPOFFL->Hopping OFF, low frequency
    res = MT8852B_Query(widgets,device,'XRESULT LEOP,HOPOFFL') 
    res_items = res.split(',')

    ## BLE Output power result
    leop_l = {'avg':res_items[3], 'max':res_items[4], 'min':res_items[5], 'peak_to_avg':res_items[6], 
            'failed':res_items[7], 'tested':res_items[8],'state':res_items[9], 'valid':res_items[2]}

    leop_l['state'] = pass_to_pass(leop_l['state'])

    ##======================================= MID FREQUENCY ============================================

    MT8852B_Query(widgets,device,'SCPTSEL?')
    MT8852B_Query(widgets,device,'OPTSTATUS?')

    ##  LEOP->BLE Output power, HOPOFFL->Hopping OFF, mid frequency
    res = MT8852B_Query(widgets,device,'XRESULT LEOP,HOPOFFM') 
    res_items = res.split(',')

    ## BLE Output power result
    leop_m = {'avg':res_items[3], 'max':res_items[4], 'min':res_items[5], 'peak_to_avg':res_items[6], 
            'failed':res_items[7], 'tested':res_items[8],'state':res_items[9], 'valid':res_items[2]}


    ##======================================= HIGH FREQUENCY ============================================

    MT8852B_Query(widgets,device,'SCPTSEL?')
    MT8852B_Query(widgets,device,'OPTSTATUS?')

    ##  LEOP->BLE Output power, HOPOFFL->Hopping OFF, high frequency
    res = MT8852B_Query(widgets,device,'XRESULT LEOP,HOPOFFH') 
    res_items = res.split(',')

    ## BLE Output power result
    leop_h = {'avg':res_items[3], 'max':res_items[4], 'min':res_items[5], 'peak_to_avg':res_items[6], 
            'failed':res_items[7], 'tested':res_items[8],'state':res_items[9], 'valid':res_items[2]}
    
    leop_result = {}
    leop_result['leop_l'] = leop_l
    leop_result['leop_m'] = leop_m
    leop_result['leop_h'] = leop_h

    print_log(widgets,str(leop_result))

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

    leop_result['status'] = leop_pass

    print('===================================================================')
    print('输出功率测试结果：',leop_pass)
    print('================= 低通道 ==== 中通道 ==== 高通道 =====================')
    print('最大功率：         ', leop_l['max'], '      ',leop_m['max'],'      ',leop_h['max'])
    print('平均功率：         ', leop_l['avg'], '      ',leop_m['avg'],'      ',leop_h['avg'])
    print('最小功率：         ', leop_l['min'], '      ',leop_m['min'],'      ',leop_h['min'])
    print('峰值功率：         ', leop_l['peak_to_avg'], '      ',leop_m['peak_to_avg'],'      ',leop_h['peak_to_avg'])
    print('测试结果：         ', leop_l['state'], '      ',leop_m['state'],'      ',leop_h['state'])

    # MT8852B_Query(widgets,device,'XRESULT LESS,HOPOFFL')   # 清除测试结果  
    # MT8852B_Query(widgets,device,'XRESULT LESS,HOPOFFM')   # 清除测试结果
    # MT8852B_Query(widgets,device,'XRESULT LESS,HOPOFFH')   # 清除测试结果


    return leop_result


    



## ================================================================================================
## ================= LEICD->BLE Carrier Frequency Offset and Drift Test Results ===================
## ================================================================================================

def leicd_result_read(widgets,device):

    ##======================================= LOW FREQUENCY ============================================

    MT8852B_Query(widgets,device,'SCPTSEL?')
    MT8852B_Query(widgets,device,'OPTSTATUS?')
    MT8852B_Query(widgets,device,'*IDN?')

    ## BLE Carrier Frequency Offset and Drift Test Results
    ## HOPOFFL->Hopping OFF, low frequency
    res = MT8852B_Query(widgets,device,'XRESULT LEICD,HOPOFFL,1')  
    res_items = res.split(',')
    leicd_l = {'valid':res_items[2], 'avg_fn':res_items[3], 'max_p_fn':res_items[4], 'max_n_fn':res_items[5],
            'max_dirft_rate':res_items[6], 'avg_drift':res_items[7], 'max_drift':res_items[8], 'failed':res_items[9],
            'tested':res_items[10], 'state':res_items[11]}

    ##======================================= MID FREQUENCY ============================================

    MT8852B_Query(widgets,device,'SCPTSEL?')
    MT8852B_Query(widgets,device,'OPTSTATUS?')
    MT8852B_Query(widgets,device,'*IDN?')

    ## BLE Carrier Frequency Offset and Drift Test Results
    ## HOPOFFL->Hopping OFF, mid frequency
    res = MT8852B_Query(widgets,device,'XRESULT LEICD,HOPOFFM,1')  
    res_items = res.split(',')
    leicd_m = {'valid':res_items[2], 'avg_fn':res_items[3], 'max_p_fn':res_items[4], 'max_n_fn':res_items[5],
            'max_dirft_rate':res_items[6], 'avg_drift':res_items[7], 'max_drift':res_items[8], 'failed':res_items[9],
            'tested':res_items[10], 'state':res_items[11]}


    ##======================================= HIGH FREQUENCY ============================================

    MT8852B_Query(widgets,device,'SCPTSEL?')
    MT8852B_Query(widgets,device,'OPTSTATUS?')
    MT8852B_Query(widgets,device,'*IDN?')

    ## BLE Carrier Frequency Offset and Drift Test Results
    ## HOPOFFL->Hopping OFF, high frequency
    res = MT8852B_Query(widgets,device,'XRESULT LEICD,HOPOFFH,1')  
    res_items = res.split(',')
    leicd_h = {'valid':res_items[2], 'avg_fn':res_items[3], 'max_p_fn':res_items[4], 'max_n_fn':res_items[5],
            'max_dirft_rate':res_items[6], 'avg_drift':res_items[7], 'max_drift':res_items[8], 'failed':res_items[9],
            'tested':res_items[10], 'state':res_items[11]}
    
    leicd_result = {}
    leicd_result['leicd_l'] = leicd_l
    leicd_result['leicd_m'] = leicd_m
    leicd_result['leicd_h'] = leicd_h

    print_log(widgets,str(leicd_result))


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

    leicd_result['status'] = leicd_pass

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


    return leicd_result





## ================================================================================================
## ======================== LESS->BLE Receiver Sensitivity Test Results ===========================
## ================================================================================================

def less_result_read(widgets,device):

##======================================= LOW FREQUENCY ============================================

    MT8852B_Query(widgets,device,'SCPTSEL?')
    MT8852B_Query(widgets,device,'OPTSTATUS?')
    MT8852B_Query(widgets,device,'*IDN?')

    ## BLE Receiver Sensitivity Test Results
    ## HOPOFFL->Hopping OFF, low frequency

    res = MT8852B_Query(widgets,device,'XRESULT LESS,HOPOFFL')  
    res_items = res.split(',')
    less_l = {'valid':res_items[2], 'over_fer_%':res_items[3], 'total_frames_counted_dut':res_items[4], 'total_frames_sent_tester':res_items[5],
            'state':res_items[6]}

    ##======================================= MID FREQUENCY ============================================

    MT8852B_Query(widgets,device,'SCPTSEL?')
    MT8852B_Query(widgets,device,'OPTSTATUS?')
    MT8852B_Query(widgets,device,'*IDN?')

    ## BLE Receiver Sensitivity Test Results
    ## HOPOFFL->Hopping OFF, mid frequency

    res = MT8852B_Query(widgets,device,'XRESULT LESS,HOPOFFM')  
    res_items = res.split(',')
    less_m = {'valid':res_items[2], 'over_fer_%':res_items[3], 'total_frames_counted_dut':res_items[4], 'total_frames_sent_tester':res_items[5],
            'state':res_items[6]}

    ##======================================= HIGH FREQUENCY ============================================

    MT8852B_Query(widgets,device,'SCPTSEL?')
    MT8852B_Query(widgets,device,'OPTSTATUS?')
    MT8852B_Query(widgets,device,'*IDN?')

    ## BLE Receiver Sensitivity Test Results
    ## HOPOFFL->Hopping OFF, high frequency

    res = MT8852B_Query(widgets,device,'XRESULT LESS,HOPOFFH')  
    res_items = res.split(',')
    less_h = {'valid':res_items[2], 'over_fer_%':res_items[3], 'total_frames_counted_dut':res_items[4], 'total_frames_sent_tester':res_items[5],
            'state':res_items[6]}
    
    less_result = {}
    less_result['less_l'] = less_l
    less_result['less_m'] = less_m
    less_result['less_h'] = less_h

    print_log(widgets,str(less_result))

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

    less_result['status'] = less_pass

    print('===================================================================')
    print('灵敏度测试(发射功率 -85dBm)：',less_pass)
    print('================= 低通道 ==== 中通道 ==== 高通道 =====================')
    print('误帧率：           ', less_l['over_fer_%'], '      ',less_m['over_fer_%'],'      ',less_h['over_fer_%'])
    print('发送包数：         ', less_l['total_frames_sent_tester'], '      ',
        less_m['total_frames_sent_tester'],'      ',less_h['total_frames_sent_tester'])
    print('接收包数：         ', less_l['total_frames_counted_dut'], '      ',
            less_m['total_frames_counted_dut'],'      ',less_h['total_frames_counted_dut'])
    print('测试结果：         ', less_l['state'], '      ',less_m['state'],'      ',less_h['state'])

    return less_result
