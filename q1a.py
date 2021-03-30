def counting_sort(A):

    #print initial
    print (A)

    max_num = max(A)                    #95
    count_array = [0]*(max_num+1)       #[0,1,2,3,...,95] --> [0,1,2,3,...,96]

    #This will add 1 to every similar number from the array given to the index
    #that indicates that the number in the array is
    for i in A:
        count_array[i] += 1
    #print(count_array)

    #This loop will cumalatively add at every index that has 1
    for i in range(1, max_num+1):
        count_array[i] += count_array[i-1]
    #print(count_array)

    #This will minimize the size array.
    ans_array = [0]*len(A)
    #print(ans_array)

    #This loop will sorting the numbers
    for i in A:
        idx = count_array[i]            #[16, 23, 30, 44, 51, 62, 84, 95]
        ans_array[idx-1] = i            #[1,2,3,4,5,6,7,8]
        count_array[i] -= 1             #[0,1,2,3,4,5,6,7]

    return ans_array
    
A = [84,23,62,44,16,30,95,51]
A= counting_sort(A)
print(A)