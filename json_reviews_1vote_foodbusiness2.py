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
            if (not restaurant_categories_set.isdisjoint(categories_set)) and (jfile['business_id'] not in businessid_list):
                businessid_list.append(jfile['business_id'])
                businessIDcsv.write(jfile['business_id']+'\n')
                try:
                    relevantBusinessJson1.write(json.dumps(jfile, ensure_ascii=False))
                    relevantBusinessJson1.write('\n')
                except ValueError:
                    pass
f.close()
relevantBusinessJson1.close()
businessIDcsv.close()
exceptionOut.close()
# print('number of relevant businesses: ' + str(len(businessid_list)))

exceptionOut = open(os.path.join(cwd, 'ExceptionOutput', 'load_dataset_review_json.txt'),'w')

useridcsv = open(os.path.join(cwd, 'code_output', 'filtered_UserId_list.csv'), 'w')
ratingscsv = open(os.path.join(cwd, 'code_output', 'ratings.csv'), 'w')
numwordscsv = open(os.path.join(cwd, 'code_output', 'numwordsList.csv'),'w')

reviewTextList = []
# reviewRelevant1 = open(os.path.join(cwd, 'big_json_big_corpus', 'dataset_review_1vote_filter.json'),'w')
count = 0
anticount = 0
worstcount1 = 0
worstcount2 = 0
worstcount3 = 0
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
                reviewTextList.append(jfile['text']+'\n')
                count += 1
            except:
                anticount += 1
                continue
            try:
                ratingscsv.write(str(jfile['stars']) + '\n')
            except:
                worstcount1 += 1
            try:
                words = jfile['text'].split()
                numwordscsv.write(str(len(words)) + '\n')
            except:
                worstcount2 += 1
            try:
                useridcsv.write(jfile['user_id'] + '\n')
            except:
                worstcount3 += 1
            # try:
            #     # reviewRelevant1.write(json.dumps(jfile, ensure_ascii=False))
            #     # reviewRelevant1.write('\n')
            # except:
            #     print('exception on json dump')
f.close()
# reviewRelevant1.close()
useridcsv.close()
ratingscsv.close()
numwordscsv.close()
exceptionOut.close()

print('number of instances (reviews): ' + str(len(reviewTextList)))
# print('number of instances (reviews) that could not be written to file: ' + str(anticount))
# print('number of missing ratings: ' + str(worstcount1))
# print('number of missing review lenth measurements: ' + str(worstcount2))
# print('number of missing userIDs: ' + str(worstcount3))

corpuscsv = open(os.path.join(cwd, 'big_json_big_corpus', 'corpus_1vote_textEncoding_filter.csv'),'w')
doublecheck = 0
for text in reviewTextList:
    try:
        corpuscsv.write(text + '\n')
        doublecheck +=1
    except:
        pass
corpuscsv.close()
if doublecheck != len(reviewTextList):
    print('warning, corpus is missing some reviews')

# corpus = open(os.path.join(cwd, 'big_json_big_corpus', 'corpus_1vote_textEncoding_filter.txt'),'w')
# doublecheck = 0
# for text in reviewTextList:
#     try:
#         corpus.write(text + '\n')
#         doublecheck +=1
#     except:
#         pass
# corpus.close()
# if doublecheck != len(reviewTextList):
#     print('warning, corpus is missing some reviews')