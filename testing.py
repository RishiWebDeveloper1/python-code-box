
print("rishi is great")
i=0
while i!=100:
    i+=1

    imp=input("Enter your number: ")
# importing the os function 
    try:
        a=int(imp)
    except:
        pass
    
    if a==1:
        print("your are not so good!")
    elif(a==2):
        print('you are good')
    elif a==999:
        break
    else:
        print('go done')

