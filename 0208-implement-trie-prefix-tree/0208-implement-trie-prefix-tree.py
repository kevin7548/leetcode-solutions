class Node:
    def __init__(self):
        self.children = {}  # {char: Node(char)}
        self.is_end = False

class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        curr_node = self.head
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = Node()
            curr_node = curr_node.children[char]
        curr_node.is_end = True

    def search(self, word: str) -> bool:
        curr_node = self.walk(self.head, word)
        if curr_node is None:
            return False
        return curr_node.is_end

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.walk(self.head, prefix)
        return curr_node is not None

    def walk(self, node, word: str):    # return 값 필요 (None)
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)