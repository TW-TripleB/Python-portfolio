import random
def lottery():
    dicT=[]
    dicT2=[]
    while len(dicT)<6:
        Ran=random.randint(1,38)
        if Ran not in dicT:
            dicT.append(Ran)
            num=sorted(dicT)
    while len(dicT2)!=1:
        R=random.randint(1,8)
        dicT2.append(R)
    return num,dicT2
