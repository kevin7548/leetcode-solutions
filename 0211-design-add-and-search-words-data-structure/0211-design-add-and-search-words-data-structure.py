class Node:
    def __init__(self):
        self.children = {}  # {char: Node()}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        curr_node = self.head
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = Node()
            curr_node = curr_node.children[char]
        curr_node.is_end = True

    def search(self, word: str) -> bool:
        return self._dfs(self.head, word)  # 재귀 시작점: head, 전체 word
        
    def _dfs(self, node, word: str) -> bool:
        # 1. 베이스: word == "" 이면 return node.is_end
        # char = word[0], rest = word[1:]
        if word == "":
            return node.is_end

        char, rest = word[0], word[1:]

        # 2. 일반 문자 (char != '.'):
        # char in node.children에 속해 있으면 return self._dfs(node.children[char], rest)   # 결과 그대로 흘림
        # 아니면 -> return False    # 없으면 즉시 실패
        if char != '.':
            if char in node.children:
                return self._dfs(node.children[char], rest)
            else:
                return False

        # 3. 와일드카드 (char == ':'):
        # node.children.values()의 모든 자식 child에 대해:
        # self._dfs(child, rest)가 하나라도 True면 -> return True
        # 다 False면 (자식 없는 경우 포함) -> return False
        else:
            return any(self._dfs(child, rest) for child in node.children.values())

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)