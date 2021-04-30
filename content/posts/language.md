---
title: "Language"
author: "linna.li"
tags: ["Language"]
categories: ["book"]
date: 2021-05-04
---
# C++ Note
1. 注意要删除指针 delete p
2. 所有的对象和方法默认都是default的，需要指定为public
3. 构造函数会被自动call，会有一个默认的
4. 静态绑定：编译阶段函数被编译出来，Person * p = new Student(); 会调用到父类的方法。如果定义虚函数，会确保使用子类的方法. 也可以像抽象函数一样用
5. 虚的destructor：确保删除父类和子类
6. 默认值（类似kotlin的）
7. 重载运算符
8. 指针和参考：rederences不可以是空，不可以被重新assign给另外的地方
9. 数组的指针指向第一个元素
10. Templates, 可以用来声明成为不同的type

# Java Note
1. Overloading（两个方法名字相同但是参数不同）
2. Overriding: 子类与父类
3. ArrayList与Vector: Vector是线程安全的，ArrayList不是线程安全的。
4. ArrayList与LinkedList: ArrayList可以指定下标，LinkedList要用iterator()
5. Thread: 
两种实现方式，实现Runnable的接口，继承Thread这个class
```java
public class RunnableThreadExample implements Runnable {
    public int count = 0;
    public void run() {
        System.out.println("RunnableThread starting.");
        try {
            while(count < 5){
                Thread.sleep(500);
                count++;
            }
        } catch(InterrruptedException exc){
             System.out.println("RunnableThread interrupted.");
        }
         System.out.println("RunnableThread terminating.");
    }
}

public static void main(string[] args){
    RunnableThreadExample instance = new RunnableThreadExample();
    Thread thread = new Thread(instance);
     Thread thread = new Thread();
    while(instance.count!=5){
        try{
            Thread.sleep(250);
        } catch(InterruptedException exc){
            exc.printStackTrace();
        }
    }
}
```
继承thread
```java
public class ThreadExample extends Thread {
    int count = 0;
    public void run(){
        System.out.println("Thread starting.");
        try {
            while(count < 5){
                Thread.sleep(500);
                System.out.println("In thread, count is "+count);
                count++;
            }
        } catch(InterruptedException exc){
            System.out.println("Thread interrupted.");
        }
        System.out.println("Thread terminating.");      
    }
}

public class ExampleB {
    public static void main(String args[]){
        ThreadExample instance = new ThreadExample();
        instance.start();
        while(instance.count != 5){
            try{
                Thread.sleep(250);
            } catch (TnterruptedException exc){
                exc.printStackTrace();
            }
        }
    }
}
```
两种方法的比较：
实现Runnable的接口更还好：因为java中不能多继承，所以继承了Thread之后的类就不能再继承其他的类；Thread中内容太多，可能只需要runnable
6. Synchronization（同步化）和锁:
用关键词 synchronized来限制多个线程对于一个方法和code的使用
静态方法的 synchronized是在class层级上的。所以如果有一个object，执行它的static方法，即使是两个不同的方法，如果加了synchronized，也不可以同时执行
```java
public class MyClass extends Thread {
    private String name;
    private MyObject myObj;

    public MyClass(MyObject obj,String n){
        name = n;
        myObj = obj;
    }

    public void run(){
        myObj.foo(name);
    }
}

public class MyObject{
    public synchronized void foo(String name) {
        try {
            System.out.println("Thread" + name + ".foo():starting");
            Thread.sleep(3000);
            System.out.println("Thread" + name + ".foo():ending");
        } catch (InterruptedException exc) {
            System.out.println("Thread " + name + ": interrupted");
        }
    }
}

// 加到块上
public class MyClasss extends Thread {
    public void run(){
        myObj.foo(name);
    }
}

public class MyObject {
    public void foo(String name){
        synchronized(this){
            ...
        }
    }
}
```

# Locks
ReentrantLock可以替代synchronized进行同步；
ReentrantLock获取锁更安全；
# 死锁与预防死锁

# 栈和堆
栈（stack）： 基本类型的变量和对象的引用变量在函数的栈内存中分配，满了就会释放。主要用来执行程序。存在栈中的数据可以共享，即虚拟机发现有了 int a = 3, 这时候再有 int b = 3, 就不会再去创建了
堆（heap）： 用于存放用new来创建的对象，在堆中分配的内存，由java虚拟机自动垃圾回收器来管理。主要用来存放对象
JVM是基于堆栈的虚拟机，JVM为每个新创建的线程都分配一个堆栈。每一个Java应用都唯一对应一个JVM实例，每一个实例唯一对应一个堆。

