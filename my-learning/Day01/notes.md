# Day01 - 初识 Python

- 学习状态：已完成
- 学习日期：2026-07-19 至 2026-07-20
- 课程讲义：[Day01 - 初识 Python](../../Day01-20/01.%E5%88%9D%E8%AF%86Python.md)

## 今日目标

- 了解 Python 的特点、应用领域、优点和不足。
- 完成 macOS、Terminal 和 VS Code 的 Python 开发环境配置。
- 学习 Python 基础输入输出、变量和数据类型。
- 完成 `input()`、`print()` 和类型转换综合练习。

## 环境检查

- [x] 完成 Python 环境安装
- [x] 确认 Python 版本：Python 3.14.3
- [x] 确认 pip 可用：pip 25.3（Python 3.14）
- [x] 确认终端可以运行 Python
- [x] 确认 VS Code 可以运行 `.py` 文件
- [x] 运行最简单的 Python 命令和完整练习程序

## 学习内容

- 使用 `python3` 启动 Python 交互解释器，使用 `exit()` 或 `Control + D` 退出。
- 使用 `print()` 输出字符串和计算结果。
- 区分字符串 `str`、整数 `int` 和浮点数 `float`。
- 理解引号中的内容是字符串，没有引号的数字可以参与数学运算。
- 理解 `+` 对整数表示加法、对字符串表示拼接。
- 理解“字符串 × 整数”表示重复字符串，整数写在左边或右边都可以。
- 创建变量、给变量赋值，并理解重新赋值会更新变量保存的值。
- 学习变量命名规则：不能包含空格、不能以数字开头，可以使用下划线。
- 使用 `input()` 接收用户输入，并确认其返回值默认是 `str`。
- 使用 `int()`、`float()` 和 `str()` 进行基础类型转换。
- 理解 Python 文件从第一行开始顺序执行。
- 区分 macOS Terminal、Python 交互解释器和 VS Code 编辑器。
- 理解交互解释器适合验证简短语句，完整程序应写入 `.py` 文件。

## 核心知识与复盘

1. Python 是一种语法简单、可读性强的解释型高级编程语言。
2. Python 适合数据分析、科学计算、人工智能、自动化和 Web 开发等领域。
3. Python 的主要优点是容易学习、开发效率高、生态强大；主要不足是运行效率通常低于 C/C++。
4. `input()` 无论接收什么内容，默认返回的都是 `str`，需要时应主动进行类型转换。
5. 变量保存数据，重新赋值会替换变量原来保存的值。

## 练习与掌握情况

- 成功输出 `hello, python` 和整数加法结果。
- 能区分 `"15"` 与 `15` 的数据类型。
- 能判断字符串拼接、整数加法和字符串重复的结果。
- 能创建、输出和重新赋值变量。
- 能使用 `input()` 获取姓名和年龄，并通过 `type()` 确认两者都是 `str`。
- 能使用 `int()` 和 `float()` 转换用户输入。
- 已在 VS Code 中创建并运行 `.py` 文件。
- 已完成复盘题和综合输入输出练习。

## 综合练习

完成用户信息输入程序：

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height（单位：米）: "))

print("你好, " + name)
print("你今年", age, "岁")
print("你的身高是", height, "米")
```

## 遇到的问题

| 问题或报错 | 原因 | 解决方法 |
|---|---|---|
| `python3 -v` 输出大量导入信息并进入交互模式 | 小写 `-v` 表示 verbose，不是查看版本 | 使用大写 `python3 -V` 或 `python3 --version` |
| `pip3 -version` 报 `no such option: -e` | 长选项需要两个连字符 | 使用 `pip3 --version` |
| `print(''hello, python''` 报 `SyntaxError` | 重复使用单引号，并缺少右括号 | 使用一对匹配的引号并补全括号：`print('hello, python')` |
| `"15" + 5` 无法运算 | `str` 和 `int` 不能直接使用 `+` | 根据目的统一类型：字符串拼接或整数加法 |
| 误以为 `"3" * 4` 和 `2 * "Go"` 会报错 | 不熟悉 Python 的字符串重复规则 | 字符串与整数相乘会重复字符串，顺序不影响结果 |
| 变量名 `your daddy` 报 `SyntaxError` | 变量名不能包含空格 | 使用下划线，例如 `your_daddy` |
| 两条赋值语句写在同一行报 `SyntaxError` | 两条语句之间没有换行或分隔符 | 在交互解释器中逐行输入；完整程序放入 `.py` 文件 |
| 直接输入 `jie` 报 `NameError` | Python 将其当作未定义的变量名 | 输出已定义的变量，或把文字写成字符串 `"jie"` |
| VS Code 没有运行按钮 | Python 扩展尚未激活或未选择解释器 | 激活 Python 扩展并选择正确的 Python 解释器 |
| 运行程序时需要手动输入路径 | 不熟悉 VS Code 的 Python 文件运行方式 | 使用 VS Code 的 Run Python File 功能 |
| 在 Terminal 直接输入 `print()` 报错 | Terminal 的 shell 不是 Python 解释器 | 先进入 Python 交互解释器，或运行 `.py` 文件 |
| `int("25.6")` 报错 | `int()` 不能直接转换带小数点的字符串 | 先使用 `float("25.6")`；如确实需要整数，再转换为 `int` |

## 今日总结

- 我已经完成 Python、pip、Terminal 和 VS Code 环境验证。
- 我已经掌握 `print()`、变量、`input()`、基础数据类型和基础类型转换。
- 我完成了 Day01 综合练习，并能够解释常见报错的原因。
- 需要继续注意：命令参数的大小写和连字符、引号与括号配对、变量命名以及数据类型是否兼容。
- Day01 已完成，下一步开始 Day02。

## 下一步

- [x] 完成 VS Code 与 `.py` 文件实践
- [x] 完成 Python 简介、应用、优点和不足问题
- [x] 学习基础类型转换
- [x] 完成综合练习
- [x] 完成最终复盘
- [ ] 开始 Day02
