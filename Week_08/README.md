学习笔记
用位运算得到的答案还是挺巧的，也比较简单呢，比如
number-of-1-bits：
n&（n-1）把最低位的1清零，终止条件是其等于零，统计次数
python里bin函数可以直接转成二进制
power-of-two:
如果是2的幂，那么n&（n-1）==0
或者 n&(-n)==n

并查集
def init(p):
    p = [i for i in range(n)]

def union(self, p, i, j):
    p1 = self.parent(p, i)
    p2 = self.parent(p, j)
    p[p1] = p2

def parent(self, p, i):
    root = i
    while p[root] != root:
	root = p[root]
    while p[i] != i:
	x = i
	i = p[i]
	p[x] = root
    return root

判断终止条件：parent是自身！
如果parent不是自身，把经过的路径上的节点的parent设置成root，可以达到压缩路径的效果。





