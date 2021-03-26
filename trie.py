class Trie:
    head = {}

    def printTrie(self):
        cur=self.head;
        print(cur)
        print()

    def add(self, word):
        for i in range(len(word)):
            cur = self.head
            for ch in word:
                if ch not in cur:
                    cur[ch] = {}

                cur = cur[ch]
                cur[ch] = True
                
            # * denotes the Trie has this word as item
            # if * doesn't exist, Trie doesn't have this word but as a path to longer word
            word= word[1:]
            
        

    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
            print(cur)

        return cur[ch]

dictionary = Trie()

dictionary.add("algorithmisfun")
# a=a[1:]
# print(a)
# dictionary.printTrie()
print(dictionary.search("fun"))
