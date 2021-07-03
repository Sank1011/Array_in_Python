from array import *
vals = array('i',[1,2,3,4,5])
print(vals)
'''
vals = array('i',[1,2,-3,4,5])
print(vals)

vals = array('I',[1,2,-3,4,5])
print(vals)
'''
print(vals.buffer_info())
print(vals.itemsize)
print(vals.typecode)
#vals.reverse()
#print(vals)
print()
newarr =array(vals.typecode, (a*a for a in vals))

for e in newarr:
    print(e)

print()
i = 0
while i<len(newarr):
    print(newarr[i])
    i+=1