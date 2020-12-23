import time


def LCS(s1,s2,n,m):
    L=[[-1 for i in range(m+1)] for j in range(n+1)]


    for i in range(n):
        for j in range(m):
            if i==0 or j==0:
                L[i][j]=0


    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1]==s2[j-1]:
                L[i][j]=L[i-1][j-1]+1
            else:
                L[i][j]=max(L[i-1][j],L[i][j-1])

    return L[n][m]
            
            

if __name__ == "__main__":
    s1=input("Enter string 1: ")
    s2=input("Enter string 2: ")
    start_time = time.time()
    print("LCS is",LCS(s1,s2,len(s1),len(s2)))

    print("--- Program executed in %s seconds ---" % (time.time() - start_time))