__author__ = 'egor'
import math

def split(size, data):
    answer = []
    for i in range(math.ceil(len(data)/size)):
        answer.append(data[size*i:size*(i+1)])
    return answer
