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

4.5 检查一棵树是不是二叉搜索树(等于的情况要在左边子树)
如果没有重复的元素，可以直接进行中序遍历，然后结果存在一个数组中，看这个数组是不是单调递增的
```java 我的
boolean isSearchTree(TreeNode node){
    List<Integer> finalList = new ArrayList<>();
    addInList(node.left,finalList);
    finalList.add(node.value);
    addInList(node.right,finalList);
    for(int i = 0;i<finalList.length()-1;i++){
        if(finalList.get(i+1)<finalList.get(i)){
            return false;
        }
    }
    return true;
}
void adddInList(TreeNode node, List<Integer> finalList){
    if(node==null){
        return;
    }
    if(node.left!=null){
         finalList.add(node.value);
    } else{
        adddInList(node.left, finalList)
    }
    if(node.right!=null){
        finalList.add(node.right, finalList);
    }
}
```
```java 答案
int index = 0;
boolean checkBST(TreeNode root){
    int[] array = new int[root.size];
    copyBST(root, array);
    for(int i = 1;i<array.length;i++){
        if(array[i] <= array[i-1]) return false;
    }
    return true;
}
void copyBST(TreeNode root, int[] array){
    if(root==null) return;
    copyBST(root.left,array);
    array[index] = root.data;
    index++;
    copyBST(root.right, array)
}
```
```java  优化，并不需要array，只需要判断新加的点和上一个点就行
Integer lastNumber = null;
boolean checkBTS(TreeNode n){
    if(n==null) return true;
    if(!checkBST(n.left)) return false;
    if(lastNumber != null && n.data <= lastNumber){
        return false;
    }
    lastNumber = n.data;
    if(!checkBST(n.righht)) return false;
    return true;
}
```
```java 另外一种解法，每次pass下去最大值和最小值
boolean checkBST(TreeNode n){
    return checkBST(n, null, null);
}
boolean checkBST(TreeNode n, Integer min, Integer max){
    if(n==null){
        return true;
    }
    if((min!=null&&n.data<=min)||(max!=null&&n.data>max)){
        return false;
    }
    if(!checkBST(n.left,min,n.data)||!checkBST(n.right,n.data,max)){
        return false;
    }
    return true;
}

```

4.6 中序遍历的情况下，找到下一个节点
```java
TreeNode inorderSucc(TreeNode n){
    if(n==null) return null;
    if(n.right!=null){
        return 
        leftMostChild(n.right);
    }else{
        TreeNode q = n;
        TreeNode x = q.parent;
        // 向上找一直到本身在一颗树的左子树上
        while(x!=null&&x.left!=q){
            q = x;
            x = x.parent;
        }
        return x;
    }
}
TreeNode lesfMostChild(TreeNode n){
    if(n==null){
        return null;
    }
    while(n.left!=null){
        n = n.left;
    }
    return n;
}
```
4.7 带有dependencies的项目解决方案
```java
// 解法1: 
// 1. 加入没有income的点
// 2. 移除所有依赖这个点的所有边
// 3. 重复1
// 需要的数据结构，每个点（包含依赖于这个点的其他点，这个点依赖的其他的点的个数）
public class Project{
    private ArrayList<Project> children = new ArrayList<Project>();
    private HashMap<String, Project> map = new HashMap<String, Project>();
    private String name;
    private int dependencies = 0;
    public Project(String n){name = n;}

    //  加自己的下一个节点，node是要依赖自己的
    public void addNeighbor(Project node){
        if(!map.containsKey(node.getName())){
            children.add(node);
            map.put(node.getName(),node);
            node.incrementDependencies();
        }
    }
}
public class Graph {
    private ArrayList<Project> nodes = new ArrayList<Project>();
    private HashMap<String, Project> map = new HashMap<String, Project>();

    public Project getOrCreateNode(String name){
        if(!map.containKey(name)){
            Project node = new Project(name);
            nodes.addd(node);
            map.put(name, node);
        }
        return map.get(name);
    }
    public void addEdge(String startName, String endName){
        Project start = getOrCreateNode(startName);
        Project end = getOrCreateNode(endName);
        start.addNeighbor(end);
    }
    public ArrayList<Project> getNodes(){return nodes;}
}

Project[] findBuildOrder(String[] projects, String[][] dependencies){
    Graph graph = buildGraph(projects, depedencies);
    return orderProjects(graph.getNodes());
}
Graph buildGraph(String[] projects,String[][] dependencies){
    Graph graph = new Graph();
    for(String project:projects){
        graph.createNode(project);
    }
    for(String[] dependency:dependencies){
        String first = dependency[0];
        String second = dependency[1];
        graph.addEdge(first, second);
    }
    return graph;
}

Project[] orderrProjects(ArrayList<Project> projects){
    Project[] order = new Project[projects.size()];
    // 把没有依赖的放进order里面
    int endOfList = addNonDependent(order, projects,0);

    int toBeProcessed = 0;
    while(toBeProcessed < order.length) {
        Project current = order[toBeProcessed];
        if(current == null){
            return null;
        }
        ArrayList<Project> children = current.getChildren();
        for(Project child : children){
            child.decrementDependencies();
        }
        endOfList = addNonDependent(order, children,endOfList);
        toBeProcessed++;
    }
    return order;
}
```
解法2: 用DFS







4.8 查找两个节点的最近的公共祖先
Solution #1: 如果有指向parents节点的指针
可以把两个节点先移动到相同的高度，然后同时向上移动
```java
TreeNode commonAncestor(TreeNode p, TreeNode q){
    int delta = depth(p) - depth(q);
    TreeNode first = delta > 0 ? q:p;
    TreeNode second = delta>0?p:q;
    second = goUpBy(second, Math.abs(delta));
    while(first != second && firsst !=null &&second!=null){
        first = first.parent;
        second = second.parent;
    }
    return first == null || second ==null?null:first;
}
```
Solution #2: 从任意一个节点开始向上找，但是只需要检查p不在的那一条子树。
如果找到一个cover了q的节点，那么这个节点就是公共祖先
```java
TreeNode commonAncestor(TreeNode root, TreeNode p, TreeNode q){
    if(!covers(root, p)||!covers(root, q)){
        return null;
    }else if(covers(p,q)){
        return p;
    }else if(covers(q,p)){
        return q;
    }
    TreeNode sibling = getSibling(p);
    TreeNode parent = p.parent;
    while(!covers(sibling,q)){
        sibling = getSibling(parent);
        parent = parent.parent;
    }
    return parent;
}
TreeNode getSibling(TreeNode node){
    if(node == null || node.parent == null){
        return null;
    }
    TreeNode parent = node.parent;
    return parent.left == node ? parent.right:parent.left;
}
```
Solution #3: 如果没有指向父母节点的时候
从根节点开始检查两个节点是不是在一边上，如果是在一边上，则需要继续往下找，如果不是在一边上就找到了
```java
TreeNode commonAncestor(TreeNode root, TreeNode p, TreeNode q){
    if(!covers(root, p)||!covers(root, q)){
        return null;
    }
    return ancestorHelper(root, p, q);
}
TreeNode ancestorHelper(TreeNode root, TreeNode p, TreeNode q){
    if(root == null || root == p|| root==q ){
        return root;
    }
    boolean pIsOnLeft = covers(root.left, p);
    boolean qIsOnLeft = covers(root.left, q);
    if(pIsOnLeft != qIsOnLeft){
        return root;
    }
    TreeNode childSide = pIsOnLeft?root.left:root.right;
    return ancestorHelper(childSide,p,q);
}
```
Solution #4: 因为解法3会存在重复检查的情况，所以可以进行优化
为了只遍历一边就判断出两个点的位置，当root的两边都有返回的时候，这个root就是最近的公共节点。
如果找到了一个，就返回找到的节点；
如果两个都没找到，说明不在；
如果两个都找到了，当前root节点就是公共的祖先节点；

Solution #5: Optimized
4有一个bug是无法区分一个节点是不是不存在的情况。
```java
TreeNode commonAncestor(TreeNode root, TreeNode p, TreeNode q){
    if(root == null) return null;
    if(root == p && root == q) return root;
    TreeNode x = commonAncestor(root.left, p, q);
    if(x!=null && y!=p && y!=q){
        return x;
    }
    TreeNode y = commonAncestor(root.right, p, q);
    if(y!=null&&y!=p&&y!=q){
        return y;
    }
    if(x!=null&&y!=null){
        return root;
    }else if (root==p||rppt==q){
        return root;
    }else{
        return x == null ? y:x;
    }
}
```
Fix bug
```java
class Result {
    public TreeNode node;
    public boolean isAncestor;
    public Result(TreeNode n, boolean isAnc){
        node = n;
        isAncestor = isAnc;
    }
}

TreeNode commonAncestor(TreeNode root, TreeNode p,TreeNode q){
    Result r = commonAncestorHelper(root,p,q);
    if(r.isAncestor){
        return r.node;
    }
    return null;
}

Result commonAncHelper(TreeNode root, TreeNode p, TreeNode q){
    if(root==null) return new Result(null, false);
    if(root == p && root == q){
        return new Result(root, true);
    }
    Result rx = commonAncHelper(root.left,p,q);
    if(rx.isAncestor){
        return rx;
    }
    Result ry = commonAncHelper(root.right,p.q);
    if(ry.isAncestor){
        return ry;
    }
    if(rx.node != null && ry.node!=null){
        return new Result(root,true);
    // root 是，而且又在root的子树中找到了一个，所以这个是合法的    
    }else if(root == p || root == q){
        boolean isAncestor = rx.node!=null||ry.node!=null;
        return new Result(root,isAncestor); 
    }else{
        // root 不是，但在root的子树中找到了一个，所以这个是不合法的 
        return new Result(rx.node!=null?rx.node:ry.node, false);
    }
}
```
4.9 查找能够形成一颗二叉搜索树的所有的数组
只要保证根节点相对于左右子树的所有节点在最前面即可，左右子树之间有大小差异，所以左右子树的节点可以位置无所谓，
但是同理，一颗子树里面一定要保证根节点在最前面

根 左根（左边子树的节点在这之后） 右根（右边子树的节点在这之后）
根 右根（右边子树的节点在这之后） 左根（左边子树的节点在这之后）

所以可以 左根+右根 所有组合，最后加上 根

weave(first, second, prefix)
因为要经常删除添加，所以适合用链表

```java
ArrayList<LinkedList<Integer>> allSequences(TreeNode node){
    ArrayList<LinkedList<Integer>> result = new ArrayList<LinkedList<Integer>>();
    if(node == null){
        result.add(new LinkedList<Integer>());
        retrun result;
    }
    LinkedList<Integer> prefix = new LinkedList<Integer>();
    prefix.add(node.data);

    ArrayList<LinkedList<Integer>> leftSeq = allSequences(node.left);
    ArrayList<LinkedList<Integer>> rightSeq = allSequences(node.right);

    for(LinkedList<Integer> left:leftSeq){
        for(LinkedList<Integer> right: rightSeq){
            ArrayList<LinkedList<Integer>> weaved = new ArrayList<LinkedList<Integer>> ();
            weaveLists(left, right, weaved, prefix);
            result.addAll(weaved); 
        }
    }
    return result;
}

void weaveLists(LinkedList<Integer> first, LinkedList<Integer> second, 
                ArrayList<LinkedList<Integer>> results, LinkedList<Integer> prefix){
    if(first.size() == 0 || second.size() == 0){
        LinkedList<Integer> result = (LinkedList<Integer>) prefix.clone();
        result.addAll(first);
        result.addAll(second);
        results.add(result);
        return;
    } 

    int headFirst = first.removeFirst();
    prefix.addLast(headFirst);
    weaveLists(first, second, results, prefix);
    prefix.removeLast();
    first.addFirst(headFirst);

    int headSecond = second.removeFiirst();
    prefix.addLast(headSecond);
    weaveLists(first, second, results,prefix);
    prefix.removeLast();
    second.addFirst(headSecond);
}
```
4.10 检查一棵树T2是不是一颗大树T1的子树
子树要求结构和数据完全一样的，所以不能通过中序遍历来检查。

比如说一颗搜索二叉树，中序遍历一定得到的是相同的有序数列，即使他的结构不一样
  3
1   4
X1X3X4X
    4
  3
1
X1X3X4X

前序遍历是可以的，但是要注意空指针不能不输出
```java
boolean containsTree(TreeNode t1, TreeNode t2){
    StringBuilder string1 = new StringBuilder();
    StringBuilder string2 = new StringBuilder();
    getOrderString(t1,string1);
    getOrderString(t2,string2);
    return string1.indexOf(string2.toString()) != -1;
}
void getOrderString(TreeNode node, StringBuilder sb){
    if(node == null){
        sb.append('X');
        return;
    }
    sb.append(node.data + " ");
    getOrderString(node.left,sb);
    getOrderString(node.right,sb);
}
```

Solution2: 从大树的跟节点开始，每次遇到和小树的跟节点一样的节点，就检查两树是不是完全一样的
```java
boolean containsTree(TreeNode t1, TreeNode t2){
    if(t2==null) return true;
    return subTree(t1,t2);
}
boolean subTree(TreeNode r1, TreeNode r2){
    if(r1 == null){
        return false;
    } else if(r1.data == r2.data && matchTree(r1,r2)){
        return true;
    }
    return subTree(r1.left, r2)|| subTree(r1.right,r2);
}
boolean matchTree(TreeNode r1, TreeNode r2){
    if(r1==null&&r2==null){
        return true
    } else if(r1==null||r2==null){
        return false;
    }else if(r1.data!=r2.data){
        return false;
    }else{
        return matchTree(r1.left, r2.left) && matchTree(r1.right, r2.right);
    }
}
```
