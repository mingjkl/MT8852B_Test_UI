
import json

with open('D:/WorkingData/BluetoothKB_Freq_test/test/setting.json', 'r') as f:
    setting_data = json.load(f)

print(setting_data['vision'])
print(setting_data['test'])
print(setting_data['box']['right'])