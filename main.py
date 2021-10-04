import sys
from math import floor
INT_MAX=2147483646
def Compute_Average(a,b):
    return (a//2)+(b//2)+((a%2+b%2)//2)
if __name__=="__main__":
    a=INT_MAX
    b=INT_MAX
    print("Actual Average",INT_MAX)
    print(Compute_Average(a,b))