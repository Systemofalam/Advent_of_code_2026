#!/usr/bin/env python3
import sys,re

f=sys.argv[1] if len(sys.argv)>1 else "input.txt"
parts=open(f,encoding="utf-8").read().strip().split("\n\n")
areas=[]
for b in parts[:-1]:
    ls=b.splitlines()
    i=int(ls[0][:-1])
    while len(areas)<=i: areas.append(0)
    areas[i]=sum(c=="#" for s in ls[1:] for c in s)

ans=0
for l in parts[-1].splitlines():
    (w,h),cnt=l.split(":")
    w,h=map(int,w.split("x"))
    cnt=list(map(int,cnt.split()))
    ans+=sum(c*areas[i] for i,c in enumerate(cnt))<=w*h

print(ans)

