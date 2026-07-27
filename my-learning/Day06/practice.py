# # # for i in range(1, 6):
# # #     print(i)
# # # for i in range(1, 10, 3):
# # #     print(i)
# # total=0
# # for i in range(1, 10):
# #     total+=i
# # print(total)
# # total = 0

# # for i in range(1, 101):
# #     total += i

# # print(total)
# # total = 0
# # for i in range(1, 101, 2):
# #     total += i
# # print(total)
# # total = 0

# # for i in range(2, 101, 2):
# #     total += i

# # # print(total)
# # i = 1
# # while i <= 5:
# #     print(i)
# #     i += 1
# for i in range(1,6):
#     if i ==3:
#         break
#     print(i)
# for i in range(1,6):
#     if i == 2:
#         continue
#     if i == 4:
#         break
#     print(i)
# for i in range(2):
#     for j in range(2):
#         print(i, j)

#     print("----")
# for i in range(1,10):
#     for j in range(1,10):
#         print(f'{i} * {j} = {i*j}', end='----')
#     # print('----')    
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()