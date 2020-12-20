def spiral(arr,R,C):
    m=0
    n=0
    while m<R and n<C :
        for i in range(m,C):
            print(arr[m][i],end=" ")
        m+=1
        for i in range(n+1,R):
            print(arr[i][C-1],end=" ")
        C-=1

        if m<R:
            for i in range(C-1,m-2,-1):
                print(arr[R-1][i],end=" ")
            R-=1

        if n<C:
            for i in range(R-1,n,-1):
                print(arr[i][n],end=" ")
            n+=1

if __name__ == "__main__":
    mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    spiral(mat,len(mat),len(mat[0]))