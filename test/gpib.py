
import pyvisa
import time

def MT8852B_Write(order):
    device.write(order)
    print("MT8852B Write: ", order)
    # time.sleep(0.1);

def MT8852B_Query(order):
    res = device.query(order)
    # time.sleep(0.1);
    print("MT8852B Query: ", order)
    print("MT8852B Result: ", res)
    return res

def MT8852B_Connect_Cheak():
    ID = MT8852B_Query('*IDN?')
    # time.sleep(0.1);
    if "MT8852B" in ID:
        print("MT8852B Connect")
        print(ID)
        return True
    else:
        print("MT8852B Lost")
        return False
    


rm = pyvisa.ResourceManager()   # 打开资源管理器
rm_list = rm.list_resources()   # 获取设备列表
# print(rm_list)

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
    print('LOG: Select Script 10 Success')
else:
    print('LOG: Select Script 10 Fail')

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
    print('LOG: Select Script 10 Success')
else:
    print('LOG: Select Script 10 Fail')

MT8852B_Write("SCPTTSTGR 10,STDTSTS,OFF")   # 关闭标准测试
MT8852B_Write("SCPTTSTGR 10,EDRTSTS,OFF")   # 关闭EDR测试
MT8852B_Write("SCPTTSTGR 10,BLETSTS,ON")   # 开启BLE测试

MT8852B_Write("RUN")    # 运行脚本
# device.set_visa_attribute(VI_ATTR_TMO_VALUE, 12000)  # 设置超时时间
opc = MT8852B_Query('*OPC?')   # 查询操作完成
if opc == '1':
    print('LOG: Select Script 10 Success')
else:
    print('LOG: Select Script 10 Fail')

# device.set_visa_attribute(VI_ATTR_TMO_VALUE, 20000)  # 设置超时时间
MT8852B_Query('*ESR?')   # 查询错误状态寄存器

## while
MT8852B_Query('*INS?')   # 查询仪器状态
## end while

ins = MT8852B_Query('*INS?')
print('LOG: Wait for Script 10 Result')
while int(ins) != 46:
    ins = device.query('*INS?')   # 查询仪器状态
    time.sleep(1)
print('LOG: Script 10 Run Success')

# device.set_visa_attribute(VI_ATTR_TMO_VALUE, 3000)  # 设置超时时间

MT8852B_Write('OPMD SCRIPT')     # 打开脚本
MT8852B_Query('ERRLST') # 查询错误列表
MT8852B_Query('*ESR?')   # 查询错误状态寄存器

MT8852B_Query('OPTSTATUS?')  # 查询测试结果
