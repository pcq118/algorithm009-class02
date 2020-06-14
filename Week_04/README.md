# 递归
## 树的遍历
```python
def preorder(self, root):
    if root:
        self.traverse_path.append(root.val)         
        self.preorder(root.left)        
        self.preorder(root.right)

def inorder(self, root):
    if root:
        self.inorder(root.left) 
        self.traverse_path.append(root.val) 
        self.inorder(root.right)

def postorder(self, root):
    if root:
        self.postorder(root.left) 
        self.postorder(root.right) 
        self.traverse_path.append(root.val)
      
```

### 最基本的递归
计算 n!
n!= 1 * 2 * 3 * ... * n

```python 
def Factorial(n): 
    if n <= 1:
        return 1
    return n * Factorial(n — 1)
```
相当于：
factorial(6)
6 * factorial(5)
6 * (5 * factorial(4))
6 * (5 * (4 * factorial(3)))
6 * (5 * (4 * (3 * factorial(2))))
6 * (5 * (4 * (3 * (2 * factorial(1)))))
6 * (5 * (4 * (3 * (2 * 1))))
6 * (5 * (4 * (3 * 2)))
6 * (5 * (4 * 6))
6 * (5 * 24)
6 * 120
720

## 递归模板

```python 
def recursion(level, param1, param2, ...): 
    # recursion terminator
    if level > MAX_LEVEL:
        process_result
        return
    # process logic in current level
    process(level, data...) 

    # drill down
    self.recursion(level + 1, p1, ...)
    
    # reverse the current level status if needed
```
 思维要点
1. 不要人肉进行递归(最大误区)
2. 找到最近最简方法，将其拆解成可重复解决的问题(重复子问题) 
3. 数学归纳法思维

## 分治模板
```python
def divide_conquer(problem, param1, param2, ...): 
    # recursion terminator
    if problem is None:
        print_result
        return
    # prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)
    # conquer subproblems
    subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
    subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
    subresult3 = self.divide_conquer(subproblems[2], p1, ...)
...
    # process and generate the final result
    result = process_result(subresult1, subresult2, subresult3, ...)
    # revert the current level states
```


### 深度优先搜索
示例代码：
```python
def dfs(node):
    if node in visited:
        #already visited
        return
    visited.add(node)
    
    #process current node
    #...# logic here
    dfs(node.left)
    dfs(node.right)

### 递归写法

visited = set()

def dfs(node,visited):
    if node in visited:# terminator
        #already visited
        return
    visited.add(node)
    #process current node here.
    ...
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node,visted)

# 非递归写法
def DFS(self, tree):
    if tree.root is None:
        return []
    visited, stack = [], [tree.root]
    while stack:
        node = stack.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)
    #other processing work
```

### BFS 
```python
def BFS(graph, start, end):
    queue = []
    queue.append([start])
    visited.add(start)
    
    while queue:
        node = queue.pop()
        visited.add(node)
        
        process(node)
        nodes  = generate_related_nodes(node)
        queue.push(nodes)
        
    #other processing work
    
```