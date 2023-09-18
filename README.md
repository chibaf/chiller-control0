# chiller-control0
chiller-control program via UARL

<img width="740" alt="selecting2-chiller" src="https://github.com/chibaf/chiller_communcations/assets/1296728/8e1d3e94-d953-46b3-ae54-6b2bd1dc4fa9">

<img width="778" alt="Screen Shot 2023-09-18 at 20 33 46" src="https://github.com/chibaf/chiller_communcations/assets/1296728/81a852b2-82bb-46ea-8762-c740f424cd2d">

## （1）BCCの計算

pythonの対話モードで

＞＞＞ 0x53^0x31^0x20^0x20^0x20^0x20^0x32^0x30^0x2e^0x30^0x03

125

＞＞＞ hex(125)

0x7d

## chillerの設定温度の取得

get_temp = b'\x04\x30\x30\x53\x31\x05'

ser.write(get_temp)  # send command to the chiller for get temp setting

line = ser.readline()  

print(line)
