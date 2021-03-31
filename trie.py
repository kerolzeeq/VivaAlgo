class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False             
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):

        for i in range(len(word)):
            curr_root = self.root
            for i in word:
                if i not in curr_root.children:
                    curr_root.children[i] = TrieNode()      #create new children of the character
                    
                curr_root = curr_root.children[i]       #move to next dictionary
                curr_root.isWord = True                 #mark character is true
            word = word[1:]                             # remove first letter

    def search(self, word):
        curr_root = self.root

        for i in word:
            if i not in curr_root.children:             # check if character is in the dictonary
                return False
            else:
                curr_root = curr_root.children[i]       # mov into character dictionary

        return curr_root.isWord                         # return boolean is word flag

trie = Trie()
string="aalgorithmisfun"
pat="fun"
trie.add_word(string)
print("Word",pat,"is",trie.search(pat),"in word", string)

