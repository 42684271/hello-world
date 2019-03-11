# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:25:17 2019

@author: aifa
"""

#sentence = raw_input('Enter a sentence : ')

#length = len(sentence)

#print '+' + '-'* length + '+'
#print '|' + ' '* length + '|'
#print '|' + sentence + '|'
#print '|' + ' '* length + '|'
#print '+' + '-'* length + '+'


# interesting list slicing operation

# initialize 2 list

a= range(20)
b= range(10)
b.reverse()

# insert b to a : postion at 3
a[3:3] = b

# insert part of b to a : position at 3
a= range(20)
a[3:3] = b[3:8]

# remove part of list a
a= range(20)
b= range(10)
a[:8] = [] # remove - replace with nothing
b[-1:-5:-1] = [100] * 4 # replacement

# delete
del b[-1:-5:-1]

#  list methods
# append, insert, append, count, index, remove, reverse, sort
m = range(10, 50, 3)
n = range(10)


# append
m.append(100)
m.append(100)
m.append(100)
print m

# remove the last 2 ones
m.pop()
m.pop()
print m

# remove the last one
print m.pop()
print m

# contcate with another one
m += n
print m

# delete part
m[-len(n):] = []
print m

# another way to delete part
m += n
print m
del m[-len(n):]
print m

# count the occurance of element, find the index
m += n*2
print m
print 'The count of element 1 : ' + str( m.count(1) )

# find the index of element
print 'The first element 1 index : ' + str( m.index(1) )

m.remove(1)
print m
m.remove(1)
print m

# reverse the list
print 'reverse...'
m.reverse()
print m

# sort..
print 'sort...'
m.sort()
print m

# sort reversely
print n
print 'sort reversely...'
n.sort(reverse=True)
print n










