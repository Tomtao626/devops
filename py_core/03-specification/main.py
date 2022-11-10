def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_seq(n):
    res = []
    if n > 0:
        res.extend(fib_seq(n-1))
    res.append(fib(n))
    return res

# 测试一下这段代码总的效率以及各个部分的效率。那么，我就只需在开头导入 cProfile 这个模块，并且在最后运行 cProfile.run() 就可以了：

import cProfile
cProfile.run('fib_seq(30)')