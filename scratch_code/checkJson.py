import json, os, csv
cwd = os.getcwd()
json_review_list = []
json_businessid_list = []
json_business_list = []

with open(os.path.join(cwd, 'scratch_academic_dataset_business.json'), 'r',encoding='utf-8') as f:
    jfile = {}
    for line in f:
        while True:
            try:
                jfile = json.loads(line)
                break
            except ValueError:
                try:
                    line += next(f)
                except StopIteration:
                    print('warning: exceptionOut, something is wrong in the json')
                    break
        # do something with jfile
        print(jfile)
        print(type(jfile))
        try:
            json.loads(json.dumps(jfile))
            print('yay')
            print(jfile)
        except ValueError:
            print('nope')
f.close()