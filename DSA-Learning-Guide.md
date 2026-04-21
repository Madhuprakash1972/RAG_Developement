# Complete DSA Learning Guide: Beginner to Professional

---

# PART 1: FUNDAMENTALS

## 1. Time and Space Complexity

### Description
Time complexity measures how the runtime of an algorithm grows as the input size increases. Space complexity measures how much memory an algorithm uses.

### Why It Matters
- Helps you choose the right algorithm
- Predicts performance on large inputs
- Essential for interview questions

### Common Complexities (Fastest to Slowest)

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Accessing array element |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Linear search |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Bubble sort |
| O(2^n) | Exponential | Fibonacci recursive |
| O(n!) | Factorial | Permutations |

### Examples

```python
# O(1) - Constant Time
def get_first_element(arr):
    return arr[0]  # Always 1 operation

# O(n) - Linear Time
def find_sum(arr):
    total = 0
    for num in arr:      # Runs n times
        total += num
    return total

# O(n²) - Quadratic Time
def print_pairs(arr):
    for i in arr:            # n times
        for j in arr:        # n times
            print(i, j)      # n * n = n²

# O(log n) - Logarithmic Time
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
    # Each iteration halves the search space
```

---

## 2. Arrays

### Description
An array is a collection of elements stored in contiguous memory locations. Each element can be accessed using an index.

### Key Operations
- **Access:** O(1) - Direct access via index
- **Search:** O(n) - Must check each element
- **Insert:** O(n) - May need to shift elements
- **Delete:** O(n) - May need to shift elements

### Examples

```python
# Basic Array Operations
arr = [1, 2, 3, 4, 5]

# Access
first = arr[0]      # 1
last = arr[-1]      # 5

# Insert at end (O(1) amortized)
arr.append(6)       # [1, 2, 3, 4, 5, 6]

# Insert at position (O(n))
arr.insert(2, 10)   # [1, 2, 10, 3, 4, 5, 6]

# Delete (O(n))
arr.remove(3)       # [1, 2, 10, 4, 5, 6]

# Slicing
sub = arr[1:4]      # [2, 10, 4]

# Common Patterns

# Pattern 1: Two Pointers
def two_sum(arr, target):
    """Find two numbers that add up to target"""
    left, right = 0, len(arr) - 1
    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]

# Pattern 2: Sliding Window
def max_sum_subarray(arr, k):
    """Find maximum sum of subarray with size k"""
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Pattern 3: Prefix Sum
def prefix_sum(arr):
    """Create prefix sum array"""
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    
    return prefix

# Get sum of range [i, j] in O(1)
def range_sum(prefix, i, j):
    if i == 0:
        return prefix[j]
    return prefix[j] - prefix[i-1]
```

### Practice Problems (Beginner)
1. **Find Maximum** - Find the largest element in array
2. **Reverse Array** - Reverse array in place
3. **Rotate Array** - Rotate array by k positions
4. **Merge Sorted Arrays** - Merge two sorted arrays
5. **Remove Duplicates** - Remove duplicates from sorted array

---

## 3. Strings

### Description
A string is a sequence of characters. Strings are immutable in most languages.

### Key Operations
- **Access:** O(1)
- **Search:** O(n)
- **Concatenate:** O(n+m)
- **Substring:** O(n)

### Examples

```python
# Basic String Operations
s = "hello world"

# Access
first = s[0]        # 'h'
last = s[-1]        # 'd'

# Slicing
sub = s[0:5]        # 'hello'
rev = s[::-1]       # 'dlrow olleh'

# Common Methods
s.upper()           # 'HELLO WORLD'
s.lower()           # 'hello world'
s.split()           # ['hello', 'world']
s.replace('o', '0') # 'hell0 w0rld'
s.find('world')     # 6
s.count('l')        # 3

# Pattern 1: Two Pointers
def is_palindrome(s):
    """Check if string is palindrome"""
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Pattern 2: Sliding Window
def longest_unique_substring(s):
    """Find length of longest substring without repeating characters"""
    seen = {}
    max_len = 0
    left = 0
    
    for right in range(len(s)):
        if s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1
        seen[s[right]] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len

# Pattern 3: Frequency Counter
def is_anagram(s1, s2):
    """Check if two strings are anagrams"""
    if len(s1) != len(s2):
        return False
    
    freq = {}
    for c in s1:
        freq[c] = freq.get(c, 0) + 1
    
    for c in s2:
        if c not in freq:
            return False
        freq[c] -= 1
        if freq[c] < 0:
            return False
    
    return True
```

### Practice Problems (Beginner)
1. **Reverse String** - Reverse a string
2. **Valid Palindrome** - Check if string is palindrome
3. **First Unique Character** - Find first non-repeating character
4. **Longest Common Prefix** - Find common prefix in array of strings
5. **Valid Parentheses** - Check if parentheses are balanced

---

# PART 2: LINEAR DATA STRUCTURES

## 4. Linked Lists

### Description
A linked list is a linear data structure where elements are stored in nodes, and each node points to the next node. Unlike arrays, elements are not stored in contiguous memory.

### Types
- **Singly Linked List:** Each node points to next node
- **Doubly Linked List:** Each node points to next AND previous node
- **Circular Linked List:** Last node points back to first node

### Node Structure
```python
# Singly Linked List Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Doubly Linked List Node
class DoublyListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
```

### Full Implementation
```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    # O(1)
    def prepend(self, val):
        """Add element at the beginning"""
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node
        self.size += 1
    
    # O(1)
    def append(self, val):
        """Add element at the end"""
        new_node = ListNode(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    # O(n)
    def delete(self, val):
        """Delete first occurrence of value"""
        if not self.head:
            return False
        
        if self.head.val == val:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            self.size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
                if not current.next:
                    self.tail = current
                self.size -= 1
                return True
            current = current.next
        return False
    
    # O(n)
    def find(self, val):
        """Find node with given value"""
        current = self.head
        while current:
            if current.val == val:
                return current
            current = current.next
        return None
    
    # O(n)
    def reverse(self):
        """Reverse the linked list"""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Example Usage
ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.reverse()  # 3 -> 2 -> 1
```

### Common Patterns

```python
# Pattern 1: Fast and Slow Pointers
def has_cycle(head):
    """Detect cycle in linked list"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next          # Move 1 step
        fast = fast.next.next     # Move 2 steps
        if slow == fast:
            return True
    return False

# Pattern 2: Find Middle
def find_middle(head):
    """Find middle of linked list"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Pattern 3: Merge Two Sorted Lists
def merge_two_lists(l1, l2):
    """Merge two sorted linked lists"""
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    current.next = l1 or l2
    return dummy.next
```

### Practice Problems (Beginner → Intermediate)
1. **Reverse Linked List** - Reverse a singly linked list
2. **Middle of Linked List** - Find the middle node
3. **Detect Cycle** - Determine if list has a cycle
4. **Merge Two Sorted Lists** - Merge two sorted lists
5. **Remove Nth Node From End** - Remove nth node from end
6. **Copy List with Random Pointer** - Deep copy of linked list

---

## 5. Stacks

### Description
A stack is a LIFO (Last In, First Out) data structure. Elements are added and removed from the same end called the "top".

### Operations
- **Push:** O(1) - Add element to top
- **Pop:** O(1) - Remove element from top
- **Peek:** O(1) - View top element
- **IsEmpty:** O(1) - Check if stack is empty

### Implementation
```python
# Stack using List
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Stack using Linked List
class StackNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None
    
    def push(self, val):
        new_node = StackNode(val)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if not self.top:
            raise IndexError("Pop from empty stack")
        val = self.top.val
        self.top = self.top.next
        return val
    
    def peek(self):
        if not self.top:
            raise IndexError("Peek from empty stack")
        return self.top.val
```

### Common Patterns

```python
# Pattern 1: Valid Parentheses
def is_valid_parentheses(s):
    """Check if parentheses string is valid"""
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in pairs.values():  # Opening bracket
            stack.append(char)
        elif char in pairs:          # Closing bracket
            if not stack or stack.pop() != pairs[char]:
                return False
    
    return len(stack) == 0

# Pattern 2: Next Greater Element
def next_greater_element(arr):
    """Find next greater element for each element"""
    result = [-1] * len(arr)
    stack = []  # Store indices
    
    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)
    
    return result

# Pattern 3: Min Stack (O(1) getMin)
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def get_min(self):
        return self.min_stack[-1]
```

### Practice Problems
1. **Valid Parentheses** - Check balanced parentheses
2. **Implement Stack using Queues** - Build stack with queues
3. **Min Stack** - Stack with O(1) getMin
4. **Next Greater Element** - Find next greater for each element
5. **Daily Temperatures** - Days until warmer temperature

---

## 6. Queues

### Description
A queue is a FIFO (First In, First Out) data structure. Elements are added at the rear and removed from the front.

### Operations
- **Enqueue:** O(1) - Add to rear
- **Dequeue:** O(1) - Remove from front
- **Front:** O(1) - View front element
- **Rear:** O(1) - View rear element

### Implementation
```python
from collections import deque

# Queue using deque (recommended)
class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.popleft()
    
    def front(self):
        return self.items[0] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Circular Queue
class CircularQueue:
    def __init__(self, k):
        self.capacity = k
        self.queue = [None] * k
        self.head = 0
        self.tail = 0
        self.size = 0
    
    def enqueue(self, val):
        if self.is_full():
            return False
        self.queue[self.tail] = val
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True
    
    def dequeue(self):
        if self.is_empty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True
    
    def front(self):
        return self.queue[self.head] if not self.is_empty() else -1
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
```

### Priority Queue (Heap-based)
```python
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.index = 0
    
    def push(self, item, priority):
        # Min-heap: lower priority value = higher priority
        heapq.heappush(self.heap, (priority, self.index, item))
        self.index += 1
    
    def pop(self):
        return heapq.heappop(self.heap)[2]
    
    def peek(self):
        return self.heap[0][2] if self.heap else None
    
    def is_empty(self):
        return len(self.heap) == 0

# Max-Heap (using negative priority)
class MaxPriorityQueue:
    def __init__(self):
        self.heap = []
    
    def push(self, item, priority):
        heapq.heappush(self.heap, (-priority, item))
    
    def pop(self):
        return heapq.heappop(self.heap)[1]
```

### Common Patterns

```python
# Pattern 1: BFS Level Order
def bfs_level_order(graph, start):
    """BFS traversal with level tracking"""
    queue = deque([(start, 0)])  # (node, level)
    visited = {start}
    result = []
    current_level = 0
    level_nodes = []
    
    while queue:
        node, level = queue.popleft()
        
        if level > current_level:
            result.append(level_nodes)
            level_nodes = []
            current_level = level
        
        level_nodes.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))
    
    if level_nodes:
        result.append(level_nodes)
    
    return result

# Pattern 2: Sliding Window Maximum
def sliding_window_max(arr, k):
    """Find maximum in each sliding window of size k"""
    from collections import deque
    result = []
    dq = deque()  # Store indices
    
    for i in range(len(arr)):
        # Remove elements outside window
        if dq and dq[0] == i - k:
            dq.popleft()
        
        # Remove smaller elements
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        
        dq.append(i)
        
        # Add max of current window
        if i >= k - 1:
            result.append(arr[dq[0]])
    
    return result
```

### Practice Problems
1. **Implement Queue using Stacks** - Build queue with stacks
2. **Generate Parentheses** - Generate valid parentheses combinations
3. **Sliding Window Maximum** - Max in sliding window
4. **Task Scheduler** - Schedule tasks with cooldown
5. **Design Circular Queue** - Implement circular queue

---

# PART 3: NON-LINEAR DATA STRUCTURES

## 7. Hash Tables

### Description
A hash table stores key-value pairs and uses a hash function to compute an index into an array of buckets. Provides O(1) average time complexity for operations.

### How It Works
1. Hash function converts key to an index
2. Value is stored at that index
3. Collisions (same index) are handled via chaining or open addressing

### Implementation
```python
class HashTable:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]
    
    def _hash(self, key):
        """Hash function"""
        return hash(key) % self.capacity
    
    def put(self, key, value):
        """Insert or update key-value pair - O(1) average"""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # Check if key exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Add new key-value pair
        bucket.append((key, value))
        self.size += 1
        
        # Resize if load factor > 0.7
        if self.size / self.capacity > 0.7:
            self._resize()
    
    def get(self, key, default=None):
        """Get value by key - O(1) average"""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        return default
    
    def delete(self, key):
        """Delete key-value pair - O(1) average"""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        return False
    
    def _resize(self):
        """Double capacity and rehash all entries"""
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)
```

### Common Patterns

```python
# Pattern 1: Two Sum
def two_sum(arr, target):
    """Find two numbers that add to target"""
    seen = {}  # value -> index
    
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return [-1, -1]

# Pattern 2: Group Anagrams
def group_anagrams(strs):
    """Group strings that are anagrams"""
    anagram_map = {}
    
    for s in strs:
        # Use sorted string as key
        key = tuple(sorted(s))
        anagram_map.setdefault(key, []).append(s)
    
    return list(anagram_map.values())

# Pattern 3: Longest Substring Without Repeating
def longest_unique_substring(s):
    """Find length of longest substring without repeating chars"""
    seen = {}
    max_len = 0
    left = 0
    
    for right in range(len(s)):
        if s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1
        seen[s[right]] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

### Practice Problems
1. **Two Sum** - Find pair that adds to target
2. **Contains Duplicate** - Check for duplicates
3. **Valid Anagram** - Check if two strings are anagrams
4. **Group Anagrams** - Group all anagrams together
5. **Top K Frequent Elements** - Find k most frequent elements
6. **Longest Consecutive Sequence** - Find longest consecutive sequence

---

## 8. Sets

### Description
A set is a collection of unique elements. It supports fast membership testing.

### Operations
- **Add:** O(1)
- **Remove:** O(1)
- **Contains:** O(1)
- **Union:** O(n + m)
- **Intersection:** O(min(n, m))

### Implementation
```python
class Set:
    def __init__(self):
        self.hash_table = {}
    
    def add(self, value):
        self.hash_table[value] = True
    
    def remove(self, value):
        if value in self.hash_table:
            del self.hash_table[value]
    
    def contains(self, value):
        return value in self.hash_table
    
    def size(self):
        return len(self.hash_table)
    
    def union(self, other):
        result = Set()
        for item in self.hash_table:
            result.add(item)
        for item in other.hash_table:
            result.add(item)
        return result
    
    def intersection(self, other):
        result = Set()
        for item in self.hash_table:
            if item in other.hash_table:
                result.add(item)
        return result
    
    def difference(self, other):
        result = Set()
        for item in self.hash_table:
            if item not in other.hash_table:
                result.add(item)
        return result
```

### Common Patterns

```python
# Pattern 1: Check Existence
def contains_duplicate(nums):
    """Check if array contains duplicates"""
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Pattern 2: Intersection
def intersection_of_arrays(arr1, arr2):
    """Find intersection of two arrays"""
    set1 = set(arr1)
    return list(set(set1) & set(arr2))

# Pattern 3: Missing Number
def missing_number(nums):
    """Find missing number in range [0, n]"""
    n = len(nums)
    expected = set(range(n + 1))
    actual = set(nums)
    return (expected - actual).pop()
```

### Practice Problems
1. **Contains Duplicate** - Check for duplicates
2. **Intersection of Two Arrays** - Find common elements
3. **Union of Two Arrays** - Find all unique elements
4. **Happy Number** - Check if number is happy
5. **Single Number** - Find element that appears once

---

## 9. Trees

### Description
A tree is a hierarchical data structure with nodes. Each node has a value and children nodes. The top node is called the root.

### Key Terms
- **Root:** Topmost node
- **Parent/Child:** Direct relationships
- **Leaf:** Node with no children
- **Depth:** Distance from root
- **Height:** Distance to farthest leaf

### Binary Tree Node
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Tree Traversals

```python
class BinaryTree:
    def __init__(self):
        self.root = None
    
    # DFS - Recursive
    def preorder(self, node):
        """Root -> Left -> Right"""
        if not node:
            return []
        return [node.val] + self.preorder(node.left) + self.preorder(node.right)
    
    def inorder(self, node):
        """Left -> Root -> Right"""
        if not node:
            return []
        return self.inorder(node.left) + [node.val] + self.inorder(node.right)
    
    def postorder(self, node):
        """Left -> Right -> Root"""
        if not node:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.val]
    
    # BFS - Level Order
    def level_order(self, node):
        """Level by level traversal"""
        if not node:
            return []
        
        result = []
        queue = deque([node])
        
        while queue:
            level_size = len(queue)
            level = []
            
            for _ in range(level_size):
                current = queue.popleft()
                level.append(current.val)
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            
            result.append(level)
        
        return result
    
    # Tree Properties
    def height(self, node):
        """Height of tree"""
        if not node:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))
    
    def diameter(self, node):
        """Diameter of tree (longest path between any two nodes)"""
        self.max_diameter = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # Update diameter through this node
            self.max_diameter = max(self.max_diameter, left_height + right_height + 1)
            
            return 1 + max(left_height, right_height)
        
        dfs(node)
        return self.max_diameter
```

### Common Patterns

```python
# Pattern 1: Maximum Depth
def max_depth(root):
    """Find maximum depth of binary tree"""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# Pattern 2: Level Order Traversal
def level_order_traversal(root):
    """BFS level order"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

# Pattern 3: Lowest Common Ancestor
def lowest_common_ancestor(root, p, q):
    """Find LCA of two nodes"""
    if not root or root == p or root == q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root
    return left or right
```

### Practice Problems
1. **Maximum Depth of Binary Tree** - Find tree height
2. **Level Order Traversal** - BFS traversal
3. **Same Tree** - Check if two trees are identical
4. **Invert Binary Tree** - Flip tree left to right
5. **Path Sum** - Check if path with sum exists
6. **Lowest Common Ancestor** - Find LCA of two nodes
7. **Binary Tree Right Side View** - Rightmost nodes at each level

---

## 10. Binary Search Trees (BST)

### Description
A BST is a binary tree where for each node, all values in left subtree are smaller and all values in right subtree are larger.

### Properties
- Left subtree < Root < Right subtree
- Inorder traversal gives sorted order
- Efficient search, insert, delete: O(h) where h = height

### Implementation
```python
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        """Insert value - O(h)"""
        self.root = self._insert(self.root, val)
    
    def _insert(self, node, val):
        if not node:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        
        return node
    
    def search(self, val):
        """Search for value - O(h)"""
        return self._search(self.root, val)
    
    def _search(self, node, val):
        if not node or node.val == val:
            return node
        
        if val < node.val:
            return self._search(node.left, val)
        return self._search(node.right, val)
    
    def delete(self, val):
        """Delete value - O(h)"""
        self.root = self._delete(self.root, val)
    
    def _delete(self, node, val):
        if not node:
            return None
        
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            # Node found
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            
            # Two children: get inorder successor
            temp = self._find_min(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)
        
        return node
    
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node
    
    def validate(self):
        """Check if tree is valid BST"""
        return self._validate(self.root, float('-inf'), float('inf'))
    
    def _validate(self, node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (self._validate(node.left, min_val, node.val) and
                self._validate(node.right, node.val, max_val))
```

### Practice Problems
1. **Validate BST** - Check if tree is valid BST
2. **Kth Smallest Element** - Find kth smallest in BST
3. **Lowest Common Ancestor of BST** - LCA in BST
4. **Convert Sorted Array to BST** - Build balanced BST
5. **Minimum Absolute Difference** - Min diff between any two nodes

---

## 11. Heaps (Priority Queues)

### Description
A heap is a complete binary tree that satisfies the heap property. In a min-heap, parent is always smaller than children.

### Types
- **Min-Heap:** Root is minimum element
- **Max-Heap:** Root is maximum element

### Operations
- **Push:** O(log n)
- **Pop:** O(log n)
- **Peek:** O(1)
- **Build Heap:** O(n)

### Implementation
```python
class MinHeap:
    def __init__(self):
        self.heap = []
    
    def _parent(self, i): return (i - 1) // 2
    def _left(self, i): return 2 * i + 1
    def _right(self, i): return 2 * i + 2
    
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def _heapify_up(self, i):
        while i > 0 and self.heap[self._parent(i)] > self.heap[i]:
            self._swap(i, self._parent(i))
            i = self._parent(i)
    
    def _heapify_down(self, i):
        smallest = i
        left = self._left(i)
        right = self._right(i)
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != i:
            self._swap(i, smallest)
            self._heapify_down(smallest)
    
    def push(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
    
    def pop(self):
        if not self.heap:
            raise IndexError("Pop from empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def peek(self):
        return self.heap[0] if self.heap else None
    
    def size(self):
        return len(self.heap)
```

### Using Python's heapq
```python
import heapq

# Min-Heap
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
print(heapq.heappop(heap))  # 1

# Max-Heap (using negative values)
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
print(-heapq.heappop(max_heap))  # 3

# Heapify (build heap from list in O(n))
arr = [5, 3, 8, 4, 1]
heapq.heapify(arr)

# Kth Largest Element
def kth_largest(arr, k):
    min_heap = []
    for num in arr:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]
```

### Common Patterns

```python
# Pattern 1: Top K Frequent Elements
def top_k_frequent(nums, k):
    """Find k most frequent elements"""
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    # Use heap to get top k
    heap = []
    for num, f in freq.items():
        heapq.heappush(heap, (f, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [num for f, num in heap]

# Pattern 2: Merge K Sorted Lists
def merge_k_sorted_lists(lists):
    """Merge k sorted linked lists"""
    result = []
    heap = []
    
    # Add first element from each list
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    
    while heap:
        val, i, node = heapq.heappop(heap)
        result.append(val)
        
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return result
```

### Practice Problems
1. **Kth Largest Element** - Find kth largest in array
2. **Top K Frequent Elements** - Most frequent elements
3. **Merge K Sorted Lists** - Merge k sorted linked lists
4. **Find Median from Data Stream** - Running median
5. **Task Scheduler** - Schedule tasks with cooldown

---

# PART 4: ALGORITHMS

## 12. Sorting Algorithms

### Comparison Sorts

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |

### Implementations

```python
# Bubble Sort - O(n²)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Selection Sort - O(n²)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Insertion Sort - O(n²)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Merge Sort - O(n log n)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort - O(n log n) average
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Heap Sort - O(n log n)
def heap_sort(arr):
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

### Practice Problems
1. **Sort an Array** - Implement any O(n log n) sort
2. **Kth Largest Element** - Find kth largest
3. **Meeting Rooms II** - Minimum meeting rooms needed
4. **Insert Interval** - Insert interval into sorted intervals
5. **Merge Intervals** - Merge overlapping intervals

---

## 13. Binary Search

### Description
Binary search finds a target in a sorted array by repeatedly dividing the search space in half.

### Implementation
```python
# Basic Binary Search - O(log n)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Find First Occurrence
def find_first(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# Find Last Occurrence
def find_last(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# Search in Rotated Sorted Array
def search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# Find Peak Element
def find_peak(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left
```

### Practice Problems
1. **Binary Search** - Basic binary search
2. **Search Insert Position** - Find where to insert
3. **Find First and Last Position** - Range of target
4. **Search in Rotated Sorted Array** - Rotated array search
5. **Find Peak Element** - Find peak element
6. **Median of Two Sorted Arrays** - Hard problem

---

## 14. Recursion and Backtracking

### Description
Recursion is when a function calls itself. Backtracking builds solutions incrementally and abandons partial solutions that can't be completed.

### Key Concepts
- **Base Case:** Condition to stop recursion
- **Recursive Case:** Function calling itself
- **Call Stack:** Tracks active function calls

### Examples

```python
# Factorial - Simple Recursion
def factorial(n):
    if n <= 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

# Fibonacci - Recursion with Memoization
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

# Permutations - Backtracking
def permutations(nums):
    result = []
    
    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            if not used[i]:
                path.append(nums[i])
                used[i] = True
                backtrack(path, used)
                path.pop()
                used[i] = False
    
    backtrack([], [False] * len(nums))
    return result

# Combinations - Backtracking
def combinations(n, k):
    result = []
    
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(1, [])
    return result

# Subsets - Backtracking
def subsets(nums):
    result = []
    
    def backtrack(start, path):
        result.append(path[:])
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result

# N-Queens - Classic Backtracking
def n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
               abs(board[i] - col) == abs(i - row):
                return False
        return True
    
    def backtrack(row):
        if row == n:
            results.append(board[:])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
    
    results = []
    backtrack([0] * n)
    return results
```

### Practice Problems
1. **Factorial** - Compute factorial
2. **Fibonacci** - Compute nth Fibonacci
3. **Subsets** - Generate all subsets
4. **Permutations** - Generate all permutations
5. **Combination Sum** - Find combinations that sum to target
6. **N-Queens** - Place n queens on n×n board
7. **Sudoku Solver** - Solve Sudoku puzzle

---

## 15. Dynamic Programming

### Description
DP solves complex problems by breaking them into simpler subproblems and storing results to avoid recomputation.

### Two Approaches
1. **Memoization (Top-Down):** Recursive with caching
2. **Tabulation (Bottom-Up):** Iterative with table

### Classic Problems

```python
# 1. Climbing Stairs
def climb_stairs(n):
    """Count ways to climb n stairs (1 or 2 steps at a time)"""
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# Space Optimized
def climb_stairs_optimized(n):
    if n <= 2:
        return n
    
    prev2, prev1 = 1, 2
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1

# 2. House Robber
def house_robber(nums):
    """Maximum amount without robbing adjacent houses"""
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[-1]

# 3. Coin Change
def coin_change(coins, amount):
    """Minimum coins needed to make amount"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# 4. Longest Increasing Subsequence
def lis(nums):
    """Length of longest increasing subsequence"""
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# 5. Longest Common Subsequence
def lcs(text1, text2):
    """Length of longest common subsequence"""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

# 6. 0/1 Knapsack
def knapsack(weights, values, capacity):
    """Maximum value without exceeding capacity"""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]  # Don't include
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], 
                    dp[i-1][w - weights[i-1]] + values[i-1])
    
    return dp[n][capacity]

# 7. Edit Distance
def edit_distance(word1, word2):
    """Minimum operations to convert word1 to word2"""
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Delete
                    dp[i][j-1],    # Insert
                    dp[i-1][j-1]   # Replace
                )
    
    return dp[m][n]
```

### Practice Problems (Easy → Hard)
1. **Climbing Stairs** - Count ways to climb
2. **House Robber** - Maximum robbery amount
3. **Coin Change** - Minimum coins needed
4. **Longest Palindromic Substring** - Find longest palindrome
5. **Word Break** - Check if string can be segmented
6. **Longest Increasing Subsequence** - Find LIS length
7. **Longest Common Subsequence** - Find LCS
8. **0/1 Knapsack** - Maximum value in knapsack
9. **Edit Distance** - Minimum edit operations
10. **Regular Expression Matching** - Pattern matching with regex

---

## 16. Graph Algorithms

### Description
A graph is a collection of nodes (vertices) connected by edges. Can be directed or undirected, weighted or unweighted.

### Representations

```python
# Adjacency List (Recommended)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

# Adjacency Matrix
# graph[i][j] = 1 if edge exists, 0 otherwise

# Weighted Graph
weighted_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2)],
    'C': [('A', 4), ('E', 3)],
    'D': [('B', 2)],
    'E': [('C', 3)]
}
```

### Graph Traversal

```python
from collections import deque, defaultdict

# DFS - Recursive
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node)  # Process node
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

# DFS - Iterative
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            stack.extend(reversed(graph[node]))
    
    return visited

# BFS
def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

# BFS with Level
def bfs_levels(graph, start):
    visited = {start}
    queue = deque([(start, 0)])  # (node, level)
    levels = []
    current_level = 0
    level_nodes = []
    
    while queue:
        node, level = queue.popleft()
        
        if level > current_level:
            levels.append(level_nodes)
            level_nodes = []
            current_level = level
        
        level_nodes.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))
    
    if level_nodes:
        levels.append(level_nodes)
    
    return levels
```

### Shortest Path Algorithms

```python
# Dijkstra's Algorithm
import heapq

def dijkstra(graph, start):
    """
    graph: {node: {neighbor: weight}}
    Returns: {node: shortest_distance}
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # (distance, node)
    
    while pq:
        dist, node = heapq.heappop(pq)
        
        if dist > distances[node]:
            continue
        
        for neighbor, weight in graph[node].items():
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return distances

# Floyd-Warshall (All Pairs Shortest Path)
def floyd_warshall(graph, n):
    """
    graph: Adjacency matrix where graph[i][j] = weight
    n: Number of vertices
    """
    dist = [row[:] for row in graph]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
```

### Union-Find (Disjoint Set)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.num_components = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        
        self.num_components -= 1
        return True
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

### Practice Problems
1. **Number of Islands** - Count connected components
2. **Clone Graph** - Deep copy of graph
3. **Course Schedule** - Detect cycle in directed graph
4. **Pacific Atlantic Water Flow** - Reach both oceans
5. **Number of Connected Components** - Count components
6. **Network Delay Time** - Dijkstra's algorithm
7. **Min Cost to Connect All Points** - MST
8. **Reconstruct Itinerary** - Eulerian path
9. **Word Ladder** - BFS shortest path
10. **Alien Dictionary** - Topological sort

---

# PART 5: ADVANCED TOPICS

## 17. Tries (Prefix Trees)

### Description
A trie is a tree-like data structure for storing strings. Each node represents a character, and paths from root represent words.

### Implementation
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert word - O(m) where m = word length"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        """Search for exact word - O(m)"""
        node = self._find_node(word)
        return node is not None and node.is_end_of_word
    
    def starts_with(self, prefix):
        """Check if prefix exists - O(m)"""
        return self._find_node(prefix) is not None
    
    def _find_node(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
    
    def delete(self, word):
        """Delete word from trie"""
        def _delete(node, word, depth):
            if depth == len(word):
                node.is_end_of_word = False
                return len(node.children) == 0
            
            char = word[depth]
            should_delete_child = _delete(node.children[char], word, depth + 1)
            
            if should_delete_child:
                del node.children[char]
                return not node.is_end_of_word and len(node.children) == 0
            
            return False
        
        _delete(self.root, word, 0)
    
    def autocomplete(self, prefix):
        """Get all words with given prefix"""
        node = self._find_node(prefix)
        if not node:
            return []
        
        result = []
        self._dfs(node, prefix, result)
        return result
    
    def _dfs(self, node, prefix, result):
        if node.is_end_of_word:
            result.append(prefix)
        
        for char, child in node.children.items():
            self._dfs(child, prefix + char, result)
```

### Practice Problems
1. **Implement Trie** - Basic trie operations
2. **Add and Search Word** - With wildcard support
3. **Word Search II** - Find words on board
4. **Longest Word in Dictionary** - Longest buildable word
5. **Prefix and Suffix Search** - Two-sided search

---

## 18. Greedy Algorithms

### Description
Greedy algorithms make the locally optimal choice at each step, hoping to find the global optimum.

### When to Use
- Problem has "greedy choice property"
- Local optimum leads to global optimum
- No need to reconsider previous choices

### Examples

```python
# 1. Activity Selection
def activity_selection(start, finish):
    """Select maximum number of non-overlapping activities"""
    # Sort by finish time
    activities = sorted(enumerate(zip(start, finish)), 
                        key=lambda x: x[1][1])
    
    selected = [activities[0][0]]
    last_finish = activities[0][1][1]
    
    for i, (s, f) in activities[1:]:
        if s >= last_finish:
            selected.append(i)
            last_finish = f
    
    return selected

# 2. Fractional Knapsack
def fractional_knapsack(items, capacity):
    """items = [(value, weight), ...]"""
    # Sort by value/weight ratio
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    
    total_value = 0
    for value, weight in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            break
    
    return total_value

# 3. Jump Game
def can_jump(nums):
    """Check if can reach end from start"""
    max_reach = 0
    
    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
    
    return True

# 4. Gas Station
def can_complete_circuit(gas, cost):
    """Find starting gas station to complete circuit"""
    if sum(gas) < sum(cost):
        return -1
    
    start = 0
    tank = 0
    
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    
    return start
```

### Practice Problems
1. **Maximum Subarray** - Kadane's algorithm
2. **Jump Game** - Can reach end
3. **Gas Station** - Complete circuit
4. **Candy** - Distribute candies fairly
5. **Insert Interval** - Insert and merge
6. **Meeting Rooms II** - Minimum rooms needed
7. **Task Scheduler** - Optimal task scheduling

---

## 19. Bit Manipulation

### Description
Working directly with bits for efficient operations.

### Common Operations
```python
# Get bit at position i
def get_bit(num, i):
    return (num >> i) & 1

# Set bit at position i
def set_bit(num, i):
    return num | (1 << i)

# Clear bit at position i
def clear_bit(num, i):
    return num & ~(1 << i)

# Toggle bit at position i
def toggle_bit(num, i):
    return num ^ (1 << i)

# Check if power of 2
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Count set bits
def count_set_bits(n):
    count = 0
    while n:
        n &= n - 1  # Clear rightmost set bit
        count += 1
    return count

# Find unique number (others appear twice)
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Find two unique numbers (others appear twice)
def single_number_iii(nums):
    xor = 0
    for num in nums:
        xor ^= num
    
    # Find rightmost set bit
    diff = xor & (-xor)
    
    a, b = 0, 0
    for num in nums:
        if num & diff:
            a ^= num
        else:
            b ^= num
    
    return [a, b]
```

### Practice Problems
1. **Single Number** - Find unique element
2. **Number of 1 Bits** - Count set bits
3. **Counting Bits** - Count bits for 0 to n
4. **Reverse Bits** - Reverse 32-bit integer
5. **Sum of Two Integers** - Without + or -
6. **Missing Number** - Find missing in range

---

## Quick Reference: When to Use What

| Problem Pattern | Algorithm/DS |
|-----------------|--------------|
| Search sorted array | Binary Search |
| Top/bottom K elements | Heap |
| All combinations/permutations | Backtracking |
| Optimization with subproblems | Dynamic Programming |
| Shortest path (unweighted) | BFS |
| Shortest path (weighted) | Dijkstra |
| Dependencies/topological order | Topological Sort |
| Connected components | Union-Find / DFS |
| Interval problems | Sorting + Linear scan |
| Subarray/substring | Sliding Window |
| Prefix/suffix search | Trie |
| Memory efficient storage | Bit manipulation |

---

# FINAL CHECKLIST

## Beginner (0-50 problems)
- [ ] Understand Big O notation
- [ ] Implement arrays and strings operations
- [ ] Implement linked list (insert, delete, reverse)
- [ ] Implement stack and queue
- [ ] Solve basic recursion problems
- [ ] Use hash tables for frequency counting

## Intermediate (50-150 problems)
- [ ] Master tree traversals (DFS, BFS)
- [ ] Implement and use BST
- [ ] Understand heaps and priority queues
- [ ] Solve basic DP problems (1D)
- [ ] Implement basic graph algorithms (DFS, BFS)
- [ ] Solve medium-level array/string problems

## Advanced (150-300+ problems)
- [ ] Solve complex DP problems (2D, optimization)
- [ ] Implement Dijkstra, MST algorithms
- [ ] Master advanced patterns (trie, segment tree)
- [ ] Solve hard interview problems
- [ ] Participate in contests for speed

## Expert (300+ problems)
- [ ] Can identify patterns quickly
- [ ] Write bug-free code under time pressure
- [ ] Explain solutions clearly
- [ ] Optimize space and time efficiently
- [ ] Handle edge cases systematically
