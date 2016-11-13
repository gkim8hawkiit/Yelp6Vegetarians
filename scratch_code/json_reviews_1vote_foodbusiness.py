import json, os, csv # , io
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

cwd = os.getcwd()

with open(os.path.join(cwd, 'a0categories.csv'), 'r') as f:
    reader = csv.reader(f)
    restaurant_categories_list = list(reader)
    restaurant_categories_set = set(restaurant_categories_list[0])
    # for restaurantcategory in restaurant_categories_list[0]:
    #     restaurant_categories_set.add(restaurantcategory)
f.close()

json_businessid_list = []

exceptionOut = open(os.path.join(cwd,'ExceptionOutput', 'load_dataset_business_json.txt'), 'w')
businessIDcsv = open(os.path.join(cwd,'code_output','relevant_businessIDs_filter_step1.csv'),'w')
relevantBusinessJson1 = open(os.path.join(cwd,'big_json_big_corpus','relevant_businesses_filter_step1.json'),'w')
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
            if (not restaurant_categories_set.isdisjoint(categories_set)) and (jfile['business_id'] not in json_businessid_list):
                json_businessid_list.append(jfile['business_id'])
                businessIDcsv.write(jfile['business_id']+'\n')
                try:
                    relevantBusinessJson1.write(json.dumps(jfile, ensure_ascii=False))
                    relevantBusinessJson1.write('\n')
                except ValueError:
                    pass

relevantBusinessJson1.close()
businessIDcsv.close()
exceptionOut.close()

json_reviewText_list = []
starlist = []
useridlist = []
numwordsList = []

reviewRelevant1 = open(os.path.join(cwd, 'big_json_big_corpus', 'dataset_review_1vote_filter.json'),'w')
exceptionOut = open(os.path.join(cwd, 'ExceptionOutput', 'load_dataset_review_json.txt'),'w')
exceptionOut2 = open(os.path.join(cwd, 'ExceptionOutput', 'write_review_text.txt'),'w')
gi2= []
gi2e= []
exceptionOut3 = open(os.path.join(cwd, 'ExceptionOutput', 'write_stars_review_length.txt'),'w')
gi3= []
gi3e= []
exceptionOut4 = open(os.path.join(cwd, 'ExceptionOutput', 'write_userID.txt'),'w')
gi4= []
gi4e= []
# exceptionOut5 = open(os.path.join(cwd, 'ExceptionOutput', 'dump_review_json.txt'),'w')
gi5= []
gi5e= []
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
        if jfile['business_id'] in json_businessid_list and (jfile['votes']['useful'] >= 1):
            try:
                json_reviewText_list.append(jfile['text'])
                gi2.append(-1)
            except:
                exceptionOut2.write(jfile['text']+'\n')
                print('exceptionOut2\n')
                gi2e.append(1)
                continue
            try:
                words = jfile['text'].split()
                numwordsList.append(len(words))
                starlist.append(jfile['stars'])
                gi3.append(-1)
            except:
                exceptionOut3.write(str(jfile['stars'])+'\n')
                print('exceptionout3\n')
                gi3e.append(1)
            try:
                useridlist.append(jfile['user_id'])
                gi4.append(-1)
            except:
                exceptionOut4.write(jfile['user_id']+'\n')
                print('exceptionout4\n')
                gi4e.append(1)
            try:
                reviewRelevant1.write(json.dumps(jfile, ensure_ascii=False))
                reviewRelevant1.write('\n')
                gi5.append(-1)
            except:
                # print('exceptionout5\n')
                gi5e.append(1)

print('gi2sum '+str(sum(gi2)))
print('gi3sum '+str(sum(gi3)))
print('gi4sum '+str(sum(gi4)))
print('gi5sum '+str(sum(gi5)))
print('gi2esum '+str(sum(gi2e)))
print('gi3esum '+str(sum(gi3e)))
print('gi4esum '+str(sum(gi4e)))
print('gi5esum '+str(sum(gi5e)))

exceptionOut.close()
exceptionOut2.write(str(sum(gi2)+'\n'))
exceptionOut2.close()
exceptionOut3.write(str(sum(gi3)+'\n'))
exceptionOut3.close()
exceptionOut4.write(str(sum(gi4)+'\n'))
exceptionOut4.close()
# exceptionOut5.write(str(sum(gi5)+'\n'))
# exceptionOut5.close()
reviewRelevant1.close()
f.close()

print('number of instances (reviews): ' + str(len(json_reviewText_list)))
f = open(os.path.join(cwd, 'code_output', 'numwordsList.csv'),'w')
for number in numwordsList:
    f.write(str(number) + '\n')
f.close()

corpus = open(os.path.join(cwd, 'big_json_big_corpus', 'corpus_1vote_textEncoding_filter.txt'),'w')
useridcsv = open(os.path.join(cwd, 'code_output', 'filtered_UserId_list.csv'), 'w')
ratingscsv = open(os.path.join(cwd, 'code_output', 'ratings.csv'), 'w')

count, count1, count2 = 0, 0 , 0
exceptionCount,exceptionCount1,exceptionCount2 = 0, 0, 0
for i in range(0,len(json_reviewText_list)):
    try:
        corpus.write(json_reviewText_list[i] + '\n')
        count2 += 1
    except:
        exceptionCount2 += 1
        continue
    try:
        useridcsv.write(useridlist[i] + '\n')
        count1 += 1
    except:
        exceptionCount1 += 1
    try:
        ratingscsv.write(str(starlist[i]) + '\n')
        count += 1
    except:
        exceptionCount += 1

corpus.close()
useridcsv.close()
ratingscsv.close()

print(str(count2)+'\n')
print(str(count1)+'\n')
print(str(count)+'\n')
print(str(exceptionCount2)+'\n')
print(str(exceptionCount1)+'\n')
print(str(exceptionCount)+'\n')