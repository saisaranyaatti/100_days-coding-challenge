#beatty sequence
import math
def beatty_seq(n):
    for i in range(1,n+1):
        print(math.floor(i*math.sqrt(2)),end=" ")
n=int(input())
beatty_seq(n)
