n = int(input("Enter the n value:"))

# ---------- Print star pattern------- #
# --------- Pattern 1
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

for i in range(n):
    for j in range(n):
        print("*", end=' ')
    print()

print("\n")
# -------- Pattern 2
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
for i in range(n):
    for j in range(i+1):
        print("*", end=' ')
    print()

print("\n")
# -------- Pattern 3
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

for i in range(n):
    for j in range(i, n):
        print("*", end=' ')
    print()

print("\n")

# -------- Pattern 4
# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 
for i in range(n):
    for j in range(i):
        print(" ", end=' ')
    for j in range(i, n):
        print("*", end=' ')
    print()

print("\n")

# -------- Pattern 5
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 
for i in range(n):
    for j in range(i, n-1):
        print(" ", end=' ')
    # for j in range(n-i, n+1):
    for j in range(i+1):
        print("*", end=' ')
    print()

print("\n")

# -------- Pattern 6 -- needs to be corrected
# * 
# # # 
# * * * 
# # # # # 
# * * * * * 

for i in range(n):
    for j in range(i+1):
        if((j+1)%2==1):
            print("*", end =' ')
        if((j+1)%2==0):
            print("#", end =' ')
    print()

print("\n")

# -------- Pattern 7
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 
for i in range(n):
    for j in range(i, n-1):
        print(" ", end=' ')
    for j in range(i):
        print("*", end=' ')
    for j in range(i+1):
        print("*", end=' ')
    print()

print("\n")

# -------- Pattern 8
# pascal triangle
#         1 
#       1 1 1 
#     1 1 1 1 1 
#   1 1 1 1 1 1 1 
# 1 1 1 1 1 1 1 1 1 
for i in range(n):
    for j in range(i, n-1):
        print(" ", end=' ')
    for j in range(i):
        print("1", end=' ')
    for j in range(i+1):
        print("1", end=' ')
    print()

print("\n")

# -------- Pattern 9 ---- fibonacci series
# 1 1 2 3 5 8 13 21 34 55 89 
n = 10
a = 1
b = 1
print(a, b, end=' ')
for i in range(1, n):
    c = a+b
    a=b
    b=c
    print(c, end=' ')
print("\n")

    


