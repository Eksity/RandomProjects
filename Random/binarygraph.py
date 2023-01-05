import random
import sys
import os
def addnum(startnum, num, lis):
    index = lis.index(startnum)
    try:
        assert lis[0] != lis[1]
    except (AssertionError, IndexError):
        if num > lis[0]:
            lis.append(num)
            return (lis[0], num)
        else:
            lis.insert(0, num)
            return (num, lis[0])
        
    while True:
        if num < lis[index]:
            try:
                if num > lis[index-1]:
                    lis.insert(index, num)
                    return (lis[lis.index(num)+1], num)
            except IndexError:
                lis.insert(0, num)
                return (lis[lis.index(num)+1], num)
            if num < lis[index-1]:
                index -= 1
        elif num > lis[index]:
            try:
                if num < lis[index+1]:
                    lis.insert(index+1, num)
                    return (lis[lis.index(num)-1], num)
            except IndexError:
                lis.append(num)
                return (lis[lis.index(num)-1], num)
            if num > lis[index+1]:
                index += 1
        elif num == lis[index]:
            sys.exit("Duplicate number found")

    

if __name__ == '__main__':
    path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Folder', 'Tools', 'Node graph maker', 'python.dot')
    numbers = list(set([random.randrange(1, 50) for i in range(20)]))
    print(numbers)
    start = numbers[0]
    orderedlist = [numbers[0]]
    with open(path, 'w') as f:
        f.write("graph{\n")
    for a in numbers[1:]:
        h = addnum(start, numbers[numbers.index(a)], orderedlist)
        with open(path, 'a') as fi:
            fi.write(f"{h[0]} -- {h[1]}\n")
        print(orderedlist)
    with open(path, 'a') as fb:
        fb.write("}\n")   
        print(orderedlist)
        print(start)

    
   