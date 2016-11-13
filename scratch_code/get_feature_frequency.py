import numpy as np
import os
from sklearn.feature_extraction.text import CountVectorizer

f = open(os.path.join(cwd,'corpus_split_bak', 'small_file_150000.txt'))

cwd = os.getcwd()
# document = os.path.join('yelp_dataset_challenge_academic_dataset', 'corpus_1vote_filter.txt')#[Huge amount of data around 7MB] # ['john is a guy', 'person guy']
vectorizer = CountVectorizer(ngram_range=(1, 3), max_features=200)
# stop_words='english', max_features=200

# Don't need both X and transformer; they should be identical
X = vectorizer.fit_transform(document)
matrix_terms = np.array(vectorizer.get_feature_names())

# Use the axis keyword to sum over rows
matrix_freq = np.asarray(X.sum(axis=0)).ravel()
final_matrix = np.array([matrix_terms,matrix_freq])
# matrixfile = open(os.path.join(cwd, 'final_matrix'), 'w')
# matrixfile.write(str(final_matrix))

np.savetxt(os.path.join(cwd,"uni_tri-gram_frequency.csv"), final_matrix, delimiter=",")
# EDIT: If you want a dictionary from term to frequency, try this after calling fit_transform:
#
# terms = vectorizer.get_feature_names()
# freqs = X.sum(axis=0).A1
# result = dict(zip(terms, freqs))

# Note that CountVectorizer can also take a file instead of a string and there's no need to read the whole file into memory. In code:

# import io
# from collections import Counter
#
# import numpy as np
# from sklearn.feature_extraction.text import CountVectorizer
#
# infile = '/path/to/input.txt'
#
# ngram_vectorizer = CountVectorizer(analyzer='word', ngram_range=(1, 1), min_df=1)
#
# with io.open(infile, 'r', encoding='utf8') as fin:
#     X = ngram_vectorizer.fit_transform(fin)
#     vocab = ngram_vectorizer.get_feature_names()
#     counts = X.sum(axis=0).A1
#     freq_distribution = Counter(dict(zip(vocab, counts)))
#     print (freq_distribution.most_common(10))


# from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer
# word_vectorizer = CountVectorizer(ngram_range=(1,2), analyzer='word')
# sparse_matrix = word_vectorizer.fit_transform(df['description'])
# frequencies = sum(sparse_matrix).toarray()[0]
# # pd.DataFrame(frequencies, index=word_vectorizer.get_feature_names(), columns=['frequency'])