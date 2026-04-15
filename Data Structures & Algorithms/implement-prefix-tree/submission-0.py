class Node:
    def __init__(self):
        self.children = {}
        self.endWord = False
class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        # Start at root of tree
        curr = self.root

        # ITERATIVE CASE 
        for c in word:
            # Add to children
            if c not in curr.children :
                curr.children[c] = Node()
            
            # Adjust curr
            curr = curr.children[c]
        
        # Add end of word flag 
        curr.endWord = True


    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        # End of word check
        return curr.endWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return True
        