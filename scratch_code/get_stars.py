import json
import os
cwd = os.getcwd()
json_review_list = []


exceptionOut = open(os.path.join(cwd,'ExceptionOutput','load_review_1vote_textEncoding_filter_json.txt'), 'w')
with open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset',
                       'dataset_review_1vote_textEncoding_filter.json'), 'r') as f:
    jfile = {}
    for line in f:
        # if len(json_review_list) > 10:
        #     break
        while True:
            try:
                jfile = json.loads(line)
                break
            except ValueError:
                # Not yet a complete JSON value
                try:
                    line += next(f)
                except StopIteration:
                    exceptionOut.write(str(line))
                    print('warning: exceptionOut, something is wrong in the json')
                    break
        # do something with jfile
        if jfile:
            json_review_list.append(jfile)
exceptionOut.close()
f.close()
countratings = []
ratingscsv = open(os.path.join(cwd, 'ratings.csv'), 'w')
print(str(json_review_list[0]))
print(str(json_review_list[len(json_review_list)-1]))
count = 0
othercount = 0
for i in range(0, len(json_review_list)):
    if json_review_list[i]['type'] == 'review':
        stars = json_review_list[i]['stars']
        if stars:
            ratingscsv.write(str(stars) + '\n')
            countratings.append(stars)
            othercount += 1
        else:
            count += 1
ratingscsv.close()
print(count) #26
print(othercount) # 809680
print(len(countratings))