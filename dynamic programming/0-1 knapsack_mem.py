global t
t=[[-1]*100]*100   #from constraint


def knapsack(weight,value,capacity,size):
    if capacity<1 or size<1:
        return 0
    if t[capacity][size]!=-1:
        return t[capacity][size]
    if weight[size-1]<=capacity:
        t[capacity][size]=max(value[size-1]+knapsack(weight,value,capacity-weight[size-1],size-1),knapsack(weight,value,capacity,size-1))
        return t[capacity][size]
    elif weight[size-1]>capacity:
        t[capacity][size]=knapsack(weight,value,capacity,size-1)
        return t[capacity][size]

weight=list(map(int,input("Enter weight: ").split()))
value=list(map(int,input("Enter value: ").split()))
capacity=int(input("Enter capacity of bag: "))
print("Maximum profit:",knapsack(weight,value,capacity,len(weight)))