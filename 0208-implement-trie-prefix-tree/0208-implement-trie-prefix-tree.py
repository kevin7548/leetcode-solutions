class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}  # {char: Node(char)}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word: str) -> None:
        curr_node = self.head
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.data = word

    def search(self, word: str) -> bool:
        curr_node = self.head
        for char in word:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        return True if curr_node.data == word else False

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.head
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        return True if curr_node else False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)