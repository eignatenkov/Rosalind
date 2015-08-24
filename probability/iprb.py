__author__ = 'egor'

# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are
# homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant
# allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

# Sample Dataset

# 2 2 2

# Sample Output

# 0.78333

with open("/home/egor/Загрузки/rosalind_iprb.txt","r") as f:
    coeffs=[int(x) for x in f.readline().strip().split(' ')]

print(1-(.25*coeffs[1]*(coeffs[1]-1)+coeffs[1]*coeffs[2]+coeffs[2]*(coeffs[2]-1))/(sum(coeffs)*(sum(coeffs)-1)))