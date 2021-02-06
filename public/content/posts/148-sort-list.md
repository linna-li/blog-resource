---
title: "LeetCode-148"
author: "linna.li"
tags: ["LinkedList", "leetcode"]
categories: ["DataStructure"]
date: 2021-01-11
---

## Description

> 给一个链表排序，要求 时间复杂度是 O(n logn)，空间复杂度是 O(logn)
## My Answer

> 这道题我自己没有做出来。。。 T T
> 我的想法是分成两份, 然后递归进行排序, 注意这个不叫二分排序！！！ 这个的思想其实是快速排序，**平均** 的时间复杂度是 O(nlogn)～O(n^2)。但是快速排序不适合链表，没办法链接起来
总结排序算法的复杂度：
![](/images/sort-algorithem.png)

> 很好懂的答案是归并排序。归并排序（特点是 可以利用递归来交换数字，适合链表）可以将链表从中间断开，排好序之后merge。
> 从中间断开的方法是： 1. 快慢指针。2.或者是统计一下长度之后断开

## Complexity
> 时间复杂度 O(nlogn)
> 空间复杂度 O(logn)
## Other Answer
> 因为其实时间复杂度不符合要求，所以最好的方法是用Bottom Up
> 思想是：https://www.youtube.com/watch?v=M1TwY0nsTZA
