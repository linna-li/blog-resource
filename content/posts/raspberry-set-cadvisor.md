---
title: "安装cadvisor"
author: "linna.li"
tags: ["raspberry"]
categories: ["note"]
date: 2021-03-13
---

1. 谷歌已经不用 dockerhub 来管理 cadvisor
2. 谷歌只提供了 linux/amd64 的 image，不能用于 linux/arm64/v8
3. 可以自己做一个 binary 然后拿来直接安装在蓝莓派上!
   https://github.com/google/cadvisor/blob/master/docs/development/build.md
4. 所以 image 其实是对系统有要求的
5. 也可以自己写 dockerfile

http://192.168.0.111:8080/containers/
