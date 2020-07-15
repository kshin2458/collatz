import sys

i=int(sys.argv[1])

for m in range(i+1):
    n=(2**m -1)/3
    if n%2==1:
        result=True
    else:
        result=False
    if result and n%1==0:
        print(int(n))
