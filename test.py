import os
path = os.getcwd() + '/review_polarity/txt_sentoken/neg/'
counter = 0
wordIndex = 0
words = []

for filename in os.listdir(path):
    with open(path + filename, 'r') as f:
        for line in f:
            for word in line.split():
                if word not in words:
                    words.append(word)
                # wordIndex += 1
                # print(word)
    counter += 1
    if counter >= 1:
        break
print(words)
