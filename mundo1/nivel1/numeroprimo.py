N=int(input())
for i in range(N): 
    X=int(input())
    divisores=0
    for d in range(1,X):
        if(X%d==0):
            divisores+=d
    if (divisores>2):
        print(X,"nao eh primo")
    else:
        print(X,"eh primo")