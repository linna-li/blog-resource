---
title: "CTCI3-Arrays and Strings"
author: "linna.li"
tags: ["data-structure"]
categories: ["book"]
date: 2021-01-18
---

> String 和 Array 总是可以互换的问题

# 实现 Hashtables

哈希表（Hashtable）又称为“散置”，Hashtable 是会根据索引键的哈希程序代码组织成的索引键（Key）和值（Value）配对的集合。

1. 根据 key 计算 hash 值
2. map hash 值到一个 index 里（array）
3. 每一个 index 是一个链表，链表里的每一个元素是 (key, value)

# 实现 ArrayList 和 Resizable Arrays

> Resizable Arrays 是可变大小的数组
> amortized insertion 的 runtime 是 O(1)
> 在向一个 list 插入数据的时候，每次满了就会把容量扩大一倍，然后之前的复制到新的里面去

# StringBuilder

链接 n 个相同长度的 string 时候，如果使用 String，时间复杂度是 O(xn^2)
如果使用了 StringBuilder（可变长度的 string）时间复杂度就是 O(n) ?

# Interview Question

1. 判断一个 String 里面的元素是不是都是不重复的，要求不使用一个多余的数据结构

#### 思考：

不能使用 map ？ 只是用 String
把每一个字符转换为他的 Ascii 码，存在数组里，如果数组中有数据了，就代表重复的。
时间复杂度 O(n), n 为字符串的长度，空间复杂度是需要一个 128 容量的 array

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

- 首先应该问面试官是 ASCII 还是 unicode: ASCII 是一个字节(1 byte (字节)= 8 bit(位))，只支持英文；Unicode 两个字节支持所有语言；UTF-8 是 1-6 个字节，英文字母一个字节汉字三个字节生僻字 4-6 个字节；
- ASCII 码一共规定了 128 个字符的编码（0 000 0000–0 111 1111），比如空格”SPACE”是 32（二进制 00100000），大写的字母 A 是 65（二进制 01000001）。这 128 个符号（包括 32 个不能打印出来的控制符号），只占用了一个字节的后面 7 位，最前面的 1 位统一规定为 0

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

时间复杂度可以说是 O(1),因为永远不会超过 128
如果只有小写的 a 到 z 的情况下，空间复杂度可以再改进

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

就是两个字符串是不是有完全一样的字符，可以用上一个题的思路，分别用两个字符串去保存两个数组。时间复杂度 O(n), 空间复杂度 O(n)

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
2. 字符一样但是排列过的算不算，例如 GOD 与 DOG
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
思路和我的很像，但是用一个 array 就可以实现了

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
   解法是遍历两次，然后从末尾开始加数据

```java
void replaceSpaces(char[] str, int trueLength){
    int spaceCount = 0;
    int index = 0;
    int i = 0;
    for(i = 0;i<trueLength; i++){
        if(str[i] == ' '){
            spaceCount++;
        }
    }
    index = trueLength + spaceCount*2;
    if(trueLength < str.length){
        str[trueLenght] = '\0'
    }
    for(i = trueLength - 1;i>=0;i--){
        if(str[i] == ' '){
            str[index - 1] = '0';
            str[index - 2] = '2';
            str[index - 3] = '%';
            index = index - 3;
        }else{
            str[index - 1] = str[i];
            index--;
        }
    }
}
```

4. 确认一个字符串可不可以组成回文字符串
   解法 1：
   用一个 hashtable 来存下每个字符出现的次数，之后进行统计。如果出现第二次技术个，就退出

```java
boolean isPermutationOfPalindrome(String phrase){
    int[] table = buildCharFrequencyTable(phrase);
    return checkMaxOndOdd(table);
}
// Check that no more than one character has an odd(奇数) count.
boolean checkMaxOneOdd(int[] table){
    boolean foundOdd = false;
    for(int count:table){
        if(count%2 == 1){
            if (foundOdd){
                return false;
            }
            foundOdd = true;
        }
    }
    return true;

// Map each character to a number.
// a -> 0, b -> 1, c->2 and etc.
// This ia case insensitive, Non-letter characters map to -1
int getCharNumber(Character c) {
    int a = Character.getNumericValue('a');
    int z = Character.getNumericValue('z');
    int val = Character.getNumericValue(c);
    if(a<=val && val <=z){
        return val - a;
    }
    return -1;
}
// count how many times each character appears
int[] buildCharFrequencyTable(String phrase){
    int[] table  = new int[Character.getNumericValue('z') - Character.getNumericValue('a') + 1];
    for(char c : phrase.toCharArray()){
        int x = getCharNumber(c);
        if(x!=-1){
            table[x]++;
        }
    }
    return table;
}
```

解法 2：由于时间复杂度不可以再进行优化，所以可以优化空间复杂度

```java
boolean isPermutationOfPalindrome(String phrase){
    int countOdd = 0;
    int[] table  = new int[Character.getNumericValue('z') - Character.getNumericValue('a') + 1];
    for(char c : phrase.toCharArray()){
        int x = getCharNumber(c);
        if(x!=1){
            table[x]++;
            if(table[x]%2 == 1){
                countOdd++;
            }else{
                countOdd--;
            }
        }
    }
    return countOdd <=1;
}
```

解法 3：不使用一个 table 来存，只用一个整数，每一位（0 或者 1）代表偶数个还是奇数个

```java
boolean isPermutationOfPalindrome(String phrase){
    int bitVector = createBitVector(phrase);
    return bitVector == 0 || checkExactlyOneBitSet(bitVector);
}
// create a bit vector for the string, for each letter with value i, toggle the ith bit.
int createBitVector(String phrase) {
    int bitVector = 0;
    for(char c : phrase.toCharArray()){
        int x = getCharNumber(c);
        bitVector = toggle(bitVector, x);
    }
    return bitVector;
}
// Toggle the ith bit in the integer
int toggle(int bitVector, int index){
    if(index<0) return bitVector;

    int mask = 1 << index; // 1 向左边移动index位
    if(bitVector & mask) == 0){ // 判断原本这里是有奇数个还是偶数个
         // 原本是0，设置为1
        bitVector |= mask; //新多出来一位奇数
    }else{
         // 原本是1，设置为0，不能影响其他位
        bitVector &= ~mask;
    }
    return bitVector;
}
// 记住就行，判断一个二进制数是不是只有1位是1的方法，就是: 这个数本身&(这个数-1）
boolean checkExactlyOneBitSet(int bitVector){
    return (bitVector & (bitVector - 1)) == 0;
}
```

5. 判断两个字符串可不可以通过一步变换得到
   思路：要实现一步变换，两个字符串的长度差或者相等，或者是 1
   解法 1：

```java
boolean oneEditAway(String first, String second){
    if(first.length() == second.length()){
        return oneEditReplace(first,second);
    }else if (first.length() +1 == second.length()){
        return oneEditInsert(first, second);
    }else if(first.length() - 1 == second.length()){
        return oneEditInsert(second, first);
    }
    return false;
}

boolean oneEditReplace(String s1, String s2){
    boolean foundDifference = false;
    for(int i = 0;i<s1.length();i++){
        if(s1.charAt(i)!=s2.charAt(i)){
            if(foundDifference){
                return false;
            }
            foundDifference = true;
        }
    }
    return true;
}
boolean oneEditInsert(String s1, String s2){
    int index1 = 0;
    int index2 = 0;
    while(index2 < s2.length() && index1 < s1.length()){
        if(s1.charAt(index1) != s2.charAt(index2)){
            if(index1!=index2){
                return false;
            }
            index2+;
        }
        else{
            index1++;
            index2++;
        }
    }
    return true;
}
```

解法 2： 只是把两个方法结合到了一起，感觉并不是很有必要

6. 压缩一个字符串
   把连续的重复的字符压缩生字符+数字的组合
   解法 1：用 String 来进行连接，这样效率不高，时间复杂度是 O(n+k\*k), k 是有多少个子序列（用 1+2+3+...k)来计算出的
   解法 2：用 StringBuilder

```java
String compress(String str){
    StringBuilder compressed = new StringBuilder();
    int countConsecutive = 0;
    for(int i = 0;i<str.length();i++){
        countConsecutive++;
        if(i+1 >= str.length()||str.charAt(i)!=str.charAt(i+1)){
            compressed.append(str.charAt(i));
            compressed.append(countConsecutive);
            countConsecutive = 0;
        }
    }
    return compressed.length() < str.length()?compressed.toString():str;
}
```

解法 3：用 StringBuilder
先检查一遍

```java
String compress(String str){
    // check final length and return input string if it would be longer
    int finalLength = countCompression(str);
    if(finalLength >= str.length()) return str;
    StringBuilder compressed = new StringBuilder(finalLength);
    int countConsecutive = 0;
    for(int i = 0;i<str.length();i++){
        countConsecutive++;
        if(i+1>=str.length()||str.charAt(i)!=str.charAt(i+1)){
            compressed.append(str.charAt(i));
            compressed.append(countConsecutive);
            countConsecutive = 0;
        }
    }
    return compressed.toString();
}
int countCompression(String str){
    int compressedLength = 0;
    int countConsecutive = 0;
    for(int i = 0;i<str.length();i++){
        countConsecutive++;
        if(i+1>=str.length()||str.charAt(i)!=str.charAt(i+1)){
            compressedLength += 1 + String.valueOf(countConsecutive).length();
            countConsecutive = 0;
        }
    }
return compressedLength;
}
```

7. 把一个矩阵顺时针旋转 90 度
   思路:一层一层地进行旋转，从内向外
   O(n\*n)

```java
boolean rotate(int[][] matrix){
    if(matrix.length == 0||matrix.length!=matrix[0].length) return false;
    int n = matrix.length;
    for(int layer = 0;layer<n/2;layer++){
        int first = layer;
        int last = n-1-layer;
        for(int i = first; i<last; i++){
            int offset = i-first;
            int top = matrix[first][i];
            // left -> top
            matrix[first][i] = matrix[last-offset][first];
            // bottom -> left
            matrix[last-offset][first] = matrix[last][last-offset];
            // right -> bottom
            matrix[last][last-offset] = matrix[i][last];
            // top -> right
            matrix[i][last] = top;
        }
    }
    return true;
}
```

8.一个矩阵中如果一行中或者一列中有一个 0，则这一行或者这一列全翻为 0
思路：如果每次发现一个就直接设置的话，会导致多设置(因为分不清是之前为 0 还是被设置成 0)
可以用一个一模一样大小的矩阵进行记录，但是没有必要用矩阵，用两个数组即可

```java
void setZeros(int[][] matrix) {
    boolean[] row = new boolean[matrix.length];
    boolean[] column = new boolean[matrix[0].length];

    for(int i = 0;i<matrix.length;i++){
       for(int j = 0;j<matrix[0].length;j++){
           if(matrix[i][j] == 0){
              row[i] = true;
              column[j] = true;
            }
       }
   }
for(int i = 0;i< row.length;i++){
    if(row[i]) nullifyRow(matrix,i);
}
for(int i = 0;i< column.length;i++){
    if(row[i]) nullifyColumn(matrix,i);
}
}
void nullifyRow(int[][] matrix, int row){
    for(int j = 0;i<matrix[0].length;j++){
        matrix[row][j] = 0;
    }
}

void nullifyColumn(int[][] matrix, int col){
    for(int j = 0;i<matrix.length;j++){
        matrix[i][col] = 0;
    }
}
```

解法 2：如果要求 O(1)的空间，可以先用两个值记录下来第一行和第一列有没有 0，然后用这两行来存储后面的情况

9. 判断 s2 是不是 s1 的一个旋转, 而且只能用一次 subString 函数
   例如 S1 = "waterBottle" = xy, S2 = "erBottlewat" = yx
   x = erBottle, y = wat
   所以如果是一个旋转的话，s2（即 yx）一定是 S1S1(即 xyxy) 的一个子序列

```java
   boolean isRotation(String s1, String s2){
       int length = s1.length();
       if(len == s2.length() && len > 0){
           String s1s1 = s1 + s1;
           return isSubString(s1s1, s2);
       }
    return false;
   }
```
