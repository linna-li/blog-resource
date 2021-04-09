---
title: "尝试自己写dockerfile"
author: "linna.li"
tags: ["docker"]
categories: ["note"]
date: 2021-04-29
---

比较简单的只要单独的dockerFile就可以
最简单：
FROM ubuntu:20.04

删除所有的image
docker rmi $(docker images -a -q)

run一个image，注意要用 -ti
### The -t is TTY and -i will keep STDIN open. if don't do this, bash will see that there is no more input on STDIN and exit.
### 
docker run -d -ti --entrypoint /bin/bash ubuntulln:v1
docker exec -ti 86f8f0e0 /bin/bash

查看硬件系统
root@86f8f0e09045:/# uname -m
x86_64

container name: the name is randomly generated if you don't set it yourself, but human readable. 
Reference: https://docs.docker.com/engine/reference/builder/

curl downloaded an uncompleted file
### prometheus.service is the systemd service definition, 
### it's needed for ubuntu + systemd, not required by prometheus itself.

EXPOSE 9090 is basically just documentation

Command: docker run -d prom:v5 --config.file=/etc/prometheus/prometheus.yml

docker exec -ti CONTAINERID /bin/bash
apt install curl
curl http://localhost:9090/metrics

127.0.0.1:80:8080/tcp



docker run -d linna:v1 -p -p 127.0.0.1:80:9090/tcp --config.file=/etc/prometheus/prometheus.yml

This binds port 8080 of the container to TCP port 80 on 127.0.0.1 of the host machine. 