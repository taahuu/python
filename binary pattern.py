n=int(input("Enter the Number of Rows: "))

for i in range(1,n+1):
    for j in range(i):
        print((i+j)%2,end='')
    print()

print("-"*20)
# for i in range(n+1):
#     for j in range(i):
#         print((i+j)%2,end='')
#     print()