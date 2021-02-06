---
title: "LeetCode-160"
author: "linna.li"
tags: ["LinkedList", "leetcode"]
categories: ["DataStructure"]
date: 2021-01-08
---

## Description

> 找到两个链表的交点

## My answer

> 这是一道easy题，但是要求时间复杂度是O(n)，于是我想了好久。。
> 后来发现最笨的方法也可以过
> 就是现求出来两个链表的差距，然后走到相同的相对位置上，看看能不能找到一个相同的节点，如果能找到，就说明这个节点是相交的节点（因为后面不会再分叉开了）

## Complexity

## Other answer

>后来我去看了讨论区，大部分人还是和我一样的解法，有一个大神的解法代码更简单，两个指针一起走，走到头了之后就去另外一个链表接着走，直到找到一个相同的节点，或者两个都是null的时候，说明没有相交节点
