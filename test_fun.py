def solution(ranks):
    listset = list(set(ranks))
    soldiers_father = []
    counts = 0
    for i in listset:
        if i + 1 in ranks:
            print(i, i + 1)
            soldiers_father.append(i)
        for i in soldiers_father:
            counts += 1


# solution([3, 4, 3, 0, 2, 2, 3, 0, 0])

# ranks = [3, 4, 3, 0, 2, 2, 3, 0, 0] r5
b =  [4, 4, 3, 3, 1, 0]
a = list(set(b))
c, d = {}, []
e = 0
for i in a:
    if i + 1 in b:
        print(i, i + 1)
        d.append(i)
        print('d',d)
    for i in d:
        c[i] = b.count(i)
        print('why',e)
        e += 1
f=0
for key,v in c.items():
    f +=v
print(c, e,f)
