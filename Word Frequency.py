def WordCount(s):
    count = dict()
    words = s.split()
    
    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
    return count
 

s = input()
hel = {}
hel = WordCount(s)

print(hel)
