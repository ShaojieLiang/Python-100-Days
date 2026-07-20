# Day01 - 初识 Python

- 学习状态：已完成
- 学习日期：2026-07-20
- 课程讲义：[Day01 - 初识 Python](../../Day01-20/01.%E5%88%9D%E8%AF%86Python.md)

## 今日目标

- 了解 Python 的特点、应用领域、优点和不足。
- 完成 macOS + VS Code Python 开发环境配置。
- 学习 Python 基础输入输出和数据类型。
- 完成变量、input、print 和类型转换综合练习。

## 环境检查

- [x] 完成 Python 环境安装
- [x] 确认 Python 版本
- [x] 确认 pip 可用
- [x] 终端运行 Python
- [x] VS Code 运行 `.py` 文件

## 今天学习的内容

- 使用 `print()` 输出内容。
- 创建变量并理解赋值。
- 使用 `input()` 获取用户输入。
- 理解 `input()` 返回值默认是 `str`。
- 学习 `int`、`float`、`str` 基础类型。
- 学习 `int()`、`float()` 类型转换。
- 理解 Python 文件从第一行开始执行。
- 区分 Terminal 和 Python 解释器环境。

## 综合练习

完成用户信息输入程序：

```python
name=input("Enter your name: ")
age=int(input("Enter your age: "))
height=float(input("Enter your height(单位: 米): "))

print('你好, ' + name)
print('你今年', age, '岁')
print('你的身高是', height, '米')
```

## 遇到的问题

| 问题 | 原因 | 解决方法 |
|---|---|---|
| VS Code 没有运行按钮 | Python 扩展未激活 | 激活 Python 扩展并选择解释器 |
| 运行需要手动输入路径 | 不熟悉 VS Code Python 运行方式 | 使用 Python Run File |
| 在 Terminal 输入 `print()` 报错 | Terminal 不是 Python 解释器 | 使用 Python 环境或运行 `.py` 文件 |
| `int("25.6")` 报错 | int 不能直接转换浮点字符串 | 先转换为 float 再转换 int |

## 今日复盘

- Python 是一种简单易学、可读性强的解释型高级编程语言。
- Python 适合数据分析、科学计算、人工智能、自动化等领域。
- 优点：语法简单、开发效率高、生态强大。
- 缺点：执行效率相比 C/C++ 较低。

## 下一步

- [x] 完成 VS Code 与 `.py` 文件实践
- [x] 完成 Python 简介、应用、优点和不足问题
- [x] 学习基础类型转换
- [x] 完成综合练习
- [x] 完成最终复盘
- [ ] 开始 Day02
