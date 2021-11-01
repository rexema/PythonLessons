import os
files=[]
my_dir="my project"

for r,d,f in os.walk(my_dir):
   for file in f:
        f_path=os.path.join(r,file)
        files.append(os.stat(f_path).st_size)
max_size=max(files)


i=1
final_dic={}
for _ in range(len(str(max_size))):
    i*=10
    final_dic[i]=0

for file in files:
    final_dic[10**len(str(file))]+=1

print(final_dic)


