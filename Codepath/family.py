# family.py
# Nayeel Imtiaz
# 12/18/22

'''
Closest In Age 

Problem: 
We are given the ages of people from two different families. We want to find the ages of the two people from the two families who are closest in age. 
For example: 

Given: 
family1 = {50, 15, 20, 55} 
family2 = {5, 2, 10, 22} 

Return: 
{20, 22} 
'''

import random # To generate pseudorandom lists for input.

def family(family1, family2):
    '''
    Sort both family1 and family2 lists.
    Initialize a pointer at index 0 for each of the lists.

    closest_difference = infinity
    closest_pair = None
    while left pointer < len(family1) and right pointer < len(family2):
        f1 = family1[left pointer]
        f2 = family2[right pointer]
        x = abs(f1 - f2)
        if x < closest_difference:
            closest_difference = x
            closest_pair = [f1, f2]
        
        if f1 <= f2:
            left pointer ++
        else:
            right pointer ++
    
    while left pointer < len(family1):
        f1 = family1[left pointer]
        f2 = family2[-1]
        x = abs(f1 - f2)
        if x < closest_difference:
            closest_difference = x
            closest_pair = [f1, f2]
        
        left pointer ++
    
    while right pointer < len(family2):
        f1 = family1[-1]
        f2 = family2[right pointer]
        x = abs(f1 - f2)
        if x < closest_difference:
            closest_difference = x
            closest_pair = [f1, f2]
        
        right pointer ++

    return closest_pair
    '''

    family1.sort()
    family2.sort()
    l, r = 0, 0
    
    closest_difference = float('infinity')
    closest_pair = None

    while l < len(family1) and r < len(family2):
        f1 = family1[l]
        f2 = family2[r]
        x = abs(f1-f2)
        if x < closest_difference:
            closest_difference = x
            closest_pair = [f1, f2]
        
        if f1 <= f2:
            l += 1
        else:
            r += 1
    
    while l < len(family1):
        f1 = family1[l]
        f2 = family2[-1]
        x = abs(f1-f2)
        if x < closest_difference:
            closest_difference = x
            closest_pair = [f1, f2]
        
        l += 1

    while r < len(family2):
        f1 = family1[-1]
        f2 = family2[r]
        x = abs(f1-f2)
        if x < closest_difference:
            closest_difference = x
            closest_pair = [f1, f2]
        
        r += 1
    
    return closest_pair

def main():
    family1 = [50, 15, 20, 55]
    family2 = [5, 2, 10, 22]

    print(family(family1, family2)) # [20, 22]

    random.seed(69)
    f3 = [random.randint(1, 100000) for i in range(50)]
    f4 = [random.randint(1, 100000) for i in range(50)]
    # print(f3)
    # print(f4)

    print(family(f3, f4)) # [8435, 8480]



if __name__ == '__main__':
    main()
