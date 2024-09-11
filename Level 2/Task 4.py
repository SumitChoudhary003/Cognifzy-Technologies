def fibo(i):
    if i <=1:
        return i
    else:
        return(fibo(i-1) + fibo(i-2))
num = 20
if num  <= 0:
    print("Enter a number: ")
else:
    print("Fibonacci Series: ",end = " ")
for i in range(num):
    print(fibo(i), end = " ")            
    