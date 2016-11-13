import os, glob, csv
cwd = os.getcwd()
smallfile_list = glob.glob(os.path.join(cwd,'small*.csv'))
count = 0
print(smallfile_list)
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
