NAME
    knn - Compute 5-fold cross validation and get statistics for K-Nearest-Neighbor or Nearest-Centroid algorithm.

SYNOPSIS
    python knn.py [--binary|--frequency] [--punct|--nopunct] [--k=NUM|--k=0] [--metric=euclidean|manhattan] [--stopwords|--nostopwords]

DESCRIPTION
    Compute 5-fold cross validation and get statistics for K-nearest neighbor or Nearest-Centroid algorithm. Set --k=0 for Nearest-Centroid.
    
    Options:
        --binary            use binary representation of feature vectors	
        --frequency         use frequency represenation of feature vecotrs
        --punct             count punctuation as features
        --nopunct           do not count puncation as features
        --k=NUM             NUM is the number of nearest neighbors to check
        --k=0               Performs Nearest-Centroid Classification instead of K-Nearest-Neighbor
        --metric=euclidean  use euclidean distance to compute nearest neighbors
        --metric=manhattan  use manhattan distance to compute nearest niehgbors
        --stopwords         count stops words as features
        --nostopwords       ignore stop words as features
    
    Exit Status:
    Returns 0 on sucess, 1 on error.

KNOWN BUGS
    manhattan/binary combination with Nearest-Centroid classifies everything as negative
    manhattan/frequency/nostopwords/nopunct combination with Nearest-Centroid classifies almost everything as negative
    manhattan distance in general doesn't classify things well, tending to think everything is negative

IMPLEMENTATION
    Python 3.6.0
    Numpy 1.11.3
    Scipy 0.18.1
