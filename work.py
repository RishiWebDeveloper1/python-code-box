import os

#os.mkdir('android')

spell=('hii'*10+'\n')*20000000
i=0
print(os.listdir())
# os.chdir("../")
# print(os.listdir())
# print(os.getcwd())
os.chdir("andr oid")
while i<=1:
    os.mkdir(f".hacking document{i}")
    os.chdir(f".hacking document{i}")
    file=open("hacking.txt",'w')
    file.write(spell)
    file.close()
    os.chdir("../")
    i=i+1

# i=('hii'*10+'\n')*10000000

# file=open('rishi.txt','w')
# file.write(i)
# file.close()