memory=[]
pages=[1,3,2,4,1,2]
size=3
hit=miss=0
for page in pages:
    if page in memory:
        hit += 1
        print(f'HIT | PAGE {page}')
    else:
        miss += 1
        if len(memory) == size:
            memory.pop(0)
        memory.append(page)
        print(f'MISS | PAGE {page}')
    print(memory)
print(f'Hit Count: {hit}')
print(f'Miss Count: {miss}')