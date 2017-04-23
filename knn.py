import os
import sys
# import json
import string
import re
import numpy as np
from numpy import linalg as la
import scipy.spatial
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
if sys.argv[1] == "--binary":
    print('Creating matrix X for binary representation...')
    x = np.zeros((2000, len(words)), dtype=np.float)
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
    x = np.zeros((2000, len(words)), dtype=np.float)
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
    metric = 'euclidean'
    p = 2
elif sys.argv[4] == '--metric=manhattan':
    metric = 'cityblock'
    p = 1
else:
    print("Invalid argument")
    sys.exit(1)

# 5 split
x1 = np.zeros((400, len(words)), dtype=np.float)
x2 = np.zeros((400, len(words)), dtype=np.float)
x3 = np.zeros((400, len(words)), dtype=np.float)
x4 = np.zeros((400, len(words)), dtype=np.float)
x5 = np.zeros((400, len(words)), dtype=np.float)
y1 = np.zeros((400), dtype=np.int)
y2 = np.zeros((400), dtype=np.int)
y3 = np.zeros((400), dtype=np.int)
y4 = np.zeros((400), dtype=np.int)
y5 = np.zeros((400), dtype=np.int)

xo = x.copy()
yo = y.copy()

print("Shuffling data matrix")
# for i in range(1, 1000):
#     if i % 2 == 0:
#         continue
#     xo[i] = x[i + 999]
#     yo[i] = y[i + 999]
#     xo[i + 999] = x[i]
#     yo[i + 999] = y[i]
randomfloat = np.random.rand(2000)
randomsort = np.argsort(randomfloat)
xo = x[randomsort]
yo = y[randomsort]

print('Normalizing feature vectors...')
for i in range(0, 2000):
    xi = np.array(xo[i])
    xinorm = la.norm(xi)
    xi = xi / xinorm
    xo[i] = xi

# 5 split
for i in range(0, 400):
    x1[i] = xo[i]
    x2[i] = xo[i + 400]
    x3[i] = xo[i + 800]
    x4[i] = xo[i + 1200]
    x5[i] = xo[i + 1600]
    y1[i] = yo[i]
    y2[i] = yo[i + 400]
    y3[i] = yo[i + 800]
    y4[i] = yo[i + 1200]
    y5[i] = yo[i + 1600]

print("Performing 5-fold cross vaidation...")
avgPrecisionP = 0
avgPrecisionN = 0
avgRecallP = 0
avgRecallN = 0
avgAccuracy = 0
avgPrecision = 0
avgRecall = 0
tie = 0
for a in range(0, 5):
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    if a == 0:
        if k == 0:
            xtrain = np.delete(xo, np.s_[0:400], axis=0)
            ytrain = np.delete(yo, np.s_[0:400])
            negCenter = 0
            posCenter = 0
            negCount = 0
            posCount = 0
            for i in range(0, 1600):
                if(ytrain[i] == 0):
                    xi = np.array(xtrain[i])
                    negCenter += xi
                    negCount += 1
                else:
                    xi = np.array(xtrain[i])
                    posCenter += xi
                    posCount += 1
            negCenter /= negCount
            posCenter /= posCount
            for i in range(0, 400):
                dneg = scipy.spatial.distance.minkowski(x1[i], negCenter, p)
                dpos = scipy.spatial.distance.minkowski(x1[i], posCenter, p)
                if dneg == dpos:
                    tie += 1
                if dneg < dpos:
                    if y1[i] == 0:
                        tn += 1
                    else:
                        fn += 1
                else:
                    if y1[i] == 1:
                        tp += 1
                    else:
                        fp += 1
        else:
            d = scipy.spatial.distance.cdist(x1, xo, metric)
            d = np.delete(d, np.s_[0:400], axis=1)
            yy = np.delete(yo, np.s_[0:400], axis=0)
            for i in range(0, 400):
                sortedd = np.argsort(d[i])
                positive = 0
                for j in range(0, k):
                    positive += yy[sortedd[j]]
                positive /= k
                if positive == .5:
                    tie += 1
                if positive >= .5:
                    if y1[i] == 1:
                        tp += 1
                    else:
                        fp += 1
                else:
                    if y1[i] == 1:
                        fn += 1
                    else:
                        tn += 1
    if a == 1:
        if k == 0:
            xtrain = np.delete(xo, np.s_[400:800], axis=0)
            ytrain = np.delete(yo, np.s_[400:800])
            negCenter = 0
            posCenter = 0
            negCount = 0
            posCount = 0
            for i in range(0, 1600):
                if(ytrain[i] == 0):
                    xi = np.array(xtrain[i])
                    negCenter += xi
                    negCount += 1
                else:
                    xi = np.array(xtrain[i])
                    posCenter += xi
                    posCount += 1
            negCenter /= negCount
            posCenter /= posCount
            for i in range(0, 400):
                dneg = scipy.spatial.distance.minkowski(x2[i], negCenter, p)
                dpos = scipy.spatial.distance.minkowski(x2[i], posCenter, p)
                if dneg == dpos:
                    tie += 1
                if dneg < dpos:
                    if y2[i] == 0:
                        tn += 1
                    else:
                        fn += 1
                else:
                    if y2[i] == 1:
                        tp += 1
                    else:
                        fp += 1
        else:
            d = scipy.spatial.distance.cdist(x2, xo, metric)
            d = np.delete(d, np.s_[400:800], axis=1)
            yy = np.delete(yo, np.s_[400:800], axis=0)
            for i in range(0, 400):
                sortedd = np.argsort(d[i])
                positive = 0
                for j in range(0, k):
                    positive += yy[sortedd[j]]
                positive /= k
                if positive == .5:
                    tie += 1
                if positive >= .5:
                    if y2[i] == 1:
                        tp += 1
                    else:
                        fp += 1
                else:
                    if y2[i] == 1:
                        fn += 1
                    else:
                        tn += 1
    if a == 2:
        if k == 0:
            xtrain = np.delete(xo, np.s_[800:1200], axis=0)
            ytrain = np.delete(yo, np.s_[800:1200])
            negCenter = 0
            posCenter = 0
            negCount = 0
            posCount = 0
            for i in range(0, 1600):
                if(ytrain[i] == 0):
                    xi = np.array(xtrain[i])
                    negCenter += xi
                    negCount += 1
                else:
                    xi = np.array(xtrain[i])
                    posCenter += xi
                    posCount += 1
            negCenter /= negCount
            posCenter /= posCount
            for i in range(0, 400):
                dneg = scipy.spatial.distance.minkowski(x3[i], negCenter, p)
                dpos = scipy.spatial.distance.minkowski(x3[i], posCenter, p)
                if dneg == dpos:
                    tie += 1
                if dneg < dpos:
                    if y3[i] == 0:
                        tn += 1
                    else:
                        fn += 1
                else:
                    if y3[i] == 1:
                        tp += 1
                    else:
                        fp += 1
        else:
            d = scipy.spatial.distance.cdist(x3, xo, metric)
            d = np.delete(d, np.s_[800:1200], axis=1)
            yy = np.delete(yo, np.s_[800:1200], axis=0)
            for i in range(0, 400):
                sortedd = np.argsort(d[i])
                positive = 0
                for j in range(0, k):
                    positive += yy[sortedd[j]]
                positive /= k
                if positive == .5:
                    tie += 1
                if positive >= .5:
                    if y3[i] == 1:
                        tp += 1
                    else:
                        fp += 1
                else:
                    if y3[i] == 1:
                        fn += 1
                    else:
                        tn += 1
    if a == 3:
        if k == 0:
            xtrain = np.delete(xo, np.s_[1200:1600], axis=0)
            ytrain = np.delete(yo, np.s_[1200:1600])
            negCenter = 0
            posCenter = 0
            negCount = 0
            posCount = 0
            for i in range(0, 1600):
                if(ytrain[i] == 0):
                    xi = np.array(xtrain[i])
                    negCenter += xi
                    negCount += 1
                else:
                    xi = np.array(xtrain[i])
                    posCenter += xi
                    posCount += 1
            negCenter /= negCount
            posCenter /= posCount
            for i in range(0, 400):
                dneg = scipy.spatial.distance.minkowski(x4[i], negCenter, p)
                dpos = scipy.spatial.distance.minkowski(x4[i], posCenter, p)
                if dneg == dpos:
                    tie += 1
                if dneg < dpos:
                    if y4[i] == 0:
                        tn += 1
                    else:
                        fn += 1
                else:
                    if y4[i] == 1:
                        tp += 1
                    else:
                        fp += 1
        else:
            d = scipy.spatial.distance.cdist(x4, xo, metric)
            d = np.delete(d, np.s_[1200:1600], axis=1)
            yy = np.delete(yo, np.s_[1200:1600], axis=0)
            for i in range(0, 400):
                sortedd = np.argsort(d[i])
                positive = 0
                for j in range(0, k):
                    positive += yy[sortedd[j]]
                positive /= k
                if positive == .5:
                    tie += 1
                if positive >= .5:
                    if y4[i] == 1:
                        tp += 1
                    else:
                        fp += 1
                else:
                    if y4[i] == 1:
                        fn += 1
                    else:
                        tn += 1
    if a == 4:
        if k == 0:
            xtrain = np.delete(xo, np.s_[1600:2000], axis=0)
            ytrain = np.delete(yo, np.s_[1600:2000])
            negCenter = 0
            posCenter = 0
            negCount = 0
            posCount = 0
            for i in range(0, 1600):
                if(ytrain[i] == 0):
                    xi = np.array(xtrain[i])
                    negCenter += xi
                    negCount += 1
                else:
                    xi = np.array(xtrain[i])
                    posCenter += xi
                    posCount += 1
            negCenter /= negCount
            posCenter /= posCount
            for i in range(0, 400):
                dneg = scipy.spatial.distance.minkowski(x5[i], negCenter, p)
                dpos = scipy.spatial.distance.minkowski(x5[i], posCenter, p)
                if dneg == dpos:
                    tie += 1
                if dneg < dpos:
                    if y5[i] == 0:
                        tn += 1
                    else:
                        fn += 1
                else:
                    if y5[i] == 1:
                        tp += 1
                    else:
                        fp += 1
        else:
            d = scipy.spatial.distance.cdist(x5, xo, metric)
            d = np.delete(d, np.s_[1600:2000], axis=1)
            yy = np.delete(yo, np.s_[1600:2000], axis=0)
            for i in range(0, 400):
                sortedd = np.argsort(d[i])
                positive = 0
                for j in range(0, k):
                    positive += yy[sortedd[j]]
                positive /= k
                if positive == .5:
                    tie += 1
                if positive >= .5:
                    if y5[i] == 1:
                        tp += 1
                    else:
                        fp += 1
                else:
                    if y5[i] == 1:
                        fn += 1
                    else:
                        tn += 1
    print("Fold: ", a + 1)
    print("TP:", tp, "FP:", fp, "TN:", tn, "FN:", fn)
    if tp + fp == 0 or tn + fn == 0 or tp + fn == 0 or tn + fp == 0:
        print("Divide by 0 error. Only computing accuracy")
        accuracy = (tp + tn) / (tp + tn + fp + fn)
        print("    Accuracy   ", accuracy)
        avgAccuracy += accuracy
    else:
        precisionP = tp / (tp + fp)
        precisionN = tn / (tn + fn)
        recallP = tp / (tp + fn)
        recallN = tn / (tn + fp)
        accuracy = (tp + tn) / (tp + tn + fp + fn)
        precision = (precisionP + precisionN) / 2
        recall = (recallP + recallN) / 2
        print("    Precision+ ", precisionP)
        print("    Precision- ", precisionN)
        print("    Recall+    ", recallP)
        print("    Recall-    ", recallN)
        print("    Accuracy   ", accuracy)
        print("    Precision  ", precision)
        print("    Recall     ", recall)
        avgPrecisionP += precisionP
        avgPrecisionN += precisionN
        avgRecallP += recallP
        avgRecallN += recallN
        avgAccuracy += accuracy
        avgPrecision += precision
        avgRecall += recall
print("Average performance measures")
print("    Precision+ ", avgPrecisionP / 5)
print("    Precision- ", avgPrecisionN / 5)
print("    Recall+    ", avgRecallP / 5)
print("    Recall-    ", avgRecallN / 5)
print("    Accuracy   ", avgAccuracy / 5)
print("    Precision  ", avgPrecision / 5)
print("    Recall     ", avgRecall / 5)
if tie != 0:
    print("Ties: ", tie)
sys.exit(0)
