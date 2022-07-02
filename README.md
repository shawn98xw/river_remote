# river_remote  
server：被控制端  
client：控制端

## 开发日志
### 2022-07-01 v0.2
1. 解决 socket 分包问题  
2. 实现图像动态刷新

### 2022-06-27 v0.1  
1. 搭建基本框架，实现 client-server socket 通信
2. server 实现截屏功能，转为 bytes 数据通过 socket 发送至 client
3. client 实现 bytes -> .jpg 转换。