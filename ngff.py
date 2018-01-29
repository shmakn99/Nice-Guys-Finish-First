import random as rd
import operator
import matplotlib.pyplot as plt
import itertools


def instance(nop):
    ret = []
    for i in range(nop):
        for j in range(i, nop):
            ret += [(i, j)]

    rd.shuffle(ret)

    return (ret)

def plot(a,b):
    colors={'aa':'r','ar':'g','tt':'b','t2t':'black','nt':'cyan'}
    
    for n,v in b.items():
        plt.scatter(a,v,c=colors[n])



def game(m1, m2):
    ret = 0, 0

    if m1 == 'a' and m2 == 'a':
        ret = -5, -5
    if m1 == 'a' and m2 == 'r':
        ret = 3, 0
    if m1 == 'r' and m2 == 'a':
        ret = 0, 3
    if m1 == 'r' and m2 == 'r':
        ret = 1, 1

    return (ret)


def nsel(p):
    ret = []
    mortal = int(0.01 * len(p))
    nop = {}
    scr = {}

    for i in p:
        nop[i[0]] = 0
        scr[i[0]] = 0

    for i in p:
        nop[i[0]] += 1
        scr[i[0]] += i[1]

    stand = sorted(scr.items(), key=operator.itemgetter(1))
    rng = 0

    for ply in nop.keys():
        rng = nop[ply]
        if ply == stand[len(stand) - 1][0]:
            rng += mortal
        if ply == stand[0][0]:
            rng -= mortal

        for i in range(rng):
            ret.append([ply, 0, []])

    return ret


def match(p1, p2):
    snd = []

    for p in [p1, p2]:
        if p[0] == 'aa':
            snd.append('a')
        if p[0] == 'ar':
            snd.append('r')
        if p[0] == 'nt':
            x = ['a', 'r']
            if len(p[2]) == 0:
                snd.append('a')
            else:
                x.remove(p[2][len(p[2]) - 1])
                snd.append(x[0])
        if p[0] == 'tt':
            if len(p[2]) == 0:
                snd.append('r')
            else:
                snd.append(p[2][len(p[2]) - 1])
        if p[0] == 't2t':
            if len(p[2]) < 2:
                snd.append('r')
            else:
                if p[2][len(p[2]) - 1] == 'a' and p[2][len(p[2]) - 2] == 'a':
                    snd.append('a')
                else:
                    snd.append('r')

    pts = game(snd[0], snd[1])
    p1[1] = p1[1] + pts[0]
    p1[2].append(snd[1])
    p2[1] = p2[1] + pts[1]
    p2[2].append(snd[0])
    return (p1, p2)


np = 100
cycle = 10
niter = 100

for cyc in range(cycle):
    print(cyc)
    cycw={}

    p = [['', 0, []] for i in range(np)]
    name = {0: 'aa', 1: 'ar', 2: 'tt', 3: 't2t', 4: 'nt'}

    split = sorted(rd.sample([i for i in range(np)], 4))
    split = [1] + split + [np + 1]

    for i in range(len(split) - 1):
        for j in range(split[i], split[i + 1]):
            p[j - 1] = [name[i], 0, []]
    
    nop1={}
    fig=plt.figure()
    for j in range(niter):
        p = nsel(p)
        # .print (len(p))
        inst = instance(len(p))
        for ins in inst:
            p[ins[0]], p[ins[1]] = match(p[ins[0]], p[ins[1]])
            nop = {}
        for k in p:
            nop[k[0]] = 0
        for k in p:
            nop[k[0]] += 1

        if j==1:
        	nop1=nop
        #print(nop)
        plot(j,nop)

    fig.suptitle('Population Split')
    plt.xlabel('Iterations')
    plt.ylabel('No. of Members')
    plt.xlim(0,niter)
    plt.ylim(0,110)

    label={'aa':'Always Attack','ar':'Always Retreat','tt':'Tit for Tat','t2t':'Tit for 2 Tats','nt':'Nasty'}
    colors={'aa':'r','ar':'g','tt':'b','t2t':'black','nt':'cyan'}

   
    
    for n,v in nop1.items():
        plt.scatter(-1,-1,c=colors[n],label=label[n])


    plt.legend(loc='upper left')
    print ('A')
    fig.savefig('Cycle_'+str(cyc))
 




