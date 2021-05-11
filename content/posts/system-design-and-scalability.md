---
title: "CTCI9-system-design-and-scalability"
author: "linna.li"
tags: ["system-design"]
categories: ["book"]
date: 2021-04-30
---
## 流程
Step1: scope the problem
多问问题，比如说shorten url
Step2: 做一些合理的假设
Step3: 画一些主要的服务器组件
Step4: 找出主要的问题 瓶颈和主要的挑战
Step5: 为了解决瓶颈进行一些redesign
## 考虑scale
一台机器可以处理的数据，如果分开之后会产生什么问题
Vertical scaling: 增加一台机器的内存（更简单）
Horizontal：增加server的数量
Load Balancer：
数据库的改进：如果是mysql，可以考虑Database Denormalization（为了提高读，避免join table） 
或者使用 NoSQl
### Partitioning
Vertical Partitioning: 根据内容分开（会导致table很大）
Keybased：缺点是不容易再增加新的server，因为需要rehash
Directioy based：使用一个lookup table

## Caching
## Asynchronous Processing & Queues
可以 pre-process，显示部分别的内容，
## Networking Metrics
Bandwidth带宽: 在一定的时间可以传递的最大数量的数据
Throughput吞吐：时间段内的
Latency延迟：从发送数据到接受数据的时间
## MapReduce
用来同时处理多个请求

# Considerations
Failures
Availability（系统可以操作的百分比） and Reliability（系统可用的可能性）
Read-heavy（考虑cache） vs. Write-heavy（考虑queue）
Security

# Example
给出大量的documents，找到包含某个特定words list的document，word可以以任何顺序出现，但是必须包含完整的word
Step1: 假设已经有了文档，如何实现 findWords => 建立一个hash table，找到交集
Step2: 考虑如何分开hash table：可以根据keyword或者document；想办法知道哪一个machine包含了data
Step3: 可以根据keyword来分开机器