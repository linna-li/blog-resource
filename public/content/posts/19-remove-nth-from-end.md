---
title: "LeetCode-19"
author: "linna.li"
tags: ["LinkedList", "leetcode"]
categories: ["DataStructure"]
date: 2021-01-10
---

## Description

> 删除从后面数第n个节点
> 要求只能遍历整个list一遍
> 这种一般就要两个指针，数学先计算一下了

## My answer

> 两个指针，一个先走 (n-1) 步； 另一个现在出发，走 length - 1 - (n - 1)；
> 倒数第n = 正数第 length - n + 1 = 正着走 length - n 步

## Complexity
> 时间复杂度 O(n)
> 空间复杂度 用了两个指针

## Other answer
> 
