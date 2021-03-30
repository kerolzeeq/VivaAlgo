# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 14:15:00 2021

@author: Khairol Hazeeq
"""
def rabinkarp(string,pattern,d_ascii):              # a=1 b=2 c=3 d=4 e=5
    m=len(string)                                   #text = abcbacbaccbcc hashtext= 18 unnecessary hit
    n=len(pattern)                                  #pattern = cba hash=18
    hashpat=0                                       # f*256^2 + u*256^1 + n * 256^0 = 
    hashgroup=0                                     # [123 - a^10^2]*c + b*10^0 - gerak
    power=n-1
    #kira hash value of pattern and first group
    for i in range(n):
        hashpat=hashpat+(ord(pattern[i])*d_ascii**power) # 97x256^4 + 90x256^3 
        hashgroup=hashgroup+(ord(string[i])*d_ascii**power)
        power-=1

    #move group next 123 - 232
    for i in range(m):
            check=0
            if(hashpat==hashgroup): #check each alphabet
                for j in range(n):
                    if string[i+j]!=pattern[j]:
                        break
                    else: check+=1
                if check==n:
                    print(pattern," found at ",i)
            if(i<m-n): 
                 hashgroup=(hashgroup-ord(string[i])*d_ascii**(n-1))*d_ascii  + ord(string[i+n]) # [hashg -= a*256^4 ]*256 f*256^3
        
        
    


#string = input("Enter string : ")
string="algorithmisfun" 
pattern = "fun"

d_ascii=256

rabinkarp(string,pattern,d_ascii)