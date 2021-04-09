---
title: "CTCI7-Bit-manipulation"
author: "linna.li"
tags: ["data-structure"]
categories: ["book"]
date: 2021-04-13
---
# 二进制处理
^是异或XOR
### 处理技巧
1. 0110 + 0110 相当于乘2，即左移动一位
2. 与自己本身取反的数进行异或，一定得到全是1的一串
## Two's Complement and Negative Numbers

### 计算机使用 *二进制补码（Two's Complement）*来存储整数的
正数存的是自己；
负数存的是他的 *绝对值（absolute value）的补码*，符号位是1，表示这是一个负数；
### 一个N位不带符号数（即绝对值）的补码，是 （2^N - 本身） 英语叫做the complement of the number with respect to 2^N.  
即  -K (negative K) as a N-bit(包括符号位) number 是 concat(1, 2^(N-1) - K)
比如说 占四个二进制位 一位是符号为，三位表示数
如果要求3的补码，就是5，5是101，所以-3就是 1101

###  也可以直接算：绝对值是3是011， 取反+1 = 100 + 1 = 101，再加上符号位

## 算数和逻辑右移
算数右移相当于除以2 用 >> 1 最左边一位补和之前相同的符号(所以一个负数一直进行算数右移动会得到 -1)
逻辑右移相当于用 >>>1 最左边一位补0
## 常用的二进制操作
### 得到一个bit
把1左移动想要的位的位数，然后与原来的数进行与操作
num & (1 << count)
### 设置一个bit
把1左移动想要的位的位数，然后与原来的数进行或操作
num | (1 << count)
### 清除一个bit
把要清除的位设置为0，其他位为1
num & (~(1 << count))
### 保留一个bit之后的所有bit
把要保留的位设置为1
num & ((1 << count)-1)
### 清除一个bit之后的所有bit
把要清除的位设置为0
num & (-1 << (count+1))
### 更新一个bit
先把那个位清理为0
然后把value设置到需要的位置
两个数或一下
num & (~(1 << count)) | (value << position)

5.1: 给定两个32位的数字N，M，两个位置i，j。把M插入到N中 
```java
int inset(int N, int M, int i, int j) {
   // i < j, 最右边是0位
   // 先清除，然后与 移动之后的M进行或操作
   return N = N | M << i
}
```
如何按照二进制输出？
5.2: 小数转为2进制，乘2取整，一直到小数位变成0
```java
int convert(double source){
   int[] result = new int[32];
   int i = 31;
   while(source > 0 && i > 0){
      int current = source * 2 > 0 ? 1 : 0;
      source = source * 2 - current;
      result[i] = current;
      i--;
   }
   if (i==0&&source>0) {
      System.out.println("ERROR");
   }
   else {
      int j = 31;
      while(j<i){
         System.out.println(result[j--]);
   }
}
```

5.3: 可以把一个0反转为1，找到最长的1的连续序列
```java
int longestSequence(int source){
   // 找到所有为0的位置
   // 11011101111 =》(4,8)
   // 11011100111 =》(3,4,8)
   // 11011110100 =》(0,1,3,8)
   int lastLength = 0;
   int lastlastLength = 0;
   int tempLength = 0;

   int resultLength = Math.min();
   // 思路：保存当前最长的一串的长度；当前的长度
   while (resource > 0) {
      // 判断当前位置是0还算是1
      int temp = resource % 2;
      // 如果是0记下来当前的位置，开始计数，同时这个数要加到前一个的结果上
      if (temp == 0) { 
         tempLength = 0;
         if(lastLength + lastlastLength + 1 > resultLength){
            resultLength = lastLength + lastlastLength + 1;
         }
         lastlastLength = lastLength;
         lastLength = tempLength;
      } else {
         tempLength++;      
      }
      resource >> 1;
   }
}
```

5.4: 给定一个正数，要求找到它的次小和次大的，但是1的个数要相同
```java
// 1001 -> 9, 0110 -> 6, 1010 => 10 
// 1000 -> 8, 0100 -> 5, 10000
// 111 -> 7, no, 31011 -> 11, 
// 找小的时候：
// 1. 如果右边可以右移(1后边有0的空位），移动一位, 返回
// 2. 如果右边不可以右移动（只有全是1的情况），如果最高位可以左移动：就移动一位，同时如果右边可以左移动，要移动到尽可能左。
// 如果不能左移动： 如果右边可以右移动，移动一位；如果不能右移动 011，说明没有更小值了

int finMin(int source){
   int result = source;
   if( ~source == 0){
      return source
   } else{
      
   }
}

void moveRightestOne(int source){

}
```