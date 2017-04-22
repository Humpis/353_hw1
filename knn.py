import os
import sys
import json
import string
import re
import numpy as np
from numpy import linalg as la
path_neg = os.getcwd() + '/review_polarity/txt_sentoken/neg/'
path_pos = os.getcwd() + '/review_polarity/txt_sentoken/pos/'
stopwords = ["a", "about", "above", "above", "across", "after",
             "afterwards", "again", "against", "all", "almost", "alone",
             "along", "already", "also", "although", "always", "am", "among",
             "amoungst", "amount", "an", "and", "another", "any", "anyhow",
             "anyone", "anything", "anyway", "anywhere", "are", "around", "as",
             "at", "back", "be", "became", "because", "become", "becomes",
             "becoming", "been", "before", "beforehand", "behind", "being",
             "below", "beside", "besides", "between", "beyond", "bill", "both",
             "bottom", "but", "by", "call", "can", "cannot", "cant", "co",
             "con", "could", "couldnt", "cry", "de", "describe", "detail",
             "done", "down", "due", "during", "each", "eg", "eight", "either",
             "eleven", "else", "elsewhere", "empty", "enough", "etc", "even",
             "ever", "every", "everyone", "everything", "everywhere", "except",
             "few", "fifteen", "fify", "fill", "find", "fire", "first", "five",
             "for", "former", "formerly", "forty", "found", "four", "from",
             "front", "full", "further", "get", "give", "go", "had", "has",
             "hasnt", "have", "he", "hence", "her", "here", "hereafter",
             "hereby", "herein", "hereupon", "hers", "herself", "him",
             "himself", "his", "how", "however", "hundred", "ie", "if", "in",
             "inc", "indeed", "interest", "into", "is", "it", "its", "itself",
             "keep", "last", "latter", "latterly", "least", "less", "ltd",
             "many", "may", "me", "meanwhile", "might", "mill", "mine", "more",
             "moreover", "most", "mostly", "move", "much", "must", "my",
             "name", "namely", "neither", "never", "nevertheless", "next",
             "no", "nobody", "none", "noone", "nor", "not", "nothing", "now",
             "nowhere", "of", "off", "often", "on", "once", "one", "only",
             "or", "other", "others", "otherwise", "our", "ours", "ourselves",
             "out", "over", "own", "part", "per", "perhaps", "please", "put",
             "rather", "re", "same", "see", "seem", "seemed", "seeming",
             "serious", "several", "she", "should", "show", "side", "since",
             "sincere", "six", "sixty", "so", "some", "somehow", "someone",
             "something", "sometime", "sometimes", "somewhere", "still",
             "system", "take", "ten", "than", "that", "the", "their", "them",
             "themselves", "then", "thence", "there", "thereafter", "thereby",
             "therefore", "therein", "thereupon", "these", "they", "thickv",
             "thin", "third", "this", "those", "though", "three", "through",
             "throughout", "thru", "thus", "to", "together", "too", "top",
             "toward", "towards", "twelve", "twenty", "two", "un", "under",
             "until", "up", "upon", "us", "very", "via", "was", "we", "well",
             "were", "what", "whatever", "when", "whence", "whenever", "where",
             "whereafter", "whereas", "whereby", "wherein", "whereupon",
             "wherever", "whether", "which", "while", "whither", "who",
             "whole", "whom", "whose", "why", "will", "with", "within",
             "would", "yet", "you", "your", "yours", "yourself", "yourselves",
             "the", "amongst", "do", "made", "myself", "nine", "onto", "seems",
             "such", "whoever", "without"]
counter = 0
words = {}
y = np.zeros((2000), dtype=np.int)
for i in range(1000, 2000):
    y[i] = 1
x = []
k = -1
metric = -1

if(len(sys.argv) == 6):
    if sys.argv[2] == "--punct":
        print("Generating list of words...")
        for filename in os.listdir(path_neg):
            with open(path_neg + filename, 'r') as f:
                for line in f:
                    for word in line.split():
                        if word not in words:
                            # Stop words
                            if(sys.argv[5] == '--stopwords'):
                                words[word] = counter
                                counter += 1
                            elif(sys.argv[5] == '--nostopwords'):
                                if word not in stopwords:
                                    words[word] = counter
                                    counter += 1
                            else:
                                print("Invalid argument")
                                sys.exit(1)
        for filename in os.listdir(path_pos):
            with open(path_pos + filename, 'r') as f:
                for line in f:
                    for word in line.split():
                        if word not in words:
                            # Stop words
                            if(sys.argv[5] == '--stopwords'):
                                words[word] = counter
                                counter += 1
                            elif(sys.argv[5] == '--nostopwords'):
                                if word not in stopwords:
                                    words[word] = counter
                                    counter += 1
                            else:
                                print("Invalid argument")
                                sys.exit(1)
        # words_file = open('punctNoStopWords.txt', 'w')
        # words_file = open('punctWords.txt', 'w')
        # json.dump(words, words_file)
        # print("Generation sucsessful")
    elif sys.argv[2] == "--nopunct":
        print("Generating list of words...")
        for filename in os.listdir(path_neg):
            with open(path_neg + filename, 'r') as f:
                for line in f:
                    for word in line.split():
                        newWord = re.sub(
                            '[' + string.punctuation + ']', '', word)
                        if newWord != '':
                            if word not in words:
                                # Stop words
                                if(sys.argv[5] == '--stopwords'):
                                    words[word] = counter
                                    counter += 1
                                elif(sys.argv[5] == '--nostopwords'):
                                    if word not in stopwords:
                                        words[word] = counter
                                        counter += 1
                                else:
                                    print("Invalid argument")
                                    sys.exit(1)
        for filename in os.listdir(path_pos):
            with open(path_pos + filename, 'r') as f:
                for line in f:
                    for word in line.split():
                        newWord = re.sub(
                            '[' + string.punctuation + ']', '', word)
                        if newWord != '':
                            if word not in words:
                                # Stop words
                                if(sys.argv[5] == '--stopwords'):
                                    words[word] = counter
                                    counter += 1
                                elif(sys.argv[5] == '--nostopwords'):
                                    if word not in stopwords:
                                        words[word] = counter
                                        counter += 1
                                else:
                                    print("Invalid argument")
                                    sys.exit(1)
        # words_file = open('nopunctnostopWords.txt', 'w')
        # words_file = open('nopunctWords.txt', 'w')
        # json.dump(words, words_file)
        # print("Generation sucsessful")
    else:
        print("Invalid argument")
        sys.exit(1)
else:
    print("Invalid arguments")
    sys.exit(1)

# Now make the matrix for binary or frequency
print(len(words))
if sys.argv[1] == "--binary":
    print('Creating matrix X for binary representation...')
    x = np.zeros((2000, len(words)), dtype=np.int)
    row = 0
    for filename in os.listdir(path_neg):
        with open(path_neg + filename, 'r') as f:
            for line in f:
                for word in line.split():
                    if words.get(word) is not None:
                        x[row][words.get(word)] = 1
        row += 1
    for filename in os.listdir(path_pos):
        with open(path_pos + filename, 'r') as f:
            for line in f:
                for word in line.split():
                    if words.get(word) is not None:
                        x[row][words.get(word)] = 1
        row += 1
    # print(x)
elif sys.argv[1] == "--frequency":
    print('Creating matrix X for frequency representation...')
    x = np.zeros((2000, len(words)), dtype=np.int)
    row = 0
    for filename in os.listdir(path_neg):
        with open(path_neg + filename, 'r') as f:
            for line in f:
                for word in line.split():
                    if words.get(word) is not None:
                        x[row][words.get(word)] = x[row][words.get(word)] + 1
        row += 1
    for filename in os.listdir(path_pos):
        with open(path_pos + filename, 'r') as f:
            for line in f:
                for word in line.split():
                    if words.get(word) is not None:
                        x[row][words.get(word)] = x[row][words.get(word)] + 1
        row += 1
else:
    print("Invalid argument")
    sys.exit(1)

if sys.argv[3][:4] == '--k=':
    try:
        k = int(sys.argv[3][4:])
    except ValueError:
        print("Error: K must be an integer")
        sys.exit(1)
else:
    print("Invalid argument")
    sys.exit(1)

if sys.argv[4] == '--metric=euclidean':
    metric = 0
elif sys.argv[4] == '--metric=manhattan':
    metric = 1
else:
    print("Invalid argument")
    sys.exit(1)

xo = x.copy()
yo = y.copy()

for i in range(1, 1000):
    if i % 2 == 0:
        continue
    xo[i] = x[i + 999]
    yo[i] = y[i + 999]
    xo[i + 999] = x[i]
    yo[i + 999] = y[i]

print('about the do this shit...')
for a in range(0, 5):
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for i in range(a * 400, a * 400 + 400):
        d = np.zeros((2000), dtype=np.float)
        for j in range(0, 2000):
            if (j >= a * 400) and (j < a * 400 + 400):
                continue

            # sumofs = 0
            # for q in range(0, len(words)):
            #     sumofs += math.pow(xo[i][q] - xo[j][q], 2)
            # d[j] = math.sqrt(sumofs)

            xi = np.array(xo[i])
            xj = np.array(xo[j])
            d[j] = la.norm(xi - xj)
        sortedd = np.argsort(d)
        positive = 0
        for j in range(0, k):
            positive += yo[sortedd[j + 400]]
        positive /= k
        if positive >= .5:
            if yo[i] == 1:
                tp += 1
            else:
                fp += 1
        else:
            if yo[i] == 1:
                fn += 1
            else:
                tn += 1
    PrecisionP = tp / (tp + fp)
    PrecisionN = tn / (tn + fn)
    RecallP = tp / (tp + fn)
    RecallN = tn / (tn + fp)
    Accuracy = (tp + tn) / (tp + tn + fp + fn)
    print("Precision+ ", PrecisionP)
    print("Precision- ", PrecisionN)
    print("Recall+ ", RecallP)
    print("Recall- ", RecallN)
    print("Accuracy ", Accuracy)
    print("Precision ", (PrecisionP + PrecisionN) / 2)
    print("Recall ", (RecallP + RecallN) / 2)
sys.exit(0)
