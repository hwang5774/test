"""이 모듈은 https://github.com/keon/algorithms의 파이썬 프로젝트의 일부입니다"""

"""
우리는 단어를 추가하고 검색할 수 있는 효율적인 데이터 구조를 설계하도록 요청받았습니다.
검색은 리터럴 단어 또는 “.”을 포함하는 정규 표현식일 수 있으며, 여기서 “.”은 모든 문자가 될 수 있습니다.

예:
addWord(“bad”)
addWord(“dad”)
addWord(“mad”)
search(“pad”) -> false
search(“bad”) -> true
search(“.ad”) -> true
search(“b..”) -> true
"""

# collections 모듈 가져오기
import collections

# TrieNode 클래스 정의
class TrieNode(object):
    def __init__(self, letter, is_terminal=False):
        # 자식 딕셔너리와 문자 초기화
        self.children = dict()
        self.letter = letter
        # is_terminal 초기화
        self.is_terminal = is_terminal

# WordDictionary 클래스 정의
class WordDictionary(object):
    def __init__(self):
        # 루트 노드 초기화
        self.root = TrieNode("")

    def add_word(self, word):
        # 현재 노드를 루트로 초기화
        cur = self.root
        # 단어의 각 문자를 반복
        for letter in word:
            # 문자가 자식에 없으면 추가
            if letter not in cur.children:
                cur.children[letter] = TrieNode(letter)
            # 다음 노드로 이동
            cur = cur.children[letter]
        # 마지막 노드를 터미널로 표시
        cur.is_terminal = True

    def search(self, word, node=None):
        # 노드가 제공되지 않으면 루트로 초기화
        cur = node
        if not cur:
            cur = self.root
        # 단어의 각 문자를 반복
        for i, letter in enumerate(word):
            # 문자가 점인 경우
            if letter == ".":
                # 마지막 문자인 경우
                if i == len(word) - 1:
                    # 자식 노드 중 하나가 터미널인지 확인
                    for child in cur.children.itervalues():
                        if child.is_terminal:
                            return True
                    return False
                # 마지막 문자가 아닌 경우
                for child in cur.children.itervalues():
                    # 다음 문자를 재귀적으로 검색
                    if self.search(word[i+1:], child) == True:
                        return True
                return False
            # 문자가 점이 아닌 경우
            if letter not in cur.children:
                return False
            # 다음 노드로 이동
            cur = cur.children[letter]
        # 마지막 노드가 터미널인 경우 반환
        return cur.is_terminal

# WordDictionary2 클래스 정의
class WordDictionary2(object):
    def __init__(self):
        # word_dict를 defaultdict로 초기화
        self.word_dict = collections.defaultdict(list)

    def add_word(self, word):
        # word_dict에 단어 추가
        if word:
            self.word_dict[len(word)].append(word)

    def search(self, word):
        # 단어가 비어 있으면 False 반환
        if not word:
            return False
        # 단어에 점이 없는 경우
        if '.' not in word:
            return word in self.word_dict[len(word)]
        # 단어에 점이 있는 경우
        for v in self.word_dict[len(word)]:
            # 단어와 v 일치
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
            else:
                return True
        return False

