def listplus(vec,arr):
    for i in range(0,len(arr)):
        vec.append(arr[i])
    return vec
lis = [1,3,5,7,9]
lis1 = [2,4,6,8,10]
print(listplus(lis,lis1))