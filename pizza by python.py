print("\n\n")
print("**************************Pizza Program****************************")
print("\n")

def pizza():

   
    pizza=10                #these are deafault stock 
    burger=10               #admin can only manipulate these values
    springroll=10
    icecream=10
    bur=0                   #these variable contain order of customer
    piz=0
    spr=0
    ice=0
    
    while(True):
       
        
        s=0       #stores total amont of order
        c=True
        print("\n\n")
        a=input("Login. ID :) ")
        print("\n")
        if a.lower()=="vanshaj" or a.lower()=="vanshajtiwari" or a.lower()=="vanshaj tiwari" :                              #admin
            print("Hello admin")
            print("what do you like to change :) ")
            print("1.Burger\n2.Pizza\n3.Springroll\n4.icecream")
            print("")
            while c==True:
                b=input("Enter code of that you want to change :) ")
                if b=="1" or b.lower()=="burger":
                    burger=int(input("New stock of Burger :) "))
                elif b=="2" or b.lower()=="pizza":
                    pizza=int(input("New stock of Pizza :) "))
                elif b=="3" or b.lower()=="springroll":
                    springroll=int(input("New stock of Springroll :)"))
                elif b=="4" or b.lower()=="icecream":
                    icecream=int(input("New stock of icecream :) "))
                else:
                    print("\n")
                    print("Please enter only given value from given list" )
                d=input("Anymore changes(y/n)")
                if d.lower()=="yes" or d.lower()=="y":
                    pass
                else:
                    c=False
        else:                                                          #customer
            print("welcome Sir")
            print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            print('''  Code        Item               Price

  1           Burger             20
  2           Pizza             100
  3           Springroll         50
  4           Icecream           30
''')
            print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            print("\n")
            while c==True:
                b=input("what would you like to order Sir :) ")
                if b=="1" or b.lower()=="burger":
                    bur=int(input("Burger Order :)"))
                    if bur>burger:
                        print("OUT OF STOCK!\n\n we offering you from available stock")
                        bur=burger
                elif b=="2" or b.lower()=="pizza":
                    piz=int(input("Pizza Order :)"))
                    if piz>pizza:
                        print("OUT OF STOCK!\n\n we offering you from available stock")
                        piz=pizza
                elif b=="3" or b.lower()=="springroll":
                    spr=int(input("Springroll order :)"))
                    if spr>springroll:
                        print("OUT OF STOCK!\n\n we offering you from available stock")
                        spr=springroll
                elif b=="4"  or b.lower()=="icecream":
                    ice=int(input("Icecream order :)"))
                    if ice>icecream:
                        print("OUT OF STOCK!\n\n we offering you from available stock")
                        ice=icecream
                else:
                    print("please enter number from given list only :)")
                d=input("Anything else (y/n):)")
                if d.lower()=="yes"or d.lower()=="y" :
                    pass
                else:
                    c=False 
            s=bur*20+spr*50+piz*100+ice*30
            print("\n")
            print("+====================================================+")
            print('Code        Item        Quantity        Amount')
            print("1           Burger        ",bur,"           ",20*bur)
            print("2           Pizza         ",piz,"           ",100*piz)
            print("3           Springroll    ",spr,"           ",50*spr)
            print("4           Icecream      ",ice,"           ",30*ice)
            print("                Total payable amount :) ",s)
            print("+=====================================================+")
            print("\n\n")
pizza()      
            
