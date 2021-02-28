---
title: "CTCI4-LinkedList"
author: "linna.li"
tags: ["data-structure"]
categories: ["book"]
date: 2021-02-07
---

# 基础知识

1. 注意 null, 头节点，尾节点
2. Runner 技术，即两个指针，一快一慢
3. 递归解法总需要至少 O(n)的空间
4. 需要移除元素的时候都要保存一个 previous 节点

# 题目

1. 从一个没有排序的链表中删除重复的元素（要求考虑不用多余空间的解法）

- 解法 1: 使用多余空间来保存已经出现过的元素，HashSet 就可以

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

- 解法 2: 不使用多余空间，就要对每个节点查一下全部的 list，时间复杂度是 O(n\*n)

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

2. 查找倒数第 k 个节点

- 如果知道长度，可以直接计算出是正数第(length - k)个元素，所以走 (length-k-1)步就可以
- 递归解法

  - 解法 1: 在找到结尾的时候返回, 但是不能返回那个节点，只能输出

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

  - 解法 2:

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

  - 解法 3:

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

4.  给一个 list 和一个目标值，要求调整这个 list 按照目标值分成两部，目标值在后半部分，不用排序。
    // 可以直接新建两个 linkedlist，先分开，然后连起来
    // 或者直接向 _头尾两个方向_ 加上节点

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

5. 给两个链表代表两个倒序的数字，求这两个数字的和
   // 思路：用递归。注意进位最多为 1；递归的返回值是当前位置上的数

```java
LinkedListNode addLists(LinkedListNode l1, LinkedListNode l2, int carry){
    if(l1==null && l2==null && carry== 0){
        return null;
    }

    LinkedListNode result = new LinkedListNode();
    int value = carry;
    if(l1!=null){
        value+=l1.data;
    }
    if(l2!=null){
        value+=l2.data;
    }
    result.data = value%10;
    if(l1!=null||l2!=null){
        LinkedListNode more = addLists(l1==null?null:l1.next, l2==null?null:l2.next, value >=10?1:0);
        result.setNext(more);
    }
    return result;
}
```

注意如果是正序的，首先是向右对齐的，需要前面填上 0。

```java
class PartialSum {
    public LinkedListNode sum = null;
    public int carry = 0;
}

LinkedListNode addLists(LinkedListNode l1, LinkedListNode l2){
    int len1 = length(l1);
    int len2 = length(l2);

    if(len1<len2>){
        l1 = padList(l1,len2-len1);
    } else{
        l2 = padList(l2,len1-len2);
    }
}

PartialSum sum = addListsHelper(l1,l2);
// 如果有一个carry value，要把它插入到链表最前面
if(sum.carry == 0){
    return sum.sum;
}else{
    LinkedListNode result = insertBefore(sum.sum,sum.carry);
    return result;
}

PartialSum addListHelper(LinkedListNode l1, LinkedListNode l2){
    if(l1==null&&l2==null){
        PartialSum sum = new PartialSum();
        return sum;
    }
    PartialSum sum = addListsHelper(l1.next,l2.next);
    int val = sum.carry + l1.data + l2.data;
    LinkedListNode full_result = insertBefore(sum.sum, val%10);
    sum.sum = full_result;
    sum.carry = val/10;
    return sum;
}

LinkedListNode padList(LinkedListNode l, int padding){
    LinkedListNode head = l;
    for(int i = 0;i<padding;i++){
        head = insertBefore(head,0);
    }
    return head;
}

LinkedListNode insertBefore(LinkedListNode list, int data){
    LinkedListNode node = new LinkedListNode(data);
    if(list!=null){
        node.next = list;
    }
    return node;
}
```

6. 检查一个链表是不是回文的
   三种解法：
   解法 1：反转这个链表，与原来的链表进行比较

   ```java
   boolean isPalindrome(LinkedListNode head){
       LinkedListNode reversed = reverseAndClone(head);
       return isEuqal(head, reversed);
   }
   LinkedListNode reverseAndClone(LinkedListNode node){
       LinkedListNode head = null;
       while(node !=null){
           LinkedListNode n = new LinkedListNode(node.data);
           n.next = head;
           head = n;
           node = node.next;
       }
       return head;
   }
   ```

   解法 2：用快慢指针的方法找到中点，然后弹出来进行比较

   ````java
   boolean isPalindrome(LinkedListNode head){
       LinkedListNode fast = head;
       LinkedListNode slow = head;

       Stack<Integer> stack = new Stack<Integer>();
       while(fast!=null&&fast.next!=null){
           stack.push(slow.data);
           slow = slow.next;
           fast = fast.next.next;
       }
       // slow代表后半部分
       if(fast!=null){
           slow = slow.next;
       }
       while(slow != null){
           int top = stack.pop().intvalue();
           if(top!=slow.data){
               return false;
           }
           slow = slow.next;
       }
       return true;
   }
   ```java
   解法 3：先求出长度，然后用递归求解
   boolean isPalindrome(LinkedListNode head){
       int length = lengthOfList(head);
       Result p = isPalindromeRecurse(head,length);
       return p.result;
   }

   Result isPalindromeRecurse(LinkedListNode head,int length){
       if(head==null || length <=0){
           return new Result(head,true);
       } else if(length == 1){
           return new Result(head.next,true);
       }
       Result res = isPalindromeRecurse(head.next, length-2);
       if(!res.result || res.node == null){
           return res;
       }
       res.result = (head.data == res.node.data);
       res.node = res.node.next;

       return res;
   }

   int lengthOfList(LinkedListNode n){
       int size = 0;
       while(n!=null){
           size++;
           n = n.next;
       }
       return size;
   }
   ````

7. 检查两个链表是不是相交的
   思路 1：可以直接用一个 HashSet，把第一个的点放进去，然后遍历第二个链表
   思路 2：首先得到长度，然后去相同的位置开始找到第一个相同的位置，找到之后比较是不是后面完全一致的

```java
LinkedListNode findIntersection(LinkedListNode list1,LinkedListNode list2){
    if(list1 == null || list2 == null){
        return null;
    }
    Result result1 = getTailAndSize(list1);
    Result result2 = getTailAndSize(list2);

    if(result1.tail != result2.tail){
        return null;
    }

    LinkedListNode shorter = result1.size < result2.size ? list1 : list2;
    LinkedListNode longer = result1.size < result2.size ? list2:list1;

    longer = getKthNode(longer, Math.abs(result1.size-result2.size));

    while(shorter != longer){
        shorter = shorter.next;
        longer = longer.next;
    }
    return longer;
}


```

8. 检查一个链表中是不是有环的
   思路： a.如果有环，那么快慢指针必定相交（可以用反证法来证明慢指针不会刚好跳过快指针）
   b.延伸：找到环的起点。记住相遇的点回到环入口的距离 = 链表开始的位置到环的入口

```java
LinkedListNode findBeginning(LinkedListNode head){
    LinkedListNode slow = head;
    LinkedListNode fast = head;

    while(fast!=null&&fast.next!=null){
        slow = slow.next;
        fast = fast.next.next;
        if(slow == fast){
            break;
        }
    }

    if(fast==null||fast.next==null){
        return null;
    }

    slow = head;
    while(slow != fast){
        slow = slow.next；
        fast = fast.next;
    }
    return fast;
}
```
