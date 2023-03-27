import pyvisa
import time

import plam_det

device = None

def print_log(widgets,msg):
    plam_det.log_display(widgets, msg)
    print("LOG: " + msg)



def connect_check(widgets, device):
    
    try:
        ID = device.query('*IDN?')
        if "MT8852B" in ID:
            print_log(widgets, "MT8852B ID: " + ID)
            print_log(widgets, "MT8852B Connected")
            return True
        else:
            print_log(widgets, "MT8852B Lost")
            return False
        
    except:
        print_log(widgets, "MT8852B Lost")
        return False
    

def MT8852B_Write(widgets,device, order):
    device.write(order)
    print_log(widgets, "MT8852B Write: " + order)

def MT8852B_Query(widgets,device, order):
    res = device.query(order)

    print_log(widgets,"MT8852B Query: " + order)
    print_log(widgets,"MT8852B Result: " + res)

    return res



def connect(widgets):
    
    try:
        rm = pyvisa.ResourceManager()   # 打开资源管理器
        rm_list = rm.list_resources()   # 获取设备列表

        for i in rm_list:
            print_log(widgets,'device: '+i)
            if '::27::INSTR' in i:
                device = rm.open_resource(i)
                connect_check(widgets, device)
                print_log(widgets,'GPIB init success')
                return device
            else:
                 print_log(widgets,'GPIB init failed')

        return None
        
    except:
        print_log(widgets,'mt8852b connect failed')
        return None

def init(widgets,device):

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
    while int(ins) != 46:
        ins = device.query('*INS?')   # 查询仪器状态
        time.sleep(1)
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




## ================================================================================================
## ================================== LEOP->BLE Output power ======================================
## ================================================================================================

def leop_result_read(widgets,device):
    ##======================================= LOW FREQUENCY ============================================

    MT8852B_Query(widgets,device,'SCPTSEL?')
    MT8852B_Query(widgets,device,'OPTSTATUS?')

    ##  LEOP->BLE Output power, HOPOFFL->Hopping OFF, low frequency
    res = MT8852B_Query(widgets,device,'XRESULT LEOP,HOPOFFL') 
    res_items = res.split(',')

    ## BLE Output power result
    leop_l = {'avg':res_items[3], 'max':res_items[4], 'min':res_items[5], 'peak_to_avg':res_items[6], 
            'failed':res_items[7], 'tested':res_items[8],'state':res_items[9], 'valid':res_items[2]}

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
    return less_result
