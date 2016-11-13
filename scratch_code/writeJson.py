import os
import io, json

cwd = os.getcwd()


with open(os.path.join(cwd, 'data.json'), 'r', encoding='utf-8') as f:
    g = open(os.path.join(cwd, 'datag.json'), 'w', encoding='utf-8')
    stopFlag = False
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
                    print(line)
                    stopFlag = True
                    break
        if stopFlag:
            break
        try:
            for i in range(5):
                g.write(json.dumps(jfile, ensure_ascii=False))
                g.write('\n')
        except ValueError:
            pass

linewrong = ''
with open(os.path.join(cwd, 'scratch_academic_dataset_business.json'), 'r', encoding='utf-8') as f:
    stopFlag = False
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
                    print(line)
                    stopFlag = True
                    break
        if stopFlag:
            break
        print(jfile)
        try:
            json.loads(json.dumps(jfile))
            print('yay\n********************\n**************')
        except ValueError:
            print('nope')
