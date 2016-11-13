import numpy as np
import os, glob
from sklearn.feature_extraction.text import CountVectorizer
cwd = os.getcwd()
smallfile_list = glob.glob(os.path.join(cwd,'corpus_split','small_file_*'))
count = 0
for smallfile in smallfile_list:
    f = open(smallfile)
    cv = CountVectorizer(ngram_range=(1, 3), max_features=300,strip_accents='unicode',decode_error='ignore')

    # Don't need both X and transformer; they should be identical
    X = cv.fit_transform(f)
    matrix_terms = np.array(cv.get_feature_names())

    # Use the axis keyword to sum over rows
    matrix_freq = np.asarray(X.sum(axis=0)).ravel()
    final_matrix = np.array([matrix_terms,matrix_freq])
    final_matrixlist = final_matrix.tolist()
    with file(os.path.join(cwd,'corpus_split','corpus_split_out','small_file_'+str(count)+'.csv'), 'w') as outfile:
        # Iterating through a ndimensional array produces slices along
        # the last axis. This is equivalent to data[i,:,:] in this case
        for data_slice in final_matrixlist:
            for item in data_slice:
                outfile.write(item+',')
            # Writing out a break to indicate different slices...
            outfile.write('\n')
    count+=1
    outfile.close()
