import os
import csv

cwd = os.getcwd()

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
