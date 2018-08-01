def word_count():
    with open("input.txt","r",encoding = 'utf-8') as file:
        wordcount = {}
        for word in file.read().split():
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
        print(wordcount)
        for k, v in wordcount.items():
            print (k,v)

    with open("output.txt","w", encoding='utf-8') as file:
        for k, v in wordcount.items():
            file.write(k+" "+str(v)+"\n")
    file.close()

word_count()