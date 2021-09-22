---
title: "Cracking the code interview1"
author: "linna.li"
tags: ["basic-knowledge"]
categories: ["book"]
date: 2021-01-13
---

## Big O 
Big O 是用来描述一个算法有效性的 O() 
空间复杂度，包好了递归函数中用到的变量
可以省略到非主流的部分：O(x!) > O(2^x) > O(x^2) > O(xlogx) > O(x) > O(logx)
### Amortized Time(均摊时间)：

在插入数据到ArrayList的时候，正常是在末尾插入，所以复杂度是O(1), 但是满了之后会扩大容量为两倍，然后复制现有的进去，再进行插入，所以花费的时间是n，所以插入x个数据的时间是：1+2+4+....+x (省略了不需要复制的时候插入消耗的时间)
所以插入每一个花费的时间是 （1+2+4+....+x）/x = 
书上说是 O（1） （不太懂 这里）

### Log N Runtime

### Recursive Runtime
2^0+2^1+....2^n = 2^(n+1) - 1
如果有递归算法的话，一般来说时间都是 O(branched^depth) 

### Example and Exercise
O(N+M) 不可以认为是 O(N)

#### Example 8
有一个String的数组，需要给每一个string自己排序，然后给整个string排序，求时间复杂度
首先第一轮循环把每个string排序。排序每一个string需要的时间是 slogs ， 假设一共是a个，所以一共需要 aslogs。
第二轮是排序这个数组 aloga 次比较，每次比较花费s， 所以是saloga
一共花费时间 aslogs + saloga  ===》 O(as(logs+loga))

#### Example 9
int sum(Node node) {
    if(node == null){
        return 0;
    }
    return sum(node.left) + node.value + sum(node.right);
}
O(2^logN) = 0(N)

#### Example 10
判断一个数是不是质数
boolean isPrime(int n){
    for(int x = 2; x * x <= n;x++){
        if( n%x == 0) {
            return false;
        }
    }
    returrn true;
}
复杂度是: n开方

#### Example 11
int factorial(int n){
    if (n<0) {
        return -1;
    } else if (n==0) {
        return 1;
    } else {
        return n*factorial(n-1)
    }
}
拆开之后是 n * (n-1) * (n-2) *(n-3) *....1，所以是计算n次

#### Example 12
排列(permutation) 
void permutation(String str){
    permutation(str, "");
}
void permutatation(String str, String prefix){
    if(str.length()==0){
        System.out.println(prefix);
    }else{
        for(int i = 0;i < str.length; i++){
            String rem = str.substring(0,i) + str.substring(i+1);
            permutation(rem, prefix + str.charAt(i));
        }
    }
}
permutatation 被call了多少次：假设有7个字符，一共会有7！次叫了84行
 （不太懂 这里，和小伙伴讨论了一下，他也觉得应该是只有 n!）
Picture a large call tree representing all the calls, There are n! leaves, as shown above. Each leaf is attached to a path of length n. Therefore, we know there will be no more than n*n! nodes (founction calls) in this tree.
每次需要花费的时间是n（可以理解）所以最终花费的时间是 O(n*n*n!)

#### Example 13
int fib(int n){
    if(n<=0) return 0;
    else if(n==1) return 1;
    else return fib(n-1) + fib(n-2);
}
可以利用树深度的规律 O(branched^depth) = O(2^n)
一般来说只要看到有多个递归的call，一般时间复杂度都是指数级别的

#### Example 14

void allFib(int n) {
    for(int i = 0;i< n; i++ ){
        System.out.println(i+fib(i));
    }
}
int fib(int n){
    if(n<=0) return 0;
    else if(n==1) return 1;
    return fib(n-1) + fib(n-2);
}
注意这个的时间复杂度不是O(n2^n)， 因为每一次进去fib的n都是不一样的
应该是2^1 + 2^2 + 2^3 +.....+ 2^n = 2^(n+1) O(2^n)

#### Example 15
加了一个cache之后，时间复杂度变成了 O(n)

#### Example 16
int powersof2(int n){
    if(n<1){
        return 0;
    }else if(n == 1){
        System.out.print(1);
        return 1;
    }else{
        iint prev = powerOf(n/2);
        int curr = prev * 2;
        System.out.println(curr);
        return curr;
    }
}
时间复杂度是 O(logn)

### VI 12

int intersection(int[] a, int[] b){
    mergeSort(b);
    int interect = 0;

    for(int x:a){
        if(binarySearch(b,x)>=0){
            intersect++;
        }
    }
    return intersect;
}
mergeSort 的时间复杂度是 blogb, binarySearch的时间复杂度是logb，a次循环所以是alogb
总共为 (a+b)logb