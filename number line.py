import math

arr = list(map(int,input().split()))

m = max(abs(min(arr)),abs(max(arr)))

left_limit , right_limit = -m, m
n = right_limit - left_limit + 1 
matrix = [[ '  ' for i in range(n) ] for i in range(n)]

# Number line 
k = left_limit
for i in range(n//2):
    matrix[n//2][i] = str(k)
    k += 1  
  
k = left_limit
matrix[n//2][n//2] = " 0" 
# Origin of the number line 
ox,oy = n//2, n//2 

k = 1
for i in range(n//2+1, n):
    matrix[n//2][i] = f" {k}"  
    k += 1    

def print_matrix():
    for i in matrix:
        print(*i)

# mark the stars 
for i in arr:
    pos = oy + i
    if i < 0:
        for j in range(1,abs(i)+1):
            matrix[ox + j][pos] = ' *'
    else:
        for j in range(1,i+1):
            matrix[ox - j][pos] = " *"

print_matrix()


