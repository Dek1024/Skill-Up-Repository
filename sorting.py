def sort(arr):
    size = len(arr)
    if size == 1:
        return arr
    for index in range(0,size -1,1):
        for index2 in range(index,size,1):
            if arr[index2] <= arr[index]:
                temp = arr[index]
                arr[index] = arr[index2]
                arr[index2] = temp
    return arr

num = 5
ans = [[1,2,4,5,7,8],[1,2,3,5,6,9],[3,3,3,3,3,3,3],[6],[1,2]]
test = [[1,4,2,8,5,7],[2,5,1,6,9,3],[3,3,3,3,3,3,3],[6],[2,1]]
for i in range(0,num,1):
    check = sort(test[i])
    if check == ans[i]:
        print("Test",i+1,"Pass")
        print("Actual Result:", check)
        print("Expected Result:", ans[i])
    else:
        print("Test",i+1,"Fail")
        print("Actual Result:", check)
        print("Expected Result:", ans[i])
