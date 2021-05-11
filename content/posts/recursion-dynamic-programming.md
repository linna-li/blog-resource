---
title: "CTCI8-"
author: "linna.li"
tags: ["system-design"]
categories: ["book"]
date: 2021-04-30
---
## 解法
bottom-up,
从解决最简单的问题开始
top-down, 
half-half
## 递归与非递归解法
每一次递归都会在栈里建立一层新的，
所以如果深度n，至少需要O(n)的memory。因此非递归的解法要更优
## 动态编程
用一个递归的算法，找到重复的子问题，缓存结果以方便未来的递归call
可以用树来表示递归算法，每一个节点就是计算一次
很容易发现会有重复计算，所以我们可以用int[] memo来缓存结果