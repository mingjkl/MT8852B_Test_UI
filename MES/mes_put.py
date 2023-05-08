'''
Author: emmovo
Date: 2023-04-29 14:07:32
LastEditors: emmovo
LastEditTime: 2023-05-05 14:31:42
FilePath: \pythond:\WorkingData\BluetoothKB_Freq_test\MES\mes_put.py
Description: 

Copyright (c) 2023 by mingjkl@live.com/emmovo.com, All Rights Reserved. 
'''



import urllib3
import requests

id = 'test'
password = 'test'
ip = '172.16.24.3'
port = '8080'


## login 方法用于登录，返回用户信息，包含token
## 其中输入参数为：ip, port, id, password 是宏定义

def login(ip, port, id,password):

    try:
        url = 'http://{ip}:{port}/api/v1/login/{id}/{password}' \
            .format(ip=ip, port=port, id=id, password=password)
        response = requests.get(url)

        if response.status_code == 200:
            user_info = response.json()
            print('Http Get Success')
            print('user_info: ', user_info)
            return user_info
        else:
            print('Http Get Err: ',response.status_code)
            if response.status_code == 401:
                print('Login:Unauthorized')
            elif response.status_code == 403:
                print('Login:Forbidden')
            elif response.status_code == 404:
                print('Login:Not Found')

            return response.status_code
    except:
        print('Http Get Err !')
        return None
    

## mes_status_put 方法用于上传测试结果，返回上传结果
## 其中输入参数为：sn_code, user_info 分别是产品条码和用户信息
## 返回信息分为以下几种：
##   1. 上传成功，返回200
##      正常RF测试端上传：
##          {'resultCode': '200', 'resultMsg': 'OK 數量:1642', 'data': {'barcode': 'A4C138C55004', 'oldBarcode': None, 'lineName': '聚明 A01', 'sectionCode': 'DIP', 'groupCode': 'RF测试', 'stationName': 'RF测试1', 'moNumber': '300000037661', 'modelName': '210201A00752', 'keyPartNo': '', 'errorCode': 'N/A', 'machineCode': '01', 'defectPosQty': 1, 'testLog': 'SUCCESS', 'memo': None, 'nextStation': None, 'userId': 'IT', 'productQty': 1642, 'defectQty': 0, 'step': 'PASS', 'ps': [{'serialNumber': 'A4C138C55004', 'shippingSn': 'A4C138C55004', 'moNumber': '300000037661', 'modelName': '210201A00752', 'lineName': '聚明 A01', 'groupName': {'groupCode': 'RF测试', 'groupName': 'RF测试', 'groupType': None, 'section': None, 'groupDesc': None, 'status': None, 'sortNum': 0}, 'errorFlag': {'typeCode': '0', 'typeName': '良品', 'typeDesc': None, 'typeClass': None, 'status': None, 'sortNum': 0}, 'inStationTime': '2023-04-25 09:37:17', 'nextStation': {'groupCode': 'N/A', 'groupName': None, 'groupType': None, 'section': None, 'groupDesc': None, 'status': None, 'sortNum': 0}, 'empNo': None, 'cartonNo': None, 'palletNo': None, 'containerNo': None, 'poNo': None, 'routeCode': 'WS', 'boxNo': None, 'machineCode': '01', 'barBillno': '0', 'stationName': 'RF测试1', 'stockNo': None, 'qaNo': None, 'qaResult': None, 'reworkNo': None, 'versionCode': '0A', 'sectionName': 'DIP', 'createDate': '2023-04-25 08:47:08', 'customerSn': None, 'internalSn': None, 'warrantyDate': None, 'bomNo': None, 'snPics': None}]}}
##      非正常强制上传到其他工段：
##          {"resultCode":"200","resultMsg":"OK 數量:-1","data":{"barcode":"A4C138C55004","oldBarcode":null,"lineName":"聚 明 A01","sectionCode":"DIP","groupCode":"SPI","stationName":"RF测试1","moNumber":"300000037661","modelName":"210201A00752","keyPartNo":"","errorCode":"N/A","machineCode":"01","defectPosQty":1,"testLog":"SUCCESS","memo":null,"nextStation":null,"userId":"IT","productQty":-1,"defectQty":-1,"step":"PASS","ps":[{"serialNumber":"A4C138C55004","shippingSn":"A4C138C55004","moNumber":"300000037661","modelName":"210201A00752","lineName":"聚明 A01","groupName":{"groupCode":"SPI","groupName":"SPI","groupType":null,"section":null,"groupDesc":null,"status":null,"sortNum":0},"errorFlag":{"typeCode":"0","typeName":"良品","typeDesc":null,"typeClass":null,"status":null,"sortNum":0},"inStationTime":"2023-04-25 09:20:13","nextStation":{"groupCode":"N/A","groupName":null,"groupType":null,"section":null,"groupDesc":null,"status":null,"sortNum":0},"empNo":null,"cartonNo":null,"palletNo":null,"containerNo":null,"poNo":null,"routeCode":"WS","boxNo":null,"machineCode":"01","barBillno":"0","stationName":"RF测试1","stockNo":null,"qaNo":null,"qaResult":null,"reworkNo":null,"versionCode":"0A","sectionName":"DIP","createDate":"2023-04-25 08:47:08","customerSn":null,"internalSn":null,"warrantyDate":null,"bomNo":null,"snPics":null}]}}
## 
##   2. 上传成功，返回500
##      已经完成RF测试，流其他工段：
##          {'resultCode': '500', 'resultMsg': '應流向:包装,當前工站為:RF测试,路由:WS', 'data': None}
##      未完成RF测试，还有上流工段未完成：
##          {"resultCode":"500","resultMsg":"應流向:SPI,當前工站為:RF测试,路由:WS","data":null}
##      SN码不存在：
##          {"resultCode":"500","resultMsg":"系統中不存在這種連接條碼與出貨條碼:A4C138C55004!","data":null}
##      
## 注意
##   1. 修改工站'groupCode'可完成其他工站的过站(可选：SPI/AOI/写码/RF测试/功能测试/包装)
##   2. 工单号需留修改接口
##   3. 产品料号需留修改接口
##   4. 需进一步确定产品数量是什么含义


def mes_status_put(ip, port, sn_code, user_info):

    url = 'http://{ip}:{port}/api/v1/production_status_test?token={token}' \
        .format(ip=ip, port=port, token=user_info['accessTocken'])
    
    print("Http put URL: ", url)

    array = {
        "barcode" : sn_code,                    # 产品条码
        "createBy" : user_info['userName'],       # 创建人
        "defectPosQty" : 1,                     # 缺陷位置
        "defectQty" : None,                     # 缺陷数量
        "errorCode" : "N/A",                    # 错误代码
        "groupCode" : "RF测试",                 # 工站
        "keyPartNo" : "",                       # 关键件料号
        "lineName" : "聚明 A01",                # 产线
        "machineCode" : "01",                     # 机台号
        "moNumber" : "300000037771",            # 工单号     
        "modelName" : "210201A33752",           # 产品料号   
        "productOty" : 492,                     # 产品数量   ## 什么东西？
        "sectionCode" : "DIP",                  # 工段
        "stationName" : "RF测试1",              # 工位
        "step" : "PASS",                        # 步骤 "PASS" 指过站
        "testLog": "SUCCESS",                   # 测试LOG
        "userId": user_info['userName'],          # 测试者
    }

    print(array)

    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.put(url, json=array, headers=headers)

    print(response)

    print(response.content.decode('utf-8'))

    if response.status_code == 200:
        print('Http PUT: Success')
        print('response: ', response.json())

        return response.json()
    elif response.status_code == 201:
        print("Http PUT: Created")
        return None
    elif response.status_code == 401:
        print("Http PUT: Unauthorized")
        return None
    elif response.status_code == 403:
        print("Http PUT: Forbidden")
        return None
    elif response.status_code == 404:
        print("Http PUT: Not Found")
        return None


if __name__ == '__main__':

    user_info = login()

    if user_info is not None:
        print('user token: ', user_info['accessTocken'])
        mes_status_put('A4C138C55004', user_info)