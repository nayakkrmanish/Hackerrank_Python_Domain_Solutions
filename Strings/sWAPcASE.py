"""
Title     : sWAP cASE
Subdomain : Strings
Domain    : Python
Author    : Ahmedur Rahman Shovon
Contributor: Manish Kumar Nayak
Created   : 16 July 2016
Updated   : 08 July 2020
Problem   : https://www.hackerrank.com/challenges/swap-case/problem
"""
# modified code by Contributor
# usage of .swapcase() method to improve code and functionality
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# original code by Author
def swap_case(sentence):
    updated_s = ""
    for c in sentence:
        if c.isupper():
            updated_s += c.lower()
        elif c.islower():
            updated_s += c.upper()
        else:
            updated_s += c
    return updated_s


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
