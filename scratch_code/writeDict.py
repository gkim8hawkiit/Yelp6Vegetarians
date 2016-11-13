import os
cwd = os.getcwd()
with open(os.path.join(cwd,'dictwrite.txt'),'w') as f:
    d = {'a':1}
    f.write(str(d))
    print(str(d))