---
title: "安装docker"
author: "linna.li"
tags: ["raspberry"]
categories: ["note"]
date: 2021-02-07
---

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04

docker pull ubuntu
docker run -it ubuntu

https://docs.docker.com/config/daemon/prometheus/
导出 metrics 并且重启 docker

```
{
  "metrics-addr" : "127.0.0.1:9323",
  "experimental" : true
}
```

开放端口 9323
我的理解是在一个 service 中，这个 service 相当于另外的 server
docker 道出了 9323 的 metics 给普罗米修斯，普罗米修斯统一用公共接口 9096 来导出到真正的外部
但是为什么 9323 会失败呢？
mount 是把我创建在 temp 中的文件给普罗米修斯用

https://www.thomas-krenn.com/en/wiki/Perl_warning_Setting_locale_failed_in_Debian

// 在一个 container 中的配置 （含义是从 9092 导出到 log 吗？）
ports: - 9092:9090
