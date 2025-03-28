a=int(input("Enter the number "))
sum=0
for n in range(1,a) :
    if n%2==0 :
        sum+=n
    else :
        print(n," is odd number")
        
print("Sum of even numbers :",sum)
for i in range(2,a):
    if a%i==0:
        print("Prime")
        break
    else:
        print("Not Prime")
        break