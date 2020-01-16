n = int(input("Enter n no "))
sum = 0
for i in range(1,n):
    print(i)
    sum = sum + i**2/2
    print('s',sum)
print("sum is:",sum)
