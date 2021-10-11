with open("nginx_logs.txt") as f:
    data=[]
    spammer={}

    for line in f:
        new_line=line.split(' ')
        data.append((new_line[0], new_line[5].replace('"', ""), new_line[6]))
        spam=new_line[0]
        spammer.setdefault(spam, 0)
        spammer[spam]+=1
spammer=sorted(spammer.items(), key=lambda x: x[1], reverse=True)
print(spammer[:5])