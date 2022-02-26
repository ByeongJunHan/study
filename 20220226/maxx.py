abc = ['10','3','12']
maxx = abc[0]
for i in range(len(abc)):
    print(i, maxx)
    if maxx <= abc[i]:
        maxx = abc[i]