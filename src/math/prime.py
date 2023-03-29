def sieve_of_eratosthenes(limit):
    """
    使用埃拉托色尼筛法生成指定范围内的所有素数。
    :param limit: 整数，生成素数的上限（不包含该整数）
    :return: 一个包含所有小于等于 limit 的素数的列表
    """
    # 初始化一个布尔值列表，表示数值的素数状态（True 表示素数，False 表示非素数）
    prime_status = [True] * limit
    prime_status[0] = False  # 0 不是素数
    prime_status[1] = False  # 1 不是素数

    # 遍历列表，使用筛选法找出素数
    for current_number in range(2, int(limit**0.5) + 1):
        # 如果当前数是素数，则将其倍数标记为非素数
        if prime_status[current_number]:
            # 从 current_number^2 开始，因为比它小的倍数已经被之前的素数标记过了
            for multiple in range(current_number**2, limit, current_number):
                prime_status[multiple] = False

    # 从布尔值列表中提取素数
    primes = [number for number in range(limit) if prime_status[number]]
    return primes

def is_prime(number):
    """
    判断给定的整数是否为素数。
    :param number: 需要判断的整数
    :return: 如果整数是素数，返回 True，否则返回 False
    """
    # 小于 2 的整数不是素数
    if number < 2:
        return False

    # 从 2 到 number 的平方根之间的整数，检查是否能够整除 number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # 如果找到一个因子，number 不是素数
    return True  # 如果没有找到任何因子，number 是素数


# sieve_of_eratosthenes方法使用例子，生成小于等于 50 的素数
limit = 51
primes = sieve_of_eratosthenes(limit)
print(f"Primes in the range [2, {limit}): {primes}")

# is_prime方法使用例子
start = 0
end = 20
primes = [number for number in range(start, end + 1) if is_prime(number)]
# 输出包含素数的列表
print(f"Primes in the range [{start}, {end}]: {primes}")