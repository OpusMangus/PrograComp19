def printIzq(dist, k, linea):
    while dist > 0:
        print("left of ")
        dist -= 1
    print (linea[k])

def printDer(dist, j, linea):
    while dist > 0:
        print("right of ",)
        dist -= 1
    print (linea[j])

n = int(input())

linea = list(map(str, input().split()))

q = int(input())
i = 0
while i < q:
    p = int(input()) - 1
    j = p
    k = p
    while (linea[j] == "?" or linea[k] == "?") and (j>0 and k<len(linea)-1):
        print ("J = ", j, " K = ", k)
        if j > 0 and linea[j] == "?":
            j -= 1
        if k < len(linea) - 1 and linea[k] == "?":
            k += 1

    if j == p and k == p:
        print(linea[p])
    elif (linea[j] != "?" and linea[k] != "?") and (p-j==k-p):
        print("middle of", linea[j],"and", linea[k])
    elif (linea[j]!= "?" and p-j<k-p):
        printDer(p - j, j, linea)
    else:
        printIzq(k - p, k, linea)
    i += 1