for i in range(5):
    try:
        # print(i)
        f.write(i)
    except:
        continue
    try:
        print('dont print this')
    except:
        pass


