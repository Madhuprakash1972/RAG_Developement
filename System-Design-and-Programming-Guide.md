# Complete System Design & Programming Topics Guide
## From Beginner to Professional

---

# PART 1: SYSTEM DESIGN

---

## Table of Contents
1. [Introduction to System Design](#1-introduction-to-system-design)
2. [Load Balancing](#2-load-balancing)
3. [Caching Strategies](#3-caching-strategies)
4. [Database Design & Sharding](#4-database-design--sharding)
5. [Message Queues](#5-message-queues)
6. [CDN & Edge Computing](#6-cdn--edge-computing)
7. [Replication & Failover](#7-replication--failover)
8. [API Design](#8-api-design)
9. [Microservices Architecture](#9-microservices-architecture)
10. [Distributed Systems Concepts](#10-distributed-systems-concepts)
11. [CAP Theorem & Consistency Models](#11-cap-theorem--consistency-models)
12. [Complete System Design Examples](#12-complete-system-design-examples)

---

## 1. Introduction to System Design

### What is System Design?

**System Design** is the process of defining the architecture, components, modules, interfaces, and data for a system to satisfy specified requirements. It's about building systems that are:

| Goal | Definition | Real-World Example |
|------|------------|-------------------|
| **Scalable** | Handle growing traffic/data | Twitter: 500M tweets/day |
| **Reliable** | Work correctly, no data loss | Bank: Transactions never lost |
| **Available** | Always accessible (99.9% uptime) | Google Search: Always up |
| **Maintainable** | Easy to update/extend | Adding new features safely |
| **Efficient** | Low latency, minimal resources | Netflix: <100ms video load |

### Key Metrics

```
Latency: Time to perform operation
  - Target: <100ms for web, <10ms for APIs

Throughput: Requests per second
  - Target: 10,000+ RPS for popular services

Availability: Uptime percentage
  - 99% = 3.65 days downtime/year
  - 99.9% = 8.76 hours downtime/year
  - 99.99% = 52 minutes downtime/year
  - 99.999% = 5 minutes downtime/year

Consistency: Data accuracy across system
  - Strong: All reads see latest write
  - Eventual: All reads eventually see latest write
```

### System Design Process

```
1. Requirements Gathering
   ├── Functional: What system does
   └── Non-functional: Performance, scalability, availability

2. Estimate Capacity
   ├── Users: 1M DAU
   ├── Requests: 100M/day
   └── Storage: 100TB/year

3. High-Level Design
   ├── Components
   ├── Data flow
   └── Technology choices

4. Detailed Design
   ├── Database schema
   ├── API endpoints
   └── Data structures

5. Identify Bottlenecks
   ├── Single points of failure
   ├── Performance bottlenecks
   └── Scaling limits

6. Iterate & Optimize
```

---

## 2. Load Balancing

### What is Load Balancing?

Load balancing distributes incoming traffic across multiple servers to prevent any single server from becoming a bottleneck.

### Why It Matters

| Without Load Balancer | With Load Balancer |
|----------------------|-------------------|
| Single server handles all traffic | Traffic distributed across servers |
| Single point of failure | High availability |
| Limited scalability | Horizontal scaling |
| Downtime for maintenance | Zero-downtime deployments |

### Architecture Diagram

```
                    ┌─────────────────────────────────────┐
                    │         Load Balancer               │
                    │      (Nginx, HAProxy, AWS ELB)      │
                    └─────────────────┬───────────────────┘
                                      │
          ┌───────────────────────────┼───────────────────────────┐
          │                           │                           │
          ▼                           ▼                           ▼
    ┌───────────┐              ┌───────────┐              ┌───────────┐
    │ Server 1  │              │ Server 2  │              │ Server 3  │
    │  (App)    │              │  (App)    │              │  (App)    │
    └───────────┘              └───────────┘              └───────────┘
```

### Load Balancing Algorithms

#### A. Round Robin

```cpp
#include <vector>
#include <string>
#include <mutex>

class RoundRobinLoadBalancer {
private:
    std::vector<std::string> servers = {
        "192.168.1.10:8080",
        "192.168.1.11:8080",
        "192.168.1.12:8080"
    };
    int currentIndex = 0;
    std::mutex mtx;
    
public:
    std::string getNextServer() {
        std::lock_guard<std::mutex> lock(mtx);
        std::string server = servers[currentIndex];
        currentIndex = (currentIndex + 1) % servers.size();
        return server;
    }
};

// Usage
// Request 1 -> Server 1
// Request 2 -> Server 2
// Request 3 -> Server 3
// Request 4 -> Server 1 (cycle repeats)
```

**When to use:** Servers have similar capacity, requests are similar size

#### B. Least Connections

```cpp
#include <map>
#include <mutex>

class LeastConnectionsBalancer {
private:
    std::map<std::string, int> activeConnections = {
        {"192.168.1.10:8080", 15},
        {"192.168.1.11:8080", 8},
        {"192.168.1.12:8080", 22}
    };
    std::mutex mtx;
    
public:
    std::string getNextServer() {
        std::lock_guard<std::mutex> lock(mtx);
        
        std::string selected;
        int minConnections = INT_MAX;
        
        for (const auto& [server, connections] : activeConnections) {
            if (connections < minConnections) {
                minConnections = connections;
                selected = server;
            }
        }
        
        return selected;
    }
    
    void incrementConnection(const std::string& server) {
        activeConnections[server]++;
    }
    
    void decrementConnection(const std::string& server) {
        activeConnections[server]--;
    }
};

// Usage
// Request goes to server with fewest active connections
// Better for long-running connections
```

**When to use:** Long-lived connections (WebSockets, database connections)

#### C. Weighted Load Balancing

```cpp
#include <random>

class WeightedLoadBalancer {
private:
    struct Server {
        std::string address;
        int weight;      // Capacity (higher = more capacity)
        int currentLoad;
    };
    
    std::vector<Server> servers = {
        {"192.168.1.10:8080", 3, 0},  // 3x capacity
        {"192.168.1.11:8080", 2, 0},  // 2x capacity
        {"192.168.1.12:8080", 1, 0}   // 1x capacity
    };
    
public:
    std::string getNextServer() {
        // Select based on weight and current load
        Server* selected = nullptr;
        double bestRatio = -1;
        
        for (auto& server : servers) {
            double loadRatio = (double)server.currentLoad / server.weight;
            if (loadRatio < bestRatio || selected == nullptr) {
                if (server.currentLoad < server.weight) {
                    bestRatio = loadRatio;
                    selected = &server;
                }
            }
        }
        
        if (selected) {
            selected->currentLoad++;
            return selected->address;
        }
        
        return "";  // All servers at capacity
    }
    
    void releaseLoad(const std::string& server) {
        for (auto& s : servers) {
            if (s.address == server) {
                s.currentLoad--;
                break;
            }
        }
    }
};

// Usage
// More powerful servers handle more requests
// Useful when servers have different hardware
```

#### D. IP Hash (Session Persistence)

```cpp
#include <functional>

class IPHashLoadBalancer {
private:
    std::vector<std::string> servers = {
        "192.168.1.10:8080",
        "192.168.1.11:8080",
        "192.168.1.12:8080"
    };
    
public:
    std::string getServerForIP(const std::string& clientIP) {
        std::hash<std::string> hasher;
        size_t hash = hasher(clientIP);
        return servers[hash % servers.size()];
    }
};

// Usage
// Same client IP always goes to same server
// Useful for session persistence without shared session store
```

### Nginx Configuration Example

```nginx
# /etc/nginx/nginx.conf
http {
    upstream backend {
        # Round robin (default)
        server 192.168.1.10:8080;
        server 192.168.1.11:8080;
        server 192.168.1.12:8080;
        
        # Or weighted
        # server 192.168.1.10:8080 weight=3;
        # server 192.168.1.11:8080 weight=2;
        # server 192.168.1.12:8080 weight=1;
        
        # Or least connections
        # least_conn;
        
        # Health checks (nginx plus)
        # max_fails=3 fail_timeout=30s;
    }
    
    server {
        listen 80;
        
        location / {
            proxy_pass http://backend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            
            # Timeout settings
            proxy_connect_timeout 60s;
            proxy_send_timeout 60s;
            proxy_read_timeout 60s;
        }
        
        # Health check endpoint
        location /health {
            return 200 "OK\n";
            add_header Content-Type text/plain;
        }
    }
}
```

---

## 3. Caching Strategies

### What is Caching?

Caching stores frequently accessed data in fast memory to reduce database load and improve response times.

### Why It Matters

| Storage Type | Latency | Cost | Capacity |
|-------------|---------|------|----------|
| CPU Cache | 0.5-1 ns | High | KB |
| RAM | 100 ns | Medium | GB |
| SSD | 100-500 μs | Low | TB |
| HDD | 5-10 ms | Very Low | TB |
| Network | 1-10 ms | Varies | Varies |

**Impact:**
- Database read: ~10-100ms
- Cache read: ~1ms (10-100x faster!)
- Can reduce database load by 80-90%

### Cache Patterns

#### A. Cache-Aside Pattern (Most Common)

```python
import redis
import json
from typing import Optional, Dict

class Cache:
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379, db=0)
        self.DEFAULT_TTL = 3600  # 1 hour
    
    def get(self, key: str) -> Optional[Dict]:
        """Get from cache, return None if not found"""
        data = self.redis.get(key)
        if data:
            return json.loads(data)
        return None
    
    def set(self, key: str, value: Dict, ttl: int = None):
        """Set in cache with optional TTL"""
        if ttl:
            self.redis.setex(key, ttl, json.dumps(value))
        else:
            self.redis.set(key, json.dumps(value))
    
    def delete(self, key: str):
        """Delete from cache"""
        self.redis.delete(key)

class UserService:
    def __init__(self):
        self.cache = Cache()
        self.db = Database()
    
    def get_user(self, user_id: int) -> Optional[Dict]:
        # Cache-aside pattern
        cache_key = f"user:{user_id}"
        
        # 1. Try cache first
        user = self.cache.get(cache_key)
        if user:
            print(f"Cache hit for user {user_id}")
            return user
        
        # 2. Cache miss - fetch from database
        print(f"Cache miss for user {user_id}, fetching from DB")
        user = self.db.query("SELECT * FROM users WHERE id = %s", user_id)
        
        # 3. Populate cache for next time
        if user:
            self.cache.set(cache_key, user, ttl=3600)
        
        return user
    
    def update_user(self, user_id: int, data: Dict):
        # Update database
        self.db.execute(
            "UPDATE users SET name = %s, email = %s WHERE id = %s",
            (data['name'], data['email'], user_id)
        )
        
        # Invalidate cache (so next read gets fresh data)
        self.cache.delete(f"user:{user_id}")
```

**Pros:** Simple, cache only stores requested data
**Cons:** Cache miss causes latency spike

#### B. Write-Through Cache

```python
class WriteThroughCache:
    def __init__(self):
        self.cache = Cache()
        self.db = Database()
    
    def save_user(self, user_id: int, data: Dict):
        # Write to BOTH cache AND database simultaneously
        cache_key = f"user:{user_id}"
        
        # 1. Write to cache first
        self.cache.set(cache_key, data)
        
        # 2. Write to database
        self.db.execute(
            "INSERT INTO users (id, name, email) VALUES (%s, %s, %s)",
            (user_id, data['name'], data['email'])
        )
        
        # Cache is always in sync with database
```

**Pros:** Data always consistent, no cache misses for writes
**Cons:** Write latency higher (must write to both)

#### C. Write-Behind Cache

```python
import queue
import threading

class WriteBehindCache:
    def __init__(self, flush_interval=5):
        self.cache = Cache()
        self.db = Database()
        self.write_queue = queue.Queue()
        self.flush_interval = flush_interval
        
        # Start background writer
        threading.Thread(target=self._background_writer, daemon=True).start()
    
    def _background_writer(self):
        """Background thread that writes to database periodically"""
        pending_writes = {}
        
        while True:
            try:
                # Wait for flush interval or queue full
                time.sleep(self.flush_interval)
                
                # Flush all pending writes
                while not self.write_queue.empty():
                    user_id, data = self.write_queue.get()
                    pending_writes[user_id] = data
                
                # Batch write to database
                if pending_writes:
                    self._batch_write(pending_writes)
                    pending_writes.clear()
                    
            except Exception as e:
                print(f"Write error: {e}")
    
    def save_user(self, user_id: int, data: Dict):
        # Write to cache immediately
        self.cache.set(f"user:{user_id}", data)
        
        # Queue write to database (async)
        self.write_queue.put((user_id, data))
```

**Pros:** Fast writes, batched database writes
**Cons:** Data loss if system crashes before flush

#### D. Read-Through Cache

```python
class ReadThroughCache:
    def __init__(self):
        self.cache = Cache()
        self.db = Database()
    
    def get_user(self, user_id: int) -> Optional[Dict]:
        cache_key = f"user:{user_id}"
        
        # Try cache
        user = self.cache.get(cache_key)
        if user:
            return user
        
        # Cache miss - fetch and populate
        user = self._fetch_from_source(user_id)
        if user:
            self.cache.set(cache_key, user)
        
        return user
    
    def _fetch_from_source(self, user_id: int) -> Optional[Dict]:
        # Fetch from database
        return self.db.query("SELECT * FROM users WHERE id = %s", user_id)
```

### Cache Eviction Policies

#### LRU (Least Recently Used)

```python
from collections import OrderedDict

class LRUCache:
    """Evict least recently used items when full"""
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key: str):
        if key not in self.cache:
            return None
        
        # Move to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key: str, value: any):
        if key in self.cache:
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        
        # Evict least recently used if over capacity
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove oldest

# Demo
lru = LRUCache(3)
lru.put("a", 1)
lru.put("b", 2)
lru.put("c", 3)
lru.get("a")  # Access 'a' to make it recently used
lru.put("d", 4)  # Evicts 'b' (least recently used)

print(lru.cache)  # OrderedDict([('a', 1), ('c', 3), ('d', 4)])
```

#### LFU (Least Frequently Used)

```python
from collections import defaultdict

class LFUCache:
    """Evict least frequently used items"""
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freq = defaultdict(int)
        self.min_freq = 0
    
    def get(self, key: str):
        if key not in self.cache:
            return None
        
        # Increment frequency
        self.freq[key] += 1
        return self.cache[key]
    
    def put(self, key: str, value: any):
        if self.capacity <= 0:
            return
        
        if key in self.cache:
            self.cache[key] = value
            self.freq[key] += 1
            return
        
        # Evict if at capacity
        if len(self.cache) >= self.capacity:
            # Find and remove LFU item
            for k in list(self.cache.keys()):
                if self.freq[k] == self.min_freq:
                    del self.cache[k]
                    del self.freq[k]
                    break
            self.min_freq = 1
        
        self.cache[key] = value
        self.freq[key] = 1
        self.min_freq = 1
```

### Real Redis Commands

```bash
# Basic operations
SET user:123 '{"name": "John"}' EX 3600  # Set with 1-hour TTL
GET user:123
DEL user:123
EXISTS user:123
EXPIRE user:123 3600  # Set expiration

# Hash (for storing objects)
HSET user:123 name "John" email "john@example.com"
HGET user:123 name
HGETALL user:123
HDEL user:123 email

# List (for queues)
LPUSH queue:emails '{"from": "user1"}'
RPOP queue:emails
LRANGE queue:emails 0 -1

# Set (for unique items)
SADD users:online "user1" "user2"
SMEMBERS users:online
SREM users:online "user1"

# Sorted Set (for leaderboards)
ZADD leaderboard 100 "player1"
ZADD leaderboard 150 "player2"
ZRANGE leaderboard 0 -1 WITHSCORES
ZINCRBY leaderboard 10 "player1"

# Pub/Sub
PUBLISH chat:general "Hello everyone!"
SUBSCRIBE chat:general

# Transactions
MULTI
SET user:1 "value1"
SET user:2 "value2"
EXEC
```

---

## 4. Database Design & Sharding

### Database Sharding

**Sharding** splits a large database into smaller pieces (shards) across multiple servers.

### Why Shard?

| Single Database | Sharded Database |
|-----------------|------------------|
| Limited by single machine | Scale horizontally |
| Single point of failure | Redundancy |
| Slow queries on large tables | Faster queries on smaller data |
| Backup/restore takes hours | Per-shard backup/restore |

### Architecture

```
                    ┌─────────────────────────────────────┐
                    │         Application                 │
                    └─────────────────┬───────────────────┘
                                      │
                                      ▼
                    ┌─────────────────────────────────────┐
                    │         Shard Router                │
                    │    (shard_key -> shard mapping)     │
                    └─────────────────┬───────────────────┘
                                      │
          ┌───────────────────────────┼───────────────────────────┐
          │                           │                           │
          ▼                           ▼                           ▼
    ┌───────────┐              ┌───────────┐              ┌───────────┐
    │ Shard 1   │              │ Shard 2   │              │ Shard 3   │
    │ Users 1M  │              │ Users 2M  │              │ Users 3M  │
    │ (MySQL)   │              │ (MySQL)   │              │ (MySQL)   │
    └───────────┘              └───────────┘              └───────────┘
```

### Sharding Strategies

#### A. Range-Based Sharding

```python
class RangeShardRouter:
    """Shard based on user ID ranges"""
    
    def __init__(self):
        self.shards = {
            'shard1': {
                'min': 0, 
                'max': 999999, 
                'db': Database('mysql://shard1')
            },
            'shard2': {
                'min': 1000000, 
                'max': 1999999, 
                'db': Database('mysql://shard2')
            },
            'shard3': {
                'min': 2000000, 
                'max': 2999999, 
                'db': Database('mysql://shard3')
            },
        }
    
    def get_shard(self, user_id: int):
        """Find which shard contains this user ID"""
        for shard_name, config in self.shards.items():
            if config['min'] <= user_id <= config['max']:
                return shard_name, config['db']
        return None, None
    
    def get_user(self, user_id: int):
        shard_name, db = self.get_shard(user_id)
        if db:
            return db.query("SELECT * FROM users WHERE id = %s", user_id)
        return None
    
    def insert_user(self, user_id: int, data: dict):
        shard_name, db = self.get_shard(user_id)
        if db:
            db.execute(
                "INSERT INTO users (id, name, email) VALUES (%s, %s, %s)",
                (user_id, data['name'], data['email'])
            )
        else:
            raise Exception("No shard found for user_id")

# Usage
router = RangeShardRouter()
router.insert_user(500000, {'name': 'Alice', 'email': 'alice@example.com'})   # shard1
router.insert_user(1500000, {'name': 'Bob', 'email': 'bob@example.com'})     # shard2
user = router.get_user(500000)  # Queries shard1
```

**Pros:** Simple, efficient range queries
**Cons:** Hot spots (recent IDs get most traffic), rebalancing difficult

#### B. Hash-Based Sharding

```python
import hashlib

class HashShardRouter:
    """Shard based on hash of user ID"""
    
    def __init__(self, num_shards=3):
        self.num_shards = num_shards
        self.shards = [Database(f'mysql://shard{i}') for i in range(num_shards)]
    
    def get_shard_index(self, user_id: int) -> int:
        """Hash user_id and map to shard"""
        hash_value = int(hashlib.md5(str(user_id).encode()).hexdigest(), 16)
        return hash_value % self.num_shards
    
    def get_user(self, user_id: int):
        shard_index = self.get_shard_index(user_id)
        db = self.shards[shard_index]
        return db.query("SELECT * FROM users WHERE id = %s", user_id)
    
    def insert_user(self, user_id: int, data: dict):
        shard_index = self.get_shard_index(user_id)
        db = self.shards[shard_index]
        db.execute(
            "INSERT INTO users (id, name, email) VALUES (%s, %s, %s)",
            (user_id, data['name'], data['email'])
        )

# Usage
router = HashShardRouter(num_shards=3)
router.insert_user(123, {'name': 'Alice', 'email': 'alice@example.com'})
# User 123 always goes to same shard (deterministic)
```

**Pros:** Even data distribution, no hot spots
**Cons:** Range queries require querying all shards

#### C. Consistent Hashing (Advanced)

```python
import hashlib

class ConsistentHashRouter:
    """Handles shard additions/removals with minimal data movement"""
    
    def __init__(self, num_virtual_nodes=100):
        self.ring = {}  # hash -> shard
        self.sorted_keys = []
        self.num_virtual_nodes = num_virtual_nodes
        self.shards = {}  # shard_name -> database
    
    def add_shard(self, shard_name: str, db):
        """Add a new shard to the ring"""
        self.shards[shard_name] = db
        
        # Add virtual nodes for this shard
        for i in range(self.num_virtual_nodes):
            key = f"{shard_name}:{i}"
            hash_value = int(hashlib.md5(key.encode()).hexdigest(), 16)
            self.ring[hash_value] = shard_name
        
        self.sorted_keys = sorted(self.ring.keys())
    
    def get_shard(self, key: str):
        """Get shard for a given key"""
        hash_value = int(hashlib.md5(key.encode()).hexdigest(), 16)
        
        # Find first hash >= key's hash (or wrap around)
        for ring_key in self.sorted_keys:
            if ring_key >= hash_value:
                return self.ring[ring_key]
        
        # Wrap around to first shard
        return self.ring[self.sorted_keys[0]]
    
    def get_database(self, key: str):
        shard_name = self.get_shard(key)
        return self.shards[shard_name]

# Usage
router = ConsistentHashRouter()
router.add_shard('shard1', Database('shard1'))
router.add_shard('shard2', Database('shard2'))

# When adding shard3, only ~1/3 of data moves (vs all data with hash mod)
router.add_shard('shard3', Database('shard3'))
```

**Pros:** Adding/removing shards moves minimal data
**Cons:** More complex, slight imbalance

### Database Indexing

```sql
-- Create indexes for common queries
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_name ON users(name);
CREATE INDEX idx_users_created ON users(created_at);

-- Composite index (for multi-column queries)
CREATE INDEX idx_users_name_email ON users(name, email);

-- Partial index (for filtered queries)
CREATE INDEX idx_users_active ON users(email) WHERE active = true;

-- Explain query plan
EXPLAIN SELECT * FROM users WHERE email = 'test@example.com';
```

---

## 5. Message Queues

### What is a Message Queue?

Message queues enable asynchronous communication between services. Producers send messages, consumers process them later.

### Why Use Message Queues?

| Without Queue | With Queue |
|--------------|------------|
| User waits for email to send | User gets instant response |
| Service must be available | Messages queue until available |
| Synchronous coupling | Asynchronous decoupling |
| Traffic spikes cause failures | Queue absorbs spikes |

### Architecture

```
                    ┌─────────────────────────────────────┐
                    │           Producer                  │
                    │      (Web Server, User Action)      │
                    └─────────────────┬───────────────────┘
                                      │
                                      │ Send message
                                      ▼
                    ┌─────────────────────────────────────┐
                    │         Message Queue               │
                    │      (RabbitMQ, Kafka, SQS)         │
                    │                                     │
                    │  ┌─────────────────────────────┐   │
                    │  │         Queue               │   │
                    │  │  [msg1][msg2][msg3][msg4]   │   │
                    │  └─────────────────────────────┘   │
                    └─────────────────┬───────────────────┘
                                      │
                                      │ Consume message
                                      ▼
                    ┌─────────────────────────────────────┐
                    │           Consumer                  │
                    │    (Background Worker, Service)     │
                    └─────────────────────────────────────┘
```

### Use Cases

| Use Case | Queue Type | Example |
|----------|-----------|---------|
| Email sending | Task Queue | Send welcome email |
| Image processing | Task Queue | Resize uploaded image |
| Event logging | Event Stream | Track user actions |
| Real-time analytics | Event Stream | Update dashboard |
| Order processing | Task Queue | Process payment |

### Simple Queue Implementation

```python
import queue
import threading
import time
import json

class MessageQueue:
    """Simple in-memory message queue"""
    
    def __init__(self):
        self.q = queue.Queue()
    
    def send(self, message: dict):
        """Producer: send message to queue"""
        self.q.put(message)
        print(f"[Producer] Sent: {message}")
    
    def receive(self):
        """Consumer: receive message from queue"""
        return self.q.get()
    
    def task_done(self):
        self.q.task_done()

class EmailWorker:
    """Consumer: processes email messages"""
    
    def __init__(self, queue: MessageQueue, worker_id: int):
        self.queue = queue
        self.worker_id = worker_id
    
    def process_email(self, email_data: dict):
        """Simulate sending email"""
        print(f"[Worker-{self.worker_id}] Processing email to {email_data['to']}")
        time.sleep(2)  # Simulate slow email sending
        print(f"[Worker-{self.worker_id}] Email sent to {email_data['to']}")
    
    def run(self):
        """Worker loop"""
        while True:
            message = self.queue.receive()
            self.process_email(message)
            self.queue.task_done()

# Demo
mq = MessageQueue()

# Start worker threads
for i in range(3):
    worker = EmailWorker(mq, i + 1)
    threading.Thread(target=worker.run, daemon=True).start()

# Producer sends emails
for i in range(10):
    mq.send({
        'to': f'user{i}@example.com',
        'subject': f'Welcome {i}',
        'body': 'Hello there!'
    })
    time.sleep(0.5)

# Wait for all messages to be processed
mq.q.join()
```

### RabbitMQ with Python

```python
import pika
import json

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare queue (persists if RabbitMQ restarts)
channel.queue_declare(queue='email_queue', durable=True)

# Producer: Send message
def send_email(to: str, subject: str, body: str):
    message = {
        'to': to,
        'subject': subject,
        'body': body
    }
    
    channel.basic_publish(
        exchange='',
        routing_key='email_queue',
        body=json.dumps(message),
        properties=pika.BasicProperties(
            delivery_mode=2,  # Make message persistent
        )
    )
    print(f"Sent email to {to}")

# Consumer: Receive and process messages
def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"Processing email to {data['to']}")
    
    # Send actual email here
    # send_actual_email(data['to'], data['subject'], data['body'])
    
    print("Email sent")
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Start consuming
channel.basic_consume(queue='email_queue', on_message_callback=callback)
print("Worker started, waiting for messages...")
channel.start_consuming()
```

### Kafka Implementation

```python
from kafka import KafkaProducer, KafkaConsumer
import json

# Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Send message to topic
producer.send('user-events', {
    'user_id': 123,
    'event': 'purchase',
    'amount': 99.99,
    'timestamp': datetime.now().isoformat()
})
producer.flush()

# Consumer
consumer = KafkaConsumer(
    'user-events',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest'
)

for message in consumer:
    event = message.value
    print(f"Received event: {event}")
    # Process event (update analytics, send notification, etc.)
```

---

## 6. CDN & Edge Computing

### What is a CDN?

**Content Delivery Network (CDN)** caches static content at edge locations worldwide for faster delivery.

### Architecture

```
                    ┌─────────────────────────────────────┐
                    │           User in Europe            │
                    └─────────────────┬───────────────────┘
                                      │
                    ┌─────────────────┼───────────────────┐
                    ▼                 │                   ▼
            ┌───────────┐             │           ┌───────────┐
            │ CDN Edge  │             │           │  Origin   │
            │ (London)  │◄────────────┤           │  Server   │
            └───────────┘             │           └───────────┘
                                      │
                    ┌─────────────────┼───────────────────┐
                    ▼                 │                   ▼
            ┌───────────┐             │           ┌───────────┐
            │ CDN Edge  │             │           │  Database │
            │ (Paris)   │             │           │           │
            └───────────┘             │           └───────────┘
```

### CDN Benefits

| Metric | Without CDN | With CDN |
|--------|-------------|----------|
| Latency (US to Asia) | 200-300ms | 50-100ms |
| Origin server load | 100% | 10-20% |
| Bandwidth cost | High | Lower |
| DDoS protection | Manual | Built-in |

### CDN Implementation

```python
import requests
import hashlib
import time

class CDNManager:
    def __init__(self, cdn_url, api_key):
        self.cdn_url = cdn_url
        self.api_key = api_key
    
    def upload(self, file_path, content_type='application/octet-stream'):
        """Upload file to CDN"""
        with open(file_path, 'rb') as f:
            content = f.read()
        
        # Generate unique filename with hash
        file_hash = hashlib.md5(content).hexdigest()
        filename = f"{file_hash}.jpg"
        
        # Upload to CDN
        response = requests.put(
            f"{self.cdn_url}/{filename}",
            data=content,
            headers={
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': content_type,
                'Cache-Control': 'public, max-age=31536000'  # 1 year
            }
        )
        
        return f"{self.cdn_url}/{filename}"
    
    def purge(self, url):
        """Clear CDN cache for specific URL"""
        requests.post(
            f"{self.cdn_url}/purge",
            json={'urls': [url]},
            headers={'Authorization': f'Bearer {self.api_key}'}
        )

# Usage
cdn = CDNManager('https://cdn.example.com', 'api_key_here')
url = cdn.upload('image.jpg', 'image/jpeg')
print(f"CDN URL: {url}")
```

### Cloudflare Configuration

```nginx
# Nginx with Cloudflare
server {
    listen 80;
    server_name example.com;
    
    # Cache static assets
    location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
        add_header X-Cache-Status $upstream_cache_status;
    }
    
    # Don't cache HTML
    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## 7. Replication & Failover

### Database Replication

**Replication** copies data from primary database to replicas for read scaling and backup.

### Architecture

```
                    ┌─────────────────────────────────────┐
                    │         Application                 │
                    └─────────────────┬───────────────────┘
                                      │
                    ┌─────────────────┼───────────────────┐
                    ▼                 │                   ▼
            ┌───────────┐             │           ┌───────────┐
            │  Master   │◄────────────┤           │  Replica  │
            │ (Writes)  │   Sync      │           │  (Reads)  │
            └───────────┘             │           └───────────┘
                                      │
                    ┌─────────────────┼───────────────────┐
                    ▼                 │                   ▼
            ┌───────────┐             │           ┌───────────┐
            │  Replica  │             │           │  Replica  │
            │  (Reads)  │             │           │  (Reads)  │
            └───────────┘             │           └───────────┘
```

### Replication Modes

#### Synchronous Replication

```sql
-- MySQL synchronous replication
SET GLOBAL binlog_format = 'ROW';
SET GLOBAL sync_binlog = 1;
SET GLOBAL innodb_flush_log_at_trx_commit = 1;

-- Wait for replica to acknowledge before committing
```

**Pros:** No data loss
**Cons:** Higher latency (must wait for replica)

#### Asynchronous Replication

```sql
-- MySQL asynchronous (default)
SHOW SLAVE STATUS;  -- Check replication status
```

**Pros:** Lower latency
**Cons:** Possible data loss if master fails

### Failover Implementation

```python
import redis
import time

class DatabaseFailover:
    def __init__(self):
        self.master = redis.Redis(host='master', port=6379)
        self.replicas = [
            redis.Redis(host='replica1', port=6379),
            redis.Redis(host='replica2', port=6379),
        ]
        self.current_replica = 0
        self.last_check = time.time()
        self.check_interval = 5  # seconds
    
    def _is_master_healthy(self):
        try:
            self.master.ping()
            return True
        except:
            return False
    
    def _get_connection(self, write=False):
        # Check master health periodically
        if time.time() - self.last_check > self.check_interval:
            if not self._is_master_healthy():
                print("Master failed! Promoting replica")
                # In production: trigger failover, update DNS, etc.
                self.master = self.replicas[0]  # Simplified
            self.last_check = time.time()
        
        if write:
            return self.master
        else:
            # Round-robin among replicas
            replica = self.replicas[self.current_replica]
            self.current_replica = (self.current_replica + 1) % len(self.replicas)
            return replica
    
    def get(self, key):
        return self._get_connection(write=False).get(key)
    
    def set(self, key, value):
        return self._get_connection(write=True).set(key, value)
```

---

## 8. API Design

### REST API Principles

```python
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Good REST API Design

# 1. Use nouns for resources
@app.route('/api/users', methods=['GET'])
def get_users():
    """GET /api/users - List all users"""
    users = db.query("SELECT * FROM users")
    return jsonify(users)

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """GET /api/users/123 - Get specific user"""
    user = db.query("SELECT * FROM users WHERE id = %s", user_id)
    return jsonify(user)

# 2. Use proper HTTP methods
@app.route('/api/users', methods=['POST'])
def create_user():
    """POST /api/users - Create new user"""
    data = request.json
    user_id = db.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s)",
        (data['name'], data['email'])
    )
    return jsonify({'id': user_id}), 201  # 201 Created

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """PUT /api/users/123 - Full update"""
    data = request.json
    db.execute(
        "UPDATE users SET name = %s, email = %s WHERE id = %s",
        (data['name'], data['email'], user_id)
    )
    return jsonify({'status': 'updated'})

@app.route('/api/users/<int:user_id>', methods=['PATCH'])
def partial_update_user(user_id):
    """PATCH /api/users/123 - Partial update"""
    data = request.json
    if 'name' in data:
        db.execute("UPDATE users SET name = %s WHERE id = %s", 
                  (data['name'], user_id))
    return jsonify({'status': 'updated'})

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """DELETE /api/users/123 - Delete user"""
    db.execute("DELETE FROM users WHERE id = %s", user_id)
    return '', 204  # 204 No Content

# 3. Use proper status codes
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user_with_status(user_id):
    user = db.query("SELECT * FROM users WHERE id = %s", user_id)
    if not user:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(user), 200

# 4. Version your API
@app.route('/api/v1/users', methods=['GET'])
def get_users_v1():
    return jsonify(users)

@app.route('/api/v2/users', methods=['GET'])
def get_users_v2():
    # New format
    return jsonify({'data': users, 'meta': {...}})

# 5. Pagination
@app.route('/api/users', methods=['GET'])
def get_users_paginated():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    
    offset = (page - 1) * per_page
    users = db.query(
        "SELECT * FROM users LIMIT %s OFFSET %s", 
        per_page, offset
    )
    
    return jsonify({
        'data': users,
        'pagination': {
            'page': page,
            'per_page': per_page,
            'total': db.query("SELECT COUNT(*) FROM users")[0][0]
        }
    })

# 6. Filtering & Sorting
@app.route('/api/users', methods=['GET'])
def get_users_filtered():
    status = request.args.get('status')
    sort_by = request.args.get('sort', 'created_at')
    order = request.args.get('order', 'desc')
    
    query = "SELECT * FROM users WHERE 1=1"
    params = []
    
    if status:
        query += " AND status = %s"
        params.append(status)
    
    query += f" ORDER BY {sort_by} {order}"
    
    users = db.query(query, *params)
    return jsonify(users)

# 7. Error handling with consistent format
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': {
            'code': 'NOT_FOUND',
            'message': 'Resource not found',
            'status': 404
        }
    }), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        'error': {
            'code': 'BAD_REQUEST',
            'message': str(error),
            'status': 400
        }
    }), 400

if __name__ == '__main__':
    app.run()
```

### API Response Format

```json
// Success Response (200 OK)
{
  "data": {
    "id": 123,
    "name": "John Doe",
    "email": "john@example.com"
  },
  "meta": {
    "timestamp": "2024-01-15T10:30:00Z",
    "request_id": "abc123"
  }
}

// Error Response (400 Bad Request)
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid email format",
    "details": [
      {
        "field": "email",
        "message": "Must be a valid email address"
      }
    ],
    "status": 400
  }
}

// Pagination Response (200 OK)
{
  "data": [...],
  "meta": {
    "page": 1,
    "per_page": 20,
    "total_pages": 5,
    "total_items": 100
  },
  "links": {
    "self": "/api/users?page=1&per_page=20",
    "first": "/api/users?page=1&per_page=20",
    "prev": null,
    "next": "/api/users?page=2&per_page=20",
    "last": "/api/users?page=5&per_page=20"
  }
}
```

---

## 9. Microservices Architecture

### What are Microservices?

Microservices architecture breaks applications into small, independent services that communicate over APIs.

### Monolith vs Microservices

| Aspect | Monolith | Microservices |
|--------|----------|---------------|
| Deployment | Single unit | Independent deployments |
| Scaling | Scale entire app | Scale individual services |
| Technology | Single tech stack | Different technologies per service |
| Fault isolation | Single point of failure | Failures contained |
| Complexity | Simple initially | Complex distributed system |

### Architecture Diagram

```
                    ┌─────────────────────────────────────┐
                    │          API Gateway                │
                    │    (Routing, Auth, Rate Limiting)   │
                    └─────────────────┬───────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────┐
        │                             │                             │
        ▼                             ▼                             ▼
┌───────────────┐             ┌───────────────┐             ┌───────────────┐
│ User Service  │             │Order Service  │             │Product Service│
│  (Node.js)    │             │   (Python)    │             │    (Go)       │
└───────┬───────┘             └───────┬───────┘             └───────┬───────┘
        │                             │                             │
        ▼                             ▼                             ▼
┌───────────────┐             ┌───────────────┐             ┌───────────────┐
│   User DB     │             │    Order DB   │             │   Product DB  │
│   (MongoDB)   │             │   (PostgreSQL)│             │    (MySQL)    │
└───────────────┘             └───────────────┘             └───────────────┘
```

### Service Communication

#### Synchronous (REST)

```python
# User Service
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    user = db.query("SELECT * FROM users WHERE id = %s", user_id)
    return jsonify(user)

# Order Service calling User Service
import requests

class OrderService:
    def get_user_details(self, user_id):
        response = requests.get(f'http://user-service:8080/api/users/{user_id}')
        return response.json()
    
    def create_order(self, user_id, items):
        # Get user details
        user = self.get_user_details(user_id)
        
        # Create order
        order = {
            'user_id': user_id,
            'user_email': user['email'],
            'items': items
        }
        # Save order...
```

#### Asynchronous (Message Queue)

```python
# Order Service - Publish event
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def create_order(user_id, items):
    order = {'user_id': user_id, 'items': items}
    
    # Save order to database
    db.execute("INSERT INTO orders ...")
    
    # Publish event
    producer.send('order-created', {
        'order_id': order_id,
        'user_id': user_id,
        'items': items,
        'timestamp': datetime.now().isoformat()
    })

# Email Service - Subscribe to event
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'order-created',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    event = message.value
    send_order_confirmation_email(event['user_id'], event['order_id'])
```

### Docker Compose for Microservices

```yaml
# docker-compose.yml
version: '3.8'

services:
  api-gateway:
    build: ./api-gateway
    ports:
      - "80:80"
    depends_on:
      - user-service
      - order-service
      - product-service

  user-service:
    build: ./user-service
    environment:
      - DATABASE_URL=mongodb://user-db:27017/users
    depends_on:
      - user-db

  order-service:
    build: ./order-service
    environment:
      - DATABASE_URL=postgresql://order-db:5432/orders
      - KAFKA_BROKER=kafka:9092
    depends_on:
      - order-db
      - kafka

  product-service:
    build: ./product-service
    environment:
      - DATABASE_URL=mysql://product-db:3306/products
    depends_on:
      - product-db

  user-db:
    image: mongo:5
    volumes:
      - user-data:/data/db

  order-db:
    image: postgres:14
    volumes:
      - order-data:/var/lib/postgresql/data

  product-db:
    image: mysql:8
    volumes:
      - product-data:/var/lib/mysql

  kafka:
    image: confluentinc/cp-kafka:latest
    environment:
      - KAFKA_BROKER_ID=1
      - KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181

  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    environment:
      - ZOOKEEPER_CLIENT_PORT=2181

volumes:
  user-data:
  order-data:
  product-data:
```

---

## 10. Distributed Systems Concepts

### CAP Theorem

**CAP Theorem** states that a distributed system can only guarantee 2 of 3 properties:

| Property | Description | Example |
|----------|-------------|---------|
| **Consistency** | All nodes see same data at same time | Bank transactions |
| **Availability** | Every request gets a response | Social media feed |
| **Partition Tolerance** | System works despite network failures | Distributed database |

### Trade-offs

```
                    ┌─────────────────────────────────────┐
                    │            CAP Theorem              │
                    └─────────────────┬───────────────────┘
                                      │
          ┌───────────────────────────┼───────────────────────────┐
          │                           │                           │
          ▼                           ▼                           ▼
    ┌───────────┐              ┌───────────┐              ┌───────────┐
    │   CP      │              │   AP      │              │   CA      │
    │ (Consistent,              │ (Available,              │ (Consistent,
    │  Partition-               │  Partition-              │  Available)
    │  Tolerant)                │  Tolerant)               │  (Single DB)
    └───────────┘              └───────────┘              └───────────┘
          │                           │                           │
    • MongoDB                   • Cassandra                • Traditional RDBMS
    • Redis                     • DynamoDB                 • PostgreSQL (single node)
    • HBase                     • CouchDB                  |
    • When: Data integrity      • When: Availability       |
      critical                  critical                   |
```

### Consistency Models

#### Strong Consistency

```python
# All reads see the latest write
def transfer_money(from_account, to_account, amount):
    # Start transaction
    db.begin_transaction()
    
    # Deduct from source
    from_balance = db.get(from_account)
    db.set(from_account, from_balance - amount)
    
    # Add to destination
    to_balance = db.get(to_account)
    db.set(to_account, to_balance + amount)
    
    # Commit (all or nothing)
    db.commit()
    
    # Any read after commit sees updated values
```

#### Eventual Consistency

```python
# Reads may see stale data temporarily
def update_profile(user_id, data):
    # Update primary
    db.primary.set(f"user:{user_id}", data)
    
    # Replicate to replicas asynchronously
    replicate_async(f"user:{user_id}", data)
    
    # Read from replica might return old data temporarily
    # But eventually all replicas converge
```

---

## 11. CAP Theorem & Consistency Models

### Consistency Levels

```python
# Cassandra consistency levels

# QUORUM - Read/Write to majority
# Good balance of consistency and availability
cassandra.execute(
    "SELECT * FROM users WHERE id = ?",
    consistency_level='QUORUM'
)

# ONE - Fastest, least consistent
cassandra.execute(
    "SELECT * FROM users WHERE id = ?",
    consistency_level='ONE'
)

# ALL - Most consistent, slowest
cassandra.execute(
    "SELECT * FROM users WHERE id = ?",
    consistency_level='ALL'
)

# LOCAL_QUORUM - Quorum in local datacenter only
cassandra.execute(
    "SELECT * FROM users WHERE id = ?",
    consistency_level='LOCAL_QUORUM'
)
```

---

## 12. Complete System Design Examples

### Example 1: URL Shortener (like bit.ly)

#### Requirements

| Type | Requirement |
|------|-------------|
| Functional | Shorten long URLs, Redirect short URLs |
| Non-functional | 100M URLs/month, 10:1 read/write ratio |
| Availability | 99.9% uptime |
| Latency | <100ms for redirects |

#### Architecture

```
                    ┌─────────────────────────────────────┐
                    │           Client                    │
                    └─────────────────┬───────────────────┘
                                      │
                    ┌─────────────────┼───────────────────┐
                    ▼                 │                   ▼
            ┌───────────┐             │           ┌───────────┐
            │   CDN     │             │           │  Load     │
            │ (Redirect)│             │           │ Balancer  │
            └───────────┘             │           └─────┬─────┘
                                      │                 │
                                      ▼                 ▼
                            ┌─────────────────────────────────────┐
                            │         API Server                  │
                            └─────────────────┬───────────────────┘
                                              │
                    ┌─────────────────────────┼─────────────────────────┐
                    ▼                         ▼                         ▼
            ┌───────────┐              ┌───────────┐              ┌───────────┐
            │   Redis   │              │  MySQL    │              │   Kafka   │
            │  (Cache)  │              │ (Sharded) │              │  (Logs)   │
            └───────────┘              └───────────┘              └───────────┘
```

#### Implementation

```python
import hashlib
import base62
import redis
import mysql.connector
from datetime import datetime

class URLShortener:
    def __init__(self):
        self.cache = redis.Redis(host='localhost', port=6379)
        self.db = mysql.connector.connect(host='localhost', database='url_shortener')
    
    def generate_short_code(self, url: str) -> str:
        """Generate unique short code"""
        # Hash URL to get unique identifier
        hash_obj = hashlib.md5(url.encode())
        hash_int = int(hash_obj.hexdigest(), 16)
        return base62.encode(hash_int)  # e.g., "abc123"
    
    def shorten(self, url: str) -> str:
        """Create short URL"""
        short_code = self.generate_short_code(url)
        cache_key = f"url:{short_code}"
        
        # Check cache first
        if self.cache.exists(cache_key):
            return f"https://short.ly/{short_code}"
        
        # Store in database
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO urls (short_code, original_url, created_at) VALUES (%s, %s, NOW())",
            (short_code, url)
        )
        self.db.commit()
        
        # Cache for fast access (24 hour TTL)
        self.cache.setex(cache_key, 86400, url)
        
        return f"https://short.ly/{short_code}"
    
    def expand(self, short_code: str) -> str:
        """Get original URL from short code"""
        cache_key = f"url:{short_code}"
        
        # Check cache first
        cached_url = self.cache.get(cache_key)
        if cached_url:
            return cached_url.decode()
        
        # Cache miss - fetch from database
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT original_url FROM urls WHERE short_code = %s",
            (short_code,)
        )
        result = cursor.fetchone()
        
        if result:
            url = result[0]
            # Update cache
            self.cache.setex(cache_key, 86400, url)
            return url
        
        raise ValueError("URL not found")

# Usage
shortener = URLShortener()
short_url = shortener.shorten("https://www.example.com/very/long/url/path")
print(f"Short URL: {short_url}")

# Redirect handler
@app.route('/<short_code>')
def redirect(short_code):
    try:
        original_url = shortener.expand(short_code)
        return redirect(original_url)
    except ValueError:
        return "Not found", 404
```

### Example 2: Chat System (like WhatsApp)

#### Architecture

```
                    ┌─────────────────────────────────────┐
                    │           Client App                │
                    └─────────────────┬───────────────────┘
                                      │
                                      │ WebSocket
                                      ▼
                    ┌─────────────────────────────────────┐
                    │         WebSocket Server            │
                    │    (Handles real-time connections)  │
                    └─────────────────┬───────────────────┘
                                      │
          ┌───────────────────────────┼───────────────────────────┐
          │                           │                           │
          ▼                           ▼                           ▼
    ┌───────────┐              ┌───────────┐              ┌───────────┐
    │   Redis   │              │  MongoDB  │              │   Kafka   │
    │ (Presence │              │ (Messages │              │  (Events) │
    │  & PubSub)│              │  Storage) │              │           │
    └───────────┘              └───────────┘              └───────────┘
```

#### Implementation

```python
import asyncio
import json
import redis
from datetime import datetime

# WebSocket Server
class ChatServer:
    def __init__(self):
        self.clients = {}  # user_id -> websocket
        self.redis = redis.Redis(host='localhost', port=6379)
    
    async def connect(self, websocket, user_id):
        """Handle new connection"""
        self.clients[user_id] = websocket
        
        # Update presence
        self.redis.set(f"presence:{user_id}", "online", ex=300)
        
        # Notify contacts
        await self.notify_contacts(user_id, 'online')
    
    async def disconnect(self, user_id):
        """Handle disconnection"""
        if user_id in self.clients:
            del self.clients[user_id]
        
        # Update presence
        self.redis.set(f"presence:{user_id}", "offline", ex=300)
        
        # Notify contacts
        await self.notify_contacts(user_id, 'offline')
    
    async def send_message(self, from_user, to_user, message):
        """Send message between users"""
        timestamp = datetime.now().isoformat()
        
        msg_data = {
            'from': from_user,
            'to': to_user,
            'message': message,
            'timestamp': timestamp,
            'status': 'sent'
        }
        
        # Store in database
        await self.store_message(msg_data)
        
        # Try to deliver via WebSocket
        if to_user in self.clients:
            await self.clients[to_user].send_json(msg_data)
            msg_data['status'] = 'delivered'
        else:
            # Queue for later delivery
            self.redis.rpush(f"queue:{to_user}", json.dumps(msg_data))
        
        # Update message status
        await self.update_message_status(from_user, to_user, 'delivered')
    
    async def notify_contacts(self, user_id, status):
        """Notify user's contacts of presence change"""
        contacts = self.redis.smembers(f"contacts:{user_id}")
        for contact in contacts:
            if contact in self.clients:
                await self.clients[contact].send_json({
                    'type': 'presence',
                    'user_id': user_id,
                    'status': status
                })

# Client
class ChatClient:
    def __init__(self, user_id):
        self.user_id = user_id
        self.websocket = None
    
    async def connect(self, url):
        self.websocket = await websocket.connect(url)
        await self.websocket.send_json({'type': 'auth', 'user_id': self.user_id})
    
    async def send_message(self, to_user, message):
        await self.websocket.send_json({
            'type': 'message',
            'to': to_user,
            'message': message
        })
    
    async def receive(self):
        while True:
            message = await self.websocket.receive_json()
            if message['type'] == 'message':
                print(f"Message from {message['from']}: {message['message']}")
            elif message['type'] == 'presence':
                print(f"{message['user_id']} is {message['status']}")
```

---

# PART 2: PROGRAMMING TOPICS TO MASTER

---

## Table of Contents
1. [Programming Fundamentals](#programming-fundamentals)
2. [Object-Oriented Programming](#object-oriented-programming)
3. [Functional Programming](#functional-programming)
4. [Data Structures](#data-structures)
5. [Algorithms](#algorithms)
6. [Database Systems](#database-systems)
7. [Networking](#networking)
8. [Operating Systems](#operating-systems)
9. [Security](#security)
10. [Software Engineering](#software-engineering)
11. [DevOps & Tools](#devops--tools)
12. [Advanced Topics](#advanced-topics)

---

## Programming Fundamentals

### Variables & Data Types

```cpp
// Basic types
int age = 25;
double price = 19.99;
char grade = 'A';
bool isActive = true;

// Strings
std::string name = "John";

// Arrays
int numbers[5] = {1, 2, 3, 4, 5};

// Vectors (dynamic arrays)
std::vector<int> vec = {1, 2, 3};
vec.push_back(4);

// Pointers
int* ptr = &age;
std::cout << *ptr << std::endl;  // Dereference

// References
int& ref = age;
ref = 30;  // Modifies age
```

### Control Structures

```cpp
// If-else
if (age >= 18) {
    std::cout << "Adult";
} else if (age >= 13) {
    std::cout << "Teen";
} else {
    std::cout << "Child";
}

// Switch
switch (day) {
    case 1: std::cout << "Monday"; break;
    case 2: std::cout << "Tuesday"; break;
    default: std::cout << "Other";
}

// For loop
for (int i = 0; i < 5; i++) {
    std::cout << i << std::endl;
}

// While loop
while (count < 10) {
    count++;
}

// Do-while
do {
    std::cout << "At least once";
} while (false);

// Range-based for
for (int num : numbers) {
    std::cout << num << std::endl;
}
```

### Functions

```cpp
// Basic function
int add(int a, int b) {
    return a + b;
}

// Default parameters
int power(int base, int exp = 2) {
    return pow(base, exp);
}

// Function overloading
int multiply(int a, int b) {
    return a * b;
}

double multiply(double a, double b) {
    return a * b;
}

// Lambda functions
auto square = [](int x) { return x * x; };
std::cout << square(5) << std::endl;

// Lambda with capture
int multiplier = 2;
auto multiply = [multiplier](int x) { return x * multiplier; };
```

---

## Object-Oriented Programming

### Classes & Objects

```cpp
class Person {
private:
    std::string name;
    int age;
    
protected:
    std::string email;
    
public:
    // Constructor
    Person(std::string n, int a) : name(n), age(a) {}
    
    // Destructor
    ~Person() {}
    
    // Member functions
    void greet() {
        std::cout << "Hello, I'm " << name << std::endl;
    }
    
    // Getter
    std::string getName() const {
        return name;
    }
    
    // Setter
    void setName(std::string n) {
        name = n;
    }
    
    // Static member
    static int personCount;
};

int Person::personCount = 0;

// Usage
Person p("Alice", 25);
p.greet();
```

### Inheritance

```cpp
class Animal {
protected:
    std::string name;
    
public:
    Animal(std::string n) : name(n) {}
    
    virtual void speak() {
        std::cout << "Some sound" << std::endl;
    }
    
    virtual ~Animal() {}
};

class Dog : public Animal {
public:
    Dog(std::string n) : Animal(n) {}
    
    void speak() override {
        std::cout << "Woof!" << std::endl;
    }
    
    void fetch() {
        std::cout << name << " is fetching" << std::endl;
    }
};

class Cat : public Animal {
public:
    Cat(std::string n) : Animal(n) {}
    
    void speak() override {
        std::cout << "Meow!" << std::endl;
    }
};

// Usage
Dog dog("Buddy");
dog.speak();  // Woof!
dog.fetch();  // Buddy is fetching
```

### Polymorphism

```cpp
void makeAnimalSpeak(Animal& animal) {
    animal.speak();  // Calls derived class version
}

Animal* animals[] = {new Dog("Rex"), new Cat("Whiskers")};

for (Animal* animal : animals) {
    makeAnimalSpeak(*animal);  // Polymorphic call
}

// Output:
// Woof!
// Meow!
```

### Encapsulation

```cpp
class BankAccount {
private:
    double balance;
    
public:
    BankAccount(double initial) : balance(initial) {}
    
    // Controlled access
    bool deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            return true;
        }
        return false;
    }
    
    bool withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            return true;
        }
        return false;
    }
    
    // Read-only access
    double getBalance() const {
        return balance;
    }
};
```

---

## Functional Programming

### Pure Functions

```cpp
// Pure function (no side effects, same input = same output)
int add(int a, int b) {
    return a + b;
}

// Impure function (has side effects)
int counter = 0;
int increment() {
    counter++;  // Side effect
    return counter;
}
```

### Map, Filter, Reduce

```cpp
#include <algorithm>
#include <vector>
#include <numeric>

std::vector<int> nums = {1, 2, 3, 4, 5};

// Map - transform each element
std::vector<int> doubled;
std::transform(nums.begin(), nums.end(), std::back_inserter(doubled),
    [](int x) { return x * 2; });
// Result: {2, 4, 6, 8, 10}

// Filter - select elements
std::vector<int> evens;
std::copy_if(nums.begin(), nums.end(), std::back_inserter(evens),
    [](int x) { return x % 2 == 0; });
// Result: {2, 4}

// Reduce - combine into single value
int sum = std::accumulate(nums.begin(), nums.end(), 0,
    [](int acc, int x) { return acc + x; });
// Result: 15
```

### Higher-Order Functions

```cpp
// Function that takes another function
int applyOperation(int a, int b, int (*op)(int, int)) {
    return op(a, b);
}

int add(int a, int b) { return a + b; }
int multiply(int a, int b) { return a * b; }

std::cout << applyOperation(5, 3, add);       // 8
std::cout << applyOperation(5, 3, multiply);  // 15
```

---

## Data Structures

### Arrays vs Vectors

```cpp
// Fixed-size array
int arr[5] = {1, 2, 3, 4, 5};
arr[0] = 10;  // O(1) access

// Dynamic vector
std::vector<int> vec;
vec.push_back(1);     // O(1) amortized
vec.push_back(2);
vec.pop_back();       // O(1)
vec.size();           // Get size
vec.empty();          // Check empty
```

### Linked List

```cpp
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// Insert at head
void insertAtHead(ListNode*& head, int val) {
    ListNode* newNode = new ListNode(val);
    newNode->next = head;
    head = newNode;
}

// Delete node
void deleteNode(ListNode*& head, int val) {
    if (!head) return;
    
    if (head->val == val) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
        return;
    }
    
    ListNode* current = head;
    while (current->next && current->next->val != val) {
        current = current->next;
    }
    
    if (current->next) {
        ListNode* temp = current->next;
        current->next = current->next->next;
        delete temp;
    }
}
```

### Stack

```cpp
#include <stack>

std::stack<int> s;
s.push(1);
s.push(2);
s.push(3);

std::cout << s.top();  // 3
s.pop();
std::cout << s.size(); // 2
std::cout << s.empty(); // false
```

### Queue

```cpp
#include <queue>

std::queue<int> q;
q.push(1);
q.push(2);
q.push(3);

std::cout << q.front();  // 1
std::cout << q.back();   // 3
q.pop();
std::cout << q.size();   // 2
```

### Hash Table

```cpp
#include <unordered_map>
#include <unordered_set>

// Map
std::unordered_map<std::string, int> scores;
scores["Alice"] = 95;
scores["Bob"] = 87;

std::cout << scores["Alice"];  // 95
scores.erase("Bob");

// Set
std::unordered_set<int> unique;
unique.insert(1);
unique.insert(2);
unique.insert(1);  // Duplicate ignored

std::cout << unique.size();  // 2
std::cout << unique.count(1); // 1 (exists)
```

### Tree

```cpp
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// Insert into BST
TreeNode* insert(TreeNode* root, int val) {
    if (!root) return new TreeNode(val);
    
    if (val < root->val) {
        root->left = insert(root->left, val);
    } else {
        root->right = insert(root->right, val);
    }
    
    return root;
}

// Inorder traversal
void inorder(TreeNode* root) {
    if (!root) return;
    inorder(root->left);
    std::cout << root->val << " ";
    inorder(root->right);
}
```

---

## Algorithms

### Sorting

```cpp
// Bubble Sort O(n²)
void bubbleSort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
            }
        }
    }
}

// Quick Sort O(n log n)
int partition(std::vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            std::swap(arr[i], arr[j]);
        }
    }
    std::swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// Using STL
std::sort(arr.begin(), arr.end());
std::sort(arr.begin(), arr.end(), std::greater<int>());  // Descending
```

### Binary Search

```cpp
int binarySearch(std::vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1;  // Not found
}

// Using STL
auto it = std::lower_bound(arr.begin(), arr.end(), target);
if (it != arr.end() && *it == target) {
    int index = std::distance(arr.begin(), it);
}
```

### Graph Algorithms

```cpp
// BFS
void bfs(std::unordered_map<int, std::vector<int>>& graph, int start) {
    std::queue<int> q;
    std::unordered_set<int> visited;
    
    q.push(start);
    visited.insert(start);
    
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        std::cout << node << " ";
        
        for (int neighbor : graph[node]) {
            if (visited.find(neighbor) == visited.end()) {
                visited.insert(neighbor);
                q.push(neighbor);
            }
        }
    }
}

// DFS
void dfs(std::unordered_map<int, std::vector<int>>& graph, 
         int node, std::unordered_set<int>& visited) {
    visited.insert(node);
    std::cout << node << " ";
    
    for (int neighbor : graph[node]) {
        if (visited.find(neighbor) == visited.end()) {
            dfs(graph, neighbor, visited);
        }
    }
}

// Dijkstra's Algorithm
std::unordered_map<int, int> dijkstra(
    std::unordered_map<int, std::vector<std::pair<int, int>>>& graph,
    int start) {
    
    std::unordered_map<int, int> dist;
    std::priority_queue<std::pair<int, int>, 
                        std::vector<std::pair<int, int>>,
                        std::greater<>> pq;
    
    for (auto& [node, _] : graph) {
        dist[node] = INT_MAX;
    }
    dist[start] = 0;
    pq.push({0, start});
    
    while (!pq.empty()) {
        int d = pq.top().first;
        int node = pq.top().second;
        pq.pop();
        
        if (d > dist[node]) continue;
        
        for (auto& [neighbor, weight] : graph[node]) {
            if (dist[node] + weight < dist[neighbor]) {
                dist[neighbor] = dist[node] + weight;
                pq.push({dist[neighbor], neighbor});
            }
        }
    }
    
    return dist;
}
```

---

## Database Systems

### SQL Basics

```sql
-- Create table
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert
INSERT INTO users (name, email, age) VALUES 
    ('Alice', 'alice@example.com', 25),
    ('Bob', 'bob@example.com', 30);

-- Select
SELECT * FROM users;
SELECT name, email FROM users WHERE age > 25;
SELECT * FROM users ORDER BY created_at DESC;
SELECT * FROM users LIMIT 10 OFFSET 20;

-- Update
UPDATE users SET age = 26 WHERE id = 1;

-- Delete
DELETE FROM users WHERE id = 1;

-- Join
SELECT u.name, o.total 
FROM users u
INNER JOIN orders o ON u.id = o.user_id;

-- Group By
SELECT department, COUNT(*) as count
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

### NoSQL (MongoDB)

```javascript
// Insert
db.users.insertOne({
    name: "Alice",
    email: "alice@example.com",
    age: 25
});

// Find
db.users.find({ age: { $gt: 25 } });
db.users.findOne({ email: "alice@example.com" });

// Update
db.users.updateOne(
    { name: "Alice" },
    { $set: { age: 26 } }
);

// Delete
db.users.deleteOne({ name: "Alice" });

// Aggregation
db.users.aggregate([
    { $match: { age: { $gt: 25 } } },
    { $group: { _id: "$department", count: { $sum: 1 } } }
]);
```

---

## Networking

### HTTP Protocol

```cpp
// Simple HTTP client
#include <curl/curl.h>

CURL* curl = curl_easy_init();
if (curl) {
    curl_easy_setopt(curl, CURLOPT_URL, "https://api.example.com/data");
    
    // GET request
    CURLcode res = curl_easy_perform(curl);
    
    // POST request
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, "{\"key\":\"value\"}");
    
    curl_easy_cleanup(curl);
}
```

### TCP Socket Programming

```cpp
// Server
#include <sys/socket.h>
#include <netinet/in.h>

int serverSocket = socket(AF_INET, SOCK_STREAM, 0);

struct sockaddr_in address;
address.sin_family = AF_INET;
address.sin_addr.s_addr = INADDR_ANY;
address.sin_port = htons(8080);

bind(serverSocket, (struct sockaddr*)&address, sizeof(address));
listen(serverSocket, 10);

int clientSocket = accept(serverSocket, NULL, NULL);
char buffer[1024];
read(clientSocket, buffer, sizeof(buffer));
write(clientSocket, "Hello", 5);

// Client
int clientSocket = socket(AF_INET, SOCK_STREAM, 0);

struct sockaddr_in serverAddr;
serverAddr.sin_family = AF_INET;
serverAddr.sin_port = htons(8080);
inet_pton(AF_INET, "127.0.0.1", &serverAddr.sin_addr);

connect(clientSocket, (struct sockaddr*)&serverAddr, sizeof(serverAddr));
write(clientSocket, "Hello", 5);
read(clientSocket, buffer, sizeof(buffer));
```

---

## Operating Systems

### Processes & Threads

```cpp
#include <thread>
#include <mutex>

// Thread
void worker(int id) {
    std::cout << "Worker " << id << std::endl;
}

std::thread t1(worker, 1);
std::thread t2(worker, 2);

t1.join();
t2.join();

// Mutex
std::mutex mtx;
int counter = 0;

void increment() {
    for (int i = 0; i < 1000; i++) {
        std::lock_guard<std::mutex> lock(mtx);
        counter++;
    }
}
```

### Memory Management

```cpp
// Stack allocation (automatic)
void func() {
    int x = 10;  // On stack
}  // x automatically freed

// Heap allocation (manual)
int* ptr = new int(10);  // On heap
delete ptr;  // Must free manually

// Smart pointers (automatic cleanup)
auto ptr = std::make_unique<int>(10);  // Auto deleted
auto shared = std::make_shared<int>(10);  // Reference counted
```

---

## Security

### Input Validation

```cpp
// SQL Injection prevention
void safeQuery(const std::string& email) {
    // Use prepared statements
    PreparedStatement* stmt = db.prepare(
        "SELECT * FROM users WHERE email = ?"
    );
    stmt->setString(1, email);
    stmt->execute();
}

// XSS prevention
std::string sanitizeHTML(const std::string& input) {
    std::string output = input;
    output = replaceAll(output, "&", "&amp;");
    output = replaceAll(output, "<", "&lt;");
    output = replaceAll(output, ">", "&gt;");
    output = replaceAll(output, "\"", "&quot;");
    return output;
}
```

### Password Hashing

```cpp
#include <bcrypt>

// Hash password
std::string hash = bcrypt::hash_password("user_password");

// Verify password
bool valid = bcrypt::verify_password("user_password", hash);
```

---

## Software Engineering

### Design Patterns

#### Singleton

```cpp
class Singleton {
private:
    static Singleton* instance;
    
    Singleton() {}  // Private constructor
    
public:
    static Singleton* getInstance() {
        if (instance == nullptr) {
            instance = new Singleton();
        }
        return instance;
    }
    
    void doSomething() {}
};

Singleton* Singleton::instance = nullptr;
```

#### Factory

```cpp
class Shape {
public:
    virtual void draw() = 0;
    virtual ~Shape() {}
};

class Circle : public Shape {
    void draw() override { std::cout << "Circle"; }
};

class Square : public Shape {
    void draw() override { std::cout << "Square"; }
};

class ShapeFactory {
public:
    static Shape* createShape(const std::string& type) {
        if (type == "circle") return new Circle();
        if (type == "square") return new Square();
        return nullptr;
    }
};

Shape* shape = ShapeFactory::createShape("circle");
shape->draw();
```

#### Observer

```cpp
class Observer {
public:
    virtual void update(const std::string& data) = 0;
};

class Subject {
    std::vector<Observer*> observers;
    
public:
    void attach(Observer* obs) {
        observers.push_back(obs);
    }
    
    void notify(const std::string& data) {
        for (auto* obs : observers) {
            obs->update(data);
        }
    }
};

class ConcreteObserver : public Observer {
    void update(const std::string& data) override {
        std::cout << "Received: " << data << std::endl;
    }
};
```

---

## DevOps & Tools

### Git Commands

```bash
# Basic operations
git init
git clone <url>
git status
git add .
git commit -m "message"
git push
git pull

# Branching
git branch
git branch <name>
git checkout <name>
git checkout -b <name>
git merge <name>

# Remote
git remote add origin <url>
git push -u origin main
```

### Docker Commands

```bash
# Build
docker build -t myapp .

# Run
docker run -p 8080:80 myapp

# Commands
docker ps
docker images
docker stop <container>
docker logs <container>

# Compose
docker-compose up
docker-compose down
```

---

## Advanced Topics

### Concurrency

```cpp
#include <future>
#include <async>

// Async
auto future = std::async(std::launch::async, []() {
    return 42;
});

int result = future.get();

// Parallel algorithms
std::vector<int> nums(1000000);
std::sort(std::execution::par, nums.begin(), nums.end());
```

### Distributed Systems

```cpp
// Consensus (simplified)
class RaftNode {
    enum State { FOLLOWER, CANDIDATE, LEADER };
    State state = FOLLOWER;
    int currentTerm = 0;
    std::string votedFor;
    
    void startElection() {
        state = CANDIDATE;
        currentTerm++;
        // Request votes from other nodes
    }
};
```

---

## Learning Path Summary

| Level | Topics | Duration |
|-------|--------|----------|
| **Beginner** | Variables, Control Flow, Functions, Basic Data Structures | 1-2 months |
| **Intermediate** | OOP, Algorithms, Databases, Networking | 3-6 months |
| **Advanced** | System Design, Concurrency, Distributed Systems | 6-12 months |
| **Expert** | Architecture, Performance, Security | 1-2 years |

---

*This guide covers the essential topics for becoming a well-rounded software developer. Practice regularly and build projects to reinforce learning.*
