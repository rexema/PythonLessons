
with open("nginx_logs.txt") as f:
    data=[]
    for line in f:
        new_line=line.split(' ')
        data.append((new_line[0], new_line[5].replace('"', ""), new_line[6]))
    print(data)











