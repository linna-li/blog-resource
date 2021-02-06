---
title: "LeetCode-83"
author: "linna.li"
tags: ["LinkedList", "leetcode"]
categories: ["DataStructure"]
date: 2021-01-10
---

## Description
> 给了一个链表，删除其中重复的节点

## My Answer
> 我的思路很简单
> 存下before和current的节点，进行比较
> 记得判断边界case，head是null的情况

## Complexity
我自己的解法时间复杂度应该是O(n)了，但是结果却是：
> Runtime: 1 ms, faster than 15.21% of Java online submissions for Remove Duplicates from Sorted List.
> Memory Usage: 41.4 MB, less than 6.06% of Java online submissions for Remove Duplicates from Sorted List.

## Other Answer

1. 可以优化成为只要一个辅助节点。优化过后是： 
> Runtime: 0 ms, faster than 100.00% of Java online submissions for Remove Duplicates from Sorted List.
> Memory Usage: 38.6 MB, less than 35.44% of Java online submissions for Remove Duplicates from Sorted List.>
2. 可以用递归