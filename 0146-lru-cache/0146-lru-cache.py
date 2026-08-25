class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}   # key -> Node
        self.head = Node()  # 센티넬: head쪽 = MRU(최근)
        self.tail = Node()  # 센티넬: tail쪽 = LRU(오래됨)
        self.head.next = self.tail  # 빈 리스트 초기 연결
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # 없으면 -1 / 있으면 _remove -> _add_front -> val 변환
        if key in self.map:
            node = self.map[key]
            self._remove(node)
            self._add_front(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # 있으면 val 갱신 후 맨앞으로 / 없으면 새로 노드 만들어 등록 + 맨앞
        # len 초과 시 tail.prev 축출: _remove + del map[...]
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._remove(node)
            self._add_front(node)
        else:
            node = Node(key, value)
            self.map[key] = node
            self._add_front(node)
        if len(self.map) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]
        
    def _remove(self, node):
        # node를 리스트에서 떼어냄 (앞뒤 재봉합)
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_front(self, node):
        first = self.head.next  # 첫 노드 기억
        # node 양손 먼저 연결
        node.prev = self.head
        node.next = first
        # 양옆이 node를 잡게
        self.head.next = node
        first.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)