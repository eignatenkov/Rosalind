__author__ = 'egor'

# Given: A positive integer n (n≤20,000) and two subsets A and B of {1,2,…,n}.
#
# Return: Six sets: A∪B, A∩B, A−B, B−A, Ac, and Bc (where set complements are taken with respect to {1,2,…,n}).
#
# Sample Dataset
#
# 10
# {1, 2, 3, 4, 5}
# {2, 8, 5, 10}
#
# Sample Output
#
# {1, 2, 3, 4, 5, 8, 10}
# {2, 5}
# {1, 3, 4}
# {8, 10}
# {8, 9, 10, 6, 7}
# {1, 3, 4, 6, 7, 9}

with open("/home/egor/Загрузки/rosalind_seto.txt","r") as f:
    size=int(f.readline().strip())
    strset1=f.readline().strip()
    strset2=f.readline().strip()

set1=eval(strset1)
set2=eval(strset2)
u={i for i in range(1,size+1)}

print(set1|set2, set1&set2, set1-set2, set2-set1, u-set1, u-set2, sep='\n',)
