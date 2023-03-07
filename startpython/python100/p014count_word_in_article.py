word_count = {}
with open ("voa.txt") as fin:
    for line in fin:
        line = line[:-1]
        words = line.split()
        for word in words:
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1

sort_result=sorted(
    word_count.items(),
    key = lambda x:x[1],
    reverse=True
)[:10]

# slicing syntax:[:10]
print(sort_result)
