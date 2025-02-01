class TrieNode:
    def __init__(self):
        self.children = {}
        self.EndOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.EndOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.EndOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


trie = Trie()
print(trie.insert("apple"))
print(trie.search("apple"))   # return True
print(trie.search("app"))     # return False
print(trie.startsWith("app")) # return True
print(trie.insert("app"))
print(trie.search("app"))     # return True