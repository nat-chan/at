#!/usr/bin/env python3
from typing import *


INF = cast(int, float("inf"))

class ArgminData(NamedTuple):
    value: int
    index: int # type: ignore

class EulerTour:
    def __init__(
            self,
            adj: List[List[int]],
            root: int = 0,
        ) -> None:
        self.N = len(adj)
        self.adj = adj
        self.root = root
        self.build()
        self.post_build()
        self.build_seg()

    def build(self) -> None:
        self.tour: List[int] = list()
        self.visited = [False]*self.N
        # prev[root] == rootにするか-1にするか迷う
        self.prev = [self.root]*self.N
        stack = [~self.root, self.root]
        while stack:
            src = stack.pop()
            if src >= 0:
                self.visited[src] = True
                self.tour.append(src)
                for dst in reversed(self.adj[src]):
                    if self.visited[dst]: continue
                    stack.append(~dst)
                    stack.append(dst)
                    self.prev[dst] = src
            else:
                self.tour.append(src)

    def post_build(self) -> None:
        self.enter = [-1]*self.N
        self.exit = [-1]*self.N
        self.tour_depth = [-1]*(2*self.N)
        d = -1
        assert len(self.tour) == 2*self.N
        for i in range(2*self.N):
            if self.tour[i] >= 0:
                self.enter[self.tour[i]] = i
                d += 1
            else:
                self.exit[~self.tour[i]] = i
                d -= 1
            self.tour_depth[i] = d

    def build_seg(self) -> None:
        from atcoder.segtree import SegTree
        e = ArgminData(INF, -1)
        v = [ArgminData(self.tour_depth[i], i) for i in range(2*self.N)]
        self.seg = SegTree(min, e, v) # Range Min Query

    def LCA_depth(self, u: int, v: int) -> int:
        iu, iv = self.enter[u], self.enter[v]
        iu, iv = min(iu, iv), max(iu, iv)
        ans = self.seg.prod(iu, iv+1).value
        return ans

    def LCA(self, u: int, v: int) -> Tuple[bool, int]:
        iu, iv = self.enter[u], self.enter[v]
        iu, iv = min(iu, iv), max(iu, iv)
        index = self.seg.prod(iu, iv+1).index
        current = self.tour[index]
        flag = current >= 0
        if flag:
#            print(f"\x1b[31m[+]{self.prev[current]}->{current}\x1b[m")
            return flag, current
        else:
#            print(f"\x1b[31m[-]{self.prev[~current]}->{current}\x1b[m")
            return flag, self.prev[~current]


from collections import deque
def bfs(adj, start=0):
    N = len(adj)
    visited = [False]*N
    d = [INF]*N
    d[start] = 0
    q = deque([start])
    while q:
        src = q.popleft()
        visited[src] = True
        for dst in adj[src]:
            if visited[dst]: continue
            if d[dst] > d[src] + 1:
                d[dst] = d[src] + 1
                q.append(dst)
    return d

def test_euler_tour():
    """
    グラフの画像: https://atcoder.jp/contests/abc202/editorial/1864
          1
         ╱ ╲
        2   3
       ╱│╲
      4 5 7
      │
      6
    """
    from align import Align
    print(test_euler_tour.__doc__)

    # prepare testcase
    N = 7
    P = [0, 0, 1, 1, 3, 1]
    adj: List[List[int]] = [list() for _ in range(N)]
    for i in range(N-1):
        adj[P[i]].append(i+1)
        adj[i+1].append(P[i])

    ET = EulerTour(adj, 0)

    # print tour, depth
    with Align():
        print("index", *range(2*N))
        print("tour", end=" ")
        for i in range(2*N):
            if ET.tour[i] >= 0:
                print(f"+{ET.tour[i]+1}", end=" ")
            else:
                print(f"-{~ET.tour[i]+1}", end=" ")
        print()
        print("depth", *ET.tour_depth)
    print()

    # print enter, exit
    with Align():
        print("index", *range(1, N+1))
        print("enter", *ET.enter)
        print("exit", *ET.exit)


    d = bfs(adj, 0)
    d2 = [bfs(adj, i) for i in range(N)]
    print()
    with Align():
        print(".", *range(1, N+1))
        for u in range(N):
            print(u+1, end=" ")
            for v in range(N):
                if u <= v:
                    print(".", end=" ")
                    continue
                ans = d[u] + d[v]-2*ET.LCA_depth(u, v)
                print(ans, end=" ")
            print()

    print()
    with Align():
        print(".", *range(1, N+1))
        for u in range(N):
            print(u+1, end=" ")
            for v in range(N):
#                if u <= v:
#                    print(".", end=" ")
#                    continue
                flag, ans = ET.LCA(u, v)
                ans += 1
                if flag:
                    print(f"\x1b[31m{ans}\x1b[m", end=" ")
                else:
                    print(f"\x1b[34m{ans}\x1b[m", end=" ")
            print()

    # assert test
    for u in range(N):
        for v in range(N):
            assert d[u] + d[v]-2*ET.LCA_depth(u, v) == d2[u][v]




if __name__ == '__main__':
    test_euler_tour()