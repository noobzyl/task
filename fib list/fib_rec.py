# coding : utf-8
'''递归法求斐波那契数列'''

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

counts = int(input("请输入需要的个数： "))
res = [fib(n) for n in range(1, counts+1)]

print(res)
