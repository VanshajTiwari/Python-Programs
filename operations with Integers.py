#facrorial to user given limit
def factorial():
    b=int(input("Enter a Number :)"))
    for j in range(1,b+1):
      c=1
      for i in range(1,j+1):
        c*=i
      print("Factorial of ",j,":)",c)

def pallindrome():
    b=int(input("Enter a Number :)"))
    c=b
    r=0
    while c>0:
        d=c%10
        c//=10
        r=r*10+d
    if b==r:
        print("Numnber is Pallindrome ")
    else:
        print("Number is Not Pallindrome ",r)

def armstrong():
    b=int(input("Enter a Number :)"))
    c=b
    i=0
    r=0
    while c>0:
      i+=1
      c//=10
    c=b
    while c>0:
        d=c%10
        c//=10
        r+=d**i
    if b==r:
        print("Number is Armstrong :)")
    else:
        print("Number is not Armstrong ")
#it reverse any value
def reverse():
    b=int(input("Enter a Number :)"))
    c=b
    r=0
    while c>0:
        d=c%10
        c//=10
        r=r*10+d
    print("Reverse of ",b," is ",r)
    
#test for prime number 
def prime():
    b=int(input("Enter a Number :) "))
    if b>2:
        for i in range(2,b):
            if b%i==0:
                
                print("\nNumber is not PRIME\n")
                break
        else:
            print("\nNumber is PRIME\n")
    else:
            print("\nNumber is not Prime\n")
#test for even odd
def even_odd():
    print("\n\n")
    b=int(input("ENTER A NUMBER :) "))
    print("\n")
    if(b%2==0):
        print("Number is Even ")
    else:
        print("Number is Odd")
#to print fibonacci series to user given limit
def fibonacci():
    b=0
    c=1
    i=int(input("Enter a number :) "))
    if i==1:
        print(b)
    elif i==2:
        print(b,"\n",c)
    elif i==0:
        print("Wrong Input :(\nMust enter number Greater than 0 ")
        fibonacci()
    else:
        print("\n\n")
        print(b)
        print(c)
        for i in range(2,i):
              d=b+c
              b,c=c,d
              print(d)
        print("\n\n")

while True:
    print("1.Factorial \n2.Pallindrome \n3.Armstrong \n4.Reverse \n5.Prime \n6.Even or Odd \n7.print Fibonacci to the given limit \n")
    a=input("enter a number :)")
    if a=="1" or a=="factorial" or a=="Factorial":
        factorial()
    elif a=="2" or a=="pallindrome" or a=="Pallindrome":
        pallindrome()
    elif a=="3" or a=="armstrong" or a=="Armstrong":
        armstrong()
    elif a=="4" or a=="reverse" or a=="Reverse":
        reverse()
    elif a=="5" or a=="Prime" or a=="prime":
        prime()
    elif a=="6" or a=="odd or even" or a=="Odd or even" or a=="ODD OR EVEN" or a=="Odd or Even":
        even_odd()
    elif a=="7" or a=="fibonacci" or a=="Fibonacci":
        fibonacci()
    else:
        print("Plz enter number only from given list :(")