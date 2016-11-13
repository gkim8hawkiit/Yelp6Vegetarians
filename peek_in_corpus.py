import json, os, csv
cwd = os.getcwd()

with open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset', 'corpus_1vote_filter.txt')) as f:
    head = [next(f) for x in range(2)]
print(head)
f.close()

with open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset', 'dataset_review_1vote_textEncoding_filter.json')) as f:
    head = [next(f) for y in range(2)]
print(head)
f.close()
with open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset', 'corpus_1vote_filter.txt')) as f:
  last = None
  for line in (line for line in f if line.rstrip('\n')):
    last = line
f.close()
print(last)