---
title: "CTCI4-LinkedList"
author: "linna.li"
tags: ["data-structure"]
categories: ["book"]
date: 2021-02-07
---
# 基础知识
1. 注意null, 头节点，尾节点
2. Runner技术，即两个指针，一快一慢
3. 递归解法总需要至少O(n)的空间
4. 需要移除元素的时候都要保存一个previous节点

# 题目
1. 从一个没有排序的链表中删除重复的元素（要求考虑不用多余空间的解法）
- 解法1: 使用多余空间来保存已经出现过的元素，HashSet就可以
```java
void deleteDups(LinkedListNode n){
    // 应该确认一下是不是都是数字
    HashSet<Integer> set = new HashSet<Integer>();
    LinkedListNode previous = null;
    while(n!=null){
        if(set.contains(n.data)){
            previous.next = n.next;
        }else{
            set.add(n.data);
            previous = n;
        }
    }
    n = n.next;
}
```
- 解法2: 不使用多余空间，就要对每个节点查一下全部的list，时间复杂度是O(n*n)
```java
void deleteDups(LinkedListNode head){
    LinkedListNode current = head;
    while(current!=null){
        LinkedListNode runner = current;
        while(runner.next!=null){
            if(runner.next.data == current.data){
                runner.next = runner.next.next;
            }else{
                runner = runner.next;
            }
        }
        current = current.next;
    }
}
```
2. 查找倒数第k个节点
- 如果知道长度，可以直接计算出是正数第(length - k)个元素，所以走 (length-k-1)步就可以
- 递归解法
  - 解法1: 在找到结尾的时候返回, 但是不能返回那个节点，只能输出
  ```java
  int printKthToLast(LinkedListNode head, int k){
      if(head==null){
          return 0;
      }
      int index = printKthToLast(head.next, k)+1;
      if(index==k){
          System.out.println(k + "th to last node is" + head.data);
      }
      return index;
  }
  ``` 
  - 解法2: 
  ```C++
  node* nthToLast(node* head, int k, int& i){
      if(head==NULL){
          return NULL;
      }
      // 第一次返回是到了末尾
      node* nd = nthToLast(head->next, k, i);
      // i = 1 表示倒数第1个
      i = i + 1;
      if(i == k){
          return head;
      }
      return nd;
  }
  node* nthToLast(node* head, int k){
      int i = 0;
      return nthTolast(head, k, i);
  }
  ```
  - 解法3: 
  ```java
  // 用一个class来保存counter和index
  class Index {
      public int value = 0;
  }
  LinkedListNode kthToLast(LinkedListNode head, int k) {
      Index idx = new Index();
      return kthIndex(head, k, idx)
  }
  LinkedListNode kthToLast(LinkedListNode head, int k, Index idx) {
      if(head==null){
          return null;
      }
      LinkedListNode node = kthToLast(head.next, k, idx);
      idx.value = idx.value+1;
      if(idx.value == k){
          return head;
      }
      return node;
  }
  ```

- 非递归解法（两个指针）　
```java
LinkedListNode nthToLast(LinkedListNode head, int k){
    LinkedListNode p1 = head;
    LinkedListNode p2 = head;
    for(int i = 0; i<k; i++){
        if(p1==null){
            return null;
        }
        p1 = p1.next;
    }
    while(p1!=null){
        p1 = p1.next;
        p2 = p2.next;
    }
    return p2;
}
```

3. 删除中间的一个节点。注意这个题没有给第一个节点，只给了中间的节点
```java
// 可以删除下一个节点，然后把下一个节点的值给当前的节点
// 注意这种做法没办法解决如果被删节点是最后一个节点的情况。
boolean deleteNode(LinkedListNode n){
    if(n==null||n.next==null){
        return false;
    }
    LinkedListNode next = n.next;
    n.data = next.data;
    n.next = next.next;
    return true;
}
```

4.  给一个list和一个目标值，要求调整这个list按照目标值分成两部，目标值在后半部分，不用排序。
// 可以直接新建两个linkedlist，先分开，然后连起来
// 或者直接向 *头尾两个方向* 加上节点
```java
LinkedListNode partition(LinkedListNode node, int x) {
    LinkedListNode head = node;
    LinkedListNode tail = node;

    while(node!=null){
        LinkedListNode next = node.next;
        if(node.data < x){
            node.next = head;
            head = node;
        }else{
            tail.next = node;
            tail = node;
        }
        node = next;
    }
    tail.next = null;
    return head;
}

```