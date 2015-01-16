word_count = open("pg10.txt", "r")
wordcount = {}

for word in file.read(word_count).split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
result = sorted(wordcount.items(), key=lambda t: t[1], reverse=True)

for word, count in result:
    print word, count