passw = int(input())

z = []

for i in range(passw):
    # spis_uch = []
    # for i in range(int(input())):
    #     spis_uch.append([i for i in input().split()])
    z.append(any([input().split()[1] == '5' for i in range(int(input()))]))
    # print(spis_uch)

print(z)
    # z.append(any(map(lambda x: x[1] == '5', spis_uch)))
# if all(z):
#     print('YES')
# else:
#     print('NO')

