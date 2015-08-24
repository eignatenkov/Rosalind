__author__ = 'egor'

# Given: Positive integers n≤100 and m≤20.

# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

with open("/home/egor/Загрузки/rosalind_fibd.txt","r") as f:
    coeffs=[int(x) for x in f.readline().strip().split(' ')]


temp=[0]*coeffs[0]
temp[0]=1
temp[1]=1
for i in range(2,coeffs[1]+1):
    temp[i]=temp[i-1]+temp[i-2]

temp[coeffs[1]]-=1

for i in range(coeffs[1]+1,coeffs[0]):
    temp[i]=temp[i-1]+temp[i-2]-temp[i-coeffs[1]-1]

print(temp[coeffs[0]-1])