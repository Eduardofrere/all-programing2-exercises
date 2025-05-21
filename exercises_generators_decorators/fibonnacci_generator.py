def fibonacci(lenght):
    a= 0
    b=1
    for i in range(lenght):
        yield a
        a, b= b, a+b

length = 100
print(list(fibonacci(length))) 


    
 