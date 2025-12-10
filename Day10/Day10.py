#!/usr/bin/env python3
import sys, re
from collections import deque
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def parse(line):
    pat = re.search(r'\[([.#]+)\]', line).group(1)
    btns = [
        [int(x) for x in s.split(',') if x.strip()]
        for s in re.findall(r'\(([^()]*)\)', line)
    ]
    t = [int(x) for x in re.search(r'\{([^}]*)\}', line).group(1).split(',')]
    return pat, btns, t

def min_lights(pat, btns):
    n = len(pat)
    tgt = 0
    for i, c in enumerate(pat):
        if c == '#':
            tgt |= 1 << i
    masks = []
    for inds in btns:
        m = 0
        for i in inds:
            if 0 <= i < n:
                m |= 1 << i
        if m:
            masks.append(m)
    if tgt == 0:
        return 0
    N = 1 << n
    dist = [-1] * N
    q = deque([0])
    dist[0] = 0
    while q:
        s = q.popleft()
        d = dist[s] + 1
        for m in masks:
            ns = s ^ m
            if dist[ns] == -1:
                if ns == tgt:
                    return d
                dist[ns] = d
                q.append(ns)
    return 0

def min_jolt(t, btns):
    m = len(t)
    B = len(btns)
    if m == 0 or B == 0:
        return 0
    A = np.zeros((m, B), dtype=float)
    for j, inds in enumerate(btns):
        for i in inds:
            if 0 <= i < m:
                A[i, j] += 1.0
    t_arr = np.array(t, dtype=float)
    c = np.ones(B, dtype=float)
    bounds = Bounds(0, np.inf)
    constr = LinearConstraint(A, t_arr, t_arr)
    integrality = np.ones(B, dtype=int)
    res = milp(c=c, constraints=[constr], bounds=bounds, integrality=integrality)
    x = np.rint(res.x).astype(int)
    return int(x.sum())

def main(path):
    p1 = p2 = 0
    for line in open(path):
        line = line.strip()
        if not line:
            continue
        pat, btns, tgt = parse(line)
        p1 += min_lights(pat, btns)
        p2 += min_jolt(tgt, btns)
    print(p1)
    print(p2)

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")

