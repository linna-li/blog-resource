---
title: "LeetCode-21"
author: "linna.li"
tags: ["LinkedList", "leetcode"]
categories: ["DataStructure"]
date: 2021-01-10
---

## Description

> 合并两个有序的链表

## My answer

> 是一个easy的题，但是我感觉写的好长，肯定有简单办法来解
> 我是定义了一个head，一个current，然后两个指针分别移动两个链表
> 比较大小，然后合并

## Complexity
> 时间复杂度 O(n + m)
> 空间复杂度 用了4个指针

## Other answer
1. 和我的想法类似，但是只用了两个指针。一个head保存答案，一个handler保存在哪个list。
2. 用递归

