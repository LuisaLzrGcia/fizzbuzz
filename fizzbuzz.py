i = 1
for i in range (1,1001):
    if i % 15==10:
        print ("FizzBuzz")
    elif i%3==0:
        print ("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print (i)