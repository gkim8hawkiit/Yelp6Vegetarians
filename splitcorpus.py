import os

cwd = os.getcwd()

lines_per_file = 15000
smallfile = None
with open(os.path.join(cwd, 'big_json_big_corpus', 'corpus_1vote_textEncoding_filter.txt'),'r') as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = os.path.join(cwd, 'corpus_split','small_file_{}.txt').format(lineno + lines_per_file)
            smallfile = open(small_filename, 'w')
        smallfile.write(line)
    if smallfile:
        smallfile.close()