def matchword(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            
            ctr += 1
            lst.append(word)
    print("Words with first and last letter same are:", lst)
    return ctr

a = matchword(['Hello','abba','alibaba','Domingo','Dominos','america'])
print(a)