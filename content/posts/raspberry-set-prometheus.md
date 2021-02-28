---
title: "安装prometheus"
author: "linna.li"
tags: ["raspberry"]
categories: ["note"]
date: 2021-01-30
---

> 成果：安装 prometheus 的 node-exporter 来导出 server 的 metrics。prometheus 是用来收集 metrics 的，grafana 通过 pull 的方式去拿数据，然后进行显示。除了 prometheus 之外也有其他的 datasource，比如 influxdb，是通过 push 的方式来向 grafana 发送数据。
> 参考文档：https://computingforgeeks.com/how-to-monitor-linux-server-performance-with-prometheus-and-grafana-in-5-minutes/

这个文档也是没有用 apt 指令，是通过 APT 仓库进行安装。但是我搞错了版本，应该用 *ARM64*的版本，但是我用的是 amd64。amd64 是 x86-64, 后来只能清理了所有的 node-exporter，直接用 apt 重新安装的。（用 lsb_release -a 可以看到 ubuntu 版本）

```
sudo apt install prometheus-node-exporter
sudo systemctl daemon-reload
sudo systemctl start prometheus-node-exporter
sudo systemctl enable prometheus-node-exporter
sudo systemctl status prometheus-node-exporter
```

成功之后发现从 server 的 local 可以看到 metrics，但是用 mac 上用 curl -GET http://localhost:9100/metrics 没有办法。
用指令来检查端口的开放情况
sudo ufw status verbose
发现 9100 端口没有开放
用指令开放：sudo ufw allow 9100/tcp
![](/images/port.png)
因为不熟悉 ubuntu server 的文件结构，所以出错了也不知道应该改哪个文件，只能参考这个文档尽量做到清除干净：
http://www.linfo.org/var.html
https://superuser.com/questions/513159/how-to-remove-systemd-services

安装 sudo apt  install tree 可以来看到文件结构。command: tree workspace/
node_exporter.service 文件可以自己 customized。如果用 apt 下载，这个文件会被叫做 prometheus-node-exporter.service

```
$ cat data/node_exporter.service
[Unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target

[Service]
User=node_exporter
Group=node_exporter
Type=simple
ExecStart=/usr/local/bin/node_exporter

[Install]
WantedBy=multi-user.target
```

### 关于 prometheus

- performance 主要是为了看 CPU, Memory, Disk I/O, Network
- 使用 pull 的方式（Scrap）从 client 中获得 metrics，然后存在它的 local time series 的数据库(TSDB)里
- alerting 使用 AlertManager, 可以自己选择 notification system
- 可以自动的发现不同的 target（不需要我们去更新 address）

注意，前一步只是安装了 prometheus-node-exporter，只是一个 node-exporter，只是带了一些配置
所以还是需要安装 prometheus 并且开放端口

```
sudo apt install prometheus
sudo systemctl daemon-reload
sudo systemctl enable prometheus
sudo systemctl status prometheus
sudo ufw allow 9090/tcp
```

sudo killall -HUP prometheus

### 关于为什么不用 apt
