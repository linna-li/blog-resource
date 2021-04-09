---
title: "CTCI7-Bit-manipulation"
author: "linna.li"
tags: ["data-structure"]
categories: ["book"]
date: 2021-04-13
---
# 二进制处理
^是异或XOR
### 处理技巧
1. 0110 + 0110 相当于乘2，即左移动一位
2. 与自己本身取反的数进行异或，一定得到全是1的一串
## Two's Complement and Negative Numbers

### 计算机使用 *二进制补码（Two's Complement）*来存储整数的
正数存的是自己；
负数存的是他的 *绝对值（absolute value）的补码*，符号位是1，表示这是一个负数；
### 一个N位不带符号数（即绝对值）的补码，是 （2^N - 本身） 英语叫做the complement of the number with respect to 2^N.  
即  -K (negative K) as a N-bit(包括符号位) number 是 concat(1, 2^(N-1) - K)
比如说 占四个二进制位 一位是符号为，三位表示数
如果要求3的补码，就是5，5是101，所以-3就是 1101

###  也可以直接算：绝对值是3是011， 取反+1 = 100 + 1 = 101，再加上符号位

## 算数和逻辑右移
算数右移相当于除以2 用 >> 1 最左边一位补和之前相同的符号(所以一个负数一直进行算数右移动会得到 -1)
逻辑右移相当于用 >>>1 最左边一位补0
## 常用的二进制操作
### 得到一个bit
把1左移动想要的位的位数，然后与原来的数进行与操作
num & (1 << count)
### 设置一个bit
把1左移动想要的位的位数，然后与原来的数进行或操作
num | (1 << count)
### 清除一个bit
把要清除的位设置为0，其他位为1
num & (~(1 << count))
### 保留一个bit之后的所有bit
把要保留的位设置为1
num & ((1 << count)-1)
### 清除一个bit之后的所有bit
把要清除的位设置为0
num & (-1 << (count+1))
### 更新一个bit
先把那个位清理为0
然后把value设置到需要的位置
两个数或一下
num & (~(1 << count)) | (value << position)