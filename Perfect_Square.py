class Soltuion : 
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(i, i+1):
            if i * i == num:
                return True
            if i * i > num:
                return False

        1, r = 1, num
        while 1 <= r:
            mid = (1 + r) // 2
            if mid * mid > num:
                r = mid - 1
            elif mid * mid < num:
                1 = mid + 1
            else:
                return True
        return False