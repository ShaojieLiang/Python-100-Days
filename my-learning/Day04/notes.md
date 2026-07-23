# Day04 学习记录：Python 运算符

## 学习日期

2026-07-23

## 记录说明

这份记录是根据我今天实际完成的 Day04 学习过程整理的个人学习记录，不是课程原文。

## 今日学习内容

今天学习 Python 运算符，重点包括：

- 算术运算符：`+`、`-`、`*`、`/`、`//`、`%`、`**`
- 赋值运算符：`=`、`+=`、`-=`、`*=`
- 比较运算符：`>`、`<`、`>=`、`<=`、`==`、`!=`
- 逻辑运算符：`and`、`or`、`not`

## 今日核心理解

### 1. `/`、`//`、`%` 的区别

```python
7 / 2    # 3.5
7 // 2   # 3
7 % 2    # 1
```

我的理解：

- `/` 是普通除法，结果是 `float`，例如 `9 / 3` 的结果是 `3.0`
- `//` 是整除，只保留整数商，例如 `9 // 3` 的结果是 `3`
- `%` 是取余数，例如 `9 % 3` 的结果是 `0`

### 2. 复合赋值

```python
score = 80
score += 10   # 90
score -= 20   # 70
score *= 2    # 140
```

我的理解：

- `score += 10` 等价于 `score = score + 10`
- `score -= 20` 等价于 `score = score - 20`
- `score *= 2` 等价于 `score = score * 2`

### 3. 比较运算符的结果是布尔值

```python
age = 20

print(age >= 18)  # True
print(age < 18)   # False
print(age == 20)  # True
print(age != 20)  # False
```

需要注意：

- `=` 是赋值
- `==` 是判断是否相等
- 布尔值必须写成 `True` 和 `False`，首字母大写

### 4. 逻辑运算符

```python
age = 20

age >= 18 and age <= 60   # True
age >= 18 or age > 60     # True
not (age == 20)           # False
```

我的理解：

- `and`：两个条件都为 `True`，结果才是 `True`
- `or`：至少一个条件为 `True`，结果就是 `True`
- `not`：把结果反过来

## 今日完成的练习

### 练习 1：算术运算符

完成了 `7` 和 `2` 的加、减、乘、普通除法、整除、取余和幂运算。

### 练习 2：赋值运算符

预测并验证了：

```text
90
70
140
```

### 练习 3：比较运算符

预测并验证了：

```text
True
False
True
False
```

### 练习 4：逻辑运算符

能够判断：

```python
age >= 18 or age > 60      # True
age < 18 and age > 60      # False
not (age == 20)            # False
```

### 练习 5：综合练习

完成了学生优惠判断：

```python
age = 22
student = True

if age <= 25 and student:
    print("你符合优惠条件")
else:
    print("你不符合优惠条件")
```

也理解了进阶规则：

```python
(age <= 25 and student) or age >= 60
```

表示：25 岁及以下的学生，或者 60 岁及以上的老人，都可以享受优惠。

## 今天暴露的问题

1. `True`、`False` 容易拼写成 `Ture`、`false`。
2. 一开始会写 `student == True`，虽然能运行，但不够 Pythonic。
3. 代码格式还需要继续养成习惯，例如赋值和运算符两边留空格。

## 修正后的写法

推荐：

```python
if age <= 25 and student:
    print("你符合优惠条件")
```

不推荐：

```python
if age <= 25 and student == True:
    print("你符合条件")
```

原因：`student` 本身已经是布尔值，直接写 `student` 就表示它为 `True`。

## 今日总结

今天 Day04 的核心内容已经完成。我能够理解并使用 Python 的算术、赋值、比较和逻辑运算符，也能写出简单的条件表达式。

后续需要重点复习：

- `/`、`//`、`%` 的区别和应用场景
- `True`、`False` 的正确拼写
- `and`、`or`、`not` 混合使用时的判断顺序
- 布尔变量直接参与条件判断的写法

## 下一步计划

开始 Day05，学习分支结构和条件判断：`if`、`elif`、`else`。
