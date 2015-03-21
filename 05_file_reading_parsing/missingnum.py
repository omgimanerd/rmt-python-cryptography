#!/usr/bin/python

def missingnum():
    file = open("nums.txt")
    data = file.read().split("\n")
    
    a = []
    for i in data:
        a.append(int(i))
    a.sort()

    for i in range(len(a)):
        if i != a[i]:
            return i

print missingnum()
