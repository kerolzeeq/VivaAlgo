
class Trie:
    head = {}

    def printTrie(self):
        cur=self.head
        print(cur)
        # print()

    def add(self, word):
        for i in range(len(word)):
            cur = self.head
            for ch in word:
                if ch not in cur:
                    cur[ch] = {}
                    # print(cur)
                cur = cur[ch]
                cur[ch] = True
                
            word= word[1:]
            
        

    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
            print(cur)
        
        print(ch)
        print(cur)
        if cur==True:
            return False
        else:
            return cur[ch]    

dictionary = Trie()

dictionary.add("apple")
# a=a[1:]
# print(a)
dictionary.printTrie()
print(dictionary.search("fun"))
