NAME
    knn - Compute 5-fold cross validation and get statistics for K-nearest neighbor algorithm.

SYNOPSIS
    python knn.py [--binary|--frequency] [--punct|--nopunct] [--k=NUM] [--metric=euclidean|manhattan] [--stopwords|--nostopwords]

DESCRIPTION
    Compute 5-fold cross validation and get statistics for K-nearest neighbor algorithm.
    
    Options:
        --binary use binary representation of feature vectors	
        --frequency use frequency represenation of feature vecotrs
        --punct count punctuation as features
        --nopunct do not count puncation as features
        --k=NUM NUM is the number of nearest neighbors to check
        --metric=euclidean use euclidean distance to compute nearest neighbors
        --metric=manhattan use manhattan distance to compute nearest niehgbors
        --stopwords count stops words as features
        --nostopwords ignore stop words as features
    
    Exit Status:
    Returns 0 on sucess, 1 on error.

IMPLEMENTATION
    Python 3.6.0
    Numpy 1.11.3
