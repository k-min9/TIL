# https://leetcode.com/problems/implement-trie-prefix-tree
# 풀이 : 직접 구현해보자

import collections

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)


class Trie:

    def __init__(self):
        # 단어의 끝인가
        self.root = TrieNode()

    # 삽입
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    # 검색
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word
        
    # 단어 존재여부 판별
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix: # 이부분이랑
            if char not in node.children:
                return False
            node = node.children[char]
        return True  # 이부분만 다름
        