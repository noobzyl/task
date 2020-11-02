# coding : utf-8
'''生成器求斐波那契数列'''

def fib_genarator(n):
    n1, n2, count = 1, 1, 2
    yield n1
    while count <= n:
        tmp = n2
        n2 = n1 + tmp
        n1 = tmp
        yield n1
        count += 1
counts = int(input("请输入需要的数列的项的个数： "))
res = fib_genarator(counts)
print(list(res))
