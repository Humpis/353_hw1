import os
import sys
import json
import string
import re
path_neg = os.getcwd() + '/review_polarity/txt_sentoken/neg/'
path_pos = os.getcwd() + '/review_polarity/txt_sentoken/pos/'
trainingStop = 500
words = {}

if(len(sys.argv) > 2):
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
                            words[word] = 0
            for filename in os.listdir(path_pos):
                with open(path_pos + filename, 'r') as f:
                    for line in f:
                        for word in line.split():
                            words[word] = 0
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
                                words[newWord] = 0
            for filename in os.listdir(path_pos):
                with open(path_pos + filename, 'r') as f:
                    for line in f:
                        for word in line.split():
                            newWord = re.sub(
                                '[' + string.punctuation + ']', '', word)
                            if newWord != '':
                                words[newWord] = 0
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
    print("bin")
elif sys.argv[1] == "--frequency":
    print("freq")
else:
    print("Invalid argument")
