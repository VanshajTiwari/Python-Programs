
from asyncio.base_futures import _FINISHED
import re #regular EXpression 
print("=============WELCOME TO BASIC PY CALCULULATOR===============")
print("Enter Quit/EXIT/no/finish to Stop")
print("\n\n")
c=True
def play():
    global c
    equation=input("Enter the expression :)")
    if "quit"==(equation).lower() or "finish"==(equation).lower() or "no"==(equation).lower() or "exit"==(equation).lower() :
        print("\n\n=========== Calculator OFF :| ==============")
        c=False
        
    else:
        equation=re.sub('[A-z . < > ? | \ = _ { } ]','',equation)
        if equation=="":
                print("=============== Invalid INPUT :( ================")
                print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= Rewrite AGAIN =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= \n")
                play()
        result=eval(equation)
        print(result)
while c==True:
    play()