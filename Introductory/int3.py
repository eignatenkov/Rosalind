__author__ = 'egor'

#Problem

#Given: A string s of length at most 200 letters and four integers a, b, c and d.

#Return: The slice of this string from indices a through b and c through d (with space in between), inclusively.

#Sample Dataset

#HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
#22 27 97 102

#Sample Output

#Humpty Dumpty

with open("/home/egor/Загрузки/rosalind_ini3.txt","r") as f:
    string=f.readline()
    indices=[int(x) for x in f.readline().split(' ')]

print(string[indices[0]:indices[1]+1]+' '+string[indices[2]:indices[3]+1])
