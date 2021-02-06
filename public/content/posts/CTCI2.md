---
title: "CTCI2-Technical Questions"
author: "linna.li"
tags: ["basic-knowledge"]
categories: ["book"]
date: 2021-01-16
---
## How to prepare
1. 自己思考，同时要思考复杂度
2. 在纸上写code
3. 纸上测试code（general cases, base cases, error cases)
4. 把纸上的code输入到电脑里，看自己有哪些错误
5. mock interview

## What you need to know
1. Practicing implementing the data structures and algorithm on paper, then on computer
2. basic： 2^10 大概是 1000， 2^20 大概是1million（100万），2^30 大概是1billion（10亿）= 1GB， 2^40 大概是 1trillion（1万亿）= 1TB

## Walking through a problem
1. Listen: 注意一些特别的词，sorted，repeatedly
2. Draw an Example: 给定值，足够大，不是一个特殊例子
3. 先考虑一个暴力解法，给定时间和空间复杂度
4. 优化：看看有没有没用到的信息；考虑一个新的例子；不正确的解决（？）；tradeoff时间和空间；提前计算；使用hash table；考虑最佳的runtime
5. 检查
6. 写代码: 从左上角开始写，避免倾斜，漂亮的代码（模块化初始化方法，做class，错误检查，命名）
7. 测试: 概念上的测试（假装自己正在给别人讲代码）；有没有看起来奇怪的代码；热点问题；小的测试例子；特殊的例子；

## 优化
1. 查找瓶颈（优化是瓶颈的那部分才有意义）
2. 去掉不必要的工作（比如说可以用多一步计算来减少一层循环）
3. 去掉重复工作（用hashmap保存下来结果）
4. 假装是自己在做，而不是考虑一个算法
5. 简化和普遍化
6. 从base case开始（n=1）
7. 过一遍所有的数据结构：linkedlist不适合accessing和给是数字排序；
8. Best Conceivable Runtime(BCR) 可能但是不一定会存在的最优时间，一般用于作为hint，也作为时间优化的上限。如果已经达到这时间，说明时间上不能再进行优化，只能优化空间。
9. 当遇到一个考过的问题，要告诉面试官
10. 选择语言：java属于比较易懂的，不用考虑memory和指针。java属于比较冗长的语言，例如python可以直接返回多个值，但是java必须要一个class
11. 好的代码：正确，高效，简洁，可读性，可维护性
12. 正确地使用数据结构
13. 写可以重复使用的代码（抽取重复部分写成一个方法）
14. 可以抽取成方法的写成一个方法（不要把一个方法写的很长）
15. 灵活性（可以对应多种例子，general）
16. 要做错误检查，参数认证检查