a = ['a', 4.0,'b' ]
count = 0
for i in range(len(a)):
    try:
        print('f'+a[i])
    except:
        count += 1
print(count)