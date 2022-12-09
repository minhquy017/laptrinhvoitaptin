from random import randint
def tap_tin5():
    dem=0
    f=input("nhập đường dẫn : ")
    x=[randint(-1000,1000) for i in range(1000)]
    print(x)
    for i in x:
        if dem <9:
            x1=open(f,"a")
            x1.write(str(x[i])+',')
            dem+=1
        else:
            x1=open(f,"a")
            x1.write(str(x[i])+"\n")
            dem=0
    x1.close()
    x1=open(f,"r")
    x2=x1.readlines()
    for i in x2:
        print(i.replace(",","\t"))
    x1.close()
tap_tin5()