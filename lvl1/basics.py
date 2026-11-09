"""

Python Back to Basics
Author: Colin Finnegan
Date: 11/9/2026

"""

def is_even(n):
    return n % 2 == 0

def greater_than_ten(nums):
    return sum([num for num in nums if num > 10])

def reverse(word):
    new_word = ""
    for char in word:
        new_word = char + new_word
    return new_word

def main():
    print(is_even(37))
    print(is_even(14))
    print(greater_than_ten([14, 3, 25, 10, 9, 11]))
    print(reverse('peacock'))

if __name__ == '__main__':
    main()