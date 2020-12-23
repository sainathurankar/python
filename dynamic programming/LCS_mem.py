import time


def init(n,m):
    global L
    L=[[None for i in range(m+1)] for j in range(n+1)]

def LCS(s1,s2,n,m):
    if n==0 or m==0:
        return 0
    if L[n-1][m-1]==None:
        if s1[n-1]==s2[m-1]:
            L[n-1][m-1]=1+LCS(s1,s2,n-1,m-1)
            return L[n-1][m-1] 
        else:
            L[n-1][m-1]=max(LCS(s1,s2,n-1,m),LCS(s1,s2,n,m-1))
            return L[n-1][m-1]
    return L[n-1][m-1]



if __name__ == "__main__":
    s1=input("Enter string 1: ")
    s2=input("Enter string 2: ")
    start_time = time.time()
    init(len(s1),len(s2))
    print("LCS is",LCS(s1,s2,len(s1),len(s2)))
    print("--- Program executed in %s seconds ---" % (time.time() - start_time))