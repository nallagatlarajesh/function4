def calcpow(number,power):
    result=1
    for i in range(1,power+1):
        result*=number
    return result

base=int(input("enter the value for the base:"))
expo=int(input("enter the value for the exponent:"))
#function calling
answer=calcpow(base,expo)
print(base,"raised to power ",expo,"is ",answer)
