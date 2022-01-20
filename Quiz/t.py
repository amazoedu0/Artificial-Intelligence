import random
ch=[2,4,4,5,2,4,4,2,4,3,4]
high=[]
for i in range(1,len(ch)+1  ):
    sum=0
    for j in range(0,i):
        sum+=ch[j]
    high.append(sum)
lower=[]
lens=len(ch)
for i in range(0,len(ch)):
    sum=0
    for j in range(0,i):
        sum+=ch[j]
    lower.append(sum)

for j in range(0,11):
    test=lower[j]
    highs=high[j]
    print(f"{test},{highs}")
    choice = random.randint(test,highs)
    choice = random.randint(test,highs)
    