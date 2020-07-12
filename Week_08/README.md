学习笔记
## 排序分类
### 比较类排序：
- 通过比较来决定元素间的相对次序，由于其时间复杂度不能突破`O(nlogn)`，因此也称为非线性时间比较类排序。

### 非比较类排序：
- 不通过比较来决定元素间的相对次序，它可以突破基于比较排序的时间下界，`以线性时间运行`，因此也称为线性时间非比较类排序。
- 缺点 一般来说只能对于整型相关的数据类型进行排序，**对字符串以及对象之间的排序无能为力。** 使用额外的内存空间。
- 
[image:DB0BFBD5-AE0A-4947-8E68-A6A87398F907-22745-000020E32AC3852D/849589-20180402133438219-1946132192.png]
### 快速排序
- 数组取标杆 pivot, 将小元素放到pivot左边，大元素放右侧
- 然后依次对左右两边的子数组继续快排，以达到整个序列有序。

```python
    def quickSort(arr, begin, end):
        if end <= begin: return
        pivot = partition(arr, begin, ends)
        quickSort(arr, begin, pivot-1)
        quickSort(arr, pivot + 1, end)
    
    def partition(arr, begin, end):
        li, pivot = begin, end
        for i in range(begin, end):
            if arr[i] < arr[pivot]:
                arr[i],arr[li] = arr[li], arr[i]
                li += 1
        arr[li], arr[pivot] = arr[pivot], arr[li]
        return li
              
```
### 归并排序
- 把长度为N的输入序列分成两个长度为 n/2 的子序列；
- 对这两个子序列分别采用归并排序
- 将两个排序好的子序列合并成一个最终排序序列

```python
    def merge( nums, start, mid, end):
        l, r = start, mid+1
        res = []
        while l <= mid and r <= end:
            if nums[l] >= nums[r]:
                res.append(nums[r])
                r += 1
            else:
                res.append(nums[l])
                l += 1
        nums[start:end+1] = res + nums[l:mid+1] + nums[r:end+1]

    def mergesort( nums, start, end):
        if start >= end:
            return 0
        mid = start + (end - start) // 2
        mergesort(nums, start, mid)
        mergesort(nums, mid+1, end)
        merge(nums, start, mid, end)
# -------------------
    def merge_sort(arr):
    """归并排序"""
    if len(arr) == 1:
        return arr
    # 使用二分法将数列分两个
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # 使用递归运算
    return marge(merge_sort(left), merge_sort(right))
def marge(left, right):
    """排序合并两个数列"""
    result = []
    # 两个数列都有值
    while len(left) > 0 and len(right) > 0:
        # 左右两个数列第一个最小放前面
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # 只有一个数列中还有值，直接添加
    result += left
    result += right
    return result
```
### 归并以及快排的比较
- 归并和快排具有相似性，但是步骤相反
- 归并: 先排序左右子数组，然后合并两个有序子数组
- 快排: 先调配出左右子数组，然后对于左右子数组进行排序

#  其他排序
### 选择
- 每次找最小值 放最前
```python
def selectSort(arr):
    for i in range(len(arr)-1):
        temp = i
        for j in range(i+1, len(arr)):
            if arr[temp] > arr[j]:
                temp = j
        arr[temp], arr[i] = arr[i], arr[temp]
    return arr
```

### 插入
- 找到对应的元素，插入合适的位置，保证前面的元素有序
```python
def insertSort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        for j in range(i-1, -1, -1):# 计数到-1 结束 但是不包括-1
            if  temp < arr[j]:  #如果第i个元素大于前i个元素中的第j个
                arr[j+1] = arr[j] #则第j个元素先后移1位
                arr[j] = temp #将i个元素赋值给空着的位置
            else:   #如果第i个元素小于等于前i个元素中的第j个则结束循环
                break
    return arr
```

### 冒泡
- 两两比较把较大的放后面
```python
def popSort(arr):
    for i in range(len(arr), 0, -1):
        for j in range(0,i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1],arr[j]
    return arr
```


#### 参考资料
- https://www.cnblogs.com/onepixel/p/7674659.html
- https://www.cnblogs.com/pythonbao/p/10800699.html


----------------------------
## 位操作
| 含义       | 运算符 | 示例 |
| :--------- | :--: | -----------: |
| 左移|  << |     0011 =>0110 |
| 右移   | >>  | 0110 => 0011|
|按位或 |/ | 0011 / 1011 => 1011 | 
|按位与 |& | 0011 & 1011 => 0011 | 
|按位取反 |~ | 0011 => 1100 | 
|按位异或(相同为0不同为1) |^ | 0011 ^1011 => 1000 | 

###  XOR - 异或
异或：相同为0，不同为1。也可以用”不进位加法“ 来理解
异或操作的特点：
```python
x ^ 0 = x
x ^ 1s = ~x # 1s = ~0
x ^(~x) = 1s
x ^ x = 0
c = a^b => a^c = b, b^c = a #交换两个数
a^b^c = a^(b^c)= (a^b)^c

```
### 指定位置的位运算
1. 将x最右边的n位清零： x & (~0<<n)
- 获取x的第n位值（0或者1）：（x>>n)&1
- 获取x的第n位的幂值：x&(1<<n)
- 仅将第n位置为1：x|(x<<n)
- 仅将第n位置为0：x&(~(1<<n))
- 将x最高位至第n位(含)清零： x&((1<<n)-1)

### 实战位运算要点
- 判断奇偶：
   - x%2==1--> (x&1)==1
   - x%2==0--> (x&1)==0
- x>>1-->x/2
   - 即： x=x/2 --> x=x>>1  
   - eg: mid= (left + right) / 2 --> (left + right) >> 1
- x=x&(x-1)清零最低位的1
- x&-x=>得到最低位的1
- x&~x=>0

