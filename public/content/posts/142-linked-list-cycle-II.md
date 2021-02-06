---
title: "LeetCode-142"
author: "linna.li"
tags: ["LinkedList", "leetcode"]
categories: ["DataStructure"]
date: 2021-01-07
---

## Description

> 如果链中有环，找到环的入口

## My Answer

> 大神给画的图.

![](/images/142.jpeg)

> 快指针和慢指针会在环的内部相遇
> 经过推导可以知道 起点到环入口的长度==相遇点到环入口的长度
> 让快慢指针每次走一步就可以找到环入口的长度

## Complexity

## Other Answer