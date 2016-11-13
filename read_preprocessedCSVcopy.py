import os
import csv
import matplotlib.pyplot as plt
# from statistics import *
import numpy as np
import glob
from sklearn.feature_extraction.text import CountVectorizer

cwd = os.getcwd()

corpuscsv = open(os.path.join(cwd, 'Data','corpus_1vote_textEncoding_filter.csv'))
reader = csv.reader(corpuscsv)
corpusList = list(reader)
corpuscsv.close()

numwordf = open(os.path.join(cwd, 'Data','numwordsList.csv'))
readernumword = csv.reader(numwordf)
numwordsList = list(readernumword)
intnumwordsList = list(map((lambda s: int(s[0])),numwordsList))
numwordf.close()

ratingsf = open(os.path.join(cwd, 'Data','ratings.csv'))
readerratings = csv.reader(ratingsf)
ratingsList = list(readerratings)
intstarlist = list(map((lambda s: int(s[0])), ratingsList))
ratingsf.close()

print('number of instances (reviews): ' + str(len(corpusList))+'\n')
print('the instances are text data, and the features are unigram, bigrams and trigrams.\n')
print('Only the top 100 are printed.\n')

######################################################################
# split massive corpus into tiny pieces
###################################################################
lines_per_file = 15000
smallfile = None
with open(os.path.join(cwd, 'Data', 'corpus_1vote_textEncoding_filter.txt'),'r') as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = os.path.join(cwd, 'Data','small_file_{}.txt').format(lineno + lines_per_file)
            smallfile = open(small_filename, 'w')
        smallfile.write(line)
    if smallfile:
        smallfile.close()

###################################################################################
# Use count vectorizer on each piece
###################################################################################
smallfile_list = glob.glob(os.path.join(cwd, 'Data','small_file_*.txt'))
count = 0
for smallfile in smallfile_list:
    f = open(smallfile)
    cv = CountVectorizer(ngram_range=(1, 3), stop_words='english', max_features=300,strip_accents='unicode',
                         decode_error='ignore')

    X = cv.fit_transform(f)
    matrix_terms = np.array(cv.get_feature_names())

    # Use the axis keyword to sum over rows
    matrix_freq = np.asarray(X.sum(axis=0)).ravel()
    final_matrix = np.array([matrix_terms,matrix_freq])
    final_matrixlist = final_matrix.tolist()
    f.close()
    with open(os.path.join(cwd, 'Data','small_file_'+str(count)+'.csv'), 'w') as outfile:
        for data_slice in final_matrixlist:
            for item in data_slice:
                outfile.write(item+',')
            # Writing out a break to indicate different slices...
            outfile.write('\n')
    count+=1
    outfile.close()

###############################################################################
# combine the frequencies of the n-grams across the corpus pieces
#################################################################################
smallfile_list = glob.glob(os.path.join(cwd, 'Data','small_file_*.csv'))
count = 0
featurefrequencydict = {}
for smallfile in smallfile_list:
    f = open(smallfile)
    reader = csv.reader(f)
    list_list = list(reader)
    featurelista = list_list[0]
    frequencylista = list_list[1]
    # try:
    #     d = []
    #     featurefrequencydicta = {d[0]:int(d[1]) for d in zip(featurelista,frequencylista)}
    # except:
    featurefrequencydicta = {}
    for d in zip(featurelista,frequencylista):
        if (d[0] != '' and  d[1] != ''):
            featurefrequencydicta[d[0]] = int(d[1])
    for d in featurefrequencydicta.items():
        if d[0] not in featurefrequencydict.keys():
            featurefrequencydict[d[0]]=0
        featurefrequencydict[d[0]]=featurefrequencydict[d[0]]+d[1]
    f.close()

outfile = open(os.path.join(cwd,'featurefrequency.csv'),'w')

list_key_value = [[d[0],d[1]] for d in featurefrequencydict.items()]
list_key_value.sort(key=lambda x: x[1],reverse=True)
for i in range(0,100):
    if i < 99:
        outfile.write(list_key_value[i][0]+',')
    if i == 99:
        outfile.write(list_key_value[i][0]+'\n')
for i in range(0,100):
    if i < 99:
        outfile.write(str(list_key_value[i][1])+',')
    if i == 99:
        outfile.write(str(list_key_value[i][1]))
outfile.close()


#############################################################################
# print feature frequencies
##################################################################
with open(os.path.join(cwd,'featurefrequency.csv'), 'r') as ff:
    readerff = csv.reader(ff)
    ff_list = list(readerff)
ff.close()
ffzip = zip(ff_list[0],ff_list[1])
for item in ffzip:
    print(item[0]+": "+item[1])

###############################################################################
# I wanted to see the histogram of the length of reviews for extra visualization.
#
# plot histogram of length of reviews (length as in number of whitespace delimited alpha-numeric characters)
###############################################################################
hist, bins = np.histogram(intnumwordsList, bins=13)
width = 0.8 * (bins[1] - bins[0])
# width = 28
# bins = [1, 41, 81, ... 1041]
center = (bins[:-1] + bins[1:]) / 2
# center = [21, 61, 101, ..., 1021]
fig1, ax1 = plt.subplots()
ax1.bar(center, hist, align='center', width=width)
ax1.set_title('Word Length Histogram of Reviews')
wordnum = range(1,1441, 80)
ax1.set_xticks(bins)
ax1.set_xticklabels(labels=wordnum, rotation=45, rotation_mode="anchor", ha="right")
plt.savefig(os.path.join(cwd, 'LengthReview_Histogram'))
plt.close()

##############################################################################
# print statistics
##############################################################################
starmean = sum(intstarlist)/len(intstarlist)
starvariance = np.var(intstarlist)
print("Ratings Mean: {:.2f}, Variance: {:.2f}".format(starmean, starvariance))


##############################################################################
# plot histogram of ratings
##############################################################################
hist, bins = np.histogram(intstarlist, bins=8)
width = 0.8 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
fig, ax = plt.subplots()
plt.bar(center, hist, align='center', width=width)
ax.set_title('Histogram of Ratings')
numbers = range(2,11)
numbers2 = []
for n in numbers:
    numbers2.append(n/2)
ax.set_xticks(numbers2)
ax.set_xticklabels(['1', '1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5'], rotation=45, rotation_mode="anchor",
                   ha="right")
plt.savefig(os.path.join(cwd, 'Ratings_Histogram'))
plt.show()
plt.close()

#####################################################################################
#plot boxplot of ratings
#####################################################################################
fig2, ax2 = plt.subplots()
plt.boxplot(intstarlist, notch=True, patch_artist=True)
ax2.set_title('BoxPlot of Ratings')
plt.savefig(os.path.join(cwd, 'Ratings_BoxPlot'))
plt.show()
plt.close()
