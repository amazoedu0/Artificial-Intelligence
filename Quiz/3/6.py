data= {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
i=1
for _ in sorted(data.items(), key=lambda x: x[1], reverse=True):
    print(f"{i} : {_[0]} {_[1]}")
    i+=1
    if i >3:
        break