# Just a fun exercise to get warmed up on Python again
# All information in this is approximate, I'm not responsible
# for anything, yada yada yada.

# MST-KRUSKAL(G,w) from Introduction to Algorithms, 3rd Edition, p.631-633
# by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein

# 1)    A = {empty set}
# 2)    for each vertex v in the set G.V
# 3)        MAKE-SET(v)
# 4)    sort the edges of G.E into nondecreasing order by weight w
# 5)    for each edge (u,v) in the set G.E, taken in nondecreasing order by weight
# 6)        if FIND-SET(u) != FIND-SET(v)
# 7)            A = A UNION {(u,v)}
# 8)            UNION(u,v)
# 9)    return A

import csv
import math


def findset(needle, haystack):
    for item in haystack:
        if needle in item:
            return haystack.index(item)


print("Here we go!")
settlements = []
xcoord = []
ycoord = []
edges = []
coord = []
trees = []
with open('location.csv', newline='') as csvinput:
    # loading all of the elements from the file into the reader
    g = csv.reader(csvinput, delimiter=',', quotechar='|')
    for row in g:
        settlements.append(row[1])
        xcoord.append(row[2])
        ycoord.append(row[3])


a = []

print(settlements)

trees = [set() for i in range(30)]
for k in range(30):
    trees[k].add(k)

for i in range(30):
    for j in range(30):
        #print('{} and {}'.format(coord[x],coord[y]))
        xdif = float(xcoord[i]) - float(xcoord[j])
        ydif = float(ycoord[i]) - float(ycoord[j])
        distance = round(math.sqrt(math.pow(xdif, 2) + math.pow(ydif, 2)),2)
        #print('Distance from {} to {} is {}'.format(i+1, j+1, distance))
        if(distance > 0 and [distance, j, i] not in edges):
            edges.append([distance, i, j])
#print(edges)
edges.sort(key=lambda x: x[0])
#print(edges)
for dist, x, y in edges:

    setx = findset(x,trees)
    sety = findset(y,trees)
    #print('setx is {} and sety is {}'.format(setx,sety))
    if setx != sety:
        a.append((x,y))
        trees[setx] = trees[setx].union(trees[sety])
        trees.remove(trees[sety])
        #print(trees)

print(a)
print(trees)
for connection in a:
    print('{} to {}'.format(settlements[connection[0]], settlements[connection[1]]))