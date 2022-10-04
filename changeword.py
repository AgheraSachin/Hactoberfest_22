class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence=list(sentence.split(" "))
        for i in range(len(sentence)):
            #print(i)
            for j in dictionary:
                if sentence[i].startswith(j):
                    sentence[i]=j
                    #print(sentence)
        return " ".join(sentence)
        
