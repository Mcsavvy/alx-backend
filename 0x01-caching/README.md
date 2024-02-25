# Caching Project

This project explores different caching algorithms in Python. Below are the different caching algorithms implemented:

### 1. Basic Cache (`0-basic_cache.py`)

This is a simple caching system called BasicCache that inherits from BaseCaching. It does not have a limit on the number of items in the cache.

- **put(key, item):** Add an item in the cache. If key or item is None, this method does nothing.

- **get(key):** Get an item by key. If key is None or the key doesn't exist in the cache, return None.

### 2. FIFO Cache (`1-fifo_cache.py`)

The FIFOCache is a caching system that follows the First-In-First-Out (FIFO) algorithm. It inherits from BaseCaching.

- **put(key, item):** Add an item in the cache. If the number of items in the cache exceeds the maximum limit (BaseCaching.MAX_ITEMS), the first item put in cache is discarded (FIFO rule).

- **get(key):** Get an item by key. If key is None or the key doesn't exist in the cache, return None.

### 3. LIFO Cache (`2-lifo_cache.py`)

The LIFOCache is a caching system that follows the Last-In-First-Out (LIFO) algorithm. It inherits from BaseCaching.

- **put(key, item):** Add an item in the cache. If the number of items in the cache exceeds the maximum limit (BaseCaching.MAX_ITEMS), the last item put in cache is discarded (LIFO rule).

- **get(key):** Get an item by key. If key is None or the key doesn't exist in the cache, return None.

### 4. LRU Cache (`3-lru_cache.py`)

The LRUCache is a caching system that follows the Least Recently Used (LRU) algorithm. It inherits from BaseCaching.

- **put(key, item):** Add an item in the cache. If the number of items in the cache exceeds the maximum limit (BaseCaching.MAX_ITEMS), the least recently used item is discarded.

- **get(key):** Get an item by key. If key is None or the key doesn't exist in the cache, return None.

### 5. MRU Cache (`4-mru_cache.py`)

The MRUCache is a caching system that follows the Most Recently Used (MRU) algorithm. It inherits from BaseCaching.

- **put(key, item):** Add an item in the cache. If the number of items in the cache exceeds the maximum limit (BaseCaching.MAX_ITEMS), the most recently used item is discarded.

- **get(key):** Get an item by key. If key is None or the key doesn't exist in the cache, return None.

### 6. LFU Cache (`100-lfu_cache.py`) - Advanced

The LFUCache is a caching system that follows the Least Frequently Used (LFU) algorithm. It inherits from BaseCaching.

- **put(key, item):** Add an item in the cache. If the number of items in the cache exceeds the maximum limit (BaseCaching.MAX_ITEMS), the least frequency used item is discarded. If multiple items have the same least frequency of use, the LRU algorithm is used to discard only the least recently used item.

- **get(key):** Get an item by key. If key is None or the key doesn't exist in the cache, return None.

Each caching system inherits from the `BaseCaching` class, which provides common caching functionalities like put, get, and a print_cache method to display the current cache.

### Requirements

- Python Scripts: All the files are interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.

- File Endings: All files end with a new line.

- Shebang: The first line of all files is "#!/usr/bin/env python3".

- Documentation: All modules, classes, and functions have appropriate docstrings.

- Style: Code should follow the pycodestyle style (version 2.5).

- Executability: All files are executable.

- Documentation Length: All modules, classes, and functions have meaningful documentation explaining their purpose.

---

Feel free to explore and experiment with the different caching algorithms implemented in this project. Have fun!