# river_remote  
server：被控制端
client：控制端

### 开发日志
2022/6/27 0.1  
搭建基本框架，实现 client-server socket 通信；  
server 实现截屏功能，转为 bytes 数据通过 socket 发送至 client；  
client 实现 bytes -> .jpg 转换。