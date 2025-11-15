def is_valid_move(current, next_num, visited):
    """
    检查从当前数字移动到下一个数字是否合法
    """
    # 定义所有需要中间点的移动及其对应的中间点
    move_rules = {
        (1, 3): 2, (3, 1): 2,
        (4, 6): 5, (6, 4): 5,
        (2, 8): 5, (8, 2): 5,
        (1, 9): 5, (9, 1): 5,
        (3, 7): 5, (7, 3): 5,
        (1, 7): 4, (7, 1): 4,
        (3, 9): 6, (9, 3): 6,
        (7, 9): 8, (9, 7): 8
    }

    move = (current, next_num)

    # 如果这个移动需要中间点
    if move in move_rules:
        mid_point = move_rules[move]
        # 检查中间点是否已经被访问过
        if not visited[mid_point]:
            return False

    return True


def generate_patterns():
    """
    生成所有合法的九宫格图案密码
    """
    all_patterns = []

    def backtrack(path, visited):
        # 如果路径长度在4到9之间，添加到结果中
        if 4 <= len(path) <= 9:
            all_patterns.append(path.copy())

        # 如果路径长度达到9，停止递归
        if len(path) == 9:
            return

        # 尝试所有可能的下一步移动
        for next_num in range(1, 10):
            if not visited[next_num]:
                current = path[-1] if path else None

                # 检查移动是否合法
                if current is None or is_valid_move(current, next_num, visited):
                    visited[next_num] = True
                    path.append(next_num)
                    backtrack(path, visited)
                    path.pop()
                    visited[next_num] = False

    # 初始化访问数组
    visited = [False] * 10  # 索引0不使用，使用1-9

    # 从每个可能的起点开始
    for start in range(1, 10):
        visited[start] = True
        backtrack([start], visited)
        visited[start] = False

    return all_patterns


# 生成所有合法图案
patterns = generate_patterns()

# 输出结果
print(f"总共有 {len(patterns)} 种合法的九宫格图案密码")
print("前10个图案示例:")
for i in range(10):
    print(patterns[i])

# 验证一些特定情况
print("\n验证特定情况:")
test_cases = [
    [2, 4, 1, 3],  # 正确：{1,3}前面有2
    [1, 3, 4, 2],  # 错误：{1,3}前面没有2
    [1, 4, 3, 5],  # 正确：{1}和{3}不相邻
]

for case in test_cases:
    # 检查是否在合法图案列表中
    is_valid = any(pattern == case for pattern in patterns)
    print(f"{case}: {'合法' if is_valid else '不合法'}")