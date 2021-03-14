---
title: "CTCI5-stacksAndQueues"
author: "linna.li"
tags: ["data-structure"]
categories: ["book"]
date: 2021-02-11
---

# 基础知识
1. stack: 后进先出
2. stack 不能在一个固定的时间内找到第几个元素，但是可以简单的插入和移除，用linkedlist可以来实现一个stack
```java
public class Mystack<T> {
    private static class StackNode<T> {
        private T data;
        private StackNode<T> next;

        public StackNode(T data) {
            this.data = data;
        }
    }
    private StackNode<T> top;

    public T pop() {
        if(top == null) throw new EmptyStackException();
        T item = top.data;
        top = top.next;
        return item;
    }

    public void push(T item){
        StackNode<T> t = new StackNode<T>(item);
        t.next = top;
        top = t;
    }

    public T peek(){
        if(top==null) throw new EmptyStackException();
        return top.data;
    }
    
    public boolean isEmpty(){
        return top==null;
    }
}
```
3. Queue: 先进先出
```java
public class MyQueue<T>  {
    private static class QueueNode<T> {
        private T data;
        private QueueNode<T> next;

        public QueueNode(T data) {
            this.data = data;
        }
    }

    private QueueNode<T> first;
    private QueueNode<T> last;

    public void add(T item) {
        QueueNode<T> t = new QueueNode<T> (item);
        if(last!=null){
            last.next = t;
        }
        last = t;
        if(first == null){
            first = last;
        }
    }

    public T remove() {
        if(first == null) throw new NoSuchElementException();
        T data = first.data;
        first = first.next;
        if(first==null){
            last = null;
        }
        return data;
    }

    public T peek(){
        if(first==null) throw new NoSuchElementException();
        return first.data;
    }

    public boolean isEmpty(){
        return first==null;
    }
}
```
# 题目
1. 用一个array实现三个栈
思路： 计算