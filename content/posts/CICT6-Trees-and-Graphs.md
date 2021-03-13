---
title: "CTCI6-Trees-and-graphs"
author: "linna.li"
tags: ["data-structure"]
categories: ["book"]
date: 2021-03-08
---

# 基础知识

1. 树：Binary Tree, Binary Search Tree, 平衡与非平衡， 完全二叉树，满二叉树，完美二叉树，三种遍历方式，二叉堆（大顶堆和小顶堆），
2. 前缀树：用\*来表示是一个完整的单词了，可以用来进行快速的前缀搜索
3. 图：树是一种没有环的图。 acyclic 无环
4. 有两种方式经常用来表示图：adjacent 临近的。a(推荐).用 Node 来表示图中所有的点，node 里面有与他相连的其他 Node；b.邻接矩阵表示 matrix[i][j]
5. 图的搜索：深度优先（适用于如果我们想访问所有 node） 广度优先（适用于找指定两个点中间的最短路径）
6. 两个方向的搜索：两个起点一起开始找

# 题目

1. 有向图，找两个点之间是否有 route

```java
// 广度优先搜索
enum State{ Unvisited, Visited, Visiting}

boolean search(Graph g, Node start,Node end){
    if(start == end) return true;
    LinkdList<Node> q = new LinkedList<Node>();
    for(Node u:g.getNodes()){
        u.state = State.Unvisited;
    }
    start.state = State.Visiting;
    q.add(start);
    Node u;
    while(!q.isEmpty()){
        u = q.removeFirst();
        if(u!=null){
            for(Node v:u.getAdjecent()){
                if(v.state == State.Unvisited){
                    if(v == end){
                        return true;
                    }else{
                        v.state = State.Visiting;
                        q.add(v);
                    }
                }
            }
            u.state = State.Visited;
        }
    }
    return false;
}
```

2. 最小高度的树

```java
// 中间的点作为跟节点，小的放左边，大的放右边

TreeNode createMinimalBST(int array[]){
    return createMinimalBST(array, 0, array.length - 1);
}

TreeNode createMinimalBTS(int arr[], int statr, int end){
    if(end < start){
        return null;
    }
    int mid = (start+end)/2;
    TreeNode n = new TreeNode(arr[mid]);
    n.left = createMinimalBST(arr, start, mid - 1);
    n.right = createMinimalBST(arr, mid + 1, end);
    return n;
}
```

3. 每一层转换为一个 list

```java
// 广度遍历
ArrayList<LinkedList<TreeNode>> createLevelLinkedList(TreeNode root){
    ArrayList<LinkedList<TreeNode>> result = new ArrayList<LinkedList<TreeNode>> ();
    // visite the node
    LinkedList<TreeNode> current = new LinkedList<TreeNode>();
    if(root!=null){
        current.add(root);
    }
    while(current.size()>0){
        result.add(current); // add previous level
        // 作为parents，去找下一层的
        LinkedList<TreeNode> parents = current;
        // 创建一个空的list来装下一层
        current = new LinkedList<TreeNode>();
        for(TreeNode parent : parents){
            // visit children
            if(parent.left!=null){
                current.add(parent.left);
            }
            if(parent.right!=null){
                current.add(parent.right);
            }
        }
    }
    return result;
}
// 前序遍历实现
void createLevelLinkedList(TreeNode root, ArrayList<LinkedList<TreeNode>> lists, int level){
    if(root == null) return null;
    LinkedList<TreeNode> list = null;
    if(lists.size() == level){ // 说明目前的这层没有在lists里面
        // 新的一层
        list = new LinkedList<TreeNode>();
        lists.add(list);
    }else{
        list = lists.get(level);
    }
    list.add(root); // 把自己加进去
    createLevelLinkedList(root.left,lists,level+1);
    createLevelLinkedList(root.right, lists, level+1);
}

ArrayList<LinkedList<TreeNode>> createLevelLinkedList(TreeNode root){
    ArrayList<LinkedList<TreeNode>> lists = new ArrayList<LinkedList<TreeNode>>();
    createLevelLinkedList(root, lists, 0);
    return lists;
}
```

4. 检查一颗树是否平衡

```java
// 递归
int getHeight(TreeNode root){
    if(root==null){
        return -1;
    }
    return Math.max(getHeight(root.left),getHeight(root.right)) +1;
}
boolean isBalanced(TreeNode root){
    if(root==null) return true;
    int heighDiff = getHeight(root.left) - getHeight(root.right);
    if(Math.abs(heightDiff)>1){
        return false
    }else{
        return isBalanced(root.left)&&isBalanced(root.right);
    }
}
// 因为要计算多次树的高度，所以效率不是很高。时间复杂度是O(NlogN)

```

改进

```java
int checkHeight(TreeNode root){
    if(root==null) return -1;
    int leftHeight = checkHeight(root.left);
    if(leftHeight == Integer.MIN_VALUE) return Integer.MIN_VALUE;
    int rightHeight = checkHeight(root.right);
    if(rightHeight == Integer.MIN_VALUE) return Integer.MIN_VALUE;

    int heightDiff = leftHeight - rightHeight;
    if(Math.abs(heightDiff) >1){
        // 发现不是balanced的时候就马上中断
        return Integer.MIN_VALUE;
    }else{
        // 只有在balanced的时候才返回高度
        return Math.max(leftHeight, rightHeight) +1;
    }
}
boolean isBalanced(TreeNode root){
    return checkHeight(root)!=Integer.MIN_VALUE;
}
```

4.5 检查一棵树是不是二叉搜索树
