# n = int(input())
# num = 96
# for i in range(0,n*2-1):
#     for j in range(i,n*2-2):
#         num1 = num+n
#         print(num1,"-",end="")
#         print("-", *n * 2 - 2, end="")
#         print()



# n = 97+3
# a = chr(n)
# print(a)
num=96
n = int(input())
for i in range(n):
    print('-'*(n*2-2),end='')
    for j in range(i+1):
        print(chr(num+n-j),end='')
        print("-",end='')
    print('-' * (n*2-2), end='')
    n=n-1
    print()