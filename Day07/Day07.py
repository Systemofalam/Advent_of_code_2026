import sys

g=[l.rstrip("\n") for l in open(sys.argv[1])]
w=max(map(len,g))
g=[l.ljust(w) for l in g]
h=len(g)
for r,row in enumerate(g):
    c=row.find("S")
    if c!=-1:
        sr,sc=r,c
        break

def part1():
    b={sc}
    s=0
    for r in range(sr+1,h):
        nb=set()
        row=g[r]
        for c in b:
            if 0<=c<w:
                if row[c]=="^":
                    s+=1
                    if c>0: nb.add(c-1)
                    if c<w-1: nb.add(c+1)
                else:
                    nb.add(c)
        b=nb
        if not b: break
    return s

def part2():
    d={sc:1}
    for r in range(sr+1,h):
        nd={}
        row=g[r]
        for c,v in d.items():
            if 0<=c<w:
                if row[c]=="^":
                    if c>0: nd[c-1]=nd.get(c-1,0)+v
                    if c<w-1: nd[c+1]=nd.get(c+1,0)+v
                else:
                    nd[c]=nd.get(c,0)+v
        d=nd
        if not d: break
    return sum(d.values())

print(part1())
print(part2())

