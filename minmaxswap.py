
a = [1, 2, 6, 5, 1, 2]
b = [3, 4, 5, 2, 2, 3]

print("debug")
for i in range(len(a)):
    if a[i] > 1 and a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
print(a,b)

x = max(a)
y = max(b)

mul = x*y
    
print(mul)



