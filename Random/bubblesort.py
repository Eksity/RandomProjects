import random
randl = set([])
while len(randl) != 10:
    randl.add(random.randrange(1, 50))
randl = list(randl)
correct = sorted(randl)
cycles = 0

def sort(lis):
    v = 0
    for x in range(len(lis)-1):
        y = lis[x]
        z = lis[x+1]
        if y > z:
            lis.remove(y)
            lis.insert(x+1, y)
            v = 1
    return v
        
if __name__ == "__main__":          
    while True:
        x = sort(randl)
        print(randl)
        if not x:
            print("Done!")
            break
        cycles += 1

