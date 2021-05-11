---
title: "Database"
author: "linna.li"
tags: ["database"]
categories: ["book"]
date: 2021-05-04
---
1. 
explicit join: 用 on
Implicit Join: 用 =
2005起不赞成使用该IMPLICIT INNER JOIN语法

2. 范式化与反范式化
Normalized范式化：
Denormalized反范式化：常用于高度分布式系统，需要存储一些冗余的数据，来避免经常join table的消耗

3. SQL 语句
4. 设计一个小的database: 弄清楚需求，设计主要的对象，分析关系，找出主要的语句。设计一个大的database：如果join用的很多，可以考虑反范式化，加入冗余数据
5. 