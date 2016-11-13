import os

cwd = os.getcwd()
f = open(os.path.join(cwd,'infile'))
count = 0
for line in f:
    print(count)
    count += 1
    line += next(f)
    print(line)
    try:
        line = next(f)
    except StopIteration:
        print('except')
        print(line)
        print('break')

