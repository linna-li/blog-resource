---
title: "安装grafana系统"
author: "linna.li"
tags: ["raspberry"]
categories: ["note"]
date: 2021-01-30
---

> 成果：安装 grafana，从外部 mac 可以 access 到 grafana 页面

参考文档：
https://computingforgeeks.com/how-to-install-grafana-on-ubuntu-debian/
没有用 apt 指令直接进行安装，是通过 APT 仓库，这样可以拿到更新的版本。（但是这样的话需要自己来开端口）
主要命令：

1. sudo apt update
2. 安装 grafana gpg key(查了一下 gpg key 是用来加密的），这一步是为了能够下载 signed 的包。sudo apt-get install -y gnupg2 curl software-properties-common curl https://packages.grafana.com/gpg.key | sudo apt-key add -
3. 安装 Grafana 的 APT 仓库（APT 是安装包管理工具）。sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
4. sudo apt-get update
5. sudo apt-get -y install grafana
6. sudo systemctl enable --now grafana-server 用来启动 server
7. systemctl status grafana-service. 检查状态
   文档里面还有设置防火墙的一步，我只做了
8. sudo apt -y install ufw （ufw 是一个防火墙的设置工具）
9. sudo ufw enable
10. sudo ufw allow ssh
11. sudo ufw allow 3000/tcp
    (最后一步是 sudo ufw allow from 192.168.50.0/24 to any port 3000
    这一步是 to allow incoming access to the server on port 3000，means that the incoming connection will only be allowed if the source address (of the computer trying to connect to the server) is in the following IP range:
    192.168.50.1 - 192.168.50.254。但是对于 ubuntu server 对于 ip 没有默认的限制，所以不需要做这一步)

可能会用到的文件（如果用 apt，这些文件会提前被设置好在正确的地方）

```
Installs binary to /usr/sbin/grafana-server
Installs Init.d script to /etc/init.d/grafana-server
Creates default file (environment vars) to /etc/default/grafana-server
Installs configuration file to /etc/grafana/grafana.ini
Installs systemd service (if systemd is available) name grafana-server.service
The default configuration sets the log file at /var/log/grafana/grafana.log
The default configuration specifies a sqlite3 db at /var/lib/grafana/grafana.db
Installs HTML/JS/CSS and other Grafana files at /usr/share/grafana
```

### NodeExporter dashboard

设置 DataSource
import 一个 dashboard：https://grafana.com/grafana/dashboards/1860?pg=dashboards&plcmt=featured-sub1

对于 grafana 来说，只有一个 DataSource 就是 prometheus，如果加了 influxdb 就是新加了一个 DataSource
但是 prometheus 可以接受不同的应用的 metrics，在 prometheus.yml 里面进行配置就行
