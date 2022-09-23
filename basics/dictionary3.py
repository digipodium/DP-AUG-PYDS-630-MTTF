import helper as h
from string import punctuation

data = h.read('basics/pride_n_prejudice.txt')
print(len(data))

# remove punctuation
for p in punctuation:
    data = data.replace(p,'')

# split into words and remove spaces and empty strings
words = [word.strip() for word in data.lower().split()]

print("TOTAL WORDS FOUND: ", len(words))
print("UNIQUE WORDS FOUND: ", len(set(words)))

# create a dictionary
wc = {}
for word in words:
    if word in wc:
        wc[word] += 1
    else:
        wc[word] = 1

# sorting the dictionary -> wc.items() returns a list of tuples
wc = sorted(wc.items(), key=lambda x: x[1], reverse=True) 

# print the top 10 words
for i in range(10):
    print(wc[i])

