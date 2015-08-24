__author__ = 'egor'
# Given: Six positive integers, each of which does not exceed 20,000. The integers correspond to the number of couples
# in a population possessing each genotype pairing for a given factor. In order, the six given integers represent
# the number of couples having the following genotypes:

# AA-AA
# AA-Aa
# AA-aa
# Aa-Aa
# Aa-aa
# aa-aa
# Return: The expected number of offspring displaying the dominant phenotype in the next generation, under
# the assumption that every couple has exactly two offspring.
#
# Sample Dataset
#
# 1 0 0 1 0 1

# Sample Output
#
# 3.5

with open("/home/egor/Загрузки/rosalind_iev.txt","r") as f:
    numbers=[int(x) for x in f.readline().strip().split(' ')]

print(2*(numbers[0]+numbers[1]+numbers[2])+1.5*numbers[3]+1*numbers[4])