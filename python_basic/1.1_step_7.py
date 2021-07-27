fib = lambda x: 1 if x <= 2 else fib(x - 1) + fib(x - 2)
print(fib(31))
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print(sum(a))
