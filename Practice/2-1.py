import numpy as np
a = np.array([4,56,1,2,3,4,5,6,7,6,9,7,0,12])
print("The actual array")
print(a)

a.sort()
print("The Sorted Array")
print(a)

print("Type of A is:  ", type(a))

b=np.array([-4.3,-2.3,12.9,8.99,10.1,-1.2])
print("Values of B before sorting: ", b)
print("Values of B after Sorting: ")
b.sort()
print(b)


c=np.array(['one','two','three','four','five','six','seven'])
print("The Unsorted values of c: ", c)
c.sort()
print("The sorted values of c: ", c)



