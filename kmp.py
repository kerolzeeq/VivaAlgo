def kmp(string, pattern):
    prefix_table = [0]*len(pattern)

    curr_longest = 0
    i = 1
    n = len(pattern)

    while i < n:
        if pattern[i] == pattern[curr_longest]:
            curr_longest += 1
            prefix_table[i] = curr_longest
            i += 1
        else:
            if curr_longest != 0:
                curr_longest = prefix_table[curr_longest - 1]
                # i not incremented because we still want to find the possible prefix with char
            else:
                prefix_table[i] = 0
                i += 1
                # no other option, it's a new prefix

    print(prefix_table)

    m =  len(string)
    i = 0
    j = 0

    while i < m:
        if string[i] == pattern[j]:
            i += 1
            j += 1
            if j == n:
                print("Match found beginning at index {index}".format(index=i-j))
        
        elif i < m and string[i] != pattern[j]: # Mismatch occurs, we look for where to go instead of restarting i
            if j != 0:
                j = prefix_table[j-1]   # Look for a previous previous prefix and go to that index.
                # This line gets repeated if string[i] != pattern[j] until j finally becomes 0
            
            else:
                i += 1



string = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
kmp(string,pattern)