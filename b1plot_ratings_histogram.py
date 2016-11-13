import os
import matplotlib.pyplot as plt
import numpy as np
import csv
from statistics import *

cwd = os.getcwd()

f = open(os.path.join(cwd, 'code_output', 'numwordsList.csv'),'r')
reader = csv.reader(f)
numwordsList = list(reader)
f.close()

intnumwordsList = list(map((lambda s: int(s[0])),numwordsList))
# print(max(intnumwordsList))
# print(min(intnumwordsList))
# plot histogram of word counts of reviews
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
plt.savefig(os.path.join(cwd,'HistogramsAndWordcounts','LengthReview_Histogram'))
plt.close()

f = open(os.path.join(cwd, 'code_output', 'ratings.csv'),'r')
reader = csv.reader(f)
starlist = list(reader)
# print(starlist)
f.close()

intstarlist = list(map((lambda s: int(s[0])), starlist))
starmean = mean(intstarlist)
starvariance = variance(intstarlist)
print("Mean: {:.2f}, Variance: {:.2f}".format(starmean, starvariance))

# print statistics
hist, bins = np.histogram(intstarlist, bins=8)

# plot histogram of ratings
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
plt.savefig(os.path.join(cwd, 'HistogramsAndWordcounts', 'Ratings_Histogram'))
plt.show()
plt.close()

#plot boxplot of ratings
fig2, ax2 = plt.subplots()
plt.boxplot(intstarlist, notch=True, patch_artist=True)
ax2.set_title('BoxPlot of Ratings')
plt.savefig(os.path.join(cwd, 'HistogramsAndWordcounts', 'Ratings_BoxPlot'))
plt.show()
plt.close()

