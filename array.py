import array as arr
#Create array with integer type
a = arr.array ('i' , [5,2,6,10,1,5,6])
#To Sort the array
a.sort()

print('The new created array is : ')
for i in range(0,10):
    print(a[i], end = " ")
print()