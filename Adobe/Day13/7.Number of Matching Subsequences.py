class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_sub(word):
            index=-1
            for ch in word:
                index=s.find(ch,index+1)
                if index==-1:
                    return False
            return True
        
        hashmap = {}
        c=0
        for word in words:
            if word in hashmap:
                if hashmap[word]:
                    c+= 1
            else:
                if is_sub(word):
                    c+= 1
                    hashmap[word] = True
                else:
                    hashmap[word] = False
        return c
