---
title: "CTCI3-Arrays and Strings"
author: "linna.li"
tags: ["data-structure"]
categories: ["book"]
date: 2021-01-18
---
> String和Array总是可以互换的问题

# 实现Hashtables
哈希表（Hashtable）又称为“散置”，Hashtable是会根据索引键的哈希程序代码组织成的索引键（Key）和值（Value）配对的集合。
1. 根据key计算hash值 
2. map hash值到一个index里（array）
3. 每一个index是一个链表，链表里的每一个元素是 (key, value)

# 实现ArrayList和Resizable Arrays
> Resizable Arrays是可变大小的数组
amortized insertion的runtime是O(1) 
在向一个list插入数据的时候，每次满了就会把容量扩大一倍，然后之前的复制到新的里面去

# StringBuilder
链接n个相同长度的string时候，如果使用String，时间复杂度是 O(xn^2)
如果使用了StringBuilder（可变长度的string）时间复杂度就是O(n) ?

# Interview Question
1. 判断一个String里面的元素是不是都是不重复的，要求不使用一个多余的数据结构
#### 思考：
不能使用map ？ 只是用String
把每一个字符转换为他的Ascii码，存在数组里，如果数组中有数据了，就代表重复的。
时间复杂度O(n), n 为字符串的长度，空间复杂度是需要一个128容量的array
```java
boolean isUnique(String s){
    if(s==null||s.length()==0){
        return true;
    }
    int[] asciiArray = new int[128];
    for(int i = 0;i < s.length();i++){
        if(asciiArray[Integer.valueOf(s.chatAt(i))]!=0){
            return false;
        }else{
            asciiArray[Integer.valueOf(s.chatAt(i))] = 1;
        }
    }
    return true;
}
```
#### 答案：
- 首先应该问面试官是ASCII还是unicode: ASCII是一个字节(1 byte (字节)= 8 bit(位))，只支持英文；Unicode两个字节支持所有语言；UTF-8是1-6个字节，英文字母一个字节汉字三个字节生僻字4-6个字节；
- ASCII码一共规定了128个字符的编码（0 000 0000–0 111 1111），比如空格”SPACE”是32（二进制00100000），大写的字母A是65（二进制01000001）。这128个符号（包括32个不能打印出来的控制符号），只占用了一个字节的后面7位，最前面的1位统一规定为0
```java
boolean isUniqueChars(String str){
    if(str.length() > 128){
        return false;
    }
    boolean[] char_set = new boolean[128];
    for(int i = 0;i<str.length();i++){
        int val = str.charAt(i);
        if(char_set[val]){
            return false;
        }
        char_set[val] = true;
    }
    return true;
}
```
时间复杂度可以说是O(1),因为永远不会超过128
如果只有小写的a到z的情况下，空间复杂度可以再改进
```java
boolean isUniqueChars(String str){
    int checker = 0; // int是4个字节
    for(int i = 0;i<str.length();i++){
        int val = str.charAt(i) - `a`;
        // 为什么要向左移动一位呢， 
        // 是为了避免两个a的情况 1 << 0 = `0000 0001`
        if((checker & (1<<val))>0){
            return false;
        }
        checker |= (1<<val)
    }
}
```
2. 给两个字符串，判断一个字符串是不是另外一个的排列
#### 思考：
就是两个字符串是不是有完全一样的字符，可以用上一个题的思路，分别用两个字符串去保存两个数组。时间复杂度 O(n), 空间复杂度O(n)
```java
boolean isPermutation(String s1, String s2){
    if(s1==null&&s2==null){
        return true;
    }
    if((s1!=null&&s2==null) || (s1==null&&s2!=null) || s1.length()!=s2.length()){
        return false;
    }
    int[] asciiArray1 = new int[128];
    for(int i = 0;i < s1.length(); i++){
        asciiArray1[Integer.valueOf(s.chatAt(i))]+=1;
    }
    for(int i = 0;i < s2.length(); i++){
        asciiArray2[Integer.valueOf(s.chatAt(i))]+=1;
    }
    int lengh = s1.length();
    int currentLength = 0;
    for(int i = 0;i < 128; i++){
        if(asciiArray1[i]!=asciiArray2[i]){
            return false
        }
        else{
            current+=asciiArray1[i];
            if(lengh==currentLength){
                return true;
            }
        }
    }
}
```
#### 答案
也是要先向面试官确认需求
例如: 
1. 大小写要不要区分
2. 字符一样但是排列过的算不算，例如GOD与DOG
3. 空格算不算一个字符

让我们假设需要区分大小写，而且空格也算字符。
Solution1:
排序
```java
String sort(String s){
    char[] content = s.toCharArray();
    Arrays.sort(content);
    return new String(content);
}
boolean permutation(String s, String t){
    if(s.length()!=t.length()){
        return false;
    }
    return sort(s).equals(sort(t));
}
```
Solution2:
思路和我的很像，但是用一个array就可以实现了
```java
boolean permutation(String s, String t){
    if(s.length()!=t.length()){
        return false;
    }
    int[] letters = new int[128]; //前提是用ASCII编码
    char[] s_array = s.toCharArray();
    for(char c : s_array){
        letters[c]++; // c 直接被强制转化成了int吗
    }
    for(int i = 0;i<t.length();i++){
        int c = (int)t.charAt(i);
        letters[c]--;
        if(letters[c] < 0){
            return false;
        }
    }
    return true;
}
```
总结经验(1/20)：
没有考虑到要向面试官确认需求！！！

3. 把一个字符串里的空格替代成为‘%20’
```java
void replaceSpace
```
