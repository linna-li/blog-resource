---
title: "CTCI5-stacks-and-queues"
author: "linna.li"
tags: ["data-structure"]
categories: ["book"]
date: 2021-03-06
---

# 基础知识

1. 注意栈的问题要检查有没有满，是不是空
2. shift 的意思是 对齐（移动）

# 题目

1. 用一个数组实现三个栈

- 解法 1: 如果可以三个栈的大小都固定，可以直接把数组划分成三部分即可

```java
class FixedMultiStack {
    private int numberOfStacks = 3;
    private int stackCapacity;
    private int[] values;
    private int[] sizes;

    public FixedMultiStack(int stackSize){
        stackCapacity = stackSize;
        values = new int[stackSize * numberOfStacks];
        sizes = new int[numberOfStacks];
    }

    public void push(int stackNum, int value) throws FullStackException {
        if(isFull(stackNum)){
            throw new FullStackException();
        }
        sizes[stackNum]++;
        values[indexOfTop(stackNum)] = value;
    }

    private int indexOfTop(int stackNum){
        // 开始位置
        int offSet = stackNum * stackCapacity;
        int size = size[stackNum];
        return offset + size - 1;
    }

    public int peek(int stackNum){
        if(isEmpty(stackNum)){
            throw new EmptyStackException();
        }
        return values[indexOfTop(stackNum)];
    }

    public int pop(int stackNum){
        if(isEmpty(stackNum)){
            throw new EmptyStackException();
        }
        int topIndex = indexOfTop(stackNum);
        int value = values[topIndex];
        values[topIndex]=0;
        sizes[stackNum]--;
        return value;
    }
}
```

- 解法 2: 要想更加灵活，如果一个满了可以 expand 扩充，扩充的意思就是去拿下一个 stack 的一个空间（下一个 stack 就少了一个空间）同时需要把下一 stack 进行移动（shift）如果下一个 stack 也满了就要去下下一个 stack 拿，两个 stack 都要进行 shift，以此类推。
  Note: java 在进行取余操作的时候会返回负数

```java
private void (int stackNum){
    shift((stack+1)%info.length);
    info[stackNum].capacity++;
}

private void shift(int stackNum){
    StackInfo stack = info[stackNum];
    if(stack.size >= stack.capacity){
        int nextStack = (stackNum + 1)%info.length;
        shift(nextStack);
        stack.capacity++;
    }

    int index = stack.lastCapacityIndex();
    // 是不是属于当前stack的元素，是的话，需要移动
    while(stack.isWithinStackCapacity(index)){
        values[index] = values[previousIndex(index)];
        index = previousIndex(index);
    }
}
```

2. 返回当前 stack 中的最小元素

用另外的一个栈保存最小的元素，注意在入栈的时候使用 <= ,  
当前的 stack 如果 pop 的元素是小栈中的顶部元素的时候，才把小栈中的元素 pop 出来一个

```java
public class StackWithMin2 extends Stack<Integer> {
    Stack<Integer> s2;
    public StackWithMin2(){
        s2 = new Stack<Integer>();
    }

    public void push(int value){
        if(value <= min()){
            s2.push(value);
        }
        super.push(value);
    }

    public int pop(){
        if(!super.isEmpty){
            int value = super.pop();
            if(value <= min){
                s2.pop();
            }
            return value;
        }
    }

    public int min(){
        if(s2.isEmpty()){
            return Integer.MAX;
        }
        return s2.peek();
    }
}
```

3. 每一个栈有固定的容量，超过之后需要建立新的栈
   思路：只需要每次 push 的时候检查一下当前的栈是不是已经满了。每次 pop 的时候检查结束之后是不是已经空了，空了之后就要删除这个栈
   拓展：实现 popAt(index). 需要注意是否需要把这个栈上面的其他栈的底部的元素补充进来（shift）

```java
public int leftShift(int index, boolean removeTop){
    Stack stack = stacks.get(index);
    int removed_item;
    if(removeTop) removed_item = stack.pop();
    else removed_item = stack.removeBottom();
    if(stack.isEmpty()){
        stacks.remove(index);
    }else if(stacks.size() > index + 1){
        int v = leftShift(index+1,false);
        stack.push(v);
    }
    return removed_item;
}
```

4. 用两个栈实现队列
   思路：每次 take 的时候需要把第一个栈里面的都放进第二个栈里面去，然后取出最上面的。
   节约时间复杂度的方法：在 take 的时候，只有第二个栈是空的时候，才把第一个栈的都放进来，否则直接从第二个栈取即可。

5. 排序一个栈，可以用一个栈作为辅助栈
   Note：首先需要理解题意，已经有了一个栈，只需要实现排序函数

2 1 3 4
4 进去，3 进去，1 进去，2 比 1 大，所以 2 出来先到一个 temp 中，1 回到第一个栈中，2 进去

6 5 3 4 2 1
1 进去 2 比 1 大 2 到 temp，1 回去，2 进去 1 进去
4 比 1 大，4 到 temp，1 回去，4 比 2 大，2 回去，4 进去

6. 动物领养站。要求实现领养一只猫，领养一只狗，领养一只动物。最先到领养站的动物要最先被领养，所以是一个队列。
   思路：直接用一个大类保存两个 ArrayList。动物用一个带着时间戳的类实现。

```java
class AnimalQueue(){
    ListedList<Dog> dogs = new LinkedList<Dog>();
    ListedList<Cat> cats = new LinkedList<Cat>();
    private int order = 0;
}

abstract class Animal {
    private int order;
    protected String name;
}

public class Dof extends Animal {
    public Dog(String n){
        super(n);
    }
}
```
