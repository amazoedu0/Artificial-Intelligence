x = [1,2,3,4,5,6,7,8,9]
y = [6,2,5,8]


def inter(x,y):
    for z in y:
        if z in x:
            x.remove(z)
    return x

print(f"Lists : \nX: {x}\nY: {y}\nAfter removing intersection\nX : {inter(x,y)} ")