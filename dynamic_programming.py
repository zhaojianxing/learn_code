# conding=utf-8
"""
动态规划算法：基本条件要素
1）具有最优子结构：原始问题分解成一个个规模更小的子问题
2）重叠子问题：
3）状态与状态转移：f(n-1)--> f(n)
4）边界条件：停止条件
"""

def flb_1(n):
    if n < 1:
        return 0
    if n <= 3:
        return 1
    return flb_1(n-1) + flb_1(n-2)

def flb_2(n):
    a, b, c = 0, 1, 1
    for i in range(3, n+1):
        c = a+b
        a, b = b, c
    return c

def backpack(number, weight, w, v):
    # 初始化二维数组，用于记录背包中个数为i，重量为j时能获得的最大价值
    result = [[0 for i in range(weight+1)]for i in range(number+1)]
    for i in range(1, number+1):
        for j in range(1, weight+1):
            if j < w[i-1]:
                result[i][j] = result[i-1][j]
            else:
                result[i][j] = max(result[i-1][j], result[i-1][j-w[i-1]]+v[i-1])
    return result[number][weight]

if __name__ == '__main__':
    print(flb_1(10))
    print(flb_2(10))
    number = 5
    weight = 10
    w = [2, 2, 6, 5, 4]
    v = [6, 3, 5, 4, 6]
    print(backpack(number, weight, w, v))