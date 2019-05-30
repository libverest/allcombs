# indexing from 0 - 7 (8) with list lenght 8 [0,0,0,0,0,0,0,0] - [7,7,7,7,7,7,7,7]
#infinite counter version
#it probably has to be a generator

def allcombs(indcount, idxlim, iterstop = 0, fromcount, tocount):
    if iterstop == 0:
        for n in range(1, indcount + 1):
            iterstop += (idxlim + 1)** n
    realim = [idxlim] * indcount
    spaces = 0
    n = indcount * [-1]
    counter = 1
    reset = False
    while True:
        for i in range(spaces):
            if n[-i - 1] == idxlim + 1:
                n[-i - 1] = 0
                n[-i - 2] += 1
                reset = True
                
        if n == realim or counter == iterstop:
            yield listremove(n, -1)
            break        
        if listremove(n, -1) != [] and reset == False:
            yield listremove(n, -1)
            counter += 1
        if reset == False:
            n[-1] += 1
        else:
            reset = False
        spaces = len(listremove(n, -1))

                     
def listremove(l, obj):
    dl = []  
    for g in l:
        if g != -1:
            dl.append(g)
    return dl
