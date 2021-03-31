import random


def kmp(string, pattern):

    prefix_table = [0]*len(pattern)

    curr_longest = 0
    i = 1  # Index begins from 1 beacuse prefix_table[0] is 0

    while i < len(pattern):
        if pattern[i] == pattern[curr_longest]:
            curr_longest += 1
            prefix_table[i] = curr_longest
            i += 1 

        else:
            if curr_longest != 0:
                curr_longest = prefix_table[curr_longest-1]
                # i is not incremented here
            else:
                prefix_table[i] = 0
                i += 1
                # Once curr_longest is 0, the current char is not part of a prefix suffix and the algorithm moves to the next char

    i = 0
    j = 0

    while i < len(string):
        if string[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            print("Match found at index {i}".format(i=i-j))
            j = prefix_table[j-1]
            #  Go back to the previous index of the pattern to find where the pattern repeated

        elif i < len(string) and string[i] != pattern[j]:
            if j != 0:
                j = prefix_table[j-1]
                # Similar to creating the prefix_table, this step is repeated to find the longest previous prefix until j = 0
            else:
                i += 1
                # No other choice, the pattern starts back at j = 0 and i is finally incremented


string = "algorithmisfun"
pattern = "fun"
print("KMP with {str}".format(str=string))
kmp(string, pattern)
n = len(string)

print()
partial_pattern_demo = "fualgorithmisfun"
print("KMP with {str}".format(str=partial_pattern_demo))
kmp(partial_pattern_demo,pattern)