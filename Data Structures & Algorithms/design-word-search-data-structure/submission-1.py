class Node:
    def __init__(self):
        self.children = {}
        self.end_word = False
class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        
        curr.end_word = True

    def search(self, word: str) -> bool:
        curr = self.root 

        def dfs(pos, c):
            # Wild card 
            if word[pos] == ".":
                # Try all keys
                for key in c.children.keys():
                    # Recursive case 
                    if pos < len(word ) - 1:
                        if dfs(pos + 1, c.children[key]):
                            return True
                    else:
                        if c.children[key].end_word:
                            return True

                # no keys work
                return False
            elif pos == len(word) - 1 and word[pos] in c.children:
                return c.children[word[pos]].end_word
            elif word[pos] not in c.children:
                return False
            else:
                return dfs(pos + 1, c.children[word[pos]])
            

        for i in range(len(word)):
            # Wild card
            if word[i] == ".":
                return dfs(i, curr)
            # False case
            elif word[i] not in curr.children:
                return False
            # Exists
            else:
                curr = curr.children[word[i]]
        # Check end of word 
        return curr.end_word

                        

