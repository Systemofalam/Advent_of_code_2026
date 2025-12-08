import sys

p=[tuple(map(int,l.split(','))) for l in open(sys.argv[1]) if l.strip()]
n=len(p)
e=[]
for i in range(n):
    x1,y1,z1=p[i]
    for j in range(i+1,n):
        x2,y2,z2=p[j]
        dx=x1-x2;dy=y1-y2;dz=z1-z2
        e.append((dx*dx+dy*dy+dz*dz,i,j))
e.sort()

def dsu():
    return list(range(n))

def find(a,pa):
    while pa[a]!=a:
        pa[a]=pa[pa[a]]
        a=pa[a]
    return a

pa=dsu()
for d,i,j in e[:min(1000,len(e))]:
    a=find(i,pa);b=find(j,pa)
    if a!=b: pa[b]=a
s={}
for i in range(n):
    r=find(i,pa)
    s[r]=s.get(r,0)+1
a,b,c=sorted(s.values(),reverse=True)[:3]
part1=a*b*c

pa=dsu()
comp=n
part2=None
for d,i,j in e:
    a=find(i,pa);b=find(j,pa)
    if a!=b:
        pa[b]=a
        comp-=1
        if comp==1:
            part2=p[i][0]*p[j][0]
            break

print(part1)
print(part2)

