# # This program prints all prime numbers between 2 and 121   
# for i in range(2, 122):
#     for j in range(2,int(i**0.5)+1):
#         if i % j == 0:
#             break
#     else:
#         print(i)
a=0
b=1
for i in range(0,50):
    a, b= b, a+b
    if a >= 50:
        break
    print(a, end='\n')