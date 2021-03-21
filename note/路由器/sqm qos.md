# sqm qos

# 基础设置

1. Basic Setting: download/upload speed设置为实测值的大小接口
2. Queue Discipline: cake+piece_of_cahe
3. Link Layer Adaptation: 设置 Ethernet with ..., Per Packet Overhaed: 46
4. 参考文档: https://www.right.com.cn/forum/thread-1207811-1-1.html

# 注意

1. 不同的端口瓶颈不一样, 需要分开设置
    比如2.4G和5G的wifi需要分别设置下载和上传的速度(即创建不同的SQM instance)
2. wan口的上传和下载是一致的
3. lan口以及wifi(wlan)的上传和下载的设置是反过来的
    (即lan口设置上传, 实际限制的是我们的下载流量)

# 实测情况

1. 设备信息
    ```
    型号	Newifi-D2
    架构	MediaTek MT7621 ver:1 eco:3
    固件版本	OpenWrt 19.07.7 r11306-c4a6851c72 / LuCI openwrt-19.07 branch git-21.044.30835-34e0d65
    内核版本	4.14.221
    ```
2. 设置qos前
    打开剑网3的下载器之后, 同机打开网页延迟高, 甚至访问路由器管理页面也很难打开, 其他设备ping百度的延迟也波动很大
3. 设置qos后
    打开剑网3下载器后, 同机可正常浏览网页, 可正常观看视频, 其他设备ping延迟有增加但稳定且增量不大

# 后续

1. 不同的Discipline以及Link Layer的含义后续有时间研究下
2. 测试只在单点测试, 不确定在不同的距离下对局Qos的影响(wifi5存在信号差的设备占用wifi所有带宽的情况)
3. 不确定在总流量跑满wifi的极限带宽的情况下, Qos是否还有效
