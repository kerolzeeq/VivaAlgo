def counting_sort(arry,exp):
    ans_array = [0]*len(arry)
    count_arry =[0]*10

    for i in arry:
        index =(i//exp)%10
        count_arry[index] += 1
    
    for i in range(1,len(count_arry)):
        count_arry[i] += count_arry[i-1]
        
    for i in range(len(arry)-1,-1,-1):
         index = (arry[i]//exp)%10
         ans_array[count_arry[index]-1] = arry[i]
         count_arry[index] -= 1
         
    return ans_array
    
def radix_sort(arry):
    max_dig=len(str(max(arry)))
    exp=1
    for i in range(0,max_dig):
        arry=counting_sort(arry,exp)
        exp *=10

    return arry

a = [84,23,62,44,16,30,95,51]
a = radix_sort(a)
print(a)