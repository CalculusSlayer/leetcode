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
            closest_pair = [left pointer, right pointer]
        
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
            closest_pair = [left pointer, right pointer]
        
        left pointer ++
    
    while right pointer < len(family2):
        f1 = family1[-1]
        f2 = family2[right pointer]
        x = abs(f1 - f2)
        if x < closest_difference:
            closest_difference = x
            closest_pair = [left pointer, right pointer]
        
        right pointer ++

    return closest_pair
        



    '''

def main():
    pass

if __name__ == '__main__':
    main()
