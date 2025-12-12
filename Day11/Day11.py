#!/usr/bin/env python3
import sys
f=sys.argv[1] if len(sys.argv)>1 else "input.txt"
g={}
for l in open(f):
    if ":" in l:
        a,b=l.split(":",1); g[a.strip()]=b.split()
    elif l.strip():
        g[l.strip()]=[]
for a in list(g):
    for v in g[a]: g.setdefault(v,[])

def count(s,t,need=()):
    need=set(need)
    memo={}
    def dfs(u,mask):
        k=(u,mask)
        if k in memo: return memo[k]
        if u==t: return 1 if mask==(1<<len(need))-1 else 0
        ans=0
        for v in g[u]:
            m=mask
            if v in idx: m|=1<<idx[v]
            ans+=dfs(v,m)
        memo[k]=ans
        return ans
    idx={x:i for i,x in enumerate(need)}
    start=0
    if s in idx: start|=1<<idx[s]
    return dfs(s,start)

print(count("you","out"))
print(count("svr","out",("dac","fft")))

