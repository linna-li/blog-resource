---
title: "LeetCode-203"
author: "linna.li"
tags: ["LinkedList", "leetcode"]
categories: ["DataStructure"]
date: 2021-01-10
---

## Description

> 从链表中删除给定的节点
> 给定了头节点，被删除的节点会有很多个

## My Answer

> 把自己的前一个节点的next指向自己的next
> 所以需要存下来before
> 注意记得修改before

## Complexity

> 时间复杂度 O(n), 不需要再优化了
> 空间复杂度 O(1), 用了两个节点保存前一个节点和本身

## Other Answer

> 大神们的解法使用递归，这样就需要多余的空间了 [3 line recursive solution](https://leetcode.com/problems/remove-linked-list-elements/discuss/57306/3-line-recursive-solution)