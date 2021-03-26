def counting_sort(arry):
    maxnum = max(arry)
    count_array = [0]*(maxnum+1)

    for i in arry:
        count_array[i]+=1

    for i in range(1,maxnum+1):
        count_array[i] += count_array[i-1]

    ans_arry = [0]*len(arry)

    for i in arry:
        idx = count_array[i]
        ans_arry[idx-1] = i
        count_array[i] -= 1
    
    return ans_arry
a = [84,23,62,44,16,30,95,51]
a= counting_sort(a)
print(a)