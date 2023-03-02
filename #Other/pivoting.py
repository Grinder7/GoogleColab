arr = [[0 for _ in range(3)] for _ in range(3)]
arr[0][0] = 4
arr[0][1] = -1
arr[0][2] = 1
arr[1][0] = -1
arr[1][1] = 4
arr[1][2] = -2
arr[2][0] = 1
arr[2][1] = -2
arr[2][2] = 4

arr2 = [[0 for _ in range(1)] for _ in range(3)]
arr2[0][0] = 12
arr2[1][0] = -1
arr2[2][0] = 15
print(arr)
print(arr2)

x = [0 for _ in range(3)]

# Mencari persamaan
for i in range(3):
    diag = 0
    diag += 1

for i in range(3):
    for j in range(3):
        i += 1
