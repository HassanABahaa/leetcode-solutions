class Solution(object):
    def minimumRounds(self, tasks):
        z = Counter(tasks)

        ans = 0
        for num in z.values():
            if num == 1:
                return -1
            ans += num // 3
            if num % 3:
                ans += 1
        return ans