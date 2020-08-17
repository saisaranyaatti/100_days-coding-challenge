#performing all arithmetic calculations
def arthmetic(a,b):
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
    def fdiv(a,b):
        return a//b
    def mod(a,b):
        return a%b
    return(print(add(a,b),sub(a,b),mul(a,b),div(a,b),fdiv(a,b),mod(a,b))) 
a=int(input("enter a value"))
b=int(input("enter b value"))
arthmetic(a,b)
