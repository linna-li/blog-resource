---
title: "CTCI11-sorting-and-searching"
author: "linna.li"
tags: ["algorithem"]
categories: ["book"]
date: 2021-04-30
---
冒泡排序：时间复杂度 O(n^2), 空间复杂度 O(1)
选择排序：时间复杂度 O(n^2), 空间复杂度 O(1)
合并排序：时间复杂度 O(nlogn), 分成两边，然后merge，merge的时候需要比较
快速排序：时间复杂度 O(nlog(n)),最差 O(n^2),空间复杂度O(nlog(n))。随机取一个数字，比它小的放左边，比它大的放右边
```java
void quicksort(int[] arr, int left, int right){
    int index =  partition(arr, left, right);
    if(left<index-1){
      quickSort(arr, left, index-1);
    }
    if(index<right){
        quickSort(arr,index,right);
    }
}

int partition(int[] arr, int left, int right){
    int pivot = arr[(left+right)/2];
    while(left<=right){
        while(arr[left]<pivot){
            left++;
        }
        while(arr[right]>pivot){
            right--;
        }
        if(left<=right){
            swap(arr,left,right);
            left++;
            right--;
        }
    }
    return left;
}
```
Radix sort基数排序 Runtime: O(kn)

### Searching Algorithms
```java
int binarySearch(int[] a, int x){
    int low = 0;
    int high = a.length - 1;
    int mid;

    while(low <= high) {
        mid = (low + high) / 2;
        if(a[mid] < x){
            low = mid + 1;
        } else if (a[mid] > x) {
            high = mid - 1;
        } else {
            return mid;
        }
    }
    return -1;
}

int binarySearchRecursive(int[] a, int x, int low, int high){
    if(low > high) return -1;

    int mid = (low+high)/2;

    if(a[mid] < x) {
        return binarySearchRecursive(a, x, mid + 1, high);
    } else if (a[mid] > x) {
        return binarySearchRecursive(a, x, low, mid - 1);
    } else {
        return mid;
    }
}
```