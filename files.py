import os

print(os.chdir('android'))

i=0
while i<=1000:
    os.chdir(f'.hacking document{i}')
    os.remove(f'hacking.txt')
    os.chdir('../')
    os.rmdir(f'.hacking document{i}')
    i=i+1

# i=0
# while i<=100:
#     os.chdir(f'rishi{i}')
#     os.rmdir(f'rishi{i}.py')
#     open(f'rishi{i}.py',"w")
#     os.chdir('../')
#     i=i+1

#open("demo.py","w")

#os.remove("demo")