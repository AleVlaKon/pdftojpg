file = open('nums.txt')
file_sod = [int(i) for i in file.read().split()]
file.close()
print(sum(file_sod))