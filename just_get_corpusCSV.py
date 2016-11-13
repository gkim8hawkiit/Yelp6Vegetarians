import json, os, csv # , io
# import numpy as np
# import matplotlib.pyplot as plt

cwd = os.getcwd()

with open(os.path.join(cwd, 'categories.csv'), 'r') as f:
    reader = csv.reader(f)
    restaurant_categories_list = list(reader)
    restaurant_categories_set = set(restaurant_categories_list[0])
    # for restaurantcategory in restaurant_categories_list[0]:
    #     restaurant_categories_set.add(restaurantcategory)
f.close()
businessid_list = []
exceptionOut = open(os.path.join(cwd,'ExceptionOutput', 'load_dataset_business_json.txt'), 'w')
with open(os.path.join(cwd, 'big_json_big_corpus',
                       'yelp_academic_dataset_business.json'), 'r') as f:
    stopFlag = False
    for line in f:
        jfile = {}
        while True:
            try:
                jfile = json.loads(line)
                break
            except ValueError:
                try:
                    line += next(f)
                except StopIteration:
                    exceptionOut.write(str(line)+'\n')
                    stopFlag = True
                    print('warning: exceptionOut, something is wrong in the json')
                    break
        # do something with jfile
        if stopFlag:
            break
        if jfile:
            categories_list = jfile['categories']
            categories_set = set(categories_list)
            # if the restaurant has at least one relevant category        AND   if we don't already have its ID stored
            if (not restaurant_categories_set.isdisjoint(categories_set)) and (jfile['business_id'] not in businessid_list):
                businessid_list.append(jfile['business_id'])
f.close()
exceptionOut.close()

exceptionOut = open(os.path.join(cwd, 'ExceptionOutput', 'load_dataset_review_json.txt'),'w')
reviewTextList = []
count = 0
anticount = 0
corpuscsv = open(os.path.join(cwd, 'big_json_big_corpus', 'corpus_1vote_textEncoding_filter.csv'),'w')
with open(os.path.join(cwd,'big_json_big_corpus', 'yelp_academic_dataset_review.json'),'r') as f:
    stopFlag = False
    for line in f:
        jfile = {}
        while True:
            try:
                jfile = json.loads(line)
                break
            except ValueError:
                try:
                    line += next(f)
                except StopIteration:
                    exceptionOut.write(str(line)+'\n')
                    stopFlag = True
                    print('warning: exceptionOut, something is wrong in the json\n')
                    break
        if stopFlag:
            break
        if jfile['business_id'] in businessid_list and (jfile['votes']['useful'] >= 1):
            try:
                corpuscsv.write(jfile['text']+'\n')
                reviewTextList.append(jfile['text']+'\n')
                count += 1
            except:
                anticount += 1
                continue
f.close()
exceptionOut.close()
corpuscsv.close()
print('number of instances (reviews): ' + str(len(reviewTextList)))