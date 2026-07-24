# # # # # # age=int(input("Enter your age: "))
# # # # # # if age>=18:
# # # # # #     print("你已经成年了")
# # # # # # print('程序结束')
# # # # # score=int(input('请输入你的成绩:'))
# # # # # if score>=60:
# # # # #     print('考试及格')
# # # # # print('成绩检查完成')
# # # # score=float(input('请输入你的成绩:'))
# # # # if score>=60:
# # # #     print('考试及格')
# # # # else:
# # # #     print('考试不及格')
# # # score = float(input('请输入你的成绩: '))

# # # if score >= 90:
# # #     print('优秀')
# # # elif score >= 80:
# # #     print('良好')
# # # elif score >= 60:
# # #     print('及格')
# # # else:
# # #     print('不及格')
# # temperature = float(input('请输入当前温度: '))  
# # if temperature >= 35:
# #     print('天气高温')
# # elif temperature >=30:
# #     print('天气炎热')
# # elif temperature >= 15:
# #     print('舒适 ')
# # else:
# #     print('天气寒冷')
# vip=input('是否是会员：y/n')
# price=float(input('请输入商品价格：'))
# if vip=='y':
#     if price>=200:
#         print('价格为:',price*0.8)
#     else:
#         print('价格为:',price*0.9)
#     print('谢谢会员光临')
# else:
#     if price>=200:
#         print('价格为:',price*0.9)
#     else:
#         print('价格为:',price)
#     print('谢谢穷逼光临')
# age=float(input('请输入年龄：'))
# if age<18:
#     print('未成年')
# elif age>=18 and age<60:
#     print('成年人')
# else:
#     print('老年人')
# a=float(input('请输入第一个数字：'))
# b=float(input('请输入第二个数字：'))
# if a>b:
#     print('最大值为：',a)
# elif a<b:
#     print('最大值为：',b)
# else:
#     print('两个数相等')
math=float(input('请输入数学成绩：'))
english=float(input('请输入英语成绩：'))
python=float(input('请输入python成绩：'))
if math>=60 and english>=60 and python>=60:
    print('三门课程都及格')
else:
    print('有课程不及格')