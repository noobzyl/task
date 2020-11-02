# coding : utf-8
'''循环法求斐波那契数列'''
def fib( n ):
    a = 1
    b = 1
    for i in range(1, counts+1 ):
        print(a, end=" ", flush=True)
        a, b = b, a + b  
counts = int(input("请输入需要的个数： "))
fib(100)  
