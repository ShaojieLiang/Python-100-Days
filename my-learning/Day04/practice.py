"""
Day04 练习：Python 运算符

本文件保存我在 Day04 亲自完成的练习代码。
"""


# 1. 算术运算符练习
# 练习 +、-、*、/、//、%、**。
a = 7
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


# 2. 赋值运算符练习
# 使用 +=、-=、*= 修改 score。
score = 80

score += 10
print(score)

score -= 20
print(score)

score *= 2
print(score)


# 3. 比较运算符练习
# 判断 age 和 18、20 的关系。
age = 20

print(age >= 18)
print(age < 18)
print(age == 20)
print(age != 20)


# 4. 逻辑运算符练习
# 练习 and、or、not。
print(age >= 18 and age <= 60)
print(age >= 18 or age > 60)
print(not (age == 20))


# 5. 综合练习
# 规则：25 岁及以下的学生，或者 60 岁及以上的老人，可以享受优惠。
age = 22
student = True

can_get_discount = (age <= 25 and student) or age >= 60
print(can_get_discount)

if can_get_discount:
    print("你符合优惠条件")
else:
    print("你不符合优惠条件")
