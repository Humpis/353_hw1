import os
import sys
import json
import string
import re
import numpy as np
from numpy import linalg as la
import math
path_neg = os.getcwd() + '/review_polarity/txt_sentoken/neg/'
path_pos = os.getcwd() + '/review_polarity/txt_sentoken/pos/'
trainingStop = 500
counter = 0
words = {}
y = np.zeros((2000), dtype=np.int)
for i in range(1000, 2000):
    y[i] = 1
x = []
k = -1
metric = -1

if(len(sys.argv) == 5):
    if sys.argv[2] == "--punct":
        print("Checking for punctuation-included words file...")
        if os.path.isfile(os.getcwd() + '/punctWords.txt'):
            print("Punctiation-included words file already exists. Loading...")
            with open(os.getcwd() + '/punctWords.txt', 'r') as f:
                try:
                    words = json.load(f)
                    # if the file is empty the ValueError will be thrown
                except ValueError:
                    words = {}
                    print("File is empty error")
                    sys.exit(0)
        else:
            print("Punctiation-included words file not found. Generating...")
            for filename in os.listdir(path_neg):
                with open(path_neg + filename, 'r') as f:
                    for line in f:
                        for word in line.split():
                            if word not in words:
                                words[word] = counter
                                counter += 1
            for filename in os.listdir(path_pos):
                with open(path_pos + filename, 'r') as f:
                    for line in f:
                        for word in line.split():
                            if word not in words:
                                words[word] = counter
                                counter += 1
            words_file = open('punctWords.txt', 'w')
            json.dump(words, words_file)
            print("Generation sucsessful")
    elif sys.argv[2] == "--nopunct":
        print("Checking for punctuation-excluded words file...")
        if os.path.isfile(os.getcwd() + '/nopunctWords.txt'):
            print("Punctiation-excluded words file already exists. Loading...")
            with open(os.getcwd() + '/nopunctWords.txt', 'r') as f:
                try:
                    words = json.load(f)
                    # if the file is empty the ValueError will be thrown
                except ValueError:
                    words = {}
                    print("File is empty error")
                    sys.exit(0)
        else:
            print("Punctiation-excluded words file not found. Generating...")
            for filename in os.listdir(path_neg):
                with open(path_neg + filename, 'r') as f:
                    for line in f:
                        for word in line.split():
                            newWord = re.sub(
                                '[' + string.punctuation + ']', '', word)
                            if newWord != '':
                                if word not in words:
                                    words[word] = counter
                                    counter += 1
            for filename in os.listdir(path_pos):
                with open(path_pos + filename, 'r') as f:
                    for line in f:
                        for word in line.split():
                            newWord = re.sub(
                                '[' + string.punctuation + ']', '', word)
                            if newWord != '':
                                if word not in words:
                                    words[word] = counter
                                    counter += 1
            words_file = open('nopunctWords.txt', 'w')
            json.dump(words, words_file)
            print("Generation sucsessful")
    else:
        print("Invalid argument")
        sys.exit(0)
else:
    print("Invalid arguments")
    sys.exit(0)
# Now make the matrix for binary or frequency
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
    sys.exit(0)

if sys.argv[3][:4] == '--k=':
    try:
        k = int(sys.argv[3][4:])
    except ValueError:
        print("Error: K must be an integer")
        sys.exit(0)
else:
    print("Invalid argument")
    sys.exit(0)

if sys.argv[4] == '--metric=euclidean':
    metric = 0
elif sys.argv[4] == '--metric=manhattan':
    metric = 1
else:
    print("Invalid argument")
    sys.exit(0)

# x1 = np.zeros((400, len(words)), dtype=np.int)
# x2 = np.zeros((400, len(words)), dtype=np.int)
# x3 = np.zeros((400, len(words)), dtype=np.int)
# x4 = np.zeros((400, len(words)), dtype=np.int)
# x5 = np.zeros((400, len(words)), dtype=np.int)
# y1 = np.zeros((400, 1), dtype=np.int)
# y2 = np.zeros((400, 1), dtype=np.int)
# y3 = np.zeros((400, 1), dtype=np.int)
# y4 = np.zeros((400, 1), dtype=np.int)
# y5 = np.zeros((400, 1), dtype=np.int)
xo = x.copy()
yo = y.copy()
# print(x)
for i in range(1, 1000):
    if i % 2 == 0:
        continue
    xo[i] = x[i + 999]
    yo[i] = y[i + 999]
    xo[i + 999] = x[i]
    yo[i + 999] = y[i]
# print(yo[390:400])

# for i in range(0, 400):
#     x1[i] = xo[i]
#     x2[i] = xo[i + 400]
#     x3[i] = xo[i + 800]
#     x4[i] = xo[i + 1200]
#     x5[i] = xo[i + 1600]
#     y1[i] = yo[i]
#     y2[i] = yo[i + 400]
#     y3[i] = yo[i + 800]
#     y4[i] = yo[i + 1200]
#     y5[i] = yo[i + 1600]
# print(x1)
# print(y2)
# print(len(x1))
# print(x2)

# for i in range(0, 400):
#     d = np.zeros((1600, 1))
#     for j in range(0, 400):
#         sumofs = 0
#         for q in range(0, len(words)):
#             sumofs = math.pow(x1[i][q] - x2[j][q], 2)   # change
#         d[j] = math.sqrt(sumofs)
#     for j in range(0, 400):
#         sumofs = 0
#         for q in range(0, len(words)):
#             sumofs = math.pow(x1[i][q] - x3[j][q], 2)   # change
#         d[j + 400] = math.sqrt(sumofs)
#     for j in range(0, 400):
#         sumofs = 0
#         for q in range(0, len(words)):
#             sumofs = math.pow(x1[i][q] - x4[j][q], 2)   # change
#         d[j + 800] = math.sqrt(sumofs)
#     for j in range(0, 400):
#         sumofs = 0
#         for q in range(0, len(words)):
#             sumofs = math.pow(x1[i][q] - x5[j][q], 2)   # change
#         d[j + 1200] = math.sqrt(sumofs)
#     sortedd = np.argsort(d)
#     for j in range(0, k):
#         print(k)

print('about the do this shit...')
for a in range(0, 5):
    # print(a)
    for i in range(a * 400, a * 400 + 400):
        # print(i)
        d = np.zeros((2000), dtype=np.float)
        # print(d)
        for j in range(0, 2000):
            if (j >= a * 400) and (j < a * 400 + 400):
                continue

            # sumofs = 0
            # for q in range(0, len(words)):
            #     sumofs += math.pow(xo[i][q] - xo[j][q], 2)
            # d[j] = math.sqrt(sumofs)
            # print(xo[i])
            xi = np.array(xo[i])
            # print(xi)
            xj = np.array(xo[j])
            d[j] = la.norm(xi - xj)
            # print(d[j])

            # print(d[j])
        # print(d)
        # print(np.argsort(d))
        sortedd = np.argsort(d)
        # print(d)
        positive = 0
        for j in range(0, k):
            # print(sortedd[j + 400])
            # print(sortedd)
            # print(d[sortedd])
            # print(sortedd[395: 405])
            # print(len(sortedd))
            positive += yo[sortedd[j + 400]]
            # print(yo[sortedd[j + 400]])
        positive /= k
        print(positive)
        print(yo[i])
