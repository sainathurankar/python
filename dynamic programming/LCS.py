import time

def LCS(s1,s2,n,m):
    if n==0 or m==0:
        return 0
    if s1[n-1]==s2[m-1]:
        return 1+LCS(s1,s2,n-1,m-1)
    return max(LCS(s1,s2,n-1,m),LCS(s1,s2,n,m-1))

if __name__ == "__main__":
    s1=input("Enter string 1: ")
    s2=input("Enter string 2: ")
    start_time = time.time()
    print("LCS is",LCS(s1,s2,len(s1),len(s2)))
    print("--- Program executed in %s seconds ---" % (time.time() - start_time))