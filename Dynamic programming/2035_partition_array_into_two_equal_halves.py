def minimumDifference(nums) -> int:
    mem = {}
    n = len(nums) / 2

    def dfs(i, diff, n1, n2):
        if i == len(nums):
            if n1 == n2 == n:
                return abs(diff)
            return float('inf')

        if (i, n1, n2) in mem:
            return mem[(i, n1, n2)]

        min_diff = float('inf')

        if n1 == n:
            min_diff = dfs(i + 1, diff - nums[i], n1, n2 + 1)
        elif n2 == n:
            min_diff = dfs(i + 1, diff + nums[i], n1 + 1, n2)
        else:
            min_diff = min(dfs(i + 1, diff + nums[i], n1 + 1, n2), dfs(i + 1, diff - nums[i], n1, n2 + 1))

        mem[i] = min_diff
        return min_diff

    return dfs(0, 0, 0, 0)


a = minimumDifference(
    [7772197, 4460211, -7641449, -8856364, 546755, -3673029, 527497, -9392076, 3130315, -5309187, -4781283, 5919119,
     3093450, 1132720, 6380128, -3954678, -1651499, -7944388, -3056827, 1610628, 7711173, 6595873, 302974, 7656726,
     -2572679, 0, 2121026, -5743797, -8897395, -9699694])
print(a)
