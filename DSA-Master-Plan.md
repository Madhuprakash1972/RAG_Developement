# Complete DSA Learning Plan: Beginner to Professional
## With C++ Implementation, OOPs Deep Dive, and Beyond

---

# TABLE OF CONTENTS
1. [Learning Roadmap Overview](#learning-roadmap-overview)
2. [Phase 1: Foundations (Weeks 1-4)](#phase-1-foundations)
3. [Phase 2: Core Data Structures (Weeks 5-10)](#phase-2-core-data-structures)
4. [Phase 3: Advanced Algorithms (Weeks 11-16)](#phase-3-advanced-algorithms)
5. [Phase 4: Expert Topics (Weeks 17-24)](#phase-4-expert-topics)
6. [OOPs Concepts Complete Guide](#oopsc-concepts-complete-guide)
7. [Additional Topics Beyond DSA](#additional-topics-beyond-dsa)
8. [Practice Problem Bank](#practice-problem-bank)

---

# LEARNING ROADMAP OVERVIEW

## What You Need to Master

| Area | Topics | Priority |
|------|--------|----------|
| **Data Structures** | Arrays, Lists, Stacks, Queues, Trees, Graphs, Hash Tables | Critical |
| **Algorithms** | Sorting, Searching, DP, Greedy, Backtracking | Critical |
| **OOPs Concepts** | Classes, Inheritance, Polymorphism, Encapsulation, Abstraction | Critical |
| **System Design Basics** | Load balancing, Caching, Databases | Important |
| **Complexity Analysis** | Time/Space complexity, Big O | Critical |
| **Problem Patterns** | Sliding window, Two pointers, DFS/BFS | Critical |

---

# PHASE 1: FOUNDATIONS (Weeks 1-4)

## Week 1: Complexity Analysis & Basic Arrays

### Description

**Time Complexity** measures how runtime grows as input size increases. It helps you predict if your solution will work for large inputs.

**Why it matters:**
- A solution that works for n=10 might fail for n=1,000,000
- Helps you choose between different approaches
- Essential for technical interviews

**Common Complexities (Fastest to Slowest):**

| Notation | Name | Example Operation | n=10 | n=1000 | n=1,000,000 |
|----------|------|-------------------|------|--------|-------------|
| O(1) | Constant | Array access | 1 | 1 | 1 |
| O(log n) | Logarithmic | Binary search | 3 | 10 | 20 |
| O(n) | Linear | Linear search | 10 | 1000 | 1,000,000 |
| O(n log n) | Linearithmic | Merge sort | 33 | 10,000 | 20,000,000 |
| O(n²) | Quadratic | Bubble sort | 100 | 1,000,000 | 1,000,000,000 |
| O(2^n) | Exponential | Fibonacci recursive | 1024 | Too large | Impossible |
| O(n!) | Factorial | Permutations | 3.6M | Too large | Impossible |

### Key Concepts Explained

**O(1) - Constant Time:**
- Execution time doesn't change with input size
- Example: Accessing array element by index

**O(log n) - Logarithmic Time:**
- Each step reduces problem size by half
- Example: Binary search cuts search space in half each iteration

**O(n) - Linear Time:**
- Time grows proportionally with input
- Example: Loop through array once

**O(n²) - Quadratic Time:**
- Nested loops where both iterate n times
- Example: Compare every pair of elements

### Code Examples with Explanation

```cpp
// O(1) - Constant Time
// No matter how big the array is, this always takes 1 operation
int getFirst(int arr[]) {
    return arr[0];  // Direct memory access
}

// O(n) - Linear Time
// If array has n elements, loop runs n times
int sumArray(int arr[], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {  // Runs n times
        sum += arr[i];
    }
    return sum;
}

// O(n²) - Quadratic Time
// For each of n elements, we iterate through n elements
void printPairs(int arr[], int n) {
    for (int i = 0; i < n; i++) {           // n times
        for (int j = 0; j < n; j++) {       // n times
            cout << arr[i] << ", " << arr[j] << endl;  // n * n = n²
        }
    }
}

// O(log n) - Logarithmic Time
// Each iteration halves the search space
int binarySearch(int arr[], int n, int target) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
        // Each iteration: search space becomes half
        // n -> n/2 -> n/4 -> ... -> 1
        // Number of iterations = log₂(n)
    }
    return -1;
}
```

### Practice Problems (Week 1)

**Easy (5 problems):**
1. Find maximum element in array
2. Find minimum element in array
3. Calculate sum of array elements
4. Reverse an array
5. Check if array is sorted

**Medium (3 problems):**
1. Rotate array by k positions
2. Move all zeros to end of array
3. Merge two sorted arrays

---

## Week 2: Arrays - Advanced Patterns

### Pattern 1: Two Pointers

**Description:** Use two pointers moving in different directions or at different speeds to solve problems efficiently.

**When to use:**
- Array is sorted (or can be sorted)
- Looking for pairs that satisfy a condition
- Need to reverse or partition array

**Why it works:**
- Avoids nested loops
- Reduces O(n²) to O(n)

```cpp
// Pattern: Two pointers from opposite ends
// Problem: Find if any two numbers sum to target

// Brute Force: O(n²)
bool twoSumBruteForce(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] + arr[j] == target) return true;
        }
    }
    return false;
}

// Two Pointers: O(n) - requires sorted array
bool twoSumTwoPointers(int arr[], int n, int target) {
    int left = 0;
    int right = n - 1;
    
    while (left < right) {
        int sum = arr[left] + arr[right];
        
        if (sum == target) return true;
        else if (sum < target) left++;   // Need larger sum
        else right--;                    // Need smaller sum
    }
    return false;
}

// Pattern: Two pointers from same direction (slow and fast)
// Problem: Remove duplicates from sorted array

int removeDuplicates(int arr[], int n) {
    if (n == 0) return 0;
    
    int slow = 0;  // Points to last unique element
    
    for (int fast = 1; fast < n; fast++) {
        if (arr[fast] != arr[slow]) {
            slow++;
            arr[slow] = arr[fast];  // Place next unique element
        }
    }
    return slow + 1;  // Number of unique elements
}
```

### Pattern 2: Sliding Window

**Description:** Maintain a "window" of elements and slide it through the array.

**When to use:**
- Subarray/substring problems
- Find maximum/minimum of subarrays of size k
- Find longest/shortest subarray satisfying condition

**Why it works:**
- Avoids recalculating from scratch
- Reuses previous computation

```cpp
// Pattern: Fixed size window
// Problem: Maximum sum of subarray with size k

int maxSumSubarray(int arr[], int n, int k) {
    // Calculate sum of first window
    int windowSum = 0;
    for (int i = 0; i < k; i++) {
        windowSum += arr[i];
    }
    
    int maxSum = windowSum;
    
    // Slide window: subtract left element, add right element
    for (int i = k; i < n; i++) {
        windowSum = windowSum - arr[i - k] + arr[i];
        maxSum = max(maxSum, windowSum);
    }
    
    return maxSum;
}

// Pattern: Variable size window
// Problem: Longest subarray with sum <= target

int longestSubarrayWithSum(int arr[], int n, int target) {
    int left = 0;
    int currentSum = 0;
    int maxLength = 0;
    
    for (int right = 0; right < n; right++) {
        currentSum += arr[right];
        
        // Shrink window while sum > target
        while (currentSum > target && left <= right) {
            currentSum -= arr[left];
            left++;
        }
        
        maxLength = max(maxLength, right - left + 1);
    }
    
    return maxLength;
}
```

### Pattern 3: Prefix Sum

**Description:** Precompute cumulative sums to answer range sum queries in O(1).

**When to use:**
- Multiple range sum queries
- Subarray sum problems

```cpp
// Build prefix sum array: O(n)
int* buildPrefixSum(int arr[], int n) {
    int* prefix = new int[n];
    prefix[0] = arr[0];
    
    for (int i = 1; i < n; i++) {
        prefix[i] = prefix[i-1] + arr[i];
    }
    return prefix;
}

// Query range sum: O(1)
int rangeSum(int prefix[], int i, int j) {
    if (i == 0) return prefix[j];
    return prefix[j] - prefix[i-1];
}

// Problem: Find subarray with given sum
bool hasSubarrayWithSum(int arr[], int n, int target) {
    int currentSum = 0;
    unordered_map<int, int> sumMap;  // sum -> index
    
    for (int i = 0; i < n; i++) {
        currentSum += arr[i];
        
        if (currentSum == target) return true;
        
        // If (currentSum - target) exists, subarray exists
        if (sumMap.find(currentSum - target) != sumMap.end()) {
            return true;
        }
        
        sumMap[currentSum] = i;
    }
    return false;
}
```

### Practice Problems (Week 2)

**Two Pointers:**
1. Two Sum (sorted array)
2. Valid Palindrome
3. Container With Most Water
4. 3Sum
5. Merge Sorted Array

**Sliding Window:**
1. Max Consecutive Ones
2. Longest Substring Without Repeating Characters
3. Minimum Size Subarray Sum
4. Sliding Window Maximum
5. Find All Anagrams in a String

**Prefix Sum:**
1. Range Sum Query - Immutable
2. Subarray Sum Equals K
3. Contiguous Array
4. Product of Array Except Self

---

## Week 3: Linked Lists

### Description

A linked list stores elements in nodes, where each node points to the next. Unlike arrays, nodes are not in contiguous memory.

**Why use linked lists:**
- O(1) insertion/deletion at known position
- No need to preallocate size
- Efficient for implementing stacks, queues

**Trade-offs:**
- O(n) access (can't jump to index)
- Extra memory for pointers
- Not cache-friendly

### Node Structure

```cpp
// Singly Linked List Node
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// Doubly Linked List Node
struct DoublyListNode {
    int val;
    DoublyListNode* prev;
    DoublyListNode* next;
    DoublyListNode(int x) : val(x), prev(nullptr), next(nullptr) {}
};
```

### Core Operations with Explanations

```cpp
class LinkedList {
private:
    ListNode* head;
    int size;

public:
    LinkedList() : head(nullptr), size(0) {}
    
    // O(1) - Add at beginning
    void prepend(int val) {
        ListNode* newNode = new ListNode(val);
        newNode->next = head;
        head = newNode;
        size++;
    }
    
    // O(1) - Add at end (with tail pointer)
    void append(int val) {
        ListNode* newNode = new ListNode(val);
        
        if (head == nullptr) {
            head = newNode;
            return;
        }
        
        ListNode* current = head;
        while (current->next != nullptr) {
            current = current->next;
        }
        current->next = newNode;
        size++;
    }
    
    // O(n) - Delete by value
    void deleteNode(int val) {
        if (head == nullptr) return;
        
        // Special case: delete head
        if (head->val == val) {
            ListNode* temp = head;
            head = head->next;
            delete temp;
            size--;
            return;
        }
        
        // Find node to delete
        ListNode* current = head;
        while (current->next != nullptr && current->next->val != val) {
            current = current->next;
        }
        
        // If found, skip it
        if (current->next != nullptr) {
            ListNode* temp = current->next;
            current->next = current->next->next;
            delete temp;
            size--;
        }
    }
    
    // O(n) - Find value
    ListNode* find(int val) {
        ListNode* current = head;
        while (current != nullptr) {
            if (current->val == val) return current;
            current = current->next;
        }
        return nullptr;
    }
};
```

### Essential Patterns

```cpp
// Pattern 1: Fast and Slow Pointers
// Problem: Detect cycle in linked list
bool hasCycle(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    
    // Fast moves 2 steps, slow moves 1 step
    // If there's a cycle, they will meet
    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
        
        if (slow == fast) return true;  // Cycle detected
    }
    return false;
}

// Pattern 2: Find Middle
// Problem: Find middle of linked list
ListNode* findMiddle(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    
    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;  // Middle node
}

// Pattern 3: Reverse Linked List
// Three approaches:
ListNode* reverseList(ListNode* head) {
    // Approach 1: Iterative (most common)
    ListNode* prev = nullptr;
    ListNode* current = head;
    
    while (current != nullptr) {
        ListNode* nextTemp = current->next;  // Save next
        current->next = prev;                 // Reverse pointer
        prev = current;                       // Move prev forward
        current = nextTemp;                   // Move current forward
    }
    return prev;
}

// Approach 2: Recursive
ListNode* reverseListRecursive(ListNode* head) {
    if (head == nullptr || head->next == nullptr) {
        return head;
    }
    
    ListNode* newHead = reverseListRecursive(head->next);
    head->next->next = head;  // Reverse the link
    head->next = nullptr;     // Break original link
    
    return newHead;
}

// Pattern 4: Merge Two Sorted Lists
ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    // Create dummy node to simplify logic
    ListNode dummy(0);
    ListNode* current = &dummy;
    
    while (l1 != nullptr && l2 != nullptr) {
        if (l1->val <= l2->val) {
            current->next = l1;
            l1 = l1->next;
        } else {
            current->next = l2;
            l2 = l2->next;
        }
        current = current->next;
    }
    
    // Attach remaining
    current->next = (l1 != nullptr) ? l1 : l2;
    
    return dummy.next;
}

// Pattern 5: Remove Nth Node From End
ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode dummy(0);
    dummy.next = head;
    
    ListNode* fast = &dummy;
    ListNode* slow = &dummy;
    
    // Move fast n+1 steps ahead
    for (int i = 0; i <= n; i++) {
        fast = fast->next;
    }
    
    // Move both until fast reaches end
    while (fast != nullptr) {
        fast = fast->next;
        slow = slow->next;
    }
    
    // slow is now at node before nth from end
    ListNode* toDelete = slow->next;
    slow->next = slow->next->next;
    delete toDelete;
    
    return dummy.next;
}
```

### Practice Problems (Week 3)

**Easy:**
1. Reverse Linked List
2. Merge Two Sorted Lists
3. Remove Linked List Elements
4. Find Middle of Linked List
5. Palindrome Linked List

**Medium:**
1. Linked List Cycle
2. Linked List Cycle II
3. Remove Nth Node From End
4. Add Two Numbers
5. Copy List with Random Pointer

**Hard:**
1. Reverse Nodes in K-Group
2. LRUCache (combine with hash map)
3. Flatten a Multilevel Doubly Linked List

---

## Week 4: Stacks and Queues

### Stack - Description

**LIFO (Last In, First Out)** - Last element added is first to be removed.

**Real-world analogy:** Stack of plates - you add and remove from the top.

**Operations:**
- Push: O(1) - Add to top
- Pop: O(1) - Remove from top
- Peek: O(1) - View top element
- Empty: O(1) - Check if empty

```cpp
// Stack Implementation using Vector
class Stack {
private:
    vector<int> data;
    
public:
    void push(int x) {
        data.push_back(x);
    }
    
    void pop() {
        if (empty()) throw runtime_error("Stack is empty");
        data.pop_back();
    }
    
    int peek() {
        if (empty()) throw runtime_error("Stack is empty");
        return data.back();
    }
    
    bool empty() {
        return data.empty();
    }
    
    int size() {
        return data.size();
    }
};

// Common Patterns

// Pattern 1: Valid Parentheses
// Problem: Check if parentheses string is valid
bool isValidParentheses(string s) {
    stack<char> st;
    unordered_map<char, char> pairs = {
        {')', '('}, {']', '['}, {'}', '{'}
    };
    
    for (char c : s) {
        // If opening bracket, push
        if (c == '(' || c == '[' || c == '{') {
            st.push(c);
        }
        // If closing bracket, check match
        else if (c == ')' || c == ']' || c == '}') {
            if (st.empty() || st.top() != pairs[c]) {
                return false;
            }
            st.pop();
        }
    }
    return st.empty();  // True if all brackets matched
}

// Pattern 2: Next Greater Element
// Problem: Find next greater element for each element
vector<int> nextGreaterElement(vector<int>& nums) {
    vector<int> result(nums.size());
    stack<int> st;  // Store indices
    
    // Traverse from right to left
    for (int i = nums.size() - 1; i >= 0; i--) {
        // Pop elements smaller than current
        while (!st.empty() && st.top() <= nums[i]) {
            st.pop();
        }
        
        // Top is next greater, or -1 if stack empty
        result[i] = st.empty() ? -1 : st.top();
        
        st.push(nums[i]);
    }
    
    return result;
}

// Pattern 3: Min Stack (O(1) getMin)
class MinStack {
private:
    stack<int> mainStack;
    stack<int> minStack;  // Tracks minimum at each level
    
public:
    void push(int x) {
        mainStack.push(x);
        // Push to minStack if empty or x is new minimum
        if (minStack.empty() || x <= minStack.top()) {
            minStack.push(x);
        }
    }
    
    void pop() {
        if (mainStack.top() == minStack.top()) {
            minStack.pop();
        }
        mainStack.pop();
    }
    
    int top() {
        return mainStack.top();
    }
    
    int getMin() {
        return minStack.top();
    }
};
```

### Queue - Description

**FIFO (First In, First Out)** - First element added is first to be removed.

**Real-world analogy:** Line at a store - first person in line is served first.

**Operations:**
- Enqueue: O(1) - Add to rear
- Dequeue: O(1) - Remove from front
- Front: O(1) - View front element

```cpp
// Queue Implementation
class Queue {
private:
    queue<int> data;
    
public:
    void enqueue(int x) {
        data.push(x);
    }
    
    void dequeue() {
        if (empty()) throw runtime_error("Queue is empty");
        data.pop();
    }
    
    int front() {
        if (empty()) throw runtime_error("Queue is empty");
        return data.front();
    }
    
    bool empty() {
        return data.empty();
    }
    
    int size() {
        return data.size();
    }
};

// Pattern: Sliding Window Maximum
// Problem: Find maximum in each sliding window of size k
vector<int> slidingWindowMax(vector<int>& nums, int k) {
    vector<int> result;
    deque<int> dq;  // Stores indices, maintains decreasing order
    
    for (int i = 0; i < nums.size(); i++) {
        // Remove indices outside window
        if (!dq.empty() && dq.front() == i - k) {
            dq.pop_front();
        }
        
        // Remove smaller elements (they can't be max)
        while (!dq.empty() && nums[dq.back()] < nums[i]) {
            dq.pop_back();
        }
        
        dq.push_back(i);
        
        // First window complete, add max to result
        if (i >= k - 1) {
            result.push_back(nums[dq.front()]);
        }
    }
    
    return result;
}
```

### Practice Problems (Week 4)

**Stack:**
1. Valid Parentheses
2. Implement Stack using Queues
3. Min Stack
4. Next Greater Element
5. Daily Temperatures
6. Largest Rectangle in Histogram

**Queue:**
1. Implement Queue using Stacks
2. Generate Parentheses
3. Sliding Window Maximum
4. Task Scheduler
5. Design Circular Queue

---

# PHASE 2: CORE DATA STRUCTURES (Weeks 5-10)

## Week 5-6: Hash Tables and Sets

### Description

**Hash Table** stores key-value pairs. A hash function converts keys to array indices for O(1) average operations.

**How it works:**
1. Hash function computes index from key
2. Store value at that index
3. Handle collisions (when two keys hash to same index)

**Collision Resolution:**
- **Chaining:** Each bucket holds a list of entries
- **Open Addressing:** Find next available slot

**Trade-offs:**
- O(1) average, O(n) worst case
- Uses more memory
- Not ordered (unless using ordered map)

```cpp
// Hash Table Implementation with Chaining
class HashTable {
private:
    vector<vector<pair<string, int>>> buckets;
    int size;
    
    int hash(string key) {
        int h = 0;
        for (char c : key) {
            h = h * 31 + c;  // Simple hash function
        }
        return h % buckets.size();
    }
    
public:
    HashTable(int capacity = 16) : buckets(capacity), size(0) {}
    
    void put(string key, int value) {
        int index = hash(key);
        
        // Check if key exists, update if found
        for (auto& pair : buckets[index]) {
            if (pair.first == key) {
                pair.second = value;
                return;
            }
        }
        
        // Add new key-value pair
        buckets[index].push_back({key, value});
        size++;
    }
    
    int get(string key) {
        int index = hash(key);
        
        for (auto& pair : buckets[index]) {
            if (pair.first == key) {
                return pair.second;
            }
        }
        throw runtime_error("Key not found");
    }
    
    void remove(string key) {
        int index = hash(key);
        
        for (auto it = buckets[index].begin(); it != buckets[index].end(); it++) {
            if (it->first == key) {
                buckets[index].erase(it);
                size--;
                return;
            }
        }
    }
};

// Common Patterns

// Pattern 1: Two Sum
// Problem: Find two numbers that add to target
vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> seen;  // value -> index
    
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        
        // If complement exists, we found our pair
        if (seen.find(complement) != seen.end()) {
            return {seen[complement], i};
        }
        
        // Store current number
        seen[nums[i]] = i;
    }
    return {};
}

// Pattern 2: Group Anagrams
// Problem: Group strings that are anagrams
vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> groups;
    
    for (string s : strs) {
        string key = s;
        sort(key.begin(), key.end());  // Sorted string is the key
        groups[key].push_back(s);
    }
    
    vector<vector<string>> result;
    for (auto& pair : groups) {
        result.push_back(pair.second);
    }
    return result;
}

// Pattern 3: Longest Substring Without Repeating
int longestUniqueSubstring(string s) {
    unordered_set<char> seen;
    int left = 0;
    int maxLength = 0;
    
    for (int right = 0; right < s.size(); right++) {
        // If duplicate found, shrink window from left
        while (seen.find(s[right]) != seen.end()) {
            seen.erase(s[left]);
            left++;
        }
        
        seen.insert(s[right]);
        maxLength = max(maxLength, right - left + 1);
    }
    
    return maxLength;
}
```

### Practice Problems (Week 5-6)

**Easy:**
1. Contains Duplicate
2. Valid Anagram
3. Intersection of Two Arrays
4. Happy Number
5. Single Number

**Medium:**
1. Two Sum
2. Group Anagrams
3. Top K Frequent Elements
4. Longest Consecutive Sequence
5. Subarray Sum Equals K
6. First Unique Character in String

**Hard:**
1. Minimum Window Substring
2. Find Median from Data Stream
3. LFU Cache

---

## Week 7-8: Trees

### Description

A **tree** is a hierarchical structure with nodes. Each node has at most two children (binary tree).

**Key Terms:**
- **Root:** Topmost node
- **Parent/Child:** Direct relationships
- **Leaf:** Node with no children
- **Depth:** Distance from root
- **Height:** Distance to farthest leaf

**Traversals:**
- **Preorder:** Root → Left → Right
- **Inorder:** Left → Root → Right
- **Postorder:** Left → Right → Root
- **Level Order:** Level by level (BFS)

```cpp
// Tree Node
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// All Traversals

// Preorder (Root, Left, Right)
vector<int> preorderTraversal(TreeNode* root) {
    vector<int> result;
    
    function<void(TreeNode*)> dfs = [&](TreeNode* node) {
        if (node == nullptr) return;
        result.push_back(node->val);      // Visit root
        dfs(node->left);                   // Traverse left
        dfs(node->right);                  // Traverse right
    };
    
    dfs(root);
    return result;
}

// Inorder (Left, Root, Right)
vector<int> inorderTraversal(TreeNode* root) {
    vector<int> result;
    
    function<void(TreeNode*)> dfs = [&](TreeNode* node) {
        if (node == nullptr) return;
        dfs(node->left);                   // Traverse left
        result.push_back(node->val);       // Visit root
        dfs(node->right);                  // Traverse right
    };
    
    dfs(root);
    return result;
}

// Postorder (Left, Right, Root)
vector<int> postorderTraversal(TreeNode* root) {
    vector<int> result;
    
    function<void(TreeNode*)> dfs = [&](TreeNode* node) {
        if (node == nullptr) return;
        dfs(node->left);                   // Traverse left
        dfs(node->right);                  // Traverse right
        result.push_back(node->val);       // Visit root
    };
    
    dfs(root);
    return result;
}

// Level Order (BFS)
vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> result;
    if (root == nullptr) return result;
    
    queue<TreeNode*> q;
    q.push(root);
    
    while (!q.empty()) {
        int levelSize = q.size();
        vector<int> level;
        
        for (int i = 0; i < levelSize; i++) {
            TreeNode* node = q.front();
            q.pop();
            level.push_back(node->val);
            
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        
        result.push_back(level);
    }
    
    return result;
}

// Common Patterns

// Pattern 1: Maximum Depth
int maxDepth(TreeNode* root) {
    if (root == nullptr) return 0;
    return 1 + max(maxDepth(root->left), maxDepth(root->right));
}

// Pattern 2: Same Tree
bool isSameTree(TreeNode* p, TreeNode* q) {
    if (p == nullptr && q == nullptr) return true;
    if (p == nullptr || q == nullptr) return false;
    if (p->val != q->val) return false;
    
    return isSameTree(p->left, q->left) && 
           isSameTree(p->right, q->right);
}

// Pattern 3: Invert/Flip Tree
TreeNode* invertTree(TreeNode* root) {
    if (root == nullptr) return nullptr;
    
    swap(root->left, root->right);  // Swap children
    invertTree(root->left);          // Recurse
    invertTree(root->right);
    
    return root;
}

// Pattern 4: Lowest Common Ancestor
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (root == nullptr) return nullptr;
    
    // If p or q is root, then root is LCA
    if (root == p || root == q) return root;
    
    // Search in left and right subtrees
    TreeNode* left = lowestCommonAncestor(root->left, p, q);
    TreeNode* right = lowestCommonAncestor(root->right, p, q);
    
    // If both found in different subtrees, root is LCA
    if (left != nullptr && right != nullptr) return root;
    
    // Otherwise, return the one that's not null
    return left != nullptr ? left : right;
}

// Pattern 5: Path Sum
bool hasPathSum(TreeNode* root, int targetSum) {
    if (root == nullptr) return false;
    
    // If leaf, check if remaining sum equals leaf value
    if (root->left == nullptr && root->right == nullptr) {
        return targetSum == root->val;
    }
    
    // Recurse with reduced target
    return hasPathSum(root->left, targetSum - root->val) ||
           hasPathSum(root->right, targetSum - root->val);
}
```

### Binary Search Tree (BST)

**Property:** Left subtree < Root < Right subtree

```cpp
// Search in BST
TreeNode* searchBST(TreeNode* root, int val) {
    if (root == nullptr || root->val == val) return root;
    
    if (val < root->val) {
        return searchBST(root->left, val);   // Go left
    } else {
        return searchBST(root->right, val);  // Go right
    }
}

// Validate BST
bool isValidBST(TreeNode* root) {
    function<bool(TreeNode*, long, long)> validate = 
        [&](TreeNode* node, long minVal, long maxVal) {
        if (node == nullptr) return true;
        
        if (node->val <= minVal || node->val >= maxVal) {
            return false;
        }
        
        return validate(node->left, minVal, node->val) &&
               validate(node->right, node->val, maxVal);
    };
    
    return validate(root, LONG_MIN, LONG_MAX);
}

// Insert into BST
TreeNode* insertIntoBST(TreeNode* root, int val) {
    if (root == nullptr) return new TreeNode(val);
    
    if (val < root->val) {
        root->left = insertIntoBST(root->left, val);
    } else {
        root->right = insertIntoBST(root->right, val);
    }
    
    return root;
}

// Kth Smallest Element
int kthSmallest(TreeNode* root, int k) {
    int count = 0;
    int result = 0;
    
    function<void(TreeNode*)> inorder = [&](TreeNode* node) {
        if (node == nullptr || count >= k) return;
        
        inorder(node->left);
        count++;
        if (count == k) {
            result = node->val;
            return;
        }
        inorder(node->right);
    };
    
    inorder(root);
    return result;
}
```

### Practice Problems (Week 7-8)

**Easy:**
1. Maximum Depth of Binary Tree
2. Same Tree
3. Invert Binary Tree
4. Balanced Binary Tree
5. Path Sum

**Medium:**
1. Level Order Traversal
2. Binary Tree Zigzag Level Order
3. Lowest Common Ancestor
4. Validate Binary Search Tree
5. Kth Smallest Element in BST
6. Convert Sorted Array to BST
7. Binary Tree Right Side View

**Hard:**
1. Serialize and Deserialize Binary Tree
2. Recover Binary Search Tree
3. Flatten Binary Tree to Linked List

---

## Week 9-10: Sorting and Searching

### Sorting Algorithms Comparison

| Algorithm | Best | Average | Worst | Space | Stable | When to Use |
|-----------|------|---------|-------|-------|--------|-------------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes | Teaching only |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | No | Small arrays |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes | Small/nearly sorted |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Stable sort needed |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | No | General purpose |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Space constrained |

### Implementations

```cpp
// Merge Sort - O(n log n)
void mergeSort(vector<int>& arr, int left, int right) {
    if (left >= right) return;
    
    int mid = left + (right - left) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}

void merge(vector<int>& arr, int left, int mid, int right) {
    vector<int> temp(right - left + 1);
    int i = left, j = mid + 1, k = 0;
    
    // Merge two sorted halves
    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) {
            temp[k++] = arr[i++];
        } else {
            temp[k++] = arr[j++];
        }
    }
    
    // Copy remaining
    while (i <= mid) temp[k++] = arr[i++];
    while (j <= right) temp[k++] = arr[j++];
    
    // Copy back to original
    for (int i = 0; i < temp.size(); i++) {
        arr[left + i] = temp[i];
    }
}

// Quick Sort - O(n log n) average
void quickSort(vector<int>& arr, int left, int right) {
    if (left >= right) return;
    
    int pivotIndex = partition(arr, left, right);
    quickSort(arr, left, pivotIndex - 1);
    quickSort(arr, pivotIndex + 1, right);
}

int partition(vector<int>& arr, int left, int right) {
    int pivot = arr[right];
    int i = left - 1;
    
    for (int j = left; j < right; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[right]);
    return i + 1;
}

// Heap Sort - O(n log n)
void heapSort(vector<int>& arr) {
    int n = arr.size();
    
    // Build max heap
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }
    
    // Extract elements
    for (int i = n - 1; i > 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}

void heapify(vector<int>& arr, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    
    if (left < n && arr[left] > arr[largest]) {
        largest = left;
    }
    if (right < n && arr[right] > arr[largest]) {
        largest = right;
    }
    
    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}
```

### Binary Search Variations

```cpp
// Basic Binary Search
int binarySearch(vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}

// Find First Occurrence
int findFirst(vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    int result = -1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            result = mid;
            right = mid - 1;  // Continue searching left
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return result;
}

// Search in Rotated Sorted Array
int searchRotated(vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) return mid;
        
        // Left half is sorted
        if (arr[left] <= arr[mid]) {
            if (arr[left] <= target && target < arr[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        // Right half is sorted
        else {
            if (arr[mid] < target && target <= arr[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }
    return -1;
}

// Find Peak Element
int findPeak(vector<int>& arr) {
    int left = 0, right = arr.size() - 1;
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] < arr[mid + 1]) {
            left = mid + 1;  // Peak is in right half
        } else {
            right = mid;     // Peak is in left half (or is mid)
        }
    }
    return left;  // or right
}
```

### Practice Problems (Week 9-10)

**Sorting:**
1. Sort an Array (implement any O(n log n))
2. Merge Intervals
3. Insert Interval
4. Meeting Rooms II
5. Kth Largest Element in Array

**Binary Search:**
1. Binary Search
2. Search Insert Position
3. Find First and Last Position
4. Search in Rotated Sorted Array
5. Find Peak Element
6. Find Minimum in Rotated Sorted Array
7. Median of Two Sorted Arrays (Hard)

---

# PHASE 3: ADVANCED ALGORITHMS (Weeks 11-16)

## Week 11-12: Heaps and Priority Queues

### Description

A **heap** is a complete binary tree that satisfies the heap property:
- **Min-Heap:** Parent ≤ Children (root is minimum)
- **Max-Heap:** Parent ≥ Children (root is maximum)

**Operations:**
- Push: O(log n) - Add and heapify up
- Pop: O(log n) - Remove root and heapify down
- Peek: O(1) - View root

```cpp
// Min-Heap Implementation
class MinHeap {
private:
    vector<int> heap;
    
    int parent(int i) { return (i - 1) / 2; }
    int left(int i) { return 2 * i + 1; }
    int right(int i) { return 2 * i + 2; }
    
    void heapifyUp(int i) {
        while (i > 0 && heap[parent(i)] > heap[i]) {
            swap(heap[i], heap[parent(i)]);
            i = parent(i);
        }
    }
    
    void heapifyDown(int i) {
        int smallest = i;
        int l = left(i);
        int r = right(i);
        
        if (l < heap.size() && heap[l] < heap[smallest]) {
            smallest = l;
        }
        if (r < heap.size() && heap[r] < heap[smallest]) {
            smallest = r;
        }
        
        if (smallest != i) {
            swap(heap[i], heap[smallest]);
            heapifyDown(smallest);
        }
    }
    
public:
    void push(int val) {
        heap.push_back(val);
        heapifyUp(heap.size() - 1);
    }
    
    int pop() {
        if (heap.empty()) throw runtime_error("Heap is empty");
        
        int root = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        
        if (!heap.empty()) {
            heapifyDown(0);
        }
        return root;
    }
    
    int peek() {
        if (heap.empty()) throw runtime_error("Heap is empty");
        return heap[0];
    }
    
    bool empty() { return heap.empty(); }
};

// Common Patterns

// Pattern 1: Kth Largest Element
int kthLargest(vector<int>& nums, int k) {
    priority_queue<int, vector<int>, greater<int>> minHeap;
    
    for (int num : nums) {
        minHeap.push(num);
        if (minHeap.size() > k) {
            minHeap.pop();  // Remove smallest
        }
    }
    
    return minHeap.top();  // Kth largest
}

// Pattern 2: Top K Frequent Elements
vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int, int> freq;
    for (int num : nums) freq[num]++;
    
    // Min-heap of (frequency, element)
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
    
    for (auto& [num, count] : freq) {
        minHeap.push({count, num});
        if (minHeap.size() > k) {
            minHeap.pop();
        }
    }
    
    vector<int> result;
    while (!minHeap.empty()) {
        result.push_back(minHeap.top().second);
        minHeap.pop();
    }
    return result;
}

// Pattern 3: Merge K Sorted Lists
ListNode* mergeKLists(vector<ListNode*>& lists) {
    // Min-heap: (value, listIndex, node)
    auto cmp = [](ListNode* a, ListNode* b) {
        return a->val > b->val;
    };
    priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> minHeap(cmp);
    
    // Add first node from each list
    for (ListNode* node : lists) {
        if (node) minHeap.push(node);
    }
    
    ListNode dummy(0);
    ListNode* current = &dummy;
    
    while (!minHeap.empty()) {
        ListNode* node = minHeap.top();
        minHeap.pop();
        
        current->next = node;
        current = current->next;
        
        if (node->next) {
            minHeap.push(node->next);
        }
    }
    
    return dummy.next;
}
```

### Practice Problems (Week 11-12)

**Easy:**
1. Kth Largest Element in Stream
2. Last Stone Weight
3. Kth Largest Element in Array

**Medium:**
1. Top K Frequent Elements
2. Merge K Sorted Lists
3. Find Median from Data Stream
4. Task Scheduler
5. Reorganize String

**Hard:**
1. Sliding Window Median
2. Maximum Frequency Stack
3. IPO

---

## Week 13-14: Dynamic Programming

### Description

**Dynamic Programming** solves complex problems by:
1. Breaking into overlapping subproblems
2. Storing results to avoid recomputation

**Two approaches:**
- **Memoization (Top-Down):** Recursive with caching
- **Tabulation (Bottom-Up):** Iterative with table

**When to use DP:**
1. **Optimal substructure:** Optimal solution uses optimal sub-solutions
2. **Overlapping subproblems:** Same subproblems solved multiple times

```cpp
// Pattern 1: 1D DP - Climbing Stairs
// Problem: Count ways to climb n stairs (1 or 2 steps at a time)

// Memoization approach
int climbStairsMemo(int n, vector<int>& memo) {
    if (n <= 2) return n;
    if (memo[n] != -1) return memo[n];
    
    memo[n] = climbStairsMemo(n - 1, memo) + climbStairsMemo(n - 2, memo);
    return memo[n];
}

int climbStairs(int n) {
    vector<int> memo(n + 1, -1);
    return climbStairsMemo(n, memo);
}

// Tabulation approach (better)
int climbStairsTab(int n) {
    if (n <= 2) return n;
    
    vector<int> dp(n + 1);
    dp[1] = 1;
    dp[2] = 2;
    
    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2];  // Can reach i from i-1 or i-2
    }
    
    return dp[n];
}

// Space optimized
int climbStairsOptimized(int n) {
    if (n <= 2) return n;
    
    int prev2 = 1, prev1 = 2;
    
    for (int i = 3; i <= n; i++) {
        int current = prev1 + prev2;
        prev2 = prev1;
        prev1 = current;
    }
    
    return prev1;
}

// Pattern 2: House Robber
// Problem: Maximum amount without robbing adjacent houses
int rob(vector<int>& nums) {
    if (nums.empty()) return 0;
    if (nums.size() == 1) return nums[0];
    
    vector<int> dp(nums.size());
    dp[0] = nums[0];
    dp[1] = max(nums[0], nums[1]);
    
    for (int i = 2; i < nums.size(); i++) {
        // Either skip house i (dp[i-1]) or rob it (dp[i-2] + nums[i])
        dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
    }
    
    return dp.back();
}

// Pattern 3: Coin Change
// Problem: Minimum coins to make amount
int coinChange(vector<int>& coins, int amount) {
    vector<int> dp(amount + 1, amount + 1);  // Initialize with impossible value
    dp[0] = 0;
    
    for (int coin : coins) {
        for (int i = coin; i <= amount; i++) {
            dp[i] = min(dp[i], dp[i - coin] + 1);
        }
    }
    
    return dp[amount] > amount ? -1 : dp[amount];
}

// Pattern 4: Longest Increasing Subsequence
int lengthOfLIS(vector<int>& nums) {
    if (nums.empty()) return 0;
    
    vector<int> dp(nums.size(), 1);  // Each element is LIS of length 1
    
    for (int i = 1; i < nums.size(); i++) {
        for (int j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }
    
    return *max_element(dp.begin(), dp.end());
}

// Pattern 5: 2D DP - Longest Common Subsequence
int longestCommonSubsequence(string text1, string text2) {
    int m = text1.size(), n = text2.size();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (text1[i-1] == text2[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    
    return dp[m][n];
}

// Pattern 6: 0/1 Knapsack
int knapsack(vector<int>& weights, vector<int>& values, int capacity) {
    int n = weights.size();
    vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));
    
    for (int i = 1; i <= n; i++) {
        for (int w = 0; w <= capacity; w++) {
            // Don't include item i
            dp[i][w] = dp[i-1][w];
            
            // Include item i (if it fits)
            if (weights[i-1] <= w) {
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1]);
            }
        }
    }
    
    return dp[n][capacity];
}

// Pattern 7: Edit Distance
int minDistance(string word1, string word2) {
    int m = word1.size(), n = word2.size();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1));
    
    // Base cases
    for (int i = 0; i <= m; i++) dp[i][0] = i;
    for (int j = 0; j <= n; j++) dp[0][j] = j;
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (word1[i-1] == word2[j-1]) {
                dp[i][j] = dp[i-1][j-1];  // No operation needed
            } else {
                dp[i][j] = 1 + min({
                    dp[i-1][j],    // Delete
                    dp[i][j-1],    // Insert
                    dp[i-1][j-1]   // Replace
                });
            }
        }
    }
    
    return dp[m][n];
}
```

### Practice Problems (Week 13-14)

**Easy:**
1. Climbing Stairs
2. House Robber
3. Maximum Subarray
4. Jump Game
5. Coin Change II

**Medium:**
1. Coin Change
2. Longest Increasing Subsequence
3. Longest Common Subsequence
4. Word Break
5. Partition Equal Subset Sum
6. Target Sum
7. Unique Paths

**Hard:**
1. Edit Distance
2. Regular Expression Matching
3. Burst Balloons
4. Best Time to Buy/Sell Stock with Cooldown
5. Palindrome Partitioning II

---

## Week 15-16: Graphs

### Description

A **graph** is a collection of nodes (vertices) connected by edges.

**Representations:**
- **Adjacency List:** `unordered_map<int, vector<int>>` - Space: O(V + E)
- **Adjacency Matrix:** `vector<vector<int>>` - Space: O(V²)

**Traversals:**
- **DFS:** Explore as deep as possible, then backtrack
- **BFS:** Explore level by level

```cpp
// Graph Representation
class Graph {
private:
    unordered_map<int, vector<int>> adj;
    
public:
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u);  // Remove for directed graph
    }
    
    // DFS - Recursive
    void dfs(int node, unordered_set<int>& visited) {
        visited.insert(node);
        cout << node << " ";
        
        for (int neighbor : adj[node]) {
            if (visited.find(neighbor) == visited.end()) {
                dfs(neighbor, visited);
            }
        }
    }
    
    // DFS - Iterative
    void dfsIterative(int start) {
        unordered_set<int> visited;
        stack<int> st;
        st.push(start);
        
        while (!st.empty()) {
            int node = st.top();
            st.pop();
            
            if (visited.find(node) == visited.end()) {
                visited.insert(node);
                cout << node << " ";
                
                for (int neighbor : adj[node]) {
                    if (visited.find(neighbor) == visited.end()) {
                        st.push(neighbor);
                    }
                }
            }
        }
    }
    
    // BFS
    void bfs(int start) {
        unordered_set<int> visited;
        queue<int> q;
        q.push(start);
        visited.insert(start);
        
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            cout << node << " ";
            
            for (int neighbor : adj[node]) {
                if (visited.find(neighbor) == visited.end()) {
                    visited.insert(neighbor);
                    q.push(neighbor);
                }
            }
        }
    }
};

// Common Patterns

// Pattern 1: Number of Islands (DFS)
int numIslands(vector<vector<char>>& grid) {
    if (grid.empty()) return 0;
    
    int rows = grid.size();
    int cols = grid[0].size();
    int count = 0;
    
    function<void(int, int)> dfs = [&](int r, int c) {
        if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] != '1') {
            return;
        }
        
        grid[r][c] = '0';  // Mark as visited
        dfs(r + 1, c);
        dfs(r - 1, c);
        dfs(r, c + 1);
        dfs(r, c - 1);
    };
    
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == '1') {
                count++;
                dfs(i, j);
            }
        }
    }
    
    return count;
}

// Pattern 2: Clone Graph (DFS with map)
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() : val(0), neighbors({}) {}
    Node(int _val) : val(_val), neighbors({}) {}
};

Node* cloneGraph(Node* node) {
    if (node == nullptr) return nullptr;
    
    unordered_map<Node*, Node*> visited;
    
    function<Node*(Node*)> dfs = [&](Node* n) -> Node* {
        if (visited.find(n) != visited.end()) {
            return visited[n];
        }
        
        Node* copy = new Node(n->val);
        visited[n] = copy;
        
        for (Node* neighbor : n->neighbors) {
            copy->neighbors.push_back(dfs(neighbor));
        }
        
        return copy;
    };
    
    return dfs(node);
}

// Pattern 3: Course Schedule (Cycle Detection)
bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
    unordered_map<int, vector<int>> graph;
    vector<int> inDegree(numCourses, 0);
    
    for (auto& prereq : prerequisites) {
        int course = prereq[0];
        int pre = prereq[1];
        graph[pre].push_back(course);
        inDegree[course]++;
    }
    
    // Queue of courses with no prerequisites
    queue<int> q;
    for (int i = 0; i < numCourses; i++) {
        if (inDegree[i] == 0) q.push(i);
    }
    
    int processed = 0;
    while (!q.empty()) {
        int course = q.front();
        q.pop();
        processed++;
        
        for (int neighbor : graph[course]) {
            inDegree[neighbor]--;
            if (inDegree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }
    
    return processed == numCourses;  // True if no cycle
}

// Pattern 4: Dijkstra's Algorithm (Shortest Path)
vector<int> dijkstra(int start, unordered_map<int, vector<pair<int, int>>>& graph, int n) {
    vector<int> dist(n, INT_MAX);
    dist[start] = 0;
    
    // Min-heap: (distance, node)
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, start});
    
    while (!pq.empty()) {
        int d = pq.top().first;
        int node = pq.top().second;
        pq.pop();
        
        if (d > dist[node]) continue;
        
        for (auto& [neighbor, weight] : graph[node]) {
            int newDist = d + weight;
            if (newDist < dist[neighbor]) {
                dist[neighbor] = newDist;
                pq.push({newDist, neighbor});
            }
        }
    }
    
    return dist;
}

// Pattern 5: Union-Find (Disjoint Set)
class UnionFind {
private:
    vector<int> parent;
    vector<int> rank;
    
public:
    UnionFind(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++) parent[i] = i;
    }
    
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);  // Path compression
        }
        return parent[x];
    }
    
    bool unite(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return false;
        
        // Union by rank
        if (rank[px] < rank[py]) swap(px, py);
        parent[py] = px;
        if (rank[px] == rank[py]) rank[px]++;
        
        return true;
    }
};

// Number of Connected Components
int countComponents(int n, vector<vector<int>>& edges) {
    UnionFind uf(n);
    int components = n;
    
    for (auto& edge : edges) {
        if (uf.unite(edge[0], edge[1])) {
            components--;
        }
    }
    
    return components;
}
```

### Practice Problems (Week 15-16)

**Easy:**
1. Number of Islands
2. Max Area of Island
3. Number of Connected Components
4. Clone Graph

**Medium:**
1. Course Schedule I & II
2. Pacific Atlantic Water Flow
3. Word Ladder
4. Network Delay Time
5. Min Cost to Connect All Points
6. Reconstruct Itinerary

**Hard:**
1. Alien Dictionary
2. Cheapest Flights Within K Stops
3. Minimum Weighted Subgraph With Two Shortest Paths

---

# OOPs CONCEPTS COMPLETE GUIDE

## Understanding Access Specifiers

### Why Use Private/Protected Instead of Public?

**Public:** Accessible from anywhere - breaks encapsulation
**Private:** Accessible only within class - full control
**Protected:** Accessible within class and derived classes - for inheritance

### Complete Example with All Access Levels

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Base class demonstrating all access levels
class BankAccount {
private:
    // Private: Only accessible within this class
    // Direct modification from outside is IMPOSSIBLE
    double balance;
    string accountNumber;
    
    // Private helper function
    void validateTransaction(double amount) {
        if (amount <= 0) {
            throw invalid_argument("Amount must be positive");
        }
    }
    
protected:
    // Protected: Accessible in this class AND derived classes
    // But NOT from outside
    string accountHolder;
    bool isActive;
    
    // Protected method for derived classes to use
    void updateLastTransaction(string type, double amount) {
        lastTransactionType = type;
        lastTransactionAmount = amount;
    }
    
private:
    string lastTransactionType;
    double lastTransactionAmount;
    
public:
    // Public: Accessible from anywhere
    BankAccount(string holder, string accNum, double initialBalance) 
        : accountHolder(holder), accountNumber(accNum), 
          balance(initialBalance), isActive(true), lastTransactionAmount(0) {}
    
    // Public interface - controls access to private data
    bool deposit(double amount) {
        validateTransaction(amount);
        balance += amount;
        updateLastTransaction("Deposit", amount);
        return true;
    }
    
    bool withdraw(double amount) {
        validateTransaction(amount);
        if (amount > balance) {
            throw insufficient_funds();
        }
        balance -= amount;
        updateLastTransaction("Withdraw", amount);
        return true;
    }
    
    // Read-only access to balance
    double getBalance() const {
        return balance;
    }
    
    string getAccountNumber() const {
        return accountNumber;
    }
    
    void display() const {
        cout << "Account: " << accountNumber << endl;
        cout << "Holder: " << accountHolder << endl;
        cout << "Balance: $" << balance << endl;
        cout << "Status: " << (isActive ? "Active" : "Inactive") << endl;
    }
    
    // Cannot do this - balance is private:
    // balance = -1000000;  // ERROR!
};

// Derived class - demonstrates protected access
class SavingsAccount : public BankAccount {
private:
    double interestRate;
    
protected:
    // Can access protected members from base class
    void applyInterest() {
        // isActive is protected - accessible here
        if (isActive) {
            double interest = getBalance() * interestRate / 100;
            // We can't directly access balance (private), 
            // but we use public interface
            deposit(interest);
            updateLastTransaction("Interest", interest);
        }
    }
    
public:
    SavingsAccount(string holder, string accNum, double initial, double rate)
        : BankAccount(holder, accNum, initial), interestRate(rate) {}
    
    void addInterest() {
        applyInterest();  // Calls protected method
    }
    
    // Can also access protected members directly
    bool isAccountActive() {
        return isActive;  // OK - protected is accessible
    }
};

// Demonstration
int main() {
    BankAccount acc("John Doe", "12345", 1000);
    
    acc.deposit(500);    // OK - public
    acc.withdraw(200);   // OK - public
    acc.display();
    
    // acc.balance = -500;        // ERROR - private!
    // acc.accountHolder = "X";   // ERROR - protected!
    // acc.isActive = false;      // ERROR - protected!
    
    SavingsAccount savings("Jane", "67890", 1000, 5);
    savings.addInterest();
    savings.display();
    
    // savings.applyInterest();   // ERROR - protected method!
    
    return 0;
}
```

## Complete OOPs Example: Library Management System

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

// Abstract Base Class - demonstrates Abstraction
class LibraryItem {
private:
    string itemId;
    string title;
    string author;
    bool isAvailable;
    
protected:
    // Protected for derived classes
    int loanPeriod;
    
public:
    LibraryItem(string id, string t, string a) 
        : itemId(id), title(t), author(a), isAvailable(true), loanPeriod(14) {}
    
    virtual ~LibraryItem() = default;
    
    // Pure virtual function - makes this class abstract
    virtual string getItemType() const = 0;
    
    // Virtual function - can be overridden
    virtual void display() const {
        cout << "Title: " << title << endl;
        cout << "Author: " << author << endl;
        cout << "Available: " << (isAvailable ? "Yes" : "No") << endl;
    }
    
    // Getters (Encapsulation - controlled access)
    string getTitle() const { return title; }
    bool getAvailability() const { return isAvailable; }
    
    // Public interface for borrowing
    bool borrow() {
        if (!isAvailable) {
            cout << "Item not available!" << endl;
            return false;
        }
        isAvailable = false;
        return true;
    }
    
    bool returnItem() {
        isAvailable = true;
        return true;
    }
};

// Derived Class 1 - Book
class Book : public LibraryItem {
private:
    string isbn;
    int pageCount;
    
public:
    Book(string id, string title, string author, string isbn, int pages)
        : LibraryItem(id, title, author), isbn(isbn), pageCount(pages) {
        loanPeriod = 21;  // Books have 3 week loan
    }
    
    string getItemType() const override {
        return "Book";
    }
    
    void display() const override {
        LibraryItem::display();
        cout << "Type: Book" << endl;
        cout << "ISBN: " << isbn << endl;
        cout << "Pages: " << pageCount << endl;
        cout << "Loan Period: " << loanPeriod << " days" << endl;
    }
};

// Derived Class 2 - DVD
class DVD : public LibraryItem {
private:
    string director;
    int duration;  // in minutes
    
public:
    DVD(string id, string title, string author, string dir, int dur)
        : LibraryItem(id, title, author), director(dir), duration(dur) {
        loanPeriod = 7;  // DVDs have 1 week loan
    }
    
    string getItemType() const override {
        return "DVD";
    }
    
    void display() const override {
        LibraryItem::display();
        cout << "Type: DVD" << endl;
        cout << "Director: " << director << endl;
        cout << "Duration: " << duration << " minutes" << endl;
        cout << "Loan Period: " << loanPeriod << " days" << endl;
    }
};

// Member class - demonstrates Composition
class Member {
private:
    string memberId;
    string name;
    string email;
    vector<LibraryItem*> borrowedItems;
    
public:
    Member(string id, string name, string email)
        : memberId(id), name(name), email(email) {}
    
    void borrowItem(LibraryItem* item) {
        if (item->borrow()) {
            borrowedItems.push_back(item);
            cout << name << " borrowed: " << item->getTitle() << endl;
        }
    }
    
    void returnItem(LibraryItem* item) {
        for (auto it = borrowedItems.begin(); it != borrowedItems.end(); it++) {
            if (*it == item) {
                item->returnItem();
                borrowedItems.erase(it);
                cout << name << " returned: " << item->getTitle() << endl;
                return;
            }
        }
    }
    
    void displayBorrowed() const {
        cout << "\n=== " << name << "'s Borrowed Items ===" << endl;
        for (LibraryItem* item : borrowedItems) {
            cout << "- " << item->getTitle() << " (" << item->getItemType() << ")" << endl;
        }
    }
    
    string getName() const { return name; }
};

// Library class - demonstrates encapsulation and data hiding
class Library {
private:
    vector<LibraryItem*> items;
    vector<Member*> members;
    unordered_map<string, LibraryItem*> itemIndex;  // itemId -> item
    
public:
    ~Library() {
        for (auto item : items) delete item;
        for (auto member : members) delete member;
    }
    
    void addItem(LibraryItem* item) {
        items.push_back(item);
        itemIndex[item->getTitle()] = item;
    }
    
    void addMember(Member* member) {
        members.push_back(member);
    }
    
    // Search functionality
    vector<LibraryItem*> searchByTitle(string title) {
        vector<LibraryItem*> results;
        for (auto item : items) {
            if (item->getTitle().find(title) != string::npos) {
                results.push_back(item);
            }
        }
        return results;
    }
    
    void displayAll() const {
        cout << "\n=== Library Catalog ===" << endl;
        for (auto item : items) {
            item->display();
            cout << "---" << endl;
        }
    }
};

// Main demonstration
int main() {
    Library library;
    
    // Create items (Polymorphism - base class pointers)
    library.addItem(new Book("B001", "The Great Gatsby", "F. Scott Fitzgerald", 
                             "978-0743273565", 180));
    library.addItem(new Book("B002", "1984", "George Orwell", 
                             "978-0451524935", 328));
    library.addItem(new DVD("D001", "Inception", "Christopher Nolan", 
                            "Christopher Nolan", 148));
    
    // Create members
    Member* alice = new Member("M001", "Alice", "alice@email.com");
    Member* bob = new Member("M002", "Bob", "bob@email.com");
    
    library.addMember(alice);
    library.addMember(bob);
    
    // Demonstrate polymorphism
    library.displayAll();
    
    // Demonstrate encapsulation
    alice->borrowItem(library.searchByTitle("Gatsby")[0]);
    bob->borrowItem(library.searchByTitle("1984")[0]);
    
    alice->displayBorrowed();
    bob->displayBorrowed();
    
    return 0;
}
```

---

# ADDITIONAL TOPICS BEYOND DSA

## 1. System Design Basics

### What is System Design?
Designing large-scale systems that are scalable, reliable, and maintainable.

### Key Concepts

```
// Load Balancing - Distribute traffic across servers
// User Request → Load Balancer → Server 1/2/3

// Caching - Store frequently accessed data
// Redis/Memcached for fast access

// Database Sharding - Split database across servers
// Users 1-1M → Shard A, Users 1M-2M → Shard B

// Message Queues - Async processing
// User Action → Queue → Background Worker
```

## 2. Bit Manipulation

```cpp
// Common Operations
bool getBit(int num, int i) { return (num >> i) & 1; }
int setBit(int num, int i) { return num | (1 << i); }
int clearBit(int num, int i) { return num & ~(1 << i); }
int toggleBit(int num, int i) { return num ^ (1 << i); }

// Check if power of 2
bool isPowerOfTwo(int n) { return n > 0 && (n & (n-1)) == 0; }

// Count set bits
int countSetBits(int n) {
    int count = 0;
    while (n) { n &= n-1; count++; }
    return count;
}

// Find unique number (others appear twice)
int singleNumber(vector<int>& nums) {
    int result = 0;
    for (int n : nums) result ^= n;
    return result;
}
```

## 3. Design Patterns

### Singleton Pattern
```cpp
class Singleton {
private:
    static Singleton* instance;
    Singleton() {}
    
public:
    static Singleton* getInstance() {
        if (instance == nullptr) {
            instance = new Singleton();
        }
        return instance;
    }
};
```

### Factory Pattern
```cpp
class Shape {
public:
    virtual void draw() = 0;
    virtual ~Shape() = default;
};

class Circle : public Shape {
    void draw() override { cout << "Circle" << endl; }
};

class Square : public Shape {
    void draw() override { cout << "Square" << endl; }
};

class ShapeFactory {
public:
    static Shape* createShape(string type) {
        if (type == "circle") return new Circle();
        if (type == "square") return new Square();
        return nullptr;
    }
};
```

---

# FINAL CHECKLIST

## Beginner (0-50 problems)
- [ ] Understand Big O notation
- [ ] Implement arrays and strings operations
- [ ] Implement linked list
- [ ] Implement stack and queue
- [ ] Solve basic recursion problems
- [ ] Use hash tables for frequency counting

## Intermediate (50-150 problems)
- [ ] Master tree traversals
- [ ] Implement and use BST
- [ ] Understand heaps
- [ ] Solve basic DP problems
- [ ] Implement DFS/BFS on graphs
- [ ] Solve medium array/string problems

## Advanced (150-300+ problems)
- [ ] Solve complex DP problems
- [ ] Implement Dijkstra, MST
- [ ] Master advanced patterns (trie, segment tree)
- [ ] Solve hard interview problems
- [ ] Participate in contests

## Beyond DSA
- [ ] Understand basic system design
- [ ] Learn design patterns
- [ ] Practice bit manipulation
- [ ] Understand database concepts
- [ ] Learn about APIs and REST

---

# Practice Problem Bank by Category

## Arrays (50 problems)
Two Sum, Best Time to Buy/Sell Stock, Contains Duplicate, Product of Array Except Self, Maximum Subarray, Merge Intervals, etc.

## Strings (40 problems)
Valid Anagram, Valid Palindrome, Longest Substring Without Repeating, Group Anagrams, etc.

## Linked List (25 problems)
Reverse Linked List, Merge Two Sorted Lists, Remove Nth Node From End, etc.

## Trees (35 problems)
Maximum Depth, Level Order Traversal, Validate BST, etc.

## DP (40 problems)
Climbing Stairs, House Robber, Coin Change, LIS, LCS, etc.

## Graphs (30 problems)
Number of Islands, Course Schedule, Clone Graph, etc.
