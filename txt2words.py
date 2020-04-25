f1 = open('./text/5600.txt','r')
f2 = open('words.txt','w')
c=0
for i in f1:
    j = i.split(' ')
    print(j)
    for k in j:
        if c>878:
            break
        else:
            if k=='\n':
                continue
            if k[-1]=='\n':
                print(k[:-1])
                f2.write(k[:-1]+'\n')
                c=c+1
            else:
                f2.write(k+'\n')
                c=c+1
print(c)