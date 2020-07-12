1.USB转串口连接HC-05上电
2.树莓派蓝牙和HC-05连接
3.执行如下命令
sudo chmod 777 /dev/ttyUSB0
sudo chmod 777 /dev/rfcomm0
4.
* 执行下面程序接受蓝牙消息：
python3 recv.py
允许控制的IO为board pin为37和38 
* 在另一个命令行窗口中执行下列命令
python3 send.py
支持的pin：37 38
支持的值：  0  1