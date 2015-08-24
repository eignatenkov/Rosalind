__author__ = 'egor'

#Given: A file containing at most 1000 lines.

#Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

with open("/home/egor/Загрузки/rosalind_ini5.txt","r") as f:
    content=f.readlines()

with open("int5_output.txt","w") as f:
    for i in range(int(len(content)/2)):
        f.write(content[2*i+1])

