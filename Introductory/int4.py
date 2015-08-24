__author__ = 'egor'

#Given: Two positive integers a and b (a<b<10000).

#Return: The sum of all odd integers from a through b, inclusively.

#Sample Dataset

#100 200

#Sample Output

#7500

with open("/home/egor/Загрузки/rosalind_ini4.txt","r") as f:
    indices=[int(x) for x in f.readline().split(' ')]

sum=0

for i in range(indices[0],indices[1]+1):
    if i%2==1:
        sum=sum+i

print(sum)