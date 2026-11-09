"""

Python Data Structures and Loops
Author: Colin Finnegan
Date: 11/9/2026

"""

#Return frequency of characters in a string
def char_freq(word):
    new_d = {}
    for char in word:
        if char in new_d:
            new_d[char] += 1
        else:
            new_d[char] = 1
    return new_d

#Print Fizz for multiples of 3, Buzz for multiples of 5, FizzBuzz for multiples of both, and the number itself if neither
def FizzBuzz():
    for num in range(1, 51):
        if num % 5 == 0 and num % 3 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)

#Remove duplicates from a list while preserving original order
def duplicates(listy):
    dups = []
    for mem in listy:
        if mem not in dups:
            dups.append(mem)
    return dups


def main():
    print(duplicates([1, 3, 4, 2, 3, 2, 4, 1]))

if __name__ == '__main__':
    main()
