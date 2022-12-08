#program to created list of the cubes of even integers of the list
a = int(input("number of terms: "))
y = {}
for i in range(1,a+1):
    if i%2==0:
        x = {i:i**3}
        y.update(x)
    else:
        x = {i:i}
        
    
print(y)