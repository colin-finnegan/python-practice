"""

Python Intermediate Problems
Author: Colin Finnegan
Date: 11/9/2026

"""

#Checks if a given word is a palindrome, ignores punctuation and capitalization
def palindrome(word):
    if len(word) == 0:
        return False
    
    cleaned = ""
    for char in word:
        if char.isalnum():
            cleaned = cleaned + char.lower()

    left = 0
    right = len(cleaned) - 1
    while left < right:
        if cleaned[left] == cleaned[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

#Two sum problem, given a list of numbers and a target, return the indexes of two numbers that add up to the target
def two_sum(listy, target):
    seen = {}
    for nums in listy:
        sum2 = target - nums
        if sum2 in seen:
                    return [listy.index(nums), listy.index(sum2)]
        else:
            seen[nums] = listy.index(nums)
        
#Duplicate problem redone using a dictionary instead of a list
def duplicates2(listy):
    listd = {}
    for mem in listy:
        if mem not in listd:
            listd[mem] = 1
    return list(listd.keys())
        


def main():
    print(palindrome('taco1ocat'))
    print(palindrome(',mantnam!&'))
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6))
    print(duplicates2([1, 3, 4, 2, 3, 2, 4, 1]))

if __name__ == "__main__":
    main()