---
title: "安装ubuntu系统"
author: "linna.li"
tags: ["raspberry"]
categories: ["note"]
date: 2021-01-23
---

> 成果：安装操作系统；运行温度测试脚本；测试网络速度；安装 git 以及同步信息到外部 mac

### 安装操作系统

> Use SD Card + SD Card Reader + Macbook Pro only. recommend selecting: Ubuntu 20.04 LTS (Pi 3/4) 64-bit server OS for arm64 architecture

1. connect the SD Card reader to the macbook pro
2. Follow the OS install instructions and install ubuntu server 20.04, there are a few options though.
   https://www.raspberrypi.org/documentation/installation/installing-images/
3. Put the SD Card into the raspberry pi (the slot is on the bottom of the device).
4. Connect the network cable first, to the router.
5. Connect the power cable.
6. While it boots, login to the router to find its IP address.
7. In the router find the DCHP Address Reservation feature, make server have a consistent IP address. the server (DCHP Client) also understands the expiration time. it will ask the router (DCHP Server) to renew the lease before it runs out.
8. ssh ubuntu@(ip set in router)

### 第一个尝试

chmod +x temperatureCheck.sh //设置这个文件成为可以执行的文件

### 安装 git

参考文档：
https://superuser.com/questions/1316300/how-to-sync-a-local-dir-to-server-using-git
sudo apt-get install git-core
git --version
git config --global user.name
git config --global user.email
git config --list
