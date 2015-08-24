__author__ = 'egor'

# Given: A positive integer n (n≤1000).
#
# Return: The total number of subsets of {1,2,…,n} modulo 1,000,000.
#
# Sample Dataset
#
# 3
#
# Sample Output
#
# 8

with open("/home/egor/Загрузки/rosalind_sset.txt","r") as f:
    size=int(f.readline())

print(pow(2,size) % 1000000)