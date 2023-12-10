# function to calculate the factorial
def calcFact(num):
    fact=1
    for i in range(num,0,-1):
        fact*=i
    print("factorial of",num,"is",fact)
    
num=int(input("entr the number:"))
calcFact(num)
